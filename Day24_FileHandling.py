file = open("texting.txt")
# print(file.read())


with open("texting.txt", mode = "a") as filee:
    filee.write("Tehman\n")
