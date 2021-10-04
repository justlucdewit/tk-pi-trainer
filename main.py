import tkinter as tk
import math

title = "PI Trainer"

# Create window
window = tk.Tk()
window.geometry("200x250")

# Todo: Add height and width properties to tk.Button()
# Display buttons
button_texts = "1234567890,"
buttons = []
for button_text in button_texts:
	buttons.append(tk.Button(window, text=button_text, width=5, height=2))

# Position the buttons
for index, button in enumerate(buttons):
	y_pos = 20 + 50 * (index // 3)
	x_pos = 30 + 50 * (index % 3)
	button.place(x = x_pos, y = y_pos)

# Set title
window.title(title)
window.mainloop()