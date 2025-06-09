import tkinter as tk
from tkinter import scrolledtext


print("Text Diff Viewer Starting...")
root = tk.Tk()
root.geometry("900x1200")
root.title("Visual Text Diff Viewer")

# Label on top
tk.Label(root, text="Left File").grid(row=0, column=0, padx=10, pady=5)

# Left-side text box
left_text = scrolledtext.ScrolledText(root, width=60, height=20)
left_text.grid(row=1, column=0, padx=10, pady=5)


root.mainloop()
