"""
[TBD], my game that will include a decent amount of randomness and selection,
as well as novel encounters and maybe a loot system!
Why not, this could be a time to showcase some creativity and create some
interesting characters and interaction. I like games, games can be fun if you
put some thought into them so why not. I'll try to make a fun game.
"""

# import modules, will need os for sure
import os

# things to search for:
#- function or perameter to allow one char to be missing from string (if statement?)
#- random function types, what can i utilize here?
#- how to lock the user terminal and set sizes (proper display of text w/o wrap)
#
#
#

#---------------------------USEFUL COMMANDS-------------------------------------
# os.get_terminal_size()




################################# CHAR IDEAS ##################################
## + perhaps a vendor or beneficial stranger that appears quite seldomly and
## rewards the player
##
## + there's this black dude, right. so he's hanging out crouching japanese style
## and he's looking pretty solemn and you really don't feel like you could even
## be around him because his presence is so...BIG. but he's a medium sized dude,
## just muscley as heck. reminds me of raiden from mortal kombat.
##
## + dude named bonadio. actually means good day in italian so perhaps only when
## weather is right.
##
## + knowledgable cat character. obligatory feline race.
##
## +
##






################################# PLAYER COMMANDS #############################
## -- (command) and plain text is mostly unrecognized
## -- perhaps having a connection between commands can work with if statements
##
## + (where) am i?
##
## + (what)-(is)-(object)? >>
##
## + (viewstats) >> realistic layout for nice viewing of stats
##
## +
##



# Player Class, it can either contain the variable for a health system or health
# variable. Should have a gear and initial loadout method, as well as a function
# for equipping.
class Player(self, **kwargs): # kwargs is a placeholder for now
    """It's you."""

    # constructor for you
    def __init__(self, name, race, class):
        pass

    # this will be for the starting atttributes
    def initattr():
        pass


# Monster Class, can roll for species upon generation? Each species would have
# it's own attributes (attr)
class Monster(self, **kwargs):
    pass


# think this is where i will store a local dictionary.
class Room(self, where, dic):
    localdic = {}
    pass


# NPC Class, perhaps could incorporate disposition but that's a lot of coding.
# Boy I'm already getting ambitious. Could be a rewarding side project however
# and a good showcase of my potential work.
class NPC(self, where):
    pass


# Wherever you start, I want it to be revisited at some point, maybe a fountain
# whose liquid changes upon every encounter. Another thought was for this game
# to be loopable, either before or after resetting. Could have persistent items
# potentially.


# name gen function, no reason why not. hell i could attempt to scrub name
# databases based on user input if i wanted. i do need to get into that.


# one of the conditions for this game in the book is that this code must be
# self-contained, and in this case means all if must have else and air tight.
# so how can i best work with those constraints?



# COMBAT SYSTEM
# using loops i would use a tick system. so buffs etc will reduce the number
# to reach in order to perform an action in combat (damage).
# for example, Player reaches an action at 1.5(ticks). Vagabond reaches their
# action potential in 0.8(ticks). When in combat they will both tick up in
# increments of 0.1 until one of the characters reaches an action potential.
# this happens behind the scenes, there is no wait time. this is just a method
# of organization.


# SPEECH SYSTEM
# although combat is very much a part of the game, non-violence should be rewarded
# incorporated.
# layered speech system 'look' -> "at what?" -> 'tree' ->
# "there aren't any trees around...". "else?" -> 'move to door' -> -enters new area-

def detectinput(input):
    # this will be the speech function, could be a mistake to have so many
    # nested functions.

    # function for looking around, compares against a local dictionary stored
    # in the room object
    def look(what):
        if what in localdic:
            print(localdic[what])
            pass
        else:
            print(f"{what} doesn't seem to be around.")
            pass


    # shouldn't need any inputs for it to work
    def inventory():
        pass


    # for using things and pushing buttons etv
    def use(object):
        # checks if item is usable and then activates it
        pass


    def attack(with=equippedwep, what):
        # takes a weapon



    # creating a dictionary for recognized words
    # will i have to define functions for each of these or is there an easier solution
    workingwords = {"look":look(),
                    "inventory":inventory(),
                    "use":
                    "attack":
                    "help":
                    "stats":
                    "move":
                    "what":



    if input.isalnum():
        words = input.split(' ')
        recwords = [words for words in workingwords]
    else:
        print(f"{input} is not recognized.")
        pass
