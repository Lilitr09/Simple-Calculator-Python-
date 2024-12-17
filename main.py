from tkinter import *


def main():
    # Layout
    # Colors
    background = "#332f2f"
    buttons = "#878383"
    active_button = "#bf9693"
    # Main window
    window = Tk()
    window.title("Calculadora")
    window.geometry("360x420")
    window.configure(bg=background)
    window.iconbitmap("C:/Users/Lisbeth/Documents/Python/Calculadora/icon.ico")

    # Structure
    title = Label(
        window,
        text="Mi Calculadora",
        font=("Arial", 30, "bold"),
        bg=background,
        fg="white",
    )  # Change this later!!
    title.grid(row=0, column=0, columnspan=4)

    expression = Entry(window, width=20)
    expression.configure(font=("Arial", 24))
    expression.grid(row=1, column=0, columnspan=4)

    # Functionality
    # Click buttons
    def button_click(number):
        current = expression.get()
        expression.delete(0, END)
        expression.insert(0, str(current) + str(number))
        return
    
    # Delete
    def button_clear():
        expression.delete(0, END)
        
    # Addition
    def button_add():
        first_number = expression.get()
        global X
        global operation
        operation = "addition"
        X = int(first_number)
        expression.delete(0, END)
        
    # Substraction
    def button_sub():
        first_number = expression.get()
        global X
        global operation
        operation = "substraction"
        X = int(first_number)
        expression.delete(0, END)
        
    # Multiplication
    def button_multp():
        first_number = expression.get()
        global X
        global operation
        operation = "multiplication"
        X = int(first_number)
        expression.delete(0, END)
        
    # Division
    def button_div():
        first_number = expression.get()
        global X
        global operation
        operation = "division"
        X = int(first_number)
        expression.delete(0, END)
        
    # Results
    def button_equal():
        Y = expression.get()
        error_message = "ERROR"
        expression.delete(0, END)
        try:
            if operation == "addition":
                result = X + int(Y)
            elif operation == "substraction":
                result = X - int(Y)
            elif operation == "multiplication":
                result = X * int(Y)
            else:
                result = X // int(Y)
            expression.insert(0, result)
        except ZeroDivisionError:
            expression.insert(0, error_message)
    
    
    # Buttons
    button_1 = Button(
        window,
        text=1,
        padx=36,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        command=lambda: button_click(1)
    )
    button_2 = Button(
        window,
        text=2,
        padx=36,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        command=lambda: button_click(2)
    )
    button_3 = Button(
        window,
        text=3,
        padx=36,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        command=lambda: button_click(3)
    )
    button_4 = Button(
        window,
        text=4,
        padx=39,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        command=lambda: button_click(4)
    )
    button_5 = Button(
        window,
        text=5,
        padx=36,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        command=lambda: button_click(5)
    )
    button_6 = Button(
        window,
        text=6,
        padx=36,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        command=lambda: button_click(6)
    )
    button_7 = Button(
        window,
        text=7,
        padx=36,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        command=lambda: button_click(7)
    )
    button_8 = Button(
        window,
        text=8,
        padx=39,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        command=lambda: button_click(8)
    )
    button_9 = Button(
        window,
        text=9,
        padx=36,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        command=lambda: button_click(9)
    )
    button_0 = Button(
        window,
        text=0,
        padx=36,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        command=lambda: button_click(0)
    )
    button_clear = Button(
        window,
        text="Borrar",
        padx=69,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        activebackground=active_button,
        command=button_clear
    )
    button_plus = Button(
        window,
        text="+",
        padx=36,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        command=button_add
    )
    button_minus = Button(
        window,
        text="-",
        padx=36,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        command=button_sub
    )
    button_multp = Button(
        window,
        text="*",
        padx=39,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        command=button_multp
    )
    button_div = Button(
        window,
        text="/",
        padx=39,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        command=button_div
    )
    button_equal = Button(
        window,
        text="=",
        padx=173,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        activebackground=active_button,
        command=button_equal
    )

    # Place the buttons
    button_1.grid(row=2, column=0)
    button_2.grid(row=2, column=1)
    button_3.grid(row=2, column=2)
    button_4.grid(row=2, column=3)
    button_5.grid(row=3, column=0)
    button_6.grid(row=3, column=1)
    button_7.grid(row=3, column=2)
    button_8.grid(row=3, column=3)
    button_9.grid(row=4, column=0)
    button_0.grid(row=4, column=1)
    button_clear.grid(row=4, column=2, columnspan=2)
    button_plus.grid(row=5, column=0)
    button_minus.grid(row=5, column=1)
    button_multp.grid(row=5, column=2)
    button_div.grid(row=5, column=3)
    button_equal.grid(row=6, column=0, columnspan=4)
    
        

    # Start the application
    window.mainloop()


if __name__ == "__main__":
    main()
