import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers.")

# Create the main window
root = tk.Tk()
root.title("Product Calculator")
root.geometry("400x400")

# Create labels and entry fields for numbers
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Create a button to calculate the product
calculate_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="Product: ")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()