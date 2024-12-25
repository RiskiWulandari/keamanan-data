from stegano import lsb
import os

def get_image_path():
    """
    meminta pengguna untuk memasukkan path gambar,
    memverivikasi apakah file tersebut ada dan memiliki format yang sesuai.
    """
    while True:
        img_path = input("masukkan path gambar (contoh:D:\\xampp\\htdocs\\keamanan_data\\craft-event1.jpg): ")
        if os.path.exists(img_path) and img_path.endswith(('.png', '.jpg')):
            return img_path
        else:
            print("path gambar tidak valid atau format file salah. silahkan coba lagi")

def hide_message():
    img_path = get_image_path()  # Fixed here: called the function
    message = input("Masukkan pesan rahasia yang akan disembunyikan: ")
    
    try:
        secret = lsb.hide(img_path, message)
        save_path = input("masukkan path untuk menyimpan gambar hasil (contoh:D:\\xampp\\htdocs\\keamanan_data\\hidden_img\\hidden_img.jpg): ")

        if not os.path.exists(os.path.dirname(save_path)):
            print("folder tujuan tidak ada. silahkan cek path yang dimasukkan")
            return
        
        # Simpan gambar hasil
        secret.save(save_path)
        print(f"File berhasil disembunyikan dalam gambar. Gambar disimpan di: {save_path}")
    except Exception as e:
        print(f"Gagal menyimpan gambar: {e}") 

def show_message():
    img_path = get_image_path()  # Fixed here: called the function
    try:
        clear_message = lsb.reveal(img_path)
        if clear_message:
             print(f"pesan tersembunyi : {clear_message}")
        else:
            print("tidak ada pesan tersembunyi dalam gambar")
    except Exception as e:
            print(f"gagal menampilkan pesan dari gambar: {e}")

def main():
    while True:
        print("\nSteganography Tool - Terminal version")
        print("1. sembunyikan pesan")
        print("2. tampilkan pesan")
        print("3. keluar")
        choice = input("pilih opsi (1/2/3): ")

        if choice == '1':
            hide_message()
        elif choice == '2':
            show_message()
        elif choice == '3':
            print("keluar dari program")
            break
        else:
            print("opsi tidak valid")

if __name__ == "__main__":  # Fixed here: corrected the if statement
    main()
