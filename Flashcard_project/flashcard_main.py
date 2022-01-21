from flashcard import Flashcard

# it's an empty to store all the flashes.
# f1 = Flashcard("subliminal", "below the threshold of sensation or consciousness")
# f2 = Flashcard("picturesque", "visually attractive, especially in a quaint or charming way.")


# print(Flashcard.flash)

# taking user input

word = input("Enter the word:")
meaning = input("And the meaning:")

f = Flashcard(word, meaning)

while True:
    option = int(input("enter 0 , if you want to add another flashcard : "))
    print(option)

    if option:
        break

    word = input("Enter another word:")
    meaning = input("And the meaning:")

    f = Flashcard(word, meaning)


print(Flashcard.flash)




