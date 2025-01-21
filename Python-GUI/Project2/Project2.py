#coding=utf-8
#import libs 
import sys
import Project2_cmd
import Project2_sty
import Fun
import os
import LeftTreeBar
import RightTextBar
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Project2:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        Fun.G_UICommandDictionary[uiName]=Project2_cmd
        Fun.Register(uiName,'root',root)
        style = Project2_sty.SetupStyle()
        if isTKroot == True:
            root.title("PythonEditor")
            Fun.WindowDraggable(root,False,0,'#00ffff')
            Fun.CenterDlg(uiName,root,820,660)
            root['background'] = '#222222'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 820)
        Form_1.configure(height = 660)
        Form_1.configure(bg = "#222222")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[820,660]
        #Create the elements of root 
        Button_2 = tkinter.Button(Form_1,text="Button")
        Fun.Register(uiName,'Button_2',Button_2)
        Fun.SetControlPlace(uiName,'Button_2',2,2,48,48)
        Button_2.configure(bg = "#EFEFEF")
        Project2_cmd.ElementBGArray[2]=Image.open("Ico/ico_new.png").convert('RGBA')
        Project2_cmd.ElementBGArray_Resize[2] = Project2_cmd.ElementBGArray[2].resize((48, 48),Image.LANCZOS)
        Project2_cmd.ElementBGArray_IM[2] = ImageTk.PhotoImage(Project2_cmd.ElementBGArray_Resize[2])
        Button_2.configure(image = Project2_cmd.ElementBGArray_IM[2])
        Button_2.configure(command=lambda:Project2_cmd.Button_2_onCommand(uiName,"Button_2"))
        Button_3 = tkinter.Button(Form_1,text="Button")
        Fun.Register(uiName,'Button_3',Button_3)
        Fun.SetControlPlace(uiName,'Button_3',52,2,48,48)
        Button_3.configure(bg = "#EFEFEF")
        Project2_cmd.ElementBGArray[3]=Image.open("Ico/ico_open.png").convert('RGBA')
        Project2_cmd.ElementBGArray_Resize[3] = Project2_cmd.ElementBGArray[3].resize((48, 48),Image.LANCZOS)
        Project2_cmd.ElementBGArray_IM[3] = ImageTk.PhotoImage(Project2_cmd.ElementBGArray_Resize[3])
        Button_3.configure(image = Project2_cmd.ElementBGArray_IM[3])
        Button_3.configure(command=lambda:Project2_cmd.Button_3_onCommand(uiName,"Button_3"))
        Button_4 = tkinter.Button(Form_1,text="Button")
        Fun.Register(uiName,'Button_4',Button_4)
        Fun.SetControlPlace(uiName,'Button_4',102,2,48,48)
        Button_4.configure(bg = "#EFEFEF")
        Project2_cmd.ElementBGArray[4]=Image.open("Ico/ico_save.png").convert('RGBA')
        Project2_cmd.ElementBGArray_Resize[4] = Project2_cmd.ElementBGArray[4].resize((48, 48),Image.LANCZOS)
        Project2_cmd.ElementBGArray_IM[4] = ImageTk.PhotoImage(Project2_cmd.ElementBGArray_Resize[4])
        Button_4.configure(image = Project2_cmd.ElementBGArray_IM[4])
        Button_4.configure(command=lambda:Project2_cmd.Button_4_onCommand(uiName,"Button_4"))
        Button_5 = tkinter.Button(Form_1,text="Button")
        Fun.Register(uiName,'Button_5',Button_5)
        Fun.SetControlPlace(uiName,'Button_5',150,2,48,48)
        Button_5.configure(bg = "#EFEFEF")
        Project2_cmd.ElementBGArray[5]=Image.open("Ico/ico_run.png").convert('RGBA')
        Project2_cmd.ElementBGArray_Resize[5] = Project2_cmd.ElementBGArray[5].resize((48, 48),Image.LANCZOS)
        Project2_cmd.ElementBGArray_IM[5] = ImageTk.PhotoImage(Project2_cmd.ElementBGArray_Resize[5])
        Button_5.configure(image = Project2_cmd.ElementBGArray_IM[5])
        Button_5.configure(command=lambda:Project2_cmd.Button_5_onCommand(uiName,"Button_5"))
        PanedWindow_6 = tkinter.PanedWindow(Form_1)
        Fun.Register(uiName,'PanedWindow_6',PanedWindow_6)
        Fun.SetControlPlace(uiName,'PanedWindow_6',0,50,820,510)
        PanedWindow_6.configure(orient = tkinter.HORIZONTAL)
        PanedWindow_6.configure(showhandle = "0")
        PanedWindow_6.configure(sashrelief = "flat")
        PanedWindow_6.configure(sashwidth = "4")
        PanedWindow_6_child1= tkinter.Canvas(PanedWindow_6,bg="#FFDD94",name="child1")
        PanedWindow_6_child1.place(x = 1,y = 1,width = 246,height = 508)
        LeftTreeBar_6 = LeftTreeBar.LeftTreeBar(PanedWindow_6_child1,False)
        Fun.Register(uiName,'LeftTreeBar_6',LeftTreeBar_6)
        PanedWindow_6.add(PanedWindow_6_child1,width =246)
        PanedWindow_6_child2= tkinter.Canvas(PanedWindow_6,bg="#D0E6A5",name="child2")
        PanedWindow_6_child2.place(x = 251,y = 1,width = 568,height = 508)
        RightTextBar_6 = RightTextBar.RightTextBar(PanedWindow_6_child2,False)
        Fun.Register(uiName,'RightTextBar_6',RightTextBar_6)
        PanedWindow_6.add(PanedWindow_6_child2,width =568)
        Fun.Register(uiName,'PanedWindow_6_child1',PanedWindow_6_child1)
        Fun.Register(uiName,'PanedWindow_6_child2',PanedWindow_6_child2)
        Text_7 = tkinter.Text(Form_1,undo=True,wrap=WORD)
        Fun.Register(uiName,'Text_7',Text_7)
        Fun.SetControlPlace(uiName,'Text_7',0,560,820,100)
        Text_7.configure(bg = "#222222")
        Text_7.configure(fg = "#CCCCCC")
        Text_7.configure(relief = "sunken")
        #Create the Menu of root 
        MainMenu=tkinter.Menu(root)
        root.config(menu = MainMenu)
        文件=tkinter.Menu(MainMenu,tearoff = 0)
        文件.add_command(label="新建",command=lambda:Project2_cmd.Menu_新建(uiName,"新建"))
        文件.add_command(label="打开",command=lambda:Project2_cmd.Menu_打开(uiName,"打开"))
        文件.add_command(label="保存",command=lambda:Project2_cmd.Menu_保存(uiName,"保存"))
        文件.add_command(label="另存为",command=lambda:Project2_cmd.Menu_另存为(uiName,"另存为"))
        文件.add_command(label="退出",command=lambda:Project2_cmd.Menu_退出(uiName,"退出"))
        MainMenu.add_cascade(label="文件",menu=文件)
        编辑=tkinter.Menu(MainMenu,tearoff = 0)
        编辑.add_command(label="剪切",command=lambda:Project2_cmd.Menu_剪切(uiName,"剪切"))
        编辑.add_command(label="拷贝",command=lambda:Project2_cmd.Menu_拷贝(uiName,"拷贝"))
        编辑.add_command(label="粘贴",command=lambda:Project2_cmd.Menu_粘贴(uiName,"粘贴"))
        MainMenu.add_cascade(label="编辑",menu=编辑)
        MainMenu.add_command(label="运行",command=lambda:Project2_cmd.Menu_运行(uiName,"运行"))
        帮助=tkinter.Menu(MainMenu,tearoff = 0)
        帮助.add_command(label="关于",command=lambda:Project2_cmd.Menu_关于(uiName,"关于"))
        MainMenu.add_cascade(label="帮助",menu=帮助)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Project2_cmd.Form_1_onLoad(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)



        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
            self.root.bind('<Escape>',self.Escape)  
    def GetRootSize(self):
        return Fun.G_RootSize[0],Fun.G_RootSize[1]
    def Escape(self,event):
        if Fun.AskBox('提示','确定退出程序？') == True:
            self.Exit()
    def Exit(self):
        if self.isTKroot == True:
            Fun.DestroyUI(self.uiName)

    def Configure(self,event):
        Form_1 = Fun.GetElement(self.uiName,'Form_1')
        if Form_1 == event.widget:
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget:
            Fun.G_RootSize=[event.width,event.height]
            uiName = self.uiName
            Project2_cmd.Form_1_onConfigure(event,self.uiName,"Form_1")
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Project2(root)
    root.mainloop()
