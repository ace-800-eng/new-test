import os
print("Hello, World!")
print("current dir: ",os.getcwd())
print(os.listdir())
if os.path.exists("test.txt"):
    with open("test.txt", "r") as f:
        print(f.read())