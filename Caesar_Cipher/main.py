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

    """
    str.maketrans()

    Return a translation table usable for str.translate().
    
    If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. 
    
    Character keys will be then converted to ordinals. 
    
    If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. 
    
    If there is a third argument, it must be a string, whose characters will be mapped to None in the result.
    """
    

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
    _continue = True

    while _continue:
        try:
            direction = int(input("Type 1 to encrypt, type 0 to decrypt (default 1):\n"))
            message = input("Type your message:\n")
            shift = int(input("Type the shift number:\n"))
            
            if shift > 26:
                shift %= 26
            
            if direction > 1 or direction < 0:
                direction = 1
            
            print(caesar(message= message, shift= shift, direction= direction))

            restart = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
            
            if restart == "no":
                _continue = False
                print("Goodbye.")
            elif restart == "yes":
                continue
            else:
                print("Sorry, I don't know what you mean! The program will continue.")

        except ValueError:
            print("Wrong format! Please try again...")
    

if __name__ == "__main__":
    main()
