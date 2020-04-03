#slicing
word = "definitely"
length = len(word)
for n in range(length):
    print(n)
    print(word[0:n + 1])


#slicing2
def word_triangle(word):
    length = len(word)
    for n in range(length):
        print(word[:length - n])