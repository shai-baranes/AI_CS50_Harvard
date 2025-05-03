from logic import *

people = ["Gilderoy", "Pomona", "Minerva", "Horace"]
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

symbols = []

knowledge = And() # initiating empty knowledge (later adding new facts)

for person in people:
    for house in houses:
        symbols.append(Symbol(f"{person}{house}")) # we get all possible combinations of a people per house




 ####################################################################################################
 #                                                                                                  #
 #          Knowledge as derived from the 'FIRST' claim (refer to the 'bmp' snapshot file):         #
 #                                                                                                  #
 ####################################################################################################


# Each person belongs to a house.
for person in people:  # adding the knowledge per person, knowing that each can belong to only one house from the list.
    knowledge.add(Or(
        Symbol(f"{person}Gryffindor"),
        Symbol(f"{person}Hufflepuff"),
        Symbol(f"{person}Ravenclaw"),
        Symbol(f"{person}Slytherin")
    ))


# Or(Symbol("GilderoyGryffindor"), Symbol("GilderoyHufflepuff"), Symbol("GilderoyRavenclaw"), Symbol("GilderoySlytherin"),)
# +  (each Or claim is added to the And() knowledge)

# Or(Symbol("PomonaGryffindor"), Symbol("PomonaHufflepuff"), Symbol("PomonaRavenclaw"), Symbol("PomonaSlytherin"),)
# +
# Or(Symbol("MinervaGryffindor"), Symbol("MinervaHufflepuff"), Symbol("MinervaRavenclaw"), Symbol("MinervaSlytherin"))
# +
# Or(Symbol("HoraceGryffindor"), Symbol("HoraceHufflepuff"), Symbol("HoraceRavenclaw"), Symbol("HoraceSlytherin"))


# Only one house per person. (2 different houses, or more, cannot belong to the same person)
for person in people:
    for h1 in houses:
        for h2 in houses:
            if h1 != h2:
                knowledge.add(
                    Implication(Symbol(f"{person}{h1}"), Not(Symbol(f"{person}{h2}")))  # results with both way implications
                )

# Only one person per house. (2 different persons, or more, cannot belong to the same house)
for house in houses:
    for p1 in people:
        for p2 in people:
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(f"{p1}{house}"), Not(Symbol(f"{p2}{house}")))
                )





 ####################################################################################################
 #                                                                                                  #
 #         Knowledge as derived from the 'SECOND' claim (refer to the 'bmp' snapshot file):         #
 #                                                                                                  #
 ####################################################################################################
knowledge.add(
    Or(Symbol("GilderoyGryffindor"), Symbol("GilderoyRavenclaw"))
)



 ####################################################################################################
 #                                                                                                  #
 #          Knowledge as derived from the 'THIRD' claim (refer to the 'bmp' snapshot file):         #
 #                                                                                                  #
 ####################################################################################################
knowledge.add(
    Not(Symbol("PomonaSlytherin"))
)



 ####################################################################################################
 #                                                                                                  #
 #          Knowledge as derived from the 'FORTH' claim (refer to the 'bmp' snapshot file):         #
 #                                                                                                  #
 ####################################################################################################
knowledge.add(
    Symbol("MinervaGryffindor")
)


for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)

these are the valid pairs, person per house given this knowledge:
# GilderoyRavenclaw
# PomonaHufflepuff
# MinervaGryffindor
# HoraceSlytherin










# -----------------------------------------------------------
# def header_creator(text):
#   print(f" {'#'*100}")    
#   print(" #", " "*96, "#")
#   print(" #", " "*int((95-len(text))/2), text, " "*int((94-len(text))/2), "#")
#   print(" #", " "*96, "#")
#   print("", "#"*100)

# header_creator("Knowledge as derived from the 'FORTH' claim (refer to the 'bmp' snapshot file):")


