import tkinter as tk
from tkinter import messagebox

# Define keyMatrix globally
keyMatrix = [[0] * 3 for i in range(3)]

def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

def encrypt(messageVector):
    cipherMatrix = [[0] for i in range(3)]  # Define cipherMatrix locally
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26
    return cipherMatrix

def HillCipher(message, key):
    getKeyMatrix(key)
    messageVector = [[0] for i in range(3)]  # Define messageVector locally
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
    cipherMatrix = encrypt(messageVector)
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
    return "".join(CipherText)

def encrypt_message():
    message = entry_plain.get()
    key = entry_key.get()

    if not message or not key:
        messagebox.showwarning("Warning", "Please enter both message and key.")
        return

    if len(message) != 3:
        messagebox.showerror("Error", "Message must be 3 characters long.")
        return

    if len(key) != 9:
        messagebox.showerror("Error", "Key must be 9 characters long.")
        return

    encrypted_text = HillCipher(message, key)
    result_label.config(text="Ciphertext: " + encrypted_text)

# Creating GUI
root = tk.Tk()
root.title("Hill Cipher")
root.geometry("400x200")  # Set window size

label_plain = tk.Label(root, text="Enter Message (3 characters):", font=("Arial", 12))
label_plain.pack()
entry_plain = tk.Entry(root, font=("Arial", 12))
entry_plain.pack()

label_key = tk.Label(root, text="Enter Key (9 characters):", font=("Arial", 12))
label_key.pack()
entry_key = tk.Entry(root, font=("Arial", 12))
entry_key.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message, font=("Arial", 12))
encrypt_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
