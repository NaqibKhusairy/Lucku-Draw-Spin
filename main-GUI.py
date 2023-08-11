import random
import tkinter as tk
from tkinter import messagebox

def spin():
    global name, winner
    if name:
        random_name = random.choice(name)
        name.remove(random_name)
        result_label.config(text="Participant names:\n" + "\n".join(name))
        messagebox.showinfo("Congrats", "You rolled: " + random_name)
        winner.append(random_name)
        if not name:
            result_label.config(text="No more names to roll.")
            spin_button.config(state=tk.DISABLED)
            winner_list = [f"{i+1}. {w}" for i, w in enumerate(winner[::-1])]
            hidden_label.config(text="Winner List:\n" + "\n".join(winner_list), fg="#27ae60")
            hidden_label.grid_forget()
            messagebox.showinfo("Congratulation", hidden_label.cget("text"))
        else:
            hidden_label.grid_forget()

def on_enter(event):
    event.widget.config(bg="#145c32")
    event.widget.config(fg="white")

def on_enter2(event):
    event.widget.config(bg="#897201")
    event.widget.config(fg="white")

def on_enter3(event):
    event.widget.config(bg="#73221a")
    event.widget.config(fg="white")

def on_leave(event):
    event.widget.config(bg="#229954")
    event.widget.config(fg="black")

def on_leave2(event):
    event.widget.config(bg="#e5be01")
    event.widget.config(fg="black")

def on_leave3(event):
    event.widget.config(bg="#c0392b")
    event.widget.config(fg="black")

def quit_spin():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        root.destroy()

def add_name():
    nama = nama_entry.get()
    if nama:
        name.append(nama)
        nama_entry.delete(0, tk.END)
        result_label.config(text=result_label.cget("text") + "\n" + nama)
        spin_button.config(state=tk.NORMAL)

name = []
winner = []

root = tk.Tk()
root.title("Lucky Draw")

root.geometry("400x350")
root.configure(bg="#2c3e50")

main_frame = tk.Frame(root, bg="#34495e")
main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

nama_label = tk.Label(main_frame, text="Participant Name:", bg="#34495e", fg="white")
nama_label.grid(row=0, column=0, padx=5, pady=5)

nama_entry = tk.Entry(main_frame)
nama_entry.grid(row=0, column=1, padx=5, pady=5)

add_button = tk.Button(main_frame, text="Add Name", command=add_name, bg="#27ae60", fg="black", activebackground="#229954")
add_button.grid(row=1, columnspan=2, padx=5, pady=10)
add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)

spin_button = tk.Button(main_frame, text="Spin", command=spin, bg="#e5be01", fg="black", activebackground="#e74c3c")
spin_button.grid(row=2, columnspan=2, padx=5, pady=10)
spin_button.bind("<Enter>", on_enter2)
spin_button.bind("<Leave>", on_leave2)

result_label = tk.Label(main_frame, text="Participant names:", bg="#34495e", fg="white")
result_label.grid(row=3, columnspan=2, padx=5, pady=10)

quit_button = tk.Button(main_frame, text="Quit", command=quit_spin, bg="#c0392b", fg="black", activebackground="#c0392b")
quit_button.grid(row=4, columnspan=2, padx=5, pady=10)
quit_button.bind("<Enter>", on_enter3)
quit_button.bind("<Leave>", on_leave3)

hidden_label = tk.Label(main_frame, text="", bg="#34495e", fg="white")
hidden_label.grid(row=5, columnspan=2, padx=5, pady=10)

main_frame.grid_rowconfigure(5, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

root.protocol("WM_DELETE_WINDOW", quit_spin)
root.mainloop()
