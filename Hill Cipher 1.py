import tkinter as tk
from tkinter import messagebox
import numpy as np

def toLowerCase(text):  
    return text.lower()

def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText

def encrypt_HillCipher(plain_text, key_matrix):
    plain_text = plain_text.replace(" ", "").upper()
    key_matrix = np.array(key_matrix).reshape(3, 3)

    if len(plain_text) % 3 != 0:
        plain_text += "X" * (3 - len(plain_text) % 3)

    encrypted_text = ""
    for i in range(0, len(plain_text), 3):
        block = [ord(char) - 65 for char in plain_text[i:i+3]]
        block = np.dot(key_matrix, block) % 26
        encrypted_text += "".join([chr(char + 65) for char in block])

    return encrypted_text

def encrypt_message():
    plain_text = entry_plain.get()
    key_matrix = entry_key.get()

    if not plain_text or not key_matrix:
        messagebox.showwarning("Warning", "Please enter both plaintext and key.")
        return

    try:
        key_matrix = [int(x) for x in key_matrix.split(",")]
        if len(key_matrix) != 9:
            messagebox.showerror("Error", "Key matrix must contain 9 elements separated by commas.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid key matrix format. Please enter numbers separated by commas.")
        return

    encrypted_text = encrypt_HillCipher(plain_text, key_matrix)

    result_label.config(text="Encrypted Text: " + encrypted_text)

# Creating GUI
root = tk.Tk()
root.title("Hill Cipher")
root.geometry("400x200")  # Set window size

label_plain = tk.Label(root, text="Enter Plain Text:", font=("Arial", 12))
label_plain.pack()
entry_plain = tk.Entry(root, font=("Arial", 12))
entry_plain.pack()

label_key = tk.Label(root, text="Enter Key Matrix (9 elements separated by commas):", font=("Arial", 12))
label_key.pack()
entry_key = tk.Entry(root, font=("Arial", 12))
entry_key.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message, font=("Arial", 12))
encrypt_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
