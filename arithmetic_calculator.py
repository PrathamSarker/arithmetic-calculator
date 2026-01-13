import tkinter as tk

root = tk.Tk()
root.title("Arithmetic Calculator")
root.geometry("400x400")


            #INPUTS
number1_text = tk.Label(root, text="Enter the first number: ")
number1_text.grid(row=0, column=0, padx=10, pady=10, sticky="w")
number1 = tk.Entry(root)
number1.grid(row=0, column=1, padx=10, pady=10)
 
number2_text = tk.Label(root, text="Enter the second number: ")
number2_text.grid(row=1, column=0, padx=10, pady=10, sticky="w")
number2 = tk.Entry(root)
number2.grid(row=1, column=1, padx=10, pady=10)

operation_text = tk.Label(root, text="Enter the operation (+ or - or / or *): ")
operation_text.grid(row=2, column=0, padx =10, pady= 10)
operation = tk.Entry(root)
operation.grid(row=2, column=1, padx =10, pady= 10, sticky="w")

            #OUTPUT
'''This is read-only to prevent manual editing'''

result= tk.Label(root, text="The result is:")
result.grid(row=4, column=0, padx=10, pady=10)
result_output = tk.Entry(root, state="readonly")
result_output.grid(row=4, column=1,padx=10, pady=10, sticky="w")

            #Error Message
invalid_text = tk.Label(root, anchor="center",text = "")
invalid_text.grid(row=7, columnspan= 2)



            #Main Operation

def not_valid():
    invalid_text.config(text = "Your Input is Invalid.\nPlease Try Again.")


def value_update(value):
    result_output.config(state = "normal")
    result_output.delete(0, tk.END)
    result_output.insert(0, value)
    result_output.config(state = "readonly")
    
arithmetic_result = 0

def calculate():
    """Main logic to perform arithmetic operations based on user input."""
    try: 
        num1 = float(number1.get())
    except ValueError:
        not_valid()
    try: 
        num2 = float(number2.get())
    except ValueError:
        not_valid()

    operation_stripped = (str(operation.get())).strip()
    
    #operation validation
    if len(operation_stripped) != 1 or operation_stripped not in "+-/*":
        not_valid()


    if operation_stripped == "+":
        arithmetic_result = num1 + num2
    elif operation_stripped == "-":
        arithmetic_result = num1 - num2
    elif operation_stripped == "/":
        try:
            arithmetic_result = num1 / num2
        except ZeroDivisionError:
            arithmetic_result = str("Undefined Result")
    elif operation_stripped == "*":
        arithmetic_result = num1 * num2


    value_update(arithmetic_result)
    return result_output


def exit():
    root.destroy()

def reset():
    invalid_text.config(text="")
    number1.delete(0, tk.END)
    number2.delete(0, tk.END)
    operation.delete(0, tk.END)
    value_update("")

            #All Buttons

btn = tk.Button(root, text= "Result", command =calculate)
btn.grid(row = 3, column = 1, padx = 10, pady= 10)

reset_button = tk.Button(root, text="Reset", command= reset)
reset_button.grid(row = 6, column = 1, padx = 10, pady= 10)

exit_button = tk.Button(root, text="Exit", command = exit)
exit_button.grid(row = 5, column = 1, padx = 10, pady= 10)


root.mainloop()