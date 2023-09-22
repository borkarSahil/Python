# file = open("main.txt")
# contents = file.read()
# print(contents)
# file.close()

# OR

# READ FILE

# with open("main.txt") as file:
#     contents = file.read()
#     print(contents)

# WRITE FILE
# mode == a for append || w for 1 time

with open("main.txt", mode="a") as file:
    file.write("\nNew Text")

with open("main.txt") as file:
    contents = file.read()
    print(contents)
