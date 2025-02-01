import tkinter as tk

root = tk.Tk()
root.title("Buttons and Labels Example")

button1 = tk.Button(root, text="PADY")
button1.pack(pady=100)

button2 = tk.Button(root, text="PLACE")
button2.place(x=100, y=50)


root.mainloop()