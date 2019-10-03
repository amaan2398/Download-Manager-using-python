from urllib import request as rq
import os
from downloadercode import downloadthread
from GUI import GUImanager

class download():
    url=""
    datasize=0
    digits=0
    information=dict()
    r=[]
    thr=[]
    file_name=""
    def __init__(self,url):
        download.url=url
        self.setfile()

    def setfile(self):
        download.file_name=download.url.split('/')[-1]

    def urlcheck(self):
        if rq.urlopen(download.url).code==200:
            return True
        return False

    def urlvalidation(self):
        download.information=dict(rq.urlopen(download.url).info())
        print(download.information)
        try:
            if download.information['Accept-Ranges']!='none':
                return True
        except:
            pass
        return False

    def partrange(self):
        try:
            os.mkdir("temp")
        except:
            pass

        _=download.information['Content-Length']
        print(_)
        download.digits=len(_)
        print(download.digits)
        download.datasize=int(_)
        x=0
        i=0
        y=10**(download.digits-1)

        while x+y<=download.datasize:
            download.thr.append(downloadthread.downloadthread(i,x,x+y))
            download.r.append(1)
            x+=y+1
            i+=1

        if x<download.datasize:
            z=download.datasize-x
            download.thr.append(downloadthread.downloadthread(i,x,x+z))
            download.r.append(1)

        for th in download.thr:
            th.start()

        gui=GUImanager.guimanager()
        gui.gui_download_anim(len(download.thr)-1)
        while sum(download.r)!=0:
            print("waiting")
            continue
        download.combine(len(download.thr)-1)



    @staticmethod
    def combine(num):
        ff=open(download.file_name,"w")
        for x in range(num+1):
            f=open("temp\\output"+str(x)+".temp","r")
            _=f.read()
            ff.write(_)
            f.close()
            os.remove("temp\\output"+str(x)+".temp")
        os.removedirs("temp")
        ff.close()

