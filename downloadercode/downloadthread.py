import threading
from urllib import request
from downloadercode import download
from GUI import load
import time
class downloadthread(threading.Thread):
    pbr=True
    def __init__(self,num,s,e):
        threading.Thread.__init__(self)
        self.num=num
        self.s=s
        self.e=e
        self.persent="0%"
        downloadthread.pbr=True

    def run(self):
        f = open("temp\\output"+str(self.num)+".temp", 'w')
        st=self.s
        ed=100+st
        time.sleep(10)
        print(str(self.num)+" "+str(st)+" "+str(ed)+" "+str(self.e))
        while ed<self.e :
            while downloadthread.pbr:
                part=download.download.information['Accept-Ranges']+"="+str(st)+"-"+str(ed)
                header={'Range':part}
                req=request.Request(url=download.download.url,headers=header)
                reqr=request.urlopen(req)
                if reqr.code == 206:
                    data=reqr.read()
                    f.write(data.decode('utf-8'))
                self.persent='{:.3f}%'.format(((ed-self.s)/(self.e-self.s))*100)
                load.guiload.l[self.num].config(text=self.persent)
                #print(str(self.num)+" "+self.persent)
                st=ed+1
                ed=100+st
                if ed>=self.e:
                    print("DONE")
                    break

        if ed-100<=self.e:
            print("DONE1")
            part=download.download.information['Accept-Ranges']+"="+str(st)+"-"+str(self.e)
            header={'Range':part}
            req=request.Request(url=download.download.url,headers=header)
            reqr=request.urlopen(req)
            if reqr.code == 206:
                data=reqr.read()
                f.write(data.decode('utf-8'))
            self.persent='{:.3f}%'.format(((ed-self.s)/(self.e-self.s))*100)
        f.close()
        download.download.r[self.num]=0

