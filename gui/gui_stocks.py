from tkinter import *
from PIL import ImageTk, Image
window=Tk()
window.title("STONKS PICKER")
window.config(padx=25,pady=25,bg="#7a3530")
canvas=Canvas(width=1080,height=676,bg="#7a3530",highlightthickness=0)
img = ImageTk.PhotoImage(Image.open("stonks_image.jpeg"))
canvas.create_image(540,338,image=img)
#canvas.create_text(540,338,text="STOCKS PICKER",font=("Arial",30,"bold"),fill="white")


#title_label=Label(text="STOCK PICKER",font=("Arial",30,"bold"),bg="#7a3530",fg="white")
stock_compute=Button(text="COMPUTE",font=("Arial",20,"bold"),bg="#7a3530",fg="white")
Button2=Button(text="Button2",font=("Arial",20,"bold"),bg="#7a3530",fg="white")
Stock_entry=Entry(width=20)
canvas.grid(row=0,column=0,columnspan=1)
stock_compute.place(x=525,y=275)
Button2.place(x=850,y=275)
Stock_entry.place(x=705,y=285)

#title_label.grid(row=1,column=0)


window.mainloop()