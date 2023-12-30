"""
1. Implement the function unique_in_order which takes as argument a sequence and
returns a list of items without any elements with the same value next to each other and
preserving the original order of elements.
For example:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3]) == [1,2,3]
"""
import ast

def unique_in_order(arg):                   # function to remove nearby duplicates
    result = []                             # initialize empty list to store the result
    arg = list(arg)                         # to convert the any type of input into list 
    result.append(arg[0])                   # append first element to the result list
    i=1                                     # initialising variable i = 1 for iteration
    while(i<len(arg)):                      # to iterate through full arg
        if arg[i] in result:                # check the current element is already present in the list or not
            if arg[i] != arg[i-1]:          # if the element is present, then check previous element is same as current element
                result.append(arg[i])       # if previous and current element is not equal then append it to the result
                i+=1                        # increment the i value
            else:                           # if it is same, then move to next iteration
                i=i+1
        else:
            result.append(arg[i])           # if the current element is not present in the result list then append the current element to the result list
            i+=1
        
    print(result)                           # print the output result list

def get_sequence_from_user():               # function the check the given input is valid or not
    user_input = input("Enter a sequence (list or string or tuple or etc.): ")  
    try:                                            # it will check the given input is valid or not
        sequence = ast.literal_eval(user_input) 
        return sequence                             # it will the input sequence
    except (SyntaxError, ValueError) as e:          # if the input sequence is not valid it will show the error
        print(f"Error: {e}")
        return None
inputSequence = get_sequence_from_user()            
unique_in_order(inputSequence)

"""
output:

Enter a sequence (list or string or tuple or etc.): 'AAAABBBCCDAABBB'
['A', 'B', 'C', 'D', 'A', 'B']

Enter a sequence (list or string or tuple or etc.): 'ABBCcAD'
['A', 'B', 'C', 'c', 'A', 'D']

Enter a sequence (list or string or tuple or etc.): [1,2,2,3,3]
[1, 2, 3]



"""
