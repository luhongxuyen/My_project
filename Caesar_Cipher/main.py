import string
from ascii_art import logo

def caesar(message: str, shift: int, direction= 1) -> str:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    result = ""
    not_char = ""

    if direction == 0:
        shift *= -1

    for i in message:
        if (i not in list(string.ascii_lowercase)) or (i not in list(string.ascii_lowercase)):
            not_char += i
            message = message.replace(i,"")

    lower_mapping = str.maketrans(lowercase, lowercase[shift:] + lowercase[:shift])
    
    upper_mapping = str.maketrans(uppercase, uppercase[shift:] + uppercase[:shift])

    result = message.translate(lower_mapping).translate(upper_mapping)

    if direction == 1:
        display = "encrypt"
    else:
        display = "decrypt"

    return f"The {display} text is: {result + not_char}"

def main():
    print(logo)
    go_again = True

    while go_again:
        try:
            direction = int(input("Type 1 to encrypt, type 0 to decrypt (default 1):\n"))
            message = input("Type your message:\n")
            shift = int(input("Type the shift number:\n"))
            
            if shift > 26:
                shift %= 26
            
            if direction > 1 or direction < 0:
                direction = 1
            
            print(caesar(message= message, shift= shift, direction= direction))

            restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

            if restart == "no":
                go_again = False
                print("Goodbye.")
            elif restart == "yes":
                continue
            else:
                print("I don't know what you mean... I'll break this for sure")
                go_again = False

        except ValueError:
            print("Wrong format! Please try again...")
    

if __name__ == "__main__":
    main()
