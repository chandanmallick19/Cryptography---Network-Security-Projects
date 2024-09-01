import tkinter as tk
from tkinter import ttk  # for better-looking widgets (optional)
from Crypto.Cipher import DES

# Disclaimer: DES is not recommended for high-security applications.
# Consider using AES or other more robust algorithms for sensitive data.

def encrypt(text, key):
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    padded_text = pad_text(text)  # Pad text to 8-byte blocks (optional)
    ciphertext = cipher.encrypt(padded_text.encode('utf-8'))
    return ciphertext.hex()  # Convert ciphertext to hexadecimal string

def decrypt(ciphertext, key):
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    plaintext = cipher.decrypt(bytes.fromhex(ciphertext))
    unpadded_text = unpad_text(plaintext)  # Remove padding (optional)
    return unpadded_text.decode('utf-8')

def pad_text(text):  # Optional function for padding (DES requires 8-byte blocks)
    pad_length = 8 - (len(text) % 8)
    return text + (pad_length * chr(pad_length)).encode('utf-8')

def unpad_text(text):  # Optional function to remove padding
    pad_value = text[-1]
    return text[:-int(pad_value)]

def perform_operation(text, key, operation_var):
    operation = operation_var.get()
    try:
        if operation == "encrypt":
            output_text.delete(1.0, tk.END)  # Clear output before encryption
            output_text.insert(tk.END, encrypt(text, key))
        elif operation == "decrypt":
            output_text.delete(1.0, tk.END)  # Clear output before decryption
            output_text.insert(tk.END, decrypt(text, key))
        else:
            raise ValueError("Invalid operation")
    except ValueError as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Error: " + str(e))

def create_gui():
    window = tk.Tk()
    window.title("DES Encryption/Decryption")

    # Input labels and entry fields
    text_label = ttk.Label(window, text="Text to Encrypt/Decrypt:")
    text_label.pack(pady=10)
    text_entry = ttk.Entry(window, width=50)
    text_entry.pack(pady=5)

    key_label = ttk.Label(window, text="Key (8 characters):")
    key_label.pack(pady=10)
    key_entry = ttk.Entry(window, width=10, show="*")  # Hide key characters with asterisks
    key_entry.pack(pady=5)

    # Radio buttons for encryption/decryption
    operation_var = tk.StringVar(value="encrypt")  # Default to encryption
    encrypt_radio = ttk.Radiobutton(window, text="Encrypt", variable=operation_var, value="encrypt")
    encrypt_radio.pack()
    decrypt_radio = ttk.Radiobutton(window, text="Decrypt", variable=operation_var, value="decrypt")
    decrypt_radio.pack()

    # Output label and text area
    output_label = ttk.Label(window, text="Output:")
    output_label.pack(pady=10)
    output_text = tk.Text(window, height=10, width=50)
    output_text.pack()

    # Button to perform encryption/decryption
    button = ttk.Button(window, text="Perform", command=lambda: perform_operation(text_entry.get(), key_entry.get(), operation_var))
    button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
