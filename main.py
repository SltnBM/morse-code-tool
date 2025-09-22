MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

def text_to_morse(text):
    words = text.upper().split(" ")
    morse_words = []
    for word in words:
        morse_chars = [MORSE_CODE_DICT.get(ch, '') for ch in word]
        morse_words.append(" ".join(morse_chars))
    return " / ".join(morse_words)

while True:
    print("\n--- Morse Code Translator ---")
    print("1. Text to Morse")
    print("2. Exit")
    choice = input("Choose (1/2): ")

    if choice == '1':
        text = input("Enter text: ")
        print("Morse Code:", text_to_morse(text))
    elif choice == '2':
        break
    else:
        print("Invalid choice!")
