import tkinter as tk
from tkinter import Tk, simpledialog, messagebox
import json
from datetime import datetime, timezone
from cryptography.fernet import Fernet

# Generate a secret key (save this securely and reuse it for both encryption and decryption)
secret_key = Fernet.generate_key()
cipher = Fernet(secret_key)


def generate_activation_key(expiration_hours: int) -> str:
    """Generate an activation key with expiration time in hours."""
    # Include the creation time and expiration duration
    key_data = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "expiration_hours": expiration_hours,
    }
    # Convert the data to a JSON string and encrypt it
    encrypted_key = cipher.encrypt(json.dumps(key_data).encode())
    return encrypted_key.decode()


def generate_activation_keys():
    n = int(number_entry.get())
    d = int(days_entry.get())
    keys = [generate_activation_key(24 * d) for _ in range(n)]
    # Save keys to a file
    with open("activation_keys.json", "w") as f:
        json.dump({"keys": {key: None for key in keys}}, f)  # None means not yet used

    with open("secret_key.txt", "wb") as s:
        s.write(secret_key)

    messagebox.showinfo(
        "Title", f"{n} activation keys generated and saved to activation_keys.json"
    )


root = Tk()

root.geometry("600x400")

tk.Label(root, text="KEY GENERATOR").grid(row=0, pady=40, column=1)
frame = tk.Frame(root)
frame.grid(row=1, pady=10)
tk.Label(frame, text="Number of Days").grid(row=0, column=0, pady=10, padx=10)
days_entry = tk.Entry(frame)
days_entry.grid(row=0, column=1)
tk.Label(frame, text="Number of keys").grid(row=1, column=0, pady=10, padx=10)
number_entry = tk.Entry(frame)
number_entry.grid(row=1, column=1)


btn_submit = tk.Button(
    root, text="Click me", padx=18, pady=8, command=generate_activation_keys
)

btn_submit.grid(row=2, padx=100)


root.mainloop()
