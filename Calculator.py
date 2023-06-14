import tkinter as tk

history = []

def button_click(number):
    current = result_label.get()
    result_label.delete(0, tk.END)
    result_label.insert(tk.END, current + str(number))

def button_clear():
    result_label.delete(0, tk.END)

def button_back():
    current = result_label.get()
    result_label.delete(0, tk.END)
    result_label.insert(tk.END, current[:-1])

def button_equal():
    expression = result_label.get()
    try:
        result = eval(expression)
        result_label.delete(0, tk.END)
        result_label.insert(tk.END, result)
        history.append(f"{expression} = {result}")
    except:
        result_label.delete(0, tk.END)
        result_label.insert(tk.END, "Error")

def show_history():
    history_window = tk.Toplevel()
    history_window.title("Calculation History")

    history_label = tk.Text(history_window, width=30, height=10)
    history_label.pack()

    for entry in history:
        history_label.insert(tk.END, entry + "\n")

window = tk.Tk()
window.title("Calculator")
window.configure(bg='#8B5FBF')

# Create the result label
result_label = tk.Entry(window, width=30)
result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
result_label.configure(bg='white', fg='#8B5FBF', font=('Arial', 12)) 

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for button_text, row, col in buttons:
    button = tk.Button(window, text=button_text, padx=10, pady=5, command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=col)
    button.configure(bg='#CEA1E7', fg='white', font=('Arial', 10)) 
    
    
clear_button = tk.Button(window, text="Clear", padx=20, pady=5, command=button_clear)
clear_button.grid(row=5, column=0, padx=10, pady=5)
clear_button.configure(bg='#CEA1E7', fg='white', font=('Arial', 10)) 

back_button = tk.Button(window, text="Back", padx=20, pady=5, command=button_back)
back_button.grid(row=5, column=1, padx=10, pady=5)
back_button.configure(bg='#CEA1E7', fg='white', font=('Arial', 10)) 

equal_button = tk.Button(window, text="Calculate", padx=20, pady=5, command=button_equal)
equal_button.grid(row=5, column=2, padx=10, pady=5)
equal_button.configure(bg='#CEA1E7', fg='white', font=('Arial', 10))

history_button = tk.Button(window, text="History", padx=20, pady=5, command=show_history)
history_button.grid(row=5, column=3, padx=10, pady=5)
history_button.configure(bg='#CEA1E7', fg='white', font=('Arial', 10))  

window.mainloop()
