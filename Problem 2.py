"""
2. Sorting a given string. Each word in the string will contain a single number. This number
is the position and the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input String will only
contain valid consecutive numbers.
Example:
"is2 Thi1s T4est 3a" --> "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2" --> "Fo1r the2 g3ood 4of th5e pe6ople"
"" --> ""
"""
import re                                                                            # importing regular expression
input_string = input("Enter input(each word contain a number from 1 to 9): ")        # getting input from the user
if input_string == "":                                                               # if input string is empty print empty
    print('""')
else:
    input_list = input_string.split()                                                # splitting the string into list for checking each word contains a number
    sorted_list = sorted(input_list,key=lambda s:int(re.search(r'\d+',s).group()))   # sort the input string based on numbers present in each word
    output = ' '.join([ele for ele in sorted_list])                                  # converting the list into string 
    print(output)

"""

Output:

Enter input(each word contain a number from 1 to 9): is2 Thi1s T4est 3a
Thi1s is2 3a T4est

Enter input(each word contain a number from 1 to 9): 4of Fo1r pe6ople g3ood th5e the2
Fo1r the2 g3ood 4of th5e pe6ople

Enter input(each word contain a number from 1 to 9): e5 c3 d4 a1 b2
a1 b2 c3 d4 e5

Enter input(each word contain a number from 1 to 9): kas3 jega4 jo2 praveen7 priya5
jo2 kas3 jega4 priya5 praveen7

Enter input(each word contain a number from 1 to 9):
""

"""



