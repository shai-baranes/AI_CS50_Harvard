# TBD: works with older python version: 3.8 or earlier version
# from: https://www.youtube.com/watch?v=5NgNicANyqM&t=04h51m14s
# TBD start working with UV
# from pomegranate import Node, DiscreteDistribution, ConditionalProbabilityTable, BayesianNetwork


from pomegranate import *


# Rain node has no parents (probabilities sums up to 1)
rain = Node(DiscreteDistribution({ # Discrete - meaning 'none-conditional'
	"none": 0.7,  # no rain
	"light": 0.2, # light rain
	"heavy": 0.1, # heavy rain

}), name="rain")


# Track maintenance node is conditional on rain
maintenance = Node(ConditionalProbabilityTable([
#   'rain'   'maint.'  'odds'
	["none",  "yes",	0.4],
	["none",  "no", 	0.6],
	["light", "yes",	0.2],
	["light", "no", 	0.8],
	["heavy", "yes",	0.1],
	["heavy", "no", 	0.9],
], [rain.distribution]), name="maintenance")


# Train node is conditional on rain and maintenance
train = Node(ConditionalProbabilityTable([
#	 'rain'	 'maint.'	'train'	  'odds'
	["none", "yes", 	"on time", 0.8],
	["none", "yes", 	"delayed", 0.2],
	["none", "no",  	"on time", 0.9],
	["none", "no",	 	"delayed", 0.1],
	["light", "yes", 	"on time", 0.6],
	["light", "yes", 	"delayed", 0.4],
	["light", "no", 	"on time", 0.7],
	["light", "no", 	"delayed", 0.3],
	["heavy", "yes", 	"on time", 0.4],
	["heavy", "yes", 	"delayed", 0.6],
	["heavy", "no", 	"on time", 0.5],
	["heavy", "no", 	"delayed", 0.5],
], [rain.distribution, maintenance.distribution]), name="train")


# Appointment node is conditional on train
appointment = Node(ConditionalProbabilityTable([
# 	 'train'	'meeting' 'odds'
	["on time",	 "attend", 0.9],
	["on time",	 "miss",   0.1],
	["delayed",	 "attend", 0.6],
	["delayed",	 "miss",   0.4],
], [train.distribution]), name="appointment")


# Create a Baysian Network and add states
model = BayesianNetwork()
model.add_states(rain, maintenance, train, appointment) # adding the 4 above created nodes

# Add edges connecting nodes (refer to connections from 'conditional_probability.png')
model.add_edge(rain, maintenance) 
model.add_edge(rain, train)
model.add_edge(maintenance, train)
model.add_edge(train, appointment)


# Finalize model
model.bake()
