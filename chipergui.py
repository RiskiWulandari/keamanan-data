def enkripsi(plain_text, shift):
    cipher_text =""
    for char in plain_text:
        # Huruf Besar
        if char.isupper():
            cipher_text += chr((ord(char) + shift -65) % 26 + 65)
        # Huruf Kecil 
        elif char.islower():
            cipher_text += chr((ord(char) + shift -97) % 26 + 97)
        else:
            # Karakter Selain Huruf Tetap
            cipher_text += char
    return cipher_text


def deskripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        # Huruf Besar
        if char.isupper():
            plain_text += chr((ord(char) - shift -65) % 26 + 65)
        # Huruf Kecil 
        elif char.islower():
            plain_text += chr((ord(char) - shift -97) % 26 + 97)
        else:
            # Karakter Selain Huruf Tetap
            plain_text += char
    return plain_text



# Interface Pengguna 

def main():
    print("Selamat datang di program kriptografi caesar")
    plain_text = input("Masukkan teks asli (plaintext): ")
    shift = int(input("Masukkan Nilai Pergeseran (1-25): "))

    #Panggil fungsi Enkripsi
    cipher_text = enkripsi(plain_text, shift)
    print("Teks terenkripsi: ", cipher_text)

    #Panggil Fungsi Deskripsi
    deskripsi_text = deskripsi(cipher_text, shift)
    print("Teks terdeskripsi: ", deskripsi_text)

if __name__ == "_main_":
    main()