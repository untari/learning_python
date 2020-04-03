 is_substring('oo', 'book')
True
 is_substring('pony', 'abracadabra')
False
 is_substring('dab', 'abracadabra')
True

def is_substring(substring, string):
    index = 0
    while index < len(string):
        if string[index : index + len(substring)] == substring:
            return True
        index += 1
    return False

#count substrings
count_substring('AAAA', 'AA') #to solve this problem use this code
if string[index : index + len(target)] == target:
    total += 1
    index += len(target)
else:
    index += 1

 #locating function
    def locate_first(string, sub):
        index = 0
        while index < len(string):
            if string[index: index + len(sub)] == sub:
                return index
            else:
                index += 1
        return -1

    #locate_all function
    >> > locate_all('cookbook', 'ook')
    [1, 5]
    >> > locate_all('yesyesyes', 'yes')
    [0, 3, 6]
    >> > locate_all('the upside down', 'barb')
    []


    def locate_all(string, sub):
        matches = []
        index = 0
        while index < len(string):
            if string[index: index + len(sub)] == sub:
                matches.append(index)
                index += len(sub)
            else:
                index += 1
        return matches


#substring in loops
 string = 'waffles'
 substring = 'ff'
 string[0 : 0 + len(substring)] == substring
False
 string[1 : 1 + len(substring)] == substring
False
 string[2 : 2 + len(substring)] == substring
True