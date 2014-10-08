
import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

strong = ""
salty = ""
bitter = ""
sweet = ""
fruity = ""

def ask():
    global strong
    strong = raw_input(questions["strong"] + " (y/n)")
    global salty
    salty = raw_input(questions["salty"] + " (y/n)")
    global bitter
    bitter = raw_input(questions["bitter"] + " (y/n)")
    global sweet
    sweet = raw_input(questions["sweet"] + " (y/n)")
    global fruity
    fruity = raw_input(questions["fruity"] + " (y/n)")

ready = raw_input('Are you ready to make your pirate drink? (y/n) ')
while ready != 'y':
    ready = raw_input('Are you ready to make your pirate drink? (y/n) ')
    print "Argsome!"
else:
    ask()

print "I'll make that right up for you!"
print "..."
if strong == "y":
    print ("just a " + random.choice(ingredients["strong"]))
if salty == "y":
    print ("a bit of " + random.choice(ingredients["salty"]))
if bitter == "y":
    print ("a good portion of " + random.choice(ingredients["bitter"]))
if sweet == "y":
    print ("and just one " + random.choice(ingredients["sweet"]))
if fruity == "y":
    print ("garnished with a " + random.choice(ingredients["fruity"]))
print "Voila!"
