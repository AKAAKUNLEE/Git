#coding=utf-8
import sys 
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
def Form_1_onConfigure(event,uiName,widgetName):
    Text_2 = Fun.GetElement(uiName,'Text_2')
    Text_2_Scrollbar = Fun.GetElement(uiName,'Text_2_Scrollbar')
    Text_2.place(x = 0,y = 0,width = event.width,height = event.height)
    Text_2_Scrollbar.place(x = event.width-20,y = 0,width = 20,height = event.height)
