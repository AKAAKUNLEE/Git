#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import tkinter
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

import threading
import subprocess
import io
G_UITreeImageArray={}
def handle_output(cmdText,OutputText):
    process = subprocess.Popen(cmdText,shell=True, bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.DEVNULL,encoding='utf-8')
    OutputText.delete('0.0',tkinter.END)
    errorText = None
    first = True
    while first == True or process.poll() is None :
          first = False
          output = process.stdout.readline()
          if output:
              OutputText.insert(tkinter.END,output)
              OutputText.see(tkinter.END)
          else:
              output = process.communicate()
              if len(output) > 0:
                  ErrorArray = output.split("
                  for line in ErrorArray:
                      OutputText.insert(tkinter.END,line)
    process.stdout.close()
")
def BuildAllFileTree(TreeCtrl,parentItem,parentPath,depth):
    from   PIL import Image,ImageTk
    global G_UITreeImageArray
    for fileName in os.listdir(parentPath):
        filename_lower = fileName.lower()
        if '__pycache__' not in fileName:
            if '.git' not in fileName:
                newPath = parentPath +'\\'+ fileName
                print(newPath)
                if os.path.isdir(newPath):
                    IcoPath = os.path.join(Fun.G_ExeDir,"Ico\dir.png")
                    if os.path.exists(IcoPath) == True:
                        imageRGBA = Image.open(IcoPath).convert('RGBA')
                        G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                        newTreeItem = TreeCtrl.insert(parentItem,'end',newPath,text=fileName,image=G_UITreeImageArray[newPath],values=("1"),tags = ('dirs',))
                        BuildAllFileTree(TreeCtrl,newTreeItem, newPath,depth +1)
                    else:
                        newTreeItem = TreeCtrl.insert(parentItem,'end',newPath,text=fileName,values=("1"),tags = ('dirs',))
                        BuildAllFileTree(TreeCtrl,newTreeItem, newPath,depth +1)
                else:
                    if filename_lower.find(".png") >= 0 or filename_lower.find(".jpg") >= 0 :
                        IcoPath =  os.path.join(Fun.G_ExeDir,"Ico\img.png")
                        if os.path.exists(IcoPath) == True:
                            imageRGBA = Image.open(IcoPath).convert('RGBA')
                            G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                            newTreeItem = TreeCtrl.insert(parentItem,'end',newPath,text=fileName,image=G_UITreeImageArray[newPath],values=("2"))
                        else:
                            newTreeItem = TreeCtrl.insert(parentItem,'end',newPath,text=fileName,values=("2"))
                    elif filename_lower.find(".mp3") >= 0:
                        IcoPath =  os.path.join(Fun.G_ExeDir,"Ico\mp3.png")
                        if os.path.exists(IcoPath) == True:
                            imageRGBA = Image.open(IcoPath).convert('RGBA')
                            G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                            newTreeItem = TreeCtrl.insert(parentItem,'end',newPath,text=fileName,image=G_UITreeImageArray[newPath],values=("2"))
                        else:
                            newTreeItem = TreeCtrl.insert(parentItem,'end',newPath,text=fileName,values=("2"))
                    elif filename_lower.find(".py") >= 0:
                        cmdfile = newPath[:-3] + "_cmd.py"
                        if os.path.exists(cmdfile) == True:
                            IcoPath =  os.path.join(Fun.G_ExeDir,"Ico\Form.png")
                            if os.path.exists(IcoPath) == True:
                                imageRGBA = Image.open(IcoPath).convert('RGBA')
                                G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                                newTreeItem = TreeCtrl.insert(parentItem,'end',newPath,text=fileName,image=G_UITreeImageArray[newPath],values=("2"))
                            else:
                                newTreeItem = TreeCtrl.insert(parentItem,'end',newPath,text=fileName,values=("2"))
                        else:
                            IcoPath = os.path.join(Fun.G_ExeDir,"Ico\py.png")
                            if os.path.exists(IcoPath) == True:
                                imageRGBA = Image.open(IcoPath).convert('RGBA')
                                G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                                newTreeItem = TreeCtrl.insert(parentItem,'end',newPath,text=fileName,image=G_UITreeImageArray[newPath],values=("2"))
                            else:
                                newTreeItem = TreeCtrl.insert(parentItem,'end',newPath,text=fileName,values=("2"))
                    else:
                        IcoPath = os.path.join(Fun.G_ExeDir,"Ico\txt.png")
                        if os.path.exists(IcoPath) == True:
                            imageRGBA = Image.open(IcoPath).convert('RGBA')
                            G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                            newTreeItem = TreeCtrl.insert(parentItem,'end',newPath,text=fileName,image=G_UITreeImageArray[newPath],values=("2"))
                        else:
                            newTreeItem = TreeCtrl.insert(parentItem,'end',newPath,text=fileName,values=("2"))
def Form_1_onLoad(uiName):
    TreeView_2 = Fun.GetElement('LeftTreeBar','TreeView_2')
    if TreeView_2 != None:
        BuildAllFileTree(TreeView_2,'',Fun.G_ExeDir,1)
def Form_1_onConfigure(event,uiName,widgetName):
    PanedWindow_6 = Fun.GetElement(uiName,'PanedWindow_6')
    Text7 = Fun.GetElement(uiName,'Text_7')
    PanedWindow_6.place(x = 0,y = 50,width = event.width,height = event.height - 51 - 100)
    Text7.place(x = 0,y = event.height - 100,width = event.width,height = 100)
#Button 'Button's Event :Command
def Button_2_onCommand(uiName,widgetName):
    Menu_新建(uiName,None)
#Button 'Button's Event :Command
def Button_3_onCommand(uiName,widgetName):
    Menu_打开(uiName,None)
#Button 'Button's Event :Command
def Button_4_onCommand(uiName,widgetName):
    Menu_保存(uiName,None)
#Button 'Button's Event :Command
def Button_5_onCommand(uiName,widgetName):
    Menu_运行(uiName,None)
def Menu_新建(uiName,itemName):
    content = Fun.GetText('RightTextBar','Text_2')
    if len(content) > 0 and content !='\n':
        result = Fun.AskBox('提示','是否保存当前文件？')
        if result == True:
            if 'CurrentFile' not in Fun.G_UserVarDict:
                savePath = Fun.SaveFile(title="保存Python文件",filetypes=[('Python File','*.py'),('All files','*')],initDir = os.path.abspath('.'),defaultextension='py')
                if savePath != None and len(savePath) > 0:
                    if True == Fun.WriteToFile(savePath,content):
                        Fun.SetText(uiName,"root","PythonEditor:" + fileName)
                        Fun.G_UserVarDict['CurrentFile']  = savePath
                        Fun.MessageBox('保存成功')
                    else:
                        Fun.MessageBox('保存失败')
                Fun.G_UserVarDict['CurrentFile']  = savePath
            else:
                if False == Fun.WriteToFile(Fun.G_UserVarDict['CurrentFile'] ,content):
                    Fun.MessageBox('保存失败')
                    return
    Fun.SetText('RightTextBar','Text_2','')
def Menu_打开(uiName,itemName):
    openPath = Fun.OpenFile(title="打开Python文件",filetypes=[('Python File','*.py'),('All files','*')],initDir = os.path.abspath('.'))
    if openPath != None and len(openPath) > 0:
        content = Fun.ReadFromFile(openPath)
        Fun.G_UserVarDict['CurrentFile'] = openPath
        Fun.SetText('RightTextBar','Text_2',content)
def Menu_保存(uiName,itemName):
    if 'CurrentFile' not in Fun.G_UserVarDict:
        savePath = Fun.SaveFile(title="保存Python文件",filetypes=[('Python File','*.py'),('All files','*')],initDir = os.path.abspath('.'),defaultextension='py')
        if savePath != None and len(savePath) > 0:
            content = Fun.GetText('RightTextBar','Text_2')
            if True == Fun.WriteToFile(savePath,content):
                Fun.SetText(uiName,"root","PythonEditor:" + fileName)
                Fun.G_UserVarDict['CurrentFile'] = savePath
                Fun.MessageBox('保存成功')
            else:
                Fun.MessageBox('保存失败')
    else:
        content = Fun.GetText('RightTextBar','Text_2')
        if True == Fun.WriteToFile(Fun.G_UserVarDict['CurrentFile'],content):
            Fun.MessageBox('保存成功')
        else:
            Fun.MessageBox('保存失败')
def Menu_另存为(uiName,itemName):
    savePath = Fun.SaveFile(title="保存Python文件",filetypes=[('Python File','*.py'),('All files','*')],initDir = os.path.abspath('.'),defaultextension='py')
    if savePath != None:
        content = Fun.GetText('RightTextBar','Text_2')
        if True == Fun.WriteToFile(savePath,content):
            Fun.SetText(uiName,"root","PythonEditor:" + fileName)
            Fun.G_UserVarDict['CurrentFile'] = savePath
            Fun.MessageBox('保存成功')
        else:
            Fun.MessageBox('保存失败')
def Menu_退出(uiName,itemName):
    Fun.DestroyUI(uiName)
def Menu_剪切(uiName,itemName):
    Fun.G_UserVarDict['CutContent'] = Fun.GetSelectText(uiName,'Text_2')
    Fun.DelSelectText(uiName,'Text_2')
def Menu_拷贝(uiName,itemName):
    Fun.G_UserVarDict['CutContent'] = Fun.GetSelectText(uiName,'Text_2')
def Menu_粘贴(uiName,itemName):
    if 'CutContent' in Fun.G_UserVarDict:
        Fun.AddLineText(uiName,'Text_2',Fun.G_UserVarDict['CutContent'],'insert')
def Menu_运行(uiName,itemName):
        TextContent = Fun.GetText('RightTextBar','Text_2')
        OutputText = Fun.GetElement(uiName,'Text_7')
        tempFileName = os.path.join(Fun.G_ExeDir,"temp.py")
        f = open(tempFileName,mode='w',encoding='utf-8')
        f.write(TextContent.strip('\n'))
        #coding=utf-8
        f.close()
        projpath, projfile = os.path.split(tempFileName)
        cmdText = r'cd '+projpath + r'&&python -u '+projfile
        run_thread = threading.Thread(target=handle_output, args=[cmdText,OutputText])
        run_thread.Daemon = True
        run_thread.start()
def Menu_关于(uiName,itemName):
    Fun.MessageBox('欢迎使用PyMe')

