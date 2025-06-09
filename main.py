import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import difflib
from difflib import SequenceMatcher
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
def compare_words(left_line, right_line):
    left_words = left_line.split()
    right_words = right_line.split()

    sm = difflib.SequenceMatcher(None, left_words, right_words)
    for opcode, i1, i2, j1, j2 in sm.get_opcodes():
        if opcode == 'equal':
            left_text.insert(tk.END, " ".join(left_words[i1:i2]) + "\n")
            right_text.insert(tk.END, " ".join(right_words[j1:j2]) + "\n")
        elif opcode == 'replace':
            left_text.insert(tk.END, " ".join(left_words[i1:i2]) + "\n", "deleted_word")
            right_text.insert(tk.END, " ".join(right_words[j1:j2]) + "\n", "added_word")
        elif opcode == 'delete':
            left_text.insert(tk.END, " ".join(left_words[i1:i2]) + "\n", "deleted_word")
        elif opcode == 'insert':
            right_text.insert(tk.END, " ".join(right_words[j1:j2]) + "\n", "added_word")

def clear_files():
    left_text.delete("1.0", tk.END)
    right_text.delete("1.0", tk.END)



def compare_files():
    

    left_lines = left_text.get("1.0", tk.END).splitlines()
    right_lines = right_text.get("1.0", tk.END).splitlines()

    # Clear boxes
    left_text.delete("1.0", tk.END)
    right_text.delete("1.0", tk.END)

    sm = difflib.SequenceMatcher(None, left_lines, right_lines)
    for opcode, i1, i2, j1, j2 in sm.get_opcodes():
        if opcode == 'equal':
            for i in range(i1, i2):
                left_text.insert(tk.END, left_lines[i] + "\n")
            for j in range(j1, j2):
                right_text.insert(tk.END, right_lines[j] + "\n")
        elif opcode == 'replace':
            for i in range(i1, i2):
                left_line = left_lines[i]
                right_line = right_lines[j1 + (i - i1)] if j1 + (i - i1) < j2 else ""
                compare_words(left_line, right_line)
        elif opcode == 'delete':
            for i in range(i1, i2):
                left_text.insert(tk.END, left_lines[i] + "\n", "deleted_line")
        elif opcode == 'insert':
            for j in range(j1, j2):
                right_text.insert(tk.END, right_lines[j] + "\n", "added_line")

    # Tag configs
    left_text.tag_config("deleted_word", background="orange")
    right_text.tag_config("added_word", background="lightblue")
    left_text.tag_config("deleted_line", background="lightcoral")
    right_text.tag_config("added_line", background="lightgreen")

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





def add_color_legend():
    legend_frame = tk.Frame(root)
    legend_frame.grid(row=6, column=0, columnspan=2, pady=10)

    tk.Label(legend_frame, text="Legend:").grid(row=0, column=0, padx=5)

    tk.Label(legend_frame, text="Deleted Line", bg="lightcoral", width=12).grid(row=0, column=1, padx=5)
    tk.Label(legend_frame, text="Added Line", bg="lightgreen", width=12).grid(row=0, column=2, padx=5)
    tk.Label(legend_frame, text="Deleted Word", bg="orange", width=12).grid(row=0, column=3, padx=5)
    tk.Label(legend_frame, text="Added Word", bg="lightblue", width=12).grid(row=0, column=4, padx=5)

add_color_legend()

root.mainloop()
