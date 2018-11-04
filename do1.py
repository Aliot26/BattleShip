def main():
    animal = input("Animal(cat/dog): ")
    age = int(input("Age of animal: "))
    result = animalYears(age, animal)
    print("Age of the", animal, "is ", result)


def animalYears(humanYears, animal):
    years = 0
    if animal == "dog":
        k = 5
    elif animal == "cat":
        k = 4
    i = 1
    while i <= humanYears:
        if i == 1:
            years += 15
        elif i == 2:
            years += 9
        else:
            years += k
        i += 1
    return years


main()
