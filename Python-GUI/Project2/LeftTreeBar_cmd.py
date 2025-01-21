#coding=utf-8
import sys 
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
photo = None
def Form_1_onConfigure(event,uiName,widgetName):
    TreeView_2 = Fun.GetElement(uiName,'TreeView_2')
    TreeView_2.place(x = 0,y = 0,width = event.width,height = event.height)
def TreeView_2_onButton1(event,uiName,widgetName):
    global photo
    TreeCtrl = Fun.GetElement(uiName,widgetName)
    item = TreeCtrl.identify("item",event.x,event.y)
    if item is not None and item != "":
        Text_2 = Fun.GetElement("RightTextBar","Text_2")
        Text_2.delete('0.0',tkinter.END)
        if os.path.isdir(item) == False:
            filename_lower = str(item).lower()
            if filename_lower.find(".png") >= 0 or filename_lower.find(".jpg") >= 0 :
                photo = PhotoImage(file=filename_lower)
                Text_2.image_create(END, image=photo)
            else:
                content = Fun.ReadFromFile(filename_lower)
                Fun.SetText("RightTextBar",'Text_2',content)
