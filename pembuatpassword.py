import tkinter as tk
import random
import string

def generate_password():
    password_length = int(entry_length.get())

    if password_length <= 0:
        label_generated_password.config(text="Panjang harus lebih dari 0")
        return

    password_characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(password_characters) for i in range(password_length))
    entry_generated_password.delete(0, tk.END)
    entry_generated_password.insert(0, generated_password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")  

label_title = tk.Label(root, text="Password Generator")
label_title.pack(pady=10)

label_length = tk.Label(root, text="Panjang Kata Sandi:")
label_length.pack()
entry_length = tk.Entry(root)
entry_length.pack()

button_generate = tk.Button(root, text="Generate", command=generate_password)
button_generate.pack(pady=10)

label_generated_password = tk.Label(root, text="Kata Sandi:")
label_generated_password.pack()
entry_generated_password = tk.Entry(root)
entry_generated_password.pack()

root.mainloop()
