from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
# window.minsize(width=250, height=100)
window.config(padx=20, pady=20)


def mile_to_km():
    number = float(input_number.get())
    km_number = round(number * 1.609)
    label_km_number.config(text=f"{km_number}")

# entry
input_number = Entry(width=10)
print(input_number.get())
input_number.grid(column=1, row=0)

# label
label_mile = Label(text="Miles")
label_mile.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

label_km_number = Label(text="0")
label_km_number.grid(column=1, row=1)

# button
button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)




window.mainloop()
