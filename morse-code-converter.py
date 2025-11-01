morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ' ': '/'
}

while True:
    text_from_user = input("Enter text to convert to Morse code: ")
    morse_text = ""

    for x in text_from_user:
        if x.upper() in morse_code:
            morse_text += morse_code[x.upper()] + " "
        else:
            print("Invalid character detected!")
            break
    else:
        print("Morse Code:", morse_text)

    again = input("Do you want to continue? (yes/no): ").strip().lower()
    if again != "yes":
        print("Program ended. Goodbye!")
        break