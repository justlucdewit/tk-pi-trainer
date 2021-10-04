import tkinter as tk

title = "Tk project"

window = tk.Tk()

# Todo: Add height and width properties to tk.Button()
button_0 = tk.Button(window, text="0")
button_1 = tk.Button(window, text="1")
button_2 = tk.Button(window, text="2")
button_3 = tk.Button(window, text="3")
button_4 = tk.Button(window, text="4")
button_5 = tk.Button(window, text="5")
button_6 = tk.Button(window, text="6")
button_7 = tk.Button(window, text="7")
button_8 = tk.Button(window, text="8")
button_9 = tk.Button(window, text="9")
button_comma = tk.Button(window, text=",")

button_7.place(x=50, y=20)
button_8.place(x=70, y=20)
button_9.place(x=90, y=20)

button_4.place(x=50, y=50)
button_5.place(x=70, y=50)
button_6.place(x=90, y=50)

button_1.place(x=50, y=80)
button_2.place(x=70, y=80)
button_3.place(x=90, y=80)

button_0.place(x=70, y=110)
button_comma.place(x=90, y=110)

window.title(title)
window.mainloop()