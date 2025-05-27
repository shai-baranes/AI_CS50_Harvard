from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Add edges connecting nodes (refer to connections from 'conditional_probability.png')
# (aka. 'Structure')
model = DiscreteBayesianNetwork([
    ('rain', 'maintenance'),
    ('rain', 'train'),
    ('maintenance', 'train'),
    ('train', 'appointment')
])

# CPDs
cpd_rain = TabularCPD(
    variable='rain',
    variable_card=3,
    values=[[0.7], [0.2], [0.1]],
    state_names={'rain': ['none', 'light', 'heavy']}
)

cpd_maintenance = TabularCPD(
    variable='maintenance',
    variable_card=2,
    values=[
        [0.4, 0.2, 0.1],  # 'yes'
        [0.6, 0.8, 0.9]   # 'no'
    ],
    evidence=['rain'],
    evidence_card=[3],
    state_names={'maintenance': ['yes', 'no'], 'rain': ['none', 'light', 'heavy']}
)

cpd_train = TabularCPD(
    variable='train',
    variable_card=2,
    values=[
        [0.8, 0.9, 0.6, 0.7, 0.4, 0.5],  # 'on time'
        [0.2, 0.1, 0.4, 0.3, 0.6, 0.5]   # 'delayed'
    ],
    evidence=['rain', 'maintenance'],
    evidence_card=[3, 2],
    state_names={
        'train': ['on time', 'delayed'],
        'rain': ['none', 'light', 'heavy'],
        'maintenance': ['yes', 'no']
    }
)

cpd_appointment = TabularCPD(
    variable='appointment',
    variable_card=2,
    values=[
        [0.9, 0.6],  # 'attend'
        [0.1, 0.4]   # 'miss'
    ],
    evidence=['train'],
    evidence_card=[2],
    state_names={'appointment': ['attend', 'miss'], 'train': ['on time', 'delayed']}
)

# Add CPDs to the model
model.add_cpds(cpd_rain, cpd_maintenance, cpd_train, cpd_appointment)

# Validate the model
assert model.check_model()

# Example inference
from pgmpy.inference import VariableElimination
infer = VariableElimination(model)BLUE
result = infer.query(variables=['appointment'], evidence={'rain': 'heavy'})
print(result)
