import tkinter as tk


def clear_entry():
    entry_var.set("")


def on_click(button_value):
    current_text = entry_var.get()
    new_text = current_text + str(button_value)
    entry_var.set(new_text)


def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")


window = tk.Tk()


window.title("Calculator")
window.geometry("365x450")
window.resizable(False, False)

entry_var = tk.StringVar()

btn_0 = tk.Button(window, text="0", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b="0": on_click(b) if b != "=" else calculate())
btn_0.grid(row=4, column=0, padx=5, pady=5)

btn_dec = tk.Button(window, text=".", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b=".": on_click(b) if b != "=" else calculate())
btn_dec.grid(row=4, column=1)

btn_plus = tk.Button(window, text="+", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b="+": on_click(b) if b != "=" else calculate())
btn_plus.grid(row=4, column=2)

btn_equal = tk.Button(window, text="=", height=3, width=7, font="comicsansms 13 bold", bg="#35dffc", command=lambda b="=": on_click(b) if b != "=" else calculate())
btn_equal.grid(row=4, column=3)

btn_1 = tk.Button(window, text="1", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b="1": on_click(b) if b != "=" else calculate())
btn_1.grid(row=3, column=0)

btn_2 = tk.Button(window, text="2", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b="2": on_click(b) if b != "=" else calculate())
btn_2.grid(row=3, column=1, padx=5, pady=5)

btn_3 = tk.Button(window, text="3", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b="3": on_click(b) if b != "=" else calculate())
btn_3.grid(row=3, column=2)

btn_minus = tk.Button(window, text="-", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b="-": on_click(b) if b != "=" else calculate())
btn_minus.grid(row=3, column=3)

btn_4 = tk.Button(window, text="4", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b="4": on_click(b) if b != "=" else calculate())
btn_4.grid(row=2, column=0)

btn_5 = tk.Button(window, text="5", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b="5": on_click(b) if b != "=" else calculate())
btn_5.grid(row=2, column=1)

btn_6 = tk.Button(window, text="6", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b="6": on_click(b) if b != "=" else calculate())
btn_6.grid(row=2, column=2, padx=5, pady=5)

btn_divide = tk.Button(window, text="/", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b="/": on_click(b) if b != "=" else calculate())
btn_divide.grid(row=2, column=3)

btn_7 = tk.Button(window, text="7", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b="7": on_click(b) if b != "=" else calculate())
btn_7.grid(row=1, column=0)

btn_8 = tk.Button(window, text="8", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b="8": on_click(b) if b != "=" else calculate())
btn_8.grid(row=1, column=1)

btn_9 = tk.Button(window, text="9", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b="9": on_click(b) if b != "=" else calculate())
btn_9.grid(row=1, column=2)

btn_multiply = tk.Button(window, text="*", height=3, width=7, font="comicsansms 13 bold", bg="#c2c9cf", command=lambda b="*": on_click(b) if b != "=" else calculate())
btn_multiply.grid(row=1, column=3, padx=5, pady=5)

btn_clear = tk.Button(window, text="C", height=3, width=33, font="comicsansms 13 bold", bg="#ff5145", command=clear_entry)
btn_clear.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

entry_box = tk.Entry(window, width=37, textvariable=entry_var, justify="right", font="comicsansms 13 bold")
entry_box.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

window.mainloop()

