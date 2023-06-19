word = input()
password = ''

#character key and value dictionary 
t_char = {
    "i": 1,
    "a": "@",
    "m": "M",
    "B": 8,
    "s": "$"
    }



#function to find and replace character
def parse_string(string, target_char):
    result = []
    string_list = list(target_char) 
    for i in range(len(string_list)):
        if string_list[i] == t_char.keys[i]:
            string_list[i] = t_char.values[i]
    
    
#convert the list back to a string
new_string = "".join(string_list)
print(new_string) 
