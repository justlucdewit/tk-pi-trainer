from functools import partial
import tkinter as tk
import math

title = "PI Trainer"
score = 0
usr_input = ""

# Create window
window = tk.Tk()
window.geometry("200x250")

# Add text
text_input = tk.Label(text = usr_input)
text_score = tk.Label(text = "score: 0")

def input_num(text):
	global score
	global usr_input

	score += 1
	usr_input += text
	text_score.config(text = "score: " + str(score))
	text_input.config(text = usr_input)


# Todo: Add height and width properties to tk.Button()
# Display buttons
button_texts = "789456123,0"
buttons = []
for button_text in button_texts:
	buttons.append(tk.Button(window, text=button_text, width=5, height=2, command=partial(input_num, button_text)))

# Position the buttons
for index, button in enumerate(buttons):
	y_pos = 50 + 50 * (index // 3)
	x_pos = 30 + 50 * (index % 3)
	button.place(x = x_pos, y = y_pos)

text_input.place(x = 30, y = 30)
text_score.place(x = 30, y = 10)

# Set title
window.title(title)
window.mainloop()