from sys import agrv

script, filename = agrv

print(f"We are going to erase {filename}")
print("If you don't want that hit CTRL-C")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file ...")
target = open(filename, 'w')
