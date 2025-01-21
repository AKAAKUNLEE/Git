#coding=utf-8
#import libs 
import RightTextBar_cmd
import RightTextBar_sty
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  RightTextBar:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        Fun.G_UICommandDictionary[uiName]=RightTextBar_cmd
        Fun.Register(uiName,'root',root)
        style = RightTextBar_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            root.wm_attributes("-topmost",1)
            root.geometry("607x585")
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 607,height = 549)
        Form_1.configure(bg = "#333333")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Text_2= tkinter.Text(root)
        Text_2.place(x = 0,y = 0,width = 607,height = 549)
        Text_2.configure(bg = "#333333")
        Text_2.configure(fg = "#ffffff")
        Text_2.configure(relief = "sunken")
        Text_2_Scrollbar = tkinter.Scrollbar(Text_2,orient=tkinter.VERTICAL)
        Text_2_Scrollbar.place(x = 587,y = 0,width = 20,height = 549)
        Text_2_Scrollbar.config(command = Text_2.yview)
        Text_2.config(yscrollcommand = Text_2_Scrollbar.set)
        Fun.Register(uiName,'Text_2',Text_2)
        Fun.Register(uiName,'Text_2_Scrollbar',Text_2_Scrollbar)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)
        root.bind('<Configure>',self.Configure)
    def Configure(self,event):
        Form_1 = Fun.GetElement(self.uiName,'Form_1')
        if Form_1 == event.widget:
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget:
            RightTextBar_cmd.Form_1_onConfigure(event,self.uiName,"Form_1")

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = RightTextBar(root)
    root.mainloop()
