    def name(name):
    return name

def age(age):
    return age

def sam():
    while True:
        name = input("Whats your name?\n")
        age = input("Whats your age?\n")
        print(f"Your name is {name}\nYour age is {age}\n")
        choice = input("Do you wish to continue? Yes/No\n").lower()
        if choice == "no":
            break

sam()