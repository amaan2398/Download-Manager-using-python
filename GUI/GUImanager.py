
from downloadercode import download,downloadthread
from GUI import GUI,load

class guimanager():
    str1=""
    def __init__(self):
        pass

    def startgui(self):
        self.t1=GUI.gui()
        self.t1.runGUI()
        #print(guimanager.str1+" 11111")
        self.waitin(guimanager.str1)

    def waitin(self,str1):
        #self.t1.exit()
        #print("1111111111111111111")
        url=str1
        print(url)
        d=download.download(url=url)
        if d.urlcheck():
            if d.urlvalidation():
                d.partrange()
                print("download is complete!")
            else:
                print("we can't divid task!")
        else:
            print("site is down!")


    def gui_download_anim(self,ver):
        t1=load.guiload(ver)
        t1.runGUI2()
