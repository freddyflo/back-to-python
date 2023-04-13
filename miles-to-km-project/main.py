import tkinter


# window
window  = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=200)
window.config(padx=20, pady=20)


# convert from miles to km method
def convert_miles_to_km():
    miles = float(input.get())
    km =  round(1.609 * miles)
    kilometer_results_label.config(text=f"{km}")
    pass


# Entry
input = tkinter.Entry(width=7)
input.grid(row=0, column=1)


# Label
miles_label = tkinter.Label()
miles_label.config(text="Miles")
miles_label.grid(row=0, column=2)


# is equal to label
is_equal_label = tkinter.Label()
is_equal_label.config(text="is equal to")
is_equal_label.grid(row=1, column=0)


# Results label
kilometer_results_label = tkinter.Label()
kilometer_results_label.config(text="0")
kilometer_results_label.grid(row=1, column=1)


# kilometer label
kilometer_label = tkinter.Label()
kilometer_label.config(text="Km")
kilometer_label.grid(row=1, column=2)


# Button
button = tkinter.Button(text="Calculate", command=convert_miles_to_km)
button.grid(row=2, column=1)



window.mainloop()