from tkinter import *

def miles_to_kilometer():
    miles = float(miles_input.get())
    km = miles * 1.60934
    result.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

kilometer = Label(text="Km")
kilometer.grid(column=2, row=1)

calculate_btn = Button(text="calculate", command=miles_to_kilometer)
calculate_btn.grid(column=1, row=2)

window.mainloop()
