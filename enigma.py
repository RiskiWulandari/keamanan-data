from tkinter import Tk, Label, Button, Text, END

class EnigmaMachine:
    def __init__(self, rotor1_pos=0, rotor2_pos=0, rotor3_pos=0):
        # Rotor dan reflektor
        self.rotor1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
        self.rotor2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
        self.rotor3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
        self.reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

        # Posisi awal rotor
        self.rotor1_pos = rotor1_pos
        self.rotor2_pos = rotor2_pos
        self.rotor3_pos = rotor3_pos

        # Invers rotor untuk proses dekripsi
        self.inverse_rotor1 = self.inverse(self.rotor1)
        self.inverse_rotor2 = self.inverse(self.rotor2)
        self.inverse_rotor3 = self.inverse(self.rotor3)

    def inverse(self, rotor):
        inverse_rotor = [0] * 26
        for i, val in enumerate(rotor):
            inverse_rotor[val] = i
        return inverse_rotor

    def shift(self, rotor, pos):
        return rotor[pos:] + rotor[:pos]

    def process(self, text, encrypt=True):
        rotor1 = self.shift(self.rotor1, self.rotor1_pos)
        rotor2 = self.shift(self.rotor2, self.rotor2_pos)
        rotor3 = self.shift(self.rotor3, self.rotor3_pos)

        inverse1 = self.shift(self.inverse_rotor1, self.rotor1_pos)
        inverse2 = self.shift(self.inverse_rotor2, self.rotor2_pos)
        inverse3 = self.shift(self.inverse_rotor3, self.rotor3_pos)

        result = ""
        for char in text.upper():
            if char.isalpha():
                idx = ord(char) - ord('A')

                if encrypt:
                    idx = rotor1[idx]
                    idx = rotor2[idx]
                    idx = rotor3[idx]
                    idx = self.reflector[idx]
                    idx = inverse3[idx]
                    idx = inverse2[idx]
                    idx = inverse1[idx]
                else:
                    idx = inverse1[idx]
                    idx = inverse2[idx]
                    idx = inverse3[idx]
                    idx = self.reflector[idx]
                    idx = rotor3[idx]
                    idx = rotor2[idx]
                    idx = rotor1[idx]

                result += chr(idx + ord('A'))
            else:
                result += char
        return result

def encrypt():
    text = input_text.get("1.0", END).strip()
    encrypted = enigma.process(text, encrypt=True)
    output_text.delete("1.0", END)
    output_text.insert(END, encrypted)

def decrypt():
    text = input_text.get("1.0", END).strip()
    decrypted = enigma.process(text, encrypt=False)
    output_text.delete("1.0", END)
    output_text.insert(END, decrypted)

# Initialize Enigma machine
enigma = EnigmaMachine()

# GUI Setup
root = Tk()
root.title("Enigma Cipher Machine")

# Input Label and Textbox
Label(root, text="Input:").grid(row=0, column=0, padx=10, pady=5)
input_text = Text(root, height=5, width=40)
input_text.grid(row=0, column=1, padx=10, pady=5)

# Output Label and Textbox
Label(root, text="Output:").grid(row=1, column=0, padx=10, pady=5)
output_text = Text(root, height=5, width=40)
output_text.grid(row=1, column=1, padx=10, pady=5)

# Buttons
encrypt_button = Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

decrypt_button = Button(root, text="Decrypt", command=decrypt)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
