from sys import argv

script, filename = argv
txt = open(filename)

print(f"Here is your file: {filename}")
print(txt.read())
txt.close()
#print("Type the filname again:")
#file_again = input("> ")

#txt_again = open(file_again)

#print(txt_again.read())
#close file
#txt_again.close()
