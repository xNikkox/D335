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
#fix hints
#1
#In the line result = target_char.replace(t_char.keys, t_char.values), the replace() method is being used on target_char, which is a single character obtained from the for loop. 
#however, replace() is a string method and cannot be directly applied to a single character. It expects a string as the target.
#2
#The keys and values in t_char.keys and t_char.values should be functions (t_char.keys() and t_char.values()) to retrieve the keys and values of the t_char dictionary correctly.