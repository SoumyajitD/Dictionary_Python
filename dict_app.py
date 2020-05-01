import json
import difflib
from difflib import get_close_matches


#importing the json data file
data=json.load(open("data.json","r"))
word=input("Enter the word: ")

#function to accept the word and check the various conditions
def word_print(string):
    #checing if data is found
    if string in data:
        print(' \n'.join(data[string]))
    #condition to check similarity of two strings namely input string and dicstionary file
    elif len(get_close_matches(string,data.keys()))>0:
        print("Did you mean %s instead? " % get_close_matches(string,data.keys())[0])
        x=input("If Yes, type Y else N: ")
        if x=="Y".casefold():
            print(' \n'.join(data[get_close_matches(string,data.keys())[0].casefold()]))
        elif x=="N".casefold():
            print("The word does not exists.\nPlease try again")
        else:
            print("Your entered data is wrong. Please enter either Y or N ")
    #condition when no similar word is found
    else:
        print("The word does not exist.\nPlease try again.")


word_print(word.casefold())
