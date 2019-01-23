from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C)")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# "w" for write and truncate
#target = open(filename, "w")
# "a" for append, then truncate() is required
target = open(filename, "a")

print("Truncating the file. Goodbye!")
#seek 4th char in file
target.seek(0)
target.truncate()

print("Now I am going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

new_line = "\n"
formatter = "{}{}{}{}{}{}"
target.write(formatter.format(line1, new_line, line2, new_line, line3, new_line))
#target.write(f"{line1}{new_line}{line2}{new_line}{line3}{new_line}")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And finally, we close the file.")
target.close()
