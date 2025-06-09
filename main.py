import tkinter as tk


print("Text Diff Viewer Starting...")
root = tk.Tk()
root.geometry("900x1200")
root.title("Visual Text Diff Viewer")

# Label on top
tk.Label(root, text="Left File").grid(row=0, column=0, padx=10, pady=5)



root.mainloop()
