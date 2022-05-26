# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True










string1 = "below"
string2 = "elbow"



def find_anagram(word, anagram):
    if (sorted(word) == sorted(anagram)):
         print ("True")
    else:
        print ("False")



find_anagram(string1, string2)

