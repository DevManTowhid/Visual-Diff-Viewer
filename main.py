import tkinter as tk
from tkinter import scrolledtext

def open_left_file():
    file_path = tk.filedialog.askopenfilename(title="Select Left File")


print("Text Diff Viewer Starting...")
root = tk.Tk()
root.geometry("1200x1200")
root.title("Visual Text Diff Viewer")

# Label on top
tk.Label(root, text="Left File").grid(row=0, column=0, padx=10, pady=5)

# Left-side text box
left_text = scrolledtext.ScrolledText(root, width=60, height=20)
left_text.grid(row=1, column=0, padx=10, pady=5)

# Right label
tk.Label(root, text="Right File").grid(row=0, column=1, padx=10, pady=5)

# Right-side text box
right_text = scrolledtext.ScrolledText(root, width=60, height=20)
right_text.grid(row=1, column=1, padx=10, pady=5)

root.mainloop()
