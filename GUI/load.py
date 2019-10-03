
from tkinter import *
from downloadercode import downloadthread

class guiload():
    l=[]
    x=""
    def __init__(self,var):
        self.mar=Toplevel()
        self.var=var
        print("Loading")

    def runGUI2(self):
        print("Loading2")
        #self.mar=Tk()
        self.mar.title('Downloader1')
        guiload.x="0%"
        for i in range(self.var+1):#download.download.thr[i].persent
            print(i)
            guiload.l.append(Label(self.mar, text = guiload.x))
            guiload.l[i].pack()
        button1=Button(self.mar, text="Pause", command=guiload.pause)
        button2=Button(self.mar, text="Resume", command=guiload.resume)
        button3=Button(self.mar, text="Refresh", command=guiload.refresh)
        button1.pack()
        button2.pack()
        button3.pack()
        self.mar.mainloop()

    @classmethod
    def refresh(cal):
        for i in range(3):
            guiload.l[i].config(text="lol")

    @classmethod
    def pause(cal):
        downloadthread.downloadthread.pbr=False
    @classmethod
    def resume(cal):
        downloadthread.downloadthread.pbr=True

'''
        button1.place(x=130,y=130,width=200)
        button2.place(x=130,y=150,width=200)
'''