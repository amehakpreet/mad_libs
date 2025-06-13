# Start game
# Ask users name and welcome them
name = input("Welcome to Mehak's Mad Libs, the title for my Mad Libs is, Pizza Pizza! Today you will be asked to choose series of words and in the end they will be all put together to make a story. May I have your name? ")
print(f"Welcome, {name}! Get ready to laugh!")

# Start game
# Tell them what to choose, and explain
print("")
print("First, choose an adjective.(A decscribing word) ")
word1 = input("Adjective = ").lower().strip() # Makes lowercase and removes the extra spaces

print("")
print("Now choose a nationality, ex: American.")
word2 = input("Nationality = ").capitalize().strip() # Makes the word capitalized

print("")
print("Next choose a person, could be anyone.")
word3 = input("Person = ").capitalize().strip()

print("")
print("Now you're going to choose a noun (Person, place or thing.)")
word4 = input("Noun = ").lower().strip()

print("")
print("Next you're gonna choose an adjective again.")
word5 = input("Adjective = ").lower().strip()

print("")
print("Select another noun.")
word6 = input("Noun = ").lower().strip()

print("")
print("Another adjective")
word7 = input("Adjective =  ").lower().strip()

print("")
print("And oneee last adjective!")
word8 = input("Adjective = ").lower().strip()

print("")
print("Now we need a plural noun, ex: cats (multiple)")
word9 = input("Plural noun= ").lower().strip()

print("")
print("Next we need just a noun")
word10 = input("Noun = ").lower().strip()

print("")
print("Now we need a number, it can be any up to billions!")
word11 = input("Number = ").lower().strip()

print("")
print("Next choose any shape (plural), ex: triangles")
word12 = input("Shapes = ").lower().strip()

print("")
print("Name any food, it could be your favourite!")
word13 = input("Food = ").lower().strip()

print("")
print("Name one more food, different from the other one")
word14 = input(" = ").lower().strip()

print("")
print("Last but not least give any number!")
word15 = input("Number = ").lower().strip()



# The story all put

print("")
print("")
print("")
print("Here is your story you have took part in! :)")
print("")
print("")
print(f"Pizza was invented by a {word1} {word2} chef named {word3}.") # F for variable
print(f"To make a pizza you need to take a lump of {word4}, and make it a thin, round {word5} {word6}.")
print(f"Then you cover it with {word7} sauce, {word8} cheese amd fresh chopped {word9}.")
print(f"Next you have to bake it in a very hot {word10}. When it is done, cut it into {word11} {word12}.")
print(f"Some kids like {word13} pizza the best, but my favourite is the {word14} pizza.")
print(f"If I could, I would eat pizza {word15} times a day!")