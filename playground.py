import re

password = input("Enter password: ")

t_char = {
    "i": "1",
    "a": "@",
    "m": "M",
    "B": "8",
    "s": "$"
}

# Function to parse a string and replace characters based on a dictionary
def parse_string(string, target_char):
    new_string = string
    for key, value in target_char.items():
        #Create a regex pattern for the current key, ignoring case sensitivity 
        pattern = re.compile(re.escape(key), re.IGNORECASE)
        #Substitue occurrences of the key with its corresponding value in the string
        new_string = pattern.sub(value, new_string)
    return new_string

#Parse the password using the target character dictionary 
parsed_password = parse_string(password, t_char)
print("Parsed pasword:", parsed_password)

word = input()
parsed_word = parse_string(word, t_char)
