
from tkinter import *
from downloadercode import downloadthread,download

class guiload():
    l=[]
    x=""
    mar=Tk()
    def __init__(self,var):
        self.mar=Toplevel()
        self.var=var
        print("Loading")

    def runGUI2(self):
        print("Loading2")
        #self.mar=Tk()
        guiload.mar.title('Downloader1')
        guiload.x="0%"
        for i in range(self.var+1):#download.download.thr[i].persent
            print(i)
            guiload.l.append(Label(guiload.mar, text = guiload.x))
            guiload.l[i].pack()
        button1=Button(guiload.mar, text="Pause", command=guiload.pause)
        button2=Button(guiload.mar, text="Resume", command=guiload.resume)
        button3=Button(guiload.mar, text="Refresh", command=guiload.refresh)
        button1.pack()
        button2.pack()
        button3.pack()

        guiload.mar.mainloop()


    @classmethod
    def refresh(cal):
        if sum(download.download.r)==0:
            download.download.combine(len(download.download.thr)-1)
            guiload.mar.close()

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