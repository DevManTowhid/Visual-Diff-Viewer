import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import difflib

from tkinter import messagebox

def export_diff_to_file():
    left_lines = left_text.get("1.0", tk.END).splitlines()
    right_lines = right_text.get("1.0", tk.END).splitlines()

    diff = list(difflib.ndiff(left_lines, right_lines))

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
        title="Save Diff As"
    )

    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                for line in diff:
                    f.write(line + "\n")
            messagebox.showinfo("Export Successful", "Diff exported successfully!")
        except Exception as e:
            messagebox.showerror("Export Failed", str(e))


def clear_files():
    left_text.delete("1.0", tk.END)
    right_text.delete("1.0", tk.END)



def compare_files():
    left_lines = left_text.get("1.0", tk.END).splitlines()
    right_lines = right_text.get("1.0", tk.END).splitlines()

    diff = list(difflib.ndiff(left_lines, right_lines))

    # Clear both boxes
    left_text.delete("1.0", tk.END)
    right_text.delete("1.0", tk.END)

    for line in diff:
        if line.startswith("- "):
            left_text.insert(tk.END, line[2:] + "\n", "deleted")
        elif line.startswith("+ "):
            right_text.insert(tk.END, line[2:] + "\n", "added")
        elif line.startswith("  "):
            left_text.insert(tk.END, line[2:] + "\n")
            right_text.insert(tk.END, line[2:] + "\n")

    # Tag styles
    left_text.tag_config("deleted", background="lightcoral")
    right_text.tag_config("added", background="lightgreen")

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


tk.Button(root, text="Compare Files", command=compare_files).grid(row=3, column=0, columnspan=2, pady=10)

tk.Button(root, text="Clear All", command=clear_files).grid(row=4, column=0, columnspan=2, pady=5)

tk.Button(root, text="Export Diff", command=export_diff_to_file).grid(row=5, column=0, columnspan=2, pady=5)


root.mainloop()
