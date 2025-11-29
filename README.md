# Morse Code Translator
A simple Python script to convert between **Text and Morse Code**.
This script supports encoding text into Morse code and decoding Morse code back into text, with `/` used as a word separator.

---

## Features
- Translate text (letters, numbers, punctuation, and symbols) to Morse code.
- Decode Morse code back to text.
- Interactive menu for user input.
- Show full Morse Code reference table in CLI.
- Handles invalid input gracefully.
- Graceful exit with goodbye message when pressing `Ctrl + C`.

---

## Requirements
- Python 3.x
- No external libraries required.

---

## How to Use
1. Make sure you have Python installed (Python 3 or higher recommended). Download it from [python.org](https://www.python.org/downloads/).
2. Clone this repository
```bash
git clone https://github.com/SltnBM/morse-code-tool.git
```
3. Navigate to the project directory
```bash
cd morse-code-tool
```
4. Run the script using terminal or command prompt
```bash
python main.py
```

---

## Example Usage
### 1. Text → Morse
```plaintext
========== Morse Code Translator ==========
1. Text  → Morse
2. Morse → Text
3. Show Table (Morse Code Reference)
4. Exit
==========================================
Choose an option (1/2/3/4): 1


Enter text: HELLO WORLD
Morse Code: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

### 2. Morse → Text
```plaintext
========== Morse Code Translator ==========
1. Text  → Morse
2. Morse → Text
3. Show Table (Morse Code Reference)
4. Exit
==========================================
Choose an option (1/2/3/4): 2


Format: separate letters with space, words with '/'
Example: .... . .-.. .-.. --- / .-- --- .-. .-.. -..


Enter Morse code: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Text: HELLO WORLD
```

---

## Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

---

## Connect With Me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sultan%20Badra-blue?logo=linkedin\&logoColor=white\&style=flat-square)](https://www.linkedin.com/in/sultan-badra)

---

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
