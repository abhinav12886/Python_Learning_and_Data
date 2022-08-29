# class Employee:
#
#     def __init__(abc, vname, vage):
#         abc.name = vname
#         abc.age = vage
#
#     def myfunc(abc):
#         print(f"my name is {abc.name} and my age is {abc.age} ")
#
#
# abhi = Employee("abhinav", 21)
# abhi.myfunc()

# -------------------------------PRACTICE  QUESTIONS-----------------------
"""
Q1. A flashcard is a card having information on both sides, which can be used as an 
      aid in memorization. Flashcards usually have a question on one side and an 
      answer on the other. Particularly in this article, we are going to create 
      flashcards that will be having a word and its meaning.
"""


class Flashcards:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"the entered word is  {self.word}  and its meaning is {self.meaning}"


flash = []
while True:
    word = input("Enter the word: ")
    meaning = input("Enter the meaning of that word: ")
    flash.append(Flashcards(word, meaning))

    option = int(input("Press 0 to enter the next word and its meaning else to exit print any other key: "))

    if option:
        break

for i in flash:
    print(">", i)

