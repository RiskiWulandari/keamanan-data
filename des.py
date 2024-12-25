from tkinter import Tk, Label, Entry, Button, Text, END
from Crypto.Cipher import DES
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt():
    key = key_entry.get().encode('utf-8')
    plaintext = plaintext_text.get("1.0", END).strip()

    if len(key) != 8:
        result_text.delete("1.0", END)
        result_text.insert(END, "Key harus 8 karakter!")
        return

    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    encrypted_text = cipher.encrypt(padded_text.encode('utf-8'))
    encrypted_base64 = base64.b64encode(encrypted_text).decode('utf-8')

    result_text.delete("1.0", END)
    result_text.insert(END, encrypted_base64)

def decrypt():
    key = key_entry.get().encode('utf-8')
    encrypted_text = plaintext_text.get("1.0", END).strip()

    if len(key) != 8:
        result_text.delete("1.0", END)
        result_text.insert(END, "Key harus 8 karakter!")
        return

    try:
        cipher = DES.new(key, DES.MODE_ECB)
        decoded_encrypted_text = base64.b64decode(encrypted_text)
        decrypted_text = cipher.decrypt(decoded_encrypted_text).decode('utf-8').strip()

        result_text.delete("1.0", END)
        result_text.insert(END, decrypted_text)
    except Exception as e:
        result_text.delete("1.0", END)
        result_text.insert(END, f"Error: {e}")

# GUI Setup
root = Tk()
root.title("DES Encryption and Decryption")

# Key input
Label(root, text="Key (8 karakter):").grid(row=0, column=0, padx=10, pady=5)
key_entry = Entry(root, width=30)
key_entry.grid(row=0, column=1, padx=10, pady=5)

# Plaintext/Encrypted input
Label(root, text="Input:").grid(row=1, column=0, padx=10, pady=5)
plaintext_text = Text(root, height=5, width=40)
plaintext_text.grid(row=1, column=1, padx=10, pady=5)

# Result output
Label(root, text="Output:").grid(row=2, column=0, padx=10, pady=5)
result_text = Text(root, height=5, width=40)
result_text.grid(row=2, column=1, padx=10, pady=5)

# Buttons
encrypt_button = Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=3, column=0, padx=10, pady=10)

decrypt_button = Button(root, text="Decrypt", command=decrypt)
decrypt_button.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
