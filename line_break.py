def breakify (string):
    return "<br>".join(string)

string = "Hello world!"
output = []
index = 0
while index < len(string):
    output.append(string[index])
    index += 1
#find and replace
print(output)
string = 'SPAM!HelloSPAM! worldSPAM!!'
output = []
index = 0
while index < len(string):
    if string[index:index+5] == 'SPAM!':
        index += 5
    else:
        output.append(string[index])
        index += 1
print("".join(output))

#find * replace2
def remove_substring(string, substring):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)



def replace_substring(string, substring, replacement):
    output = []
    index = 0
    while index < (len(string)):
        if string[index:index+len(substring)] == substring:
                  index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "-".join(output)
print(replace_substring('Hot SPAM!drop soup, and curry with SPAM!plant.', 'SPAM!', 'egg'))
print(replace_substring("The word 'definately' is definately often misspelled.", 'definately', 'definitely'))


