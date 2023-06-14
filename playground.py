success word = input()
password = ''

''' Type your code here. '''
t_char = {
    "i": 1,
    "a": "@",
    "m": "M",
    "B": 8,
    "s": "$"
    }

def parse_string(string, target_char):
    result = []
    for char in string:
        if char == target_char:
            result = target_char.replace(t_char.keys, t_char.values)
            print(result)

#fix hints
#1
#In the line result = target_char.replace(t_char.keys, t_char.values), the replace() method is being used on target_char, which is a single character obtained from the for loop. 
#owever, replace() is a string method and cannot be directly applied to a single character. It expects a string as the target.
#2
#The keys and values in t_char.keys and t_char.values should be functions (t_char.keys() and t_char.values()) to retrieve the keys and values of the t_char dictionary correctly.