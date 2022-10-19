import requests

#query_params is a good way to organize everything without having to clutter up your functions 
# with so many varibles getting passed around!  just like my king of tokyo projecgt.

#can query params have things in it that don't get assigned?  maybe have a default?

query_params = {
    #"id" : 5
    #this is empty now, but let's leave it, in case we want to pass info later. 
}
#this gets all of charmeleons data.  still need to figure out how to dig through it.
#remember to get it working first, get it pretty later.  ideas are worthless without EXECUTION.
id = 5
path = "https://pokeapi.co/api/v2/pokemon/" + str(id)

pokemon5 = requests.get(path, query_params)

print(pokemon5.json())

#how do you get a list of pokemon by number. 
#table of the pokemon, their number, and a list of what games they have been in. 
#I'd like to make this, and I think I can.
#advice from online is to get all the information on the pokemon once, and store it in a list, so you can use it. 




def get_pokemon_info_by_num(params = query_params):
    pass


def print_pokemon_summary_by_num(id_number):
    #handle valid input:
    #retreive the pokemon's information file
    #process that (that is, pull out each element that you are interested in printing)
    # chellenge idea: print what game each is in (use a table that links their codes to the strings of the game!!)
    #make this for AoS units, as well!!!!! <3  Then make youtube videos ABOUT how i did this (to teach others)
    #call it Data and Dev at home 
    pass
