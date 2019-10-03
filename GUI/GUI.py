import threading
from GUI import GUImanager


from tkinter import *

class gui():
    def __init__(self):
        #threading.Thread.__init__(self)
        pass

    def runGUI(self):
        self.m=Tk()
        self.m.title('Downloader')
        c=Canvas(self.m,width=500,height=250)
        c.pack()
        lable_1=Label(self.m,text="URL:")
        self.entry1=Entry(self.m)
        button1=Button(self.m,text="Download",command=self.call1)
        lable_1.place(x=100,y=100,width=100)
        self.entry1.place(x=170,y=100,width=150)
        button1.place(x=130,y=130,width=200)
        self.m.mainloop()

    def call1(self):
        GUImanager.guimanager.str1=self.entry1.get()
        if self.m.quit() and self.m.destroy():
            print("DONE")




