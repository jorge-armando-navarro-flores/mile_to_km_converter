from tkinter import *


def calculate():
    miles = int(miles_input.get())
    km = str(miles * 1.609)
    result_label.config(text=km)


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)


miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

mile_label = Label(text="Miles", font=("Arial", 12, "bold"))
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)

result_label = Label(text="0", font=("Arial", 12))
result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()
