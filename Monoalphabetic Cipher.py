#GUI BASED PROJECT FOR MONO-ALPHABETIC ENCRYPTION

import tkinter as tk

def encrypt():
    plaintext = plaintext_entry.get()
    key = key_entry.get()
    encrypted_text = monoalphabetic_encrypt(plaintext, key)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, encrypted_text)

def decrypt():
    ciphertext = ciphertext_entry.get()
    key = key_entry.get()
    decrypted_text = monoalphabetic_decrypt(ciphertext, key)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, decrypted_text)

def monoalphabetic_encrypt(plaintext, key):
    result = ""
    key = key.lower()  # Convert key to lowercase for consistency
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                result += key[ord(char) - ord('a')]
            elif char.isupper():
                result += key[ord(char.lower()) - ord('a')].upper()
            key_index = (key_index + 1) % len(key)  # Move to the next key character
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

def monoalphabetic_decrypt(ciphertext, key):
    result = ""
    key = key.lower()  # Convert key to lowercase for consistency
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                result += chr(key.index(char) + ord('a'))
            elif char.isupper():
                result += chr(key.index(char.lower()) + ord('a')).upper()
            key_index = (key_index + 1) % len(key)  # Move to the next key character
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

root = tk.Tk()
root.title("Monoalphabetic Cipher")

plaintext_label = tk.Label(root, text="Enter Plaintext:")
plaintext_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

plaintext_entry = tk.Entry(root, width=40)
plaintext_entry.grid(row=0, column=1, padx=5, pady=5)

key_label = tk.Label(root, text="Enter Key:")
key_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")

key_entry = tk.Entry(root, width=40)
key_entry.grid(row=1, column=1, padx=5, pady=5)

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
