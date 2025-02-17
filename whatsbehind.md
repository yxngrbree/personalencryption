Fepo Encryption Software 🛡️🔐
Overview
Fepo Encryption Software is a simple Python program that encrypts and decrypts messages using a custom character substitution method. Users can choose between encryption and decryption through a menu-driven interface.

How It Works
1. User Menu
When the program starts, it displays a welcome message and presents two options:

1. Encrypt a message
2. Decrypt a message
The user inputs their choice, and the program proceeds accordingly.

2. Encryption Process
The user enters a message to be encrypted.
Each character in the message is mapped to a unique encoded string from a predefined dictionary.
The encrypted message is displayed for the user to copy.
3. Decryption Process
The user enters an encrypted message.
The program reads the message in fixed-length chunks.
Each chunk is translated back to its original character using a decryption dictionary.
The decrypted message is displayed.
Code Breakdown
1. Encryption
Converts each character into a unique symbol sequence.
Uses multiple if conditions to map characters.
2. Decryption
Reads the encrypted text in segments.
Uses a dictionary lookup to reconstruct the original message.
Potential Improvements
✔️ Fix undefined message variable in encryption.
✔️ Replace multiple if statements with dictionary lookups for efficiency.
✔️ Expand character set to include punctuation and special symbols.
✔️ Improve handling of variable-length encrypted sequences.

Usage
Run the script and follow the on-screen instructions:

bash
python fepo_encryption.py


Contributing
Feel free to fork this project, suggest improvements, or report issues! 🚀

License
This project is open-source and available under the MIT License.
