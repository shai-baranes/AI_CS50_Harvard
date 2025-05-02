from logic import *
import termcolor # user defined color for any text print to console :)

# initiating the propositional symbols:
ColMustard = Symbol("ColMustard") # Col. Mustard is in the envelope
ProPlum = Symbol("ProPlum") # Prof. Plum is in the envelope
MsScarlet = Symbol("MsScarlet") # Ms. Scarlet is in the envelope
characters = [ColMustard, ProPlum, MsScarlet]

ballroon = Symbol("ballroon") # the Ballroon room is in the envelope
kitchen = Symbol("kitchen") # the Kitchen room is in the envelope
library = Symbol("library") # the Library room is in the envelope
rooms = [ballroon, kitchen, library]

knife = Symbol("knife") # the Knife weapon  is in the envelope
revolver = Symbol("revolver") # the Revolver weapon  is in the envelope
wrench = Symbol("wrench") # the Revolver Wrench  is in the envelope
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol): # checking if the model_check is true. (False here mean that we don't know if the model check is True)
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)): # now checking if the model_check is not-true (resulting w/ True here meanign that we also don't know if the model check is False for certain)
            print(f"{symbol}: MAYBE") # the maybe here is because of the 'not' above
        else:
            termcolor.cprint(f"{symbol}: NO", "red")





knowledge = And(                    #(And) since there are multiple things that we know are true, as depicted below:
    Or(ColMustard, ProPlum, MsScarlet),     # only one of these people is in the envelope
    Or(ballroon, kitchen, library), # only one of these rooms is in the envelope
    Or(knife, revolver, wrench),    # only one of these weapons is in the envelope
)


# Eliminating some 'Maybes'
knowledge.add(Not(ColMustard)) # we can add new data to the knowledge (here we know that Col. mustard is not in the envelope)
knowledge.add(Not(kitchen)) 
knowledge.add(Not(revolver)) 


knowledge.add(Or(
    Not(MsScarlet), Not(library), Not(wrench)
))


knowledge.add(Not(ProPlum))



print(knowledge.formula())
# (ColMustard ∨  ProPlum ∨  MsScarlet) ∧ (ballroon ∨  kitchen ∨  library) ∧ (knife ∨  revolver ∨  wrench) ∧ (¬ColMustard) ∧ (¬kitchen) ∧ (¬revolver)

# print(model_check(knowledge, MsScarlet))

print(check_knowledge(knowledge)) # not enough data for solution at this point!
# ColMustard: NO
# ProPlum: NO
# MsScarlet: YES
# ballroon: MAYBE
# kitchen: NO
# library: MAYBE
# knife: MAYBE
# revolver: NO
# wrench: MAYBE


# continue from: https://www.youtube.com/watch?v=5NgNicANyqM&t=9856s