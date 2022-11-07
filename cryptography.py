from steganography import Steganography


def main_menu():
    s = Steganography()
    menu = [ 'Encode a message        - E\n',
             'Decode a message        - D\n',
             'Print a message         - P\n',
             'Show an image           - S\n',
             'Quit the program        - Q\n']
    while True:
        print("\nChoose an operation:")
        for i in menu: print(i, end='')
        op = input('\n').upper()
        if op == 'Q':
            break
        if op != 'P':
            filein = input("Choose an image file:\n")
        if op == 'E':
            fileout = input("Choose an output image file:\n")
            s.encode(filein, fileout, get_message(), get_codec())
            s.print()
        elif op == 'D':
            s.decode(filein, get_codec())
            s.print()
        elif op == 'P':
            s.print()
        elif op == 'S':
            s.show(filein)


def get_message():
    message = ''
    while True:
        message = input("Please type a message, use only ASCII characters:\n")
        try:
            for char in message: code = ord(char)
            if len(message) > 0: break
        except:
            print(f"The message contains not an ASCII character {char}!!!")
    return message


def get_codec():
    while True:
        choice = input("\nChoose a codec method or return to the main menu:\n\
Steganography only               - S\n\
Steganography & Caesar Cypher    - C\n\
Steganography & Huffman Codes    - H\n\
Return to the main menu          - Q\n").upper()

        if choice == 'Q':
            break
        elif choice == 'S':
            return 'binary'
        elif choice == 'C':
            return 'caesar'
        elif choice == 'H':
            return 'huffman'

if __name__ == '__main__':
    main_menu()