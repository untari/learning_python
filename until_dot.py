until_dot("This is a sentence. This is another.")
'This is a sentence'
until_dot("192.168.200.2")
'192'

def until_dot(s):
    index = 0
    while index < len(s) and s[index] != '.':
        # No dots yet, keep going.
        index += 1
    # We either found a dot or ran out of string.
    return s[:index]

def until_dot(s):
    for index in range(len(s)):
        if s[index] == '.':
            # A dot! Return everything up to here.
            return s[:index]
    # We ran out of string without seeing any dots.
    # Return the whole string.
    return s