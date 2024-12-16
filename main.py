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
    )
    button_clear = Button(
        window,
        text="borrar",
        padx=69,
        pady=20,
        bg=buttons,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        activebackground=active_button,
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
