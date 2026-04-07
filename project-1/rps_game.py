import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    comp_choice = random.choice(choices)
    
    if user_choice == comp_choice:
        result = "Draw 🤝"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win 🎉"
    else:
        result = "You Lose 😢"
    
    label.config(text=f"You: {user_choice}\nComputer: {comp_choice}\n{result}")

# window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("300x300")

label = tk.Label(root, text="Choose one", font=("Arial", 12))
label.pack(pady=20)

tk.Button(root, text="Rock", command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", command=lambda: play("Scissors")).pack(pady=5)

root.mainloop()
