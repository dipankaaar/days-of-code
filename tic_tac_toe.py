import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"
buttons = []

def check_winner():
    combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    
    for combo in combos:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            return True
    return False

def on_click(i):
    global current_player
    
    if buttons[i]["text"] == "":
        buttons[i]["text"] = current_player
        
        if check_winner():
            label.config(text=f"Player {current_player} Wins 🎉")
            disable_buttons()
        else:
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"Player {current_player}'s Turn")

def disable_buttons():
    for b in buttons:
        b.config(state="disabled")

def reset():
    global current_player
    current_player = "X"
    label.config(text="Player X's Turn")
    for b in buttons:
        b.config(text="", state="normal")

label = tk.Label(root, text="Player X's Turn", font=("Arial", 14))
label.grid(row=0, column=0, columnspan=3)

for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=(i//3)+1, column=i%3)
    buttons.append(btn)

reset_btn = tk.Button(root, text="Reset", command=reset)
reset_btn.grid(row=4, column=0, columnspan=3)

root.mainloop()