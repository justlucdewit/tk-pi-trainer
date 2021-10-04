from functools import partial
import tkinter as tk
import math

with open("pi.txt") as file:
    pi = file.readline()

title = "PI"
score = 0
usr_input = ""

# Create window
window = tk.Tk()
window.geometry("200x250")
window.resizable(False, False)

class GameState:
    # Object for handling the game state and variables
    def __init__(self) -> None:
        self.score = 0
        self.lost = False
        self.user_input = ''
        self.text_input = tk.Label(text = usr_input)
        self.text_score = tk.Label(text = "score: 0")
    
    def handle_input(self, text):
    	if not self.lost:
	        self.add_input(text)
	        self.check_input()
	        if not self.lost:
		        self.update_text_input()
		        self.update_text_score()

    def add_input(self, text):
        self.user_input += text
        self.score += 1

    def check_input(self):
        if not pi.startswith(self.user_input):
            print("Game over")
            self.score -= 1
            self.lost = True

    def update_text_input(self):
        self.text_input.config(text=self.user_input)

    def update_text_score(self):
       	self.text_score.config(text="score: " + str(self.score))

state = GameState()


# Todo: Add height and width properties to tk.Button()
# Display buttons
button_texts = "789456123.0"
buttons = []
for button_text in button_texts:
	buttons.append(tk.Button(window, text=button_text, width=5, height=2, command=partial(state.handle_input, button_text)))

# Position the buttons
for index, button in enumerate(buttons):
	y_pos = 50 + 50 * (index // 3)
	x_pos = 30 + 50 * (index % 3)
	button.place(x = x_pos, y = y_pos)

state.text_input.place(x = 30, y = 30)
state.text_score.place(x = 30, y = 10)

# Set title
window.title(title)

if __name__ == "__main__":
    window.mainloop()
