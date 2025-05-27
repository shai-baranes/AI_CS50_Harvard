

from torchegranate import BayesianNetwork, DiscreteDistribution, ConditionalProbabilityTable
# from pomegranate import BayesianNetwork, DiscreteDistribution, ConditionalProbabilityTable

# Define state mappings for readability
rain_states = {"none": 0, "light": 1, "heavy": 2}
maint_states = {"yes": 1, "no": 0}
train_states = {"on time": 1, "delayed": 0}
appoint_states = {"attend": 1, "miss": 0}

# Rain distribution (root node)
rain = DiscreteDistribution({
    rain_states["none"]: 0.7,
    rain_states["light"]: 0.2,
    rain_states["heavy"]: 0.1
})

# Maintenance conditional probability table
maintenance = ConditionalProbabilityTable([
    # Parent(rain), Child(maint), Probability
    [0, 1, 0.4],  # none → yes
    [0, 0, 0.6],  # none → no
    [1, 1, 0.2],  # light → yes
    [1, 0, 0.8],  # light → no
    [2, 1, 0.1],  # heavy → yes
    [2, 0, 0.9],  # heavy → no
], [rain])

# Train conditional probability table
train = ConditionalProbabilityTable([
    # Parents(rain, maint), Child(train), Probability
    [0, 1, 1, 0.8],  # none+yes → on time
    [0, 1, 0, 0.2],  # none+yes → delayed
    [0, 0, 1, 0.9],  # none+no → on time
    [0, 0, 0, 0.1],  # none+no → delayed
    [1, 1, 1, 0.6],  # light+yes → on time
    [1, 1, 0, 0.4],  # light+yes → delayed
    [1, 0, 1, 0.7],  # light+no → on time
    [1, 0, 0, 0.3],  # light+no → delayed
    [2, 1, 1, 0.4],  # heavy+yes → on time
    [2, 1, 0, 0.6],  # heavy+yes → delayed
    [2, 0, 1, 0.5],  # heavy+no → on time
    [2, 0, 0, 0.5],  # heavy+no → delayed
], [rain, maintenance])

# Appointment conditional probability table
appointment = ConditionalProbabilityTable([
    # Parent(train), Child(appoint), Probability
    [1, 1, 0.9],  # on time → attend
    [1, 0, 0.1],  # on time → miss
    [0, 1, 0.6],  # delayed → attend
    [0, 0, 0.4],  # delayed → miss
], [train])

# Create and structure the network
model = BayesianNetwork()
model.add_nodes(rain, maintenance, train, appointment)
model.add_edge(rain, maintenance)
model.add_edge(rain, train)
model.add_edge(maintenance, train)
model.add_edge(train, appointment)

# Finalize the model
model.bake()




rain_states = {"none": 0, "light": 1, "heavy": 2}
reverse_rain_states = {v: k for k, v in rain_states.items()}
print(reverse_rain_states)
# {0: 'none', 1: 'light', 2: 'heavy'}

# or
for key, value in rain_states.items():
	print(f"{value}: {key}")
# 0: none
# 1: light
# 2: heavy



