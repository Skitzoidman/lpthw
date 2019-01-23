import sys, codecs

script, input_encoding, error = sys.argv

file = open("b_languages.txt", "w")

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        #
        raw_bytes = line.strip().encode(encoding, errors = errors)

        file.write(raw_bytes.hex() + '\n')
        return main(language_file, encoding, errors)

languages = open("languages.txt", encoding = "utf-8")

main(languages, input_encoding, error)
