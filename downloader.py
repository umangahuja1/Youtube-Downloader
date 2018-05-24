from tkinter import *
from song import song
from video import video

root = Tk()
root.title('Youtube Downloader')
c = Canvas(root, width=300, height=190)
#image = PhotoImage(file='/home/umang/Documents/bg.png')
image=None
bg_label = Label(root, image=image)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

c.grid()

v = IntVar()
v.set('0')

options = {
    0: ('Song', song),
    1: ('Video', video)
}

title = Label(bg_label, text='Get Set Python')
title.config(font=("",12))
title.place(x=150, y=25,anchor='center')

label = Label(bg_label, text='Enter Name ')
e = Entry(bg_label)
label.grid(row=0, pady=(50,10))
e.grid(row=0, column=1, padx=(0,20), pady=(50,10))

for opt in sorted(options.keys()):
    radio = Radiobutton(bg_label, text=options[opt][0], padx=10, variable=v, value=opt)
    radio.grid(row=5, column=opt, padx=20, pady=5)

download = Button(bg_label, text='Download', command= lambda : options[v.get()][1](e))
download.grid(columnspan=2, pady=7)

root.mainloop()

