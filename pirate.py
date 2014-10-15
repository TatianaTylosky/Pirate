
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

def ask():
    print "Argsome!"
    response = {}
    for key in questions:
        response[key] = raw_input(questions[key] + " (y/n)")
    return response

def make_drink(response):
    for key in response:
        if response[key] == "y":
            print("just a " + random.choice(ingredients[key]))

def ready():
    return raw_input('Are you ready to make your pirate drink? (y/n) ')

while ready() != 'y':
    print("How sad!")

response = ask()
print "I'll make that right up for you!"
print "..."
make_drink(response)

if 'y' not in response.values():
    print "Just straight rum for you then!"
else:
    print "Voila!"
