import random


class FlashcardAnother:
    def __init__(self):
        self.fruits = {'apple': 'green',
                       'banana': 'yellow',
                       'watermelon': 'red'}

    def quiz(self):
        fruit, colour = random.choice(list(self.fruits.items()))

        print(f"what's the colour of {fruit}?")
        answer = input()

        if answer.lower() == colour:
            print("right guess")
            exit()
        else:
            print("Wrong!!!")

        while True:
            option = int(input("enter 0 guess again and any other number to quit: "))

            if option:
                break

            answer = input("Your guess: ")

            if answer.lower() == colour:
                print("right guess")
                exit()
            else:
                print("Wrong!!!")


obj = FlashcardAnother()
obj.quiz()
