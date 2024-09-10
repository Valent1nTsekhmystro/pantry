import random

number = random.randint(0, 100)

print("Випадкове число вибране спробуй його відгадати!")

while True:
    number_people = (int(input("Напиши число:")))
    if number_people < number:
        print("Спробуй більше число!")
    elif number_people > number:
        print("Спробуй менше число!")
    elif number_people == number:
        print("Молодець ти перміг!!!")
        break
