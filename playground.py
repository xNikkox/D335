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
