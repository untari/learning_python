while True:
    print("help! i'm trapped in an infinite loops")
    #to break  the loops click ctrl+ c

    #or using break statement
    def no_repeating():
        words = []
        while True:
            word = input("Tell me a word: ")
            if word in words:
                print("You told me that word already!")
                break
            words.append(word)
        return words