import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    #encode string to get hex code
    raw_bytes = next_lang.encode(encoding, errors = errors)
    #get "next_lang"-string as hex code, decode it to get char-string
    cooked_string = bytearray.fromhex(next_lang).decode()

    print(raw_bytes, "<===>", cooked_string)

languages = open("b_languages.txt", encoding = "utf-8")

main(languages, input_encoding, error)
