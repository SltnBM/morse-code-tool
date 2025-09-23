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
        morse_chars = [MORSE_CODE_DICT.get(ch, '?') for ch in word]
        morse_words.append(" ".join(morse_chars))
    return " / ".join(morse_words)

def morse_to_text(morse):
    morse_dict_reversed = {v: k for k, v in MORSE_CODE_DICT.items()}
    words = [w.strip() for w in morse.strip().split(" / ") if w.strip()]
    decoded_words = []
    for word in words:
        chars = [morse_dict_reversed.get(code, '?') for code in word.split()]
        decoded_words.append("".join(chars))
    return " ".join(decoded_words)

if __name__ == "__main__":
    try:
        while True:
            print("\n========== Morse Code Translator ==========")
            print("1. Text  → Morse")
            print("2. Morse → Text")
            print("3. Exit")
            print("==========================================")
            choice = input("Choose an option (1/2/3): ").strip()

            if choice == '1':
                text = input("\nEnter text: ")
                print("Morse Code:", text_to_morse(text))
            elif choice == '2':
                print("\nFormat: separate letters with space, words with '/'")
                print("   Example: .... . .-.. .-.. --- / .-- --- .-. .-.. -..")
                morse = input("Enter Morse code: ")
                print("Text:", morse_to_text(morse))
            elif choice == '3':
                print("\nExiting, Goodbye!")
                break
            else:
                print("\nInvalid choice! Please select 1, 2, or 3.")
    except KeyboardInterrupt:
        print("\n\nExiting, Goodbye!")
