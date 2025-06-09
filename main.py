import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog


def open_left_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            left_text.delete("1.0", tk.END)
            left_text.insert(tk.END, content)

def open_right_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            right_text.delete("1.0", tk.END)
            right_text.insert(tk.END, content)


            
print("Text Diff Viewer Starting...")
root = tk.Tk()
root.geometry("1200x1200")
root.title("Visual Text Diff Viewer")

# Label on top
tk.Label(root, text="Left File").grid(row=0, column=0, padx=10, pady=5)

# Left-side text box
left_text = scrolledtext.ScrolledText(root, width=60, height=20)
left_text.grid(row=1, column=0, padx=10, pady=5)

# Button to open left file
tk.Button(root, text="Open Left File", command=open_left_file).grid(row=2, column=0, pady=5)


# Right label
tk.Label(root, text="Right File").grid(row=0, column=1, padx=10, pady=5)

# Right-side text box
right_text = scrolledtext.ScrolledText(root, width=60, height=20)
right_text.grid(row=1, column=1, padx=10, pady=5)


# Button to open right file

tk.Button(root, text="Open Right File", command=open_right_file).grid(row=2, column=1, pady=5)




root.mainloop()
