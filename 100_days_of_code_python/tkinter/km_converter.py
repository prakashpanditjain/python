import tkinter

#create the window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=400,height=200)

#get the input
input = tkinter.Entry(width=10)
input.grid(column=1,row=0)


#Function to convert miles to km
def miles_to_km():
    miles= float(input.get())
    km = miles* 1.609
    display_km.config(text=f'{km}')
# convert_km = miles_to_km(get_miles)

#get the label
Mile = tkinter.Label(text='Miles',font=('Courier',20))
Mile.grid(column=2, row=0)

new_text = tkinter.Label(text= 'is equal to',font=('Courier',20))
new_text.grid(column=0,row=1)

#Get the converted km label
display_km = tkinter.Label(text= '0',font=('Courier',20))
display_km.grid(column=1,row=1)
display_km.config(padx=20,pady=20)

#get the KM label next to calculated km
KM = tkinter.Label(text= 'Km',font=('Courier',20))
KM.grid(column=2,row=1)

#get the button to calculate the miles
button = tkinter.Button(text='Calculate',command=miles_to_km)
button.grid(column=1,row=3)





window.mainloop()