import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2 if num2 != 0 else "Error (div by 0)"
        else:
            result = "Select operation"
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Result: Error (invalid input)")

root = tk.Tk()
root.title("Arithmetic Calculator")
root.geometry("500x350")

tk.Label(root, text="Number 1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Number 2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

operation = tk.StringVar(value="+")
tk.Label(root, text="Operation:").pack()

# Create a frame for radio buttons and use grid inside it
op_frame = tk.Frame(root)
op_frame.pack(pady=10)

for idx, op in enumerate(["+", "-", "*", "/"]):
    tk.Radiobutton(op_frame, text=op, variable=operation, value=op).grid(row=0, column=idx, padx=15)

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)
result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()