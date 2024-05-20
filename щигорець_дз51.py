from tkinter import*
root=Tk()
weather = ["Холодно", "Дощ"]
weather_listbox = Listbox()
for w in weather:
    weather_listbox.insert(END, w)
weather_listbox.pack()
btn = Button(text="Погода сьогодні",command=weather_listbox)
btn.pack()


a1=IntVar()
a2=IntVar()
a3=IntVar()
a4=IntVar()
a5=IntVar()
a6=IntVar()
ch1=Checkbutton(root, text="Дощ",variable=a1,onvalue=1,offvalue=0)
ch2=Checkbutton(root, text=" Сніг", variable=a2,onvalue=2,offvalue=0)
ch3=Checkbutton(root, text=" Вітер", variable=a3,onvalue=3,offvalue=0)
ch4=Checkbutton(root, text=" Сонце", variable=a4,onvalue=4,offvalue=0)
ch5=Checkbutton(root, text=" Тепло", variable=a5,onvalue=5,offvalue=0)
ch6=Checkbutton(root, text=" Холодно", variable=a6,onvalue=6,offvalue=0)
ch1.pack()
ch2.pack()
ch3.pack()
ch4.pack()
ch5.pack()
ch6.pack()

root.mainloop()
