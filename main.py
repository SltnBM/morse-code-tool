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

def morse_to_text(morse):
    morse_dict_reversed = {v: k for k, v in MORSE_CODE_DICT.items()}
    words = morse.split(" / ")
    decoded_words = []
    for word in words:
        chars = [morse_dict_reversed.get(code, '') for code in word.split()]
        decoded_words.append("".join(chars))
    return " ".join(decoded_words)

try:
    while True:
        print("\n--- Morse Code Translator ---")
        print("1. Text to Morse")
        print("2. Morse to Text")
        print("3. Exit")
        choice = input("Choose (1/2/3): ")

        if choice == '1':
            text = input("Enter text: ")
            print("Morse Code:", text_to_morse(text))
        elif choice == '2':
            morse = input("Enter Morse code (letters: space, words: /): ")
            print("Text:", morse_to_text(morse))
        elif choice == '3':
            break
        else:
            print("Invalid choice!")
except KeyboardInterrupt:
    print("\nExiting, Good Bye.")
