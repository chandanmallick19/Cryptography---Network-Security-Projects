# A GUI BASED PROJECT ON CAESER CIPHER ENCRYPTION

import tkinter as tk

def encrypt():
    plaintext = plaintext_entry.get()
    shift = int(shift_entry.get())
    encrypted_text = caesar_cipher(plaintext, shift)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, encrypted_text)

def decrypt():
    ciphertext = ciphertext_entry.get()
    shift = int(shift_entry.get())
    decrypted_text = caesar_cipher(ciphertext, -shift)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, decrypted_text)

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

root = tk.Tk()
root.title("Caesar Cipher")

plaintext_label = tk.Label(root, text="Enter Plaintext:")
plaintext_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

plaintext_entry = tk.Entry(root, width=40)
plaintext_entry.grid(row=0, column=1, padx=5, pady=5)

shift_label = tk.Label(root, text="Enter Shift Value:")
shift_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")

shift_entry = tk.Entry(root, width=10)
shift_entry.grid(row=1, column=1, padx=5, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

ciphertext_label = tk.Label(root, text="Enter Ciphertext:")
ciphertext_label.grid(row=3, column=0, padx=5, pady=5, sticky="W")

ciphertext_entry = tk.Entry(root, width=40)
ciphertext_entry.grid(row=3, column=1, padx=5, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

output_label = tk.Label(root, text="Output:")
output_label.grid(row=5, column=0, padx=5, pady=5, sticky="W")

output_text = tk.Text(root, width=40, height=5)
output_text.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()
