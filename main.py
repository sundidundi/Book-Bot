def main():
    with open('books/frankenstein.txt') as new_file:
        file_info = new_file.read()
    return file_info

def get_num_text():
    text = str(main())
    return(len(text.split()))

print(get_num_text())
