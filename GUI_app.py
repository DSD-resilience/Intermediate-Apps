import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My First GUI")
window.minsize(width=300, height=200)

# Add a label widget
label = tk.Label(text="Hello, Tkinter!")
label.pack()

# Run the application
window.mainloop()
