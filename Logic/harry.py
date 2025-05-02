from logic import *

# initiating the propositional symbols:
rain = Symbol("rain") # It is raining.
hagrid = Symbol("hagrid") # Harry visited Hagrid.
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore.



knowledge = And(                    #(And) since there are multiple things that we know are true, as depicted below:
    Implication(Not(rain), hagrid), #1 "if it is not ranining then Harry visited Hagrid" { 'formula': (¬rain) => hagrid }
    Or(hagrid, dumbledore),         #2 Harry visited Hagrid or Dumbledore.
    Not(And(hagrid, dumbledore)),   #3 and we also know that Harry didn't visit them both.
    dumbledore                      #4 and we know that Harry was actually visiting Dumbledore
)

print(model_check(knowledge, rain))
# True, the model verified that indeed it was raning that day!


print(knowledge.formula())
# ((¬rain) => hagrid) ∧ (hagrid ∨  dumbledore) ∧ (¬(hagrid ∧ dumbledore)) ∧ dumbledore




# # my perliminary practice
# sentence = And(rain, hagrid)
# print(sentence.formula()) # rain ∧ hagrid

# sentence = Or(And(rain, hagrid), And(rain, dumbledore))
# print(sentence.formula()) # (rain ∧ hagrid) ∨  (rain ∧ dumbledore)


