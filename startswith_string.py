def start_K (s):
    if s[0] =="K":
        return True
    else:
        return False
    #or
def start_K (s):
    return s[0] == "K"

def starts_with(s1, s2):
    if s1[0] == s2[0]:
        return True
    else:
        return False

#Define function with two parameters
def start_with(long, short):
    for position in range(len(short)):
        if long [position] != short [position]:
            return False
        return True

#startswith and method
"define".startswith("def")
#True
"define".startswith("ine")
#False

#slicing/string
def start_with(long, short):
    if long[0:len(short)] == short:
        return True
    else:
        return False

#string predict
def possible_tag(word):
        if word.startswith("<") and word.endswith(">"):
            print(word, "could maybe be an HTML tag")
        else:
            print(word, "is definitely not an HTML tag (but might contain one)")