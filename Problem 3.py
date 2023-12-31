"""
3. An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an
isogram. Assume the empty string is an isogram. Ignore the letter case.
Example:
is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false
"""

def is_isogram(word):                                                               # function to check input string is an Isogram    
    dict={}                                                                         # initialising an empty dict
    for char in word:                                                               # iterate through whole string
        if char not in dict:                                                        # check the character is present in the dict
            dict[char] = 1                                                          # assign the value to that character
        else:
            return False                                                            # if the character is already present it returns false  
    return True
input_string = input("Enter the input: ")                                           # getting input from the user
if input_string == "":                                                              # if input string is empty we assume that the string is an Isogram       
    print("You entered Empty String. Therefore, Given String is an Isogram")        
else:
    input_string = input_string.lower()                                             # for avoiding the letter case
    result = is_isogram(input_string)                                               # function call to check input string is an Isogram
    print(result)
    if result:                                                                      # if the is_isogram function returns true given string is an isogram
        print(f"Given String '{input_string}' is an Isogram")
    else:                                                                           # else is_isogram function returns false given string is not an isogram
        print(f"Given String '{input_string}' is not an Isogram")

"""

Output:

Enter the input: Dermatoglyphics
True
Given String 'dermatoglyphics' is an Isogram

Enter the input: aba
False
Given String 'aba' is not an Isogram

Enter the input: moOse
False
Given String 'moose' is not an Isogram

Enter the input:
You entered Empty String. Therefore, Given String is an Isogram

"""


