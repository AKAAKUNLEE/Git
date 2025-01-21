#coding=utf-8
#coding=utf-8
#coding=utf-8
#coding=utf-8
importimportimportimport sys
 sys
 sys
 sys
importimportimportimport os
 os
 os
 os
fromfromfrom   os.path from   os.path    os.path importimport   os.path import abspath, dirname
 abspath, dirname
import abspath, dirname
 abspath, dirname
sys.path.sys.path.sys.path.insertinsertsys.path.insert(0,abspath(dirname(__file__)))
(0,abspath(dirname(__file__)))
insert(0,abspath(dirname(__file__)))
(0,abspath(dirname(__file__)))
importimportimport tkinter
 tkinter
 tkinter
import tkinter
fromfromfrom   tkinter    tkinter    tkinter fromimportimportimport   tkinter  *
 *
 *
import *
importimportimport Fun
 Fun
 Fun
import Fun
ElementBGArray={}  
ElementBGArray={}  
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_Resize={} 
ElementBGArray_Resize={} 
ElementBGArray={}  
ElementBGArray_IM={} 
ElementBGArray_IM={} 
ElementBGArray_IM={} 
ElementBGArray_Resize={} 


ElementBGArray_IM={} 


importimportimport threading
 threading
 threading
import threading
importimportimport subprocess
 subprocess
 subprocess
import subprocess
importimportimport io
 io
 io
importG_UITreeImageArray={}
G_UITreeImageArray={}
G_UITreeImageArray={}
 io
G_UITreeImageArray={}
defdefdef handle_output handle_output handle_output(cmdText,OutputText):
(cmdText,OutputText):
(cmdText,OutputText):
def handle_output(cmdText,OutputText):
      process = subprocess.Popen(cmdText,shell=True, bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.DEVNULL,encoding=   process = subprocess.Popen(cmdText,shell=True, bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.DEVNULL,encoding=   process = subprocess.Popen(cmdText,shell=True, bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.DEVNULL,encoding='utf-8''utf-8''utf-8' )
)
)
   process = subprocess.Popen(cmdText,shell=True, bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.DEVNULL,encoding='utf-8')
      OutputText.   OutputText.   OutputText.deldeldel ete(ete(ete(   OutputText.'0.0''0.0''0.0'del,tkinter.END)
,tkinter.END)
,tkinter.END)
ete('0.0',tkinter.END)
      errorText = None
   errorText = None
   errorText = None
    errorText = None
      first = True
   first = True
   first = True
    first = True
            while whilewhile first     first  first ==while== == first  True ==True True  or Trueor process.poll(or  process.poll( process.poll(or)  process.poll() is) is is)  None isNone :
None  :
 :
None :
                               first = False
      first = False
 first = False
  first = False
                               output = process.stdout.readline()
      output = process.stdout.readline()
 output = process.stdout.readline()
   output = process.stdout.readline()
                              if       if if output:
   ifoutput:
output:
 output:
                                               OutputText.     insert OutputText. OutputText. (tkinter.END,output)
insertinsert OutputText.(tkinter.END,output)
(tkinter.END,output)
insert(tkinter.END,output)
                                               OutputText.see(tkinter.END)
      OutputText.see(tkinter.END)
 OutputText.see(tkinter.END)
  OutputText.see(tkinter.END)
                               else:
      else:
 else:
  else:
                                               output = process.communicate()
      output = process.communicate()
 output = process.communicate()
   output = process.communicate()
                                             if     if    iflen(output) > 0:
   len(output) > 0:
 iflen(output) > 0:
  len(output) > 0:
                                                             ErrorArray = output.   split ErrorArray = output. ErrorArray = output.   (splitsplit "
(( ErrorArray = output."
"
split(")
"
")
")
  ")
                                                                    forforfor  line in ErrorArray:
 line in ErrorArray:
 line in ErrorArray:
 for  line in ErrorArray:
                                                                               OutputText. OutputText.  OutputText.insertinsert   insert(tkinter.END,line)
(tkinter.END,line)
 (tkinter.END,line)
 OutputText.insert  (tkinter.END,line)
   process.stdout.close()
   process.stdout.close()
    process.stdout.close()
def def BuildAllFileTree   process.stdout.close()
def BuildAllFileTree(TreeCtrl,parentItem,parentPath,depth):
 BuildAllFileTree(TreeCtrl,parentItem,parentPath,depth):
(TreeCtrl,parentItem,parentPath,depth):
def  BuildAllFileTree    (TreeCtrl,parentItem,parentPath,depth):
    from   from   PIL from   PIL import    PIL import Image,ImageTk
   import Image,ImageTk
from Image,ImageTk
   PIL  import      Image,ImageTk
global       G_UITreeImageArray
globalglobal G_UITreeImageArray
  G_UITreeImageArray
    global     G_UITreeImageArray
 for       fileName forforin fileName   fileName  os.listdir(parentPath):
in   in os.listdir(parentPath):
for os.listdir(parentPath):
 fileName  in      os.listdir(parentPath):
          filename_lower = fileName.lower()
     filename_lower = fileName.lower()
   filename_lower = fileName.lower()
                 filename_lower = fileName.lower()
     if        if '__pycache__'        if'__pycache__' not      '__pycache__'notifin    fileName:
notin'__pycache__'  fileName:
in   fileName:
not         in      fileName:
            if         if'.git'        if'.git' not      not in '.git'    fileName:
if in not fileName:
'.git'   in   not  fileName:
        in   fileName:
                    newPath = parentPath +       '\\'   newPath = parentPath +  + fileName
'\\'      + fileName
     newPath = parentPath +    '\\'     + fileName
   newPath = parentPath +    '\\'    + fileName
                            print     (newPath)
print      (newPath)
         print     (newPath)
       print   (newPath)
                             if      os.path.isdir(newPath):
      if   os.path.isdir(newPath):
        if       os.path.isdir(newPath):
  if       os.path.isdir(newPath):
                                 IcoPath = os.path.     join            (Fun.G_ExeDir,       IcoPath = os.path."Ico\dir.png"    join)
   IcoPath = os.path. join   IcoPath = os.path.(Fun.G_ExeDir,join"Ico\dir.png" (Fun.G_ExeDir,)
   "Ico\dir.png"(Fun.G_ExeDir, )
"Ico\dir.png"    )
                                        if      os.path.exists(IcoPath)        ==             Trueif    :
 os.path.exists(IcoPath) if   == os.path.exists(IcoPath) if == os.path.exists(IcoPath)  True ==   :
True  :
True   :
                                                  imageRGBA = Image.open(IcoPath).convert(       'RGBA'     )
                imageRGBA = Image.open(IcoPath).convert(       imageRGBA = Image.open(IcoPath).convert('RGBA'    'RGBA')
   imageRGBA = Image.open(IcoPath).convert( )
'RGBA'   )
                                                  G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                               G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
            G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
   G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                                               newTreeItem = TreeCtrl.         insert   (parentItem,         'end'   ,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=("1"),tags = (      newTreeItem = TreeCtrl.   'dirs' insert ,))
   newTreeItem = TreeCtrl.(parentItem,   newTreeItem = TreeCtrl.insert'end'insert(parentItem,,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=("1"),tags = ((parentItem, 'end''dirs''end'   ,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=("1"),tags = (,))
,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=("1"),tags = ( 'dirs''dirs'   ,))
,))
                                               BuildAllFileTree(TreeCtrl,newTreeItem, newPath,depth +1)
                                  BuildAllFileTree(TreeCtrl,newTreeItem, newPath,depth +1)
            BuildAllFileTree(TreeCtrl,newTreeItem, newPath,depth +1)
    BuildAllFileTree(TreeCtrl,newTreeItem, newPath,depth +1)
                            else:
                                     else:
          else:
     else:
                                            newTreeItem = TreeCtrl.     insert       (parentItem,     'end'       ,newPath,text=fileName,values=("1"),tags = (     'dirs'   newTreeItem = TreeCtrl.    ,))
insert   newTreeItem = TreeCtrl. (parentItem,insert   newTreeItem = TreeCtrl.'end'(parentItem,insert ,newPath,text=fileName,values=("1"),tags = ('end'(parentItem,   'dirs',newPath,text=fileName,values=("1"),tags = ('end' ,))
'dirs',newPath,text=fileName,values=("1"),tags = (   ,))
'dirs' ,))
                                            BuildAllFileTree(TreeCtrl,newTreeItem, newPath,depth +1)
                                            BuildAllFileTree(TreeCtrl,newTreeItem, newPath,depth +1)
   BuildAllFileTree(TreeCtrl,newTreeItem, newPath,depth +1)
     BuildAllFileTree(TreeCtrl,newTreeItem, newPath,depth +1)
            else:
                                            else:
   else:
     else:
                                if      filename_lower.       find     (       ".png"     ) >= 0 or filename_lower.find(       ".jpg"ifif   )  filename_lower. filename_lower.if>=findfind filename_lower. 0 :
((find".png"".png"() >= 0 or filename_lower.find() >= 0 or filename_lower.find( ".png"".jpg"".jpg"   ) >= 0 or filename_lower.find() )  ".jpg">=>=   )  0 :
 0 :
 >=    0 :
                                      IcoPath =  os.path.       join            (Fun.G_ExeDir,     "Ico\img.png"       )
        IcoPath =  os.path.   IcoPath =  os.path. joinjoin   IcoPath =  os.path. join   (Fun.G_ExeDir,(Fun.G_ExeDir, "Ico\img.png""Ico\img.png"(Fun.G_ExeDir,   )
)
"Ico\img.png" )
                                                if      os.path.exists(IcoPath)        ==             True     :
       ifif    os.path.exists(IcoPath)  os.path.exists(IcoPath)  if====    os.path.exists(IcoPath)    ==TrueTrue    :
:
 True   :
                                                   imageRGBA = Image.open(IcoPath).convert(         'RGBA'   )
                                  imageRGBA = Image.open(IcoPath).convert(   imageRGBA = Image.open(IcoPath).convert(  'RGBA''RGBA'      imageRGBA = Image.open(IcoPath).convert()
)
 'RGBA'   )
                                                      G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                                               G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
   G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
        G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                                                      newTreeItem = TreeCtrl.       insert     (parentItem,       'end'     ,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=(       "2"     ))
   newTreeItem = TreeCtrl.   newTreeItem = TreeCtrl. insertinsert   newTreeItem = TreeCtrl.(parentItem,(parentItem, insert'end''end'   (parentItem,,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=(,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=( 'end'"2""2"   ,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=())
))
 "2"   ))
                                   else:
                                                  else:
    else:
       else:
                                                  newTreeItem = TreeCtrl.       insert     (parentItem,       'end'     ,newPath,text=fileName,values=(       "2"     ))
       newTreeItem = TreeCtrl.   newTreeItem = TreeCtrl. insertinsert   newTreeItem = TreeCtrl.(parentItem, (parentItem,insert'end'   'end'(parentItem,,newPath,text=fileName,values=( ,newPath,text=fileName,values=('end'"2"   "2",newPath,text=fileName,values=())
 ))
"2"   ))
                         elif      filename_lower.       find     (       ".mp3"     )        >=    elif 0:
elif    filename_lower. filename_lower.eliffindfind filename_lower.( (find".mp3"   ".mp3"()  ) ".mp3">=   >=)  0:
  0:
>=    0:
                                  IcoPath =  os.path.       join            (Fun.G_ExeDir,     "Ico\mp3.png"       )
            IcoPath =  os.path.    IcoPath =  os.path.join    IcoPath =  os.path.join   join(Fun.G_ExeDir, (Fun.G_ExeDir,"Ico\mp3.png"   (Fun.G_ExeDir,"Ico\mp3.png")
 "Ico\mp3.png")
   )
                                         if      os.path.exists(IcoPath)        ==             True     :
           ifif     os.path.exists(IcoPath)  os.path.exists(IcoPath) if   ==== os.path.exists(IcoPath)    ==   TrueTrue  :
:
True   :
                                                 imageRGBA = Image.open(IcoPath).convert(     'RGBA'       )
                                     imageRGBA = Image.open(IcoPath).convert(    imageRGBA = Image.open(IcoPath).convert(   'RGBA'   imageRGBA = Image.open(IcoPath).convert('RGBA' )
'RGBA')
   )
                                                     G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                                                 G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
    G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
   G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                                                        newTreeItem = TreeCtrl.     insert       (parentItem,     'end'       ,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=(     "2"       ))
     newTreeItem = TreeCtrl.   newTreeItem = TreeCtrl.   newTreeItem = TreeCtrl.insertinsertinsert(parentItem, (parentItem,(parentItem,'end'   'end''end',newPath,text=fileName,image=G_UITreeImageArray[newPath],values=( ,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=(,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=("2"   "2""2"))
 ))
))
                                        else:
                                                 else:
    else:
   else:
                                                          newTreeItem = TreeCtrl.         insert   (parentItem,         'end'   ,newPath,text=fileName,values=(         "2"   ))
   newTreeItem = TreeCtrl.   newTreeItem = TreeCtrl.   newTreeItem = TreeCtrl.insertinsertinsert(parentItem,(parentItem,(parentItem, 'end''end''end'   ,newPath,text=fileName,values=(,newPath,text=fileName,values=(,newPath,text=fileName,values=( "2""2""2"   ))
))
))
                                    elif    filename_lower.         find   (         ".py"   )          >=elifelifelif 0:
 filename_lower. filename_lower. filename_lower.findfindfind((( ".py"".py"".py"   ) ) )  >=>=>=    0:
 0:
 0:
                                           cmdfile = newPath[:-3] +          "_cmd.py"   
                               cmdfile = newPath[:-3] +    cmdfile = newPath[:-3] +    cmdfile = newPath[:-3] +  "_cmd.py""_cmd.py""_cmd.py"   


                                                    if    os.path.exists(cmdfile)          ==             True   :
         ififif os.path.exists(cmdfile)  os.path.exists(cmdfile)  os.path.exists(cmdfile)  ======       TrueTrueTrue   :
:
:
                                                              IcoPath =  os.path.       join            (Fun.G_ExeDir,     "Ico\Form.png"       )
     IcoPath =  os.path.   IcoPath =  os.path.   IcoPath =  os.path.joinjoinjoin (Fun.G_ExeDir,   (Fun.G_ExeDir,(Fun.G_ExeDir,"Ico\Form.png" "Ico\Form.png""Ico\Form.png")
   )
)
                                                                         if      os.path.exists(IcoPath)        ==             True    if:
if    os.path.exists(IcoPath)  os.path.exists(IcoPath) if==== os.path.exists(IcoPath)    ==True   True :
 :
True   :
                                                                                  imageRGBA = Image.open(IcoPath).convert(       'RGBA'     )
                   imageRGBA = Image.open(IcoPath).convert(    imageRGBA = Image.open(IcoPath).convert( 'RGBA'   'RGBA'   imageRGBA = Image.open(IcoPath).convert()
 )
'RGBA'   )
                                                                               G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                                      G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
        G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
   G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                                                                                        newTreeItem = TreeCtrl.   insert         (parentItem,   'end'         newTreeItem = TreeCtrl.,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=(  insert"2"   newTreeItem = TreeCtrl.   newTreeItem = TreeCtrl.(parentItem,))
insertinsert'end'(parentItem,(parentItem,,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=('end''end' "2",newPath,text=fileName,image=G_UITreeImageArray[newPath],values=(,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=(   ))
"2""2" ))
))
                                                                        else:
                                else:
     else:
   else:
                                                                                        newTreeItem = TreeCtrl.     insert       (parentItem,     'end'       ,newPath,text=fileName,values=(   newTreeItem = TreeCtrl.  "2"insert   newTreeItem = TreeCtrl.   newTreeItem = TreeCtrl.))
(parentItem,insertinsert'end'(parentItem,(parentItem,,newPath,text=fileName,values=('end''end' "2",newPath,text=fileName,values=(,newPath,text=fileName,values=(   ))
"2""2" ))
))
                                                        else:
                               else:
      else:
      else:
                                                                  IcoPath = os.path.       join            (Fun.G_ExeDir,     "Ico\py.png"      IcoPath = os.path.  join   IcoPath = os.path.)
   IcoPath = os.path.joinjoin(Fun.G_ExeDir,"Ico\py.png"(Fun.G_ExeDir, (Fun.G_ExeDir,)
"Ico\py.png"   "Ico\py.png")
 )
                                                                                    if      os.path.exists(IcoPath)        ==      if      True os.path.exists(IcoPath) ifif:
== os.path.exists(IcoPath)  os.path.exists(IcoPath)  ====True   :
TrueTrue   :
:
                                                                                              imageRGBA = Image.open(IcoPath).convert(       'RGBA'     )
          imageRGBA = Image.open(IcoPath).convert(  'RGBA'   imageRGBA = Image.open(IcoPath).convert(   imageRGBA = Image.open(IcoPath).convert( )
'RGBA''RGBA'   )
)
                                                                                              G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                       G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
        G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
   G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                                                                                               newTreeItem = TreeCtrl.         insert   (parentItem,         newTreeItem = TreeCtrl.'end'  insert,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=(   newTreeItem = TreeCtrl.   newTreeItem = TreeCtrl.(parentItem,"2"insertinsert'end'))
(parentItem,(parentItem,,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=('end''end'"2",newPath,text=fileName,image=G_UITreeImageArray[newPath],values=(,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=())
 "2""2"   ))
))
                                                                               else:
                      else:
        else:
   else:
                                                                                                     newTreeItem = TreeCtrl.     insert       (parentItem,     newTreeItem = TreeCtrl.'end'   newTreeItem = TreeCtrl.   newTreeItem = TreeCtrl.insert,newPath,text=fileName,values=(insertinsert(parentItem,"2"(parentItem,(parentItem,'end'))
'end''end',newPath,text=fileName,values=(,newPath,text=fileName,values=("2",newPath,text=fileName,values=("2"))
 "2"))
   ))
                                                  else:
                   else:
     else:
      else:
                                                                  IcoPath = os.path.       join            IcoPath = os.path.(Fun.G_ExeDir,    IcoPath = os.path.join"Ico\txt.png"   IcoPath = os.path.join)
join(Fun.G_ExeDir,(Fun.G_ExeDir,"Ico\txt.png"(Fun.G_ExeDir,"Ico\txt.png")
 "Ico\txt.png")
   )
                                                                         if      os.path.exists(IcoPath)        ==    if    if os.path.exists(IcoPath) Trueif os.path.exists(IcoPath) ==:
 os.path.exists(IcoPath) == == True True:
 True:
   :
                                                                                  imageRGBA = Image.open(IcoPath).convert(       'RGBA'     )
       imageRGBA = Image.open(IcoPath).convert(    imageRGBA = Image.open(IcoPath).convert('RGBA'   imageRGBA = Image.open(IcoPath).convert('RGBA' )
'RGBA')
   )
                                                                                     G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
     G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
   G_UITreeImageArray[newPath] = ImageTk.PhotoImage(imageRGBA)
                                                                                        newTreeItem = TreeCtrl.     insert       (parentItem,     newTreeItem = TreeCtrl.'end'   newTreeItem = TreeCtrl.   newTreeItem = TreeCtrl.insert,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=(insertinsert(parentItem,"2"(parentItem,(parentItem,'end'))
'end''end',newPath,text=fileName,image=G_UITreeImageArray[newPath],values=(,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=(,newPath,text=fileName,image=G_UITreeImageArray[newPath],values=("2""2""2"))
 ))
))
                                                                         else:
                else:
    else:
   else:
                                                                                        newTreeItem = TreeCtrl.     insert       (parentItem,   newTreeItem = TreeCtrl.  'end'insert   newTreeItem = TreeCtrl.   newTreeItem = TreeCtrl.,newPath,text=fileName,values=((parentItem,insertinsert"2"'end'(parentItem,(parentItem,))
,newPath,text=fileName,values=('end''end'"2",newPath,text=fileName,values=(,newPath,text=fileName,values=())
"2""2"def))
))
 Form_1_onConfigure(event,uiName,widgetName):
def Form_1_onConfiguredefdef(event,uiName,widgetName):
 Form_1_onConfigure Form_1_onConfigure (event,uiName,widgetName):
(event,uiName,widgetName):
   PanedWindow_6 =  Fun.   PanedWindow_6 = GetElement  Fun.(uiName,   PanedWindow_6 =    PanedWindow_6 = GetElement'PanedWindow_6'Fun.Fun.(uiName,)
GetElementGetElement'PanedWindow_6'(uiName,(uiName,)
'PanedWindow_6''PanedWindow_6' )
)
   Text7 =  Fun.   Text7 =   GetElementFun.   Text7 =    Text7 = (uiName,GetElementFun.Fun.'Text_7'(uiName,GetElementGetElement)
'Text_7'(uiName,(uiName,)
'Text_7''Text_7')
)
     PanedWindow_6.place(x = 0,y = 50,width = event.width,height = event.height - 51 - 100)
   PanedWindow_6.place(x = 0,y = 50,width = event.width,height = event.height - 51 - 100)
     PanedWindow_6.place(x = 0,y = 50,width = event.width,height = event.height - 51 - 100)
   PanedWindow_6.place(x = 0,y = 50,width = event.width,height = event.height - 51 - 100)
     Text7.place(x = 0,y = event.height - 100,width = event.width,height = 100)
   Text7.place(x = 0,y = event.height - 100,width = event.width,height = 100)
     Text7.place(x = 0,y = event.height - 100,width = event.width,height = 100)
   Text7.place(x = 0,y = event.height - 100,width = event.width,height = 100)
def Form_1_onLoaddef(uiName):
 Form_1_onLoaddefdef(uiName):
 Form_1_onLoad Form_1_onLoad(uiName):
(uiName):
    TreeView_2 =  Fun.   TreeView_2 =  GetElement Fun.   TreeView_2 = (   TreeView_2 = Fun.'LeftTreeBar'Fun.GetElementGetElement,GetElement(('TreeView_2'('LeftTreeBar''LeftTreeBar')
'LeftTreeBar',,,'TreeView_2''TreeView_2''TreeView_2')
)
 )
   if   TreeView_2 !=        None   ifif:
if TreeView_2 !=  TreeView_2 !=  TreeView_2 != NoneNoneNone:
:
 :
          BuildAllFileTree(TreeView_2,         ''   ,Fun.G_ExeDir,1)
   BuildAllFileTree(TreeView_2,   BuildAllFileTree(TreeView_2,   BuildAllFileTree(TreeView_2,'''''',Fun.G_ExeDir,1)
,Fun.G_ExeDir,1)
,Fun.G_ExeDir,1)
#Button 'Button's Event :Command
#Button 'Button's Event :Command
#Button 'Button's Event :Command
#Button 'Button's Event :Command
def Button_2_onCommand(uiName,widgetName):
defdefdef Button_2_onCommand Button_2_onCommand Button_2_onCommand(uiName,widgetName):
 (uiName,widgetName):
(uiName,widgetName):
   Menu_新建(uiName,None)
     Menu_新建(uiName,None)
#Button 'Button's Event :Command
    Menu_新建(uiName,None)
   Menu_新建(uiName,None)
#Button 'Button's Event :Command
def#Button 'Button's Event :Command
 Button_3_onCommand#Button 'Button's Event :Command
(uiName,widgetName):
def Button_3_onCommanddefdef(uiName,widgetName):
 Button_3_onCommand Button_3_onCommand (uiName,widgetName):
(uiName,widgetName):
   Menu_打开(uiName,None)
     Menu_打开(uiName,None)
 #Button 'Button's Event :Command
   Menu_打开(uiName,None)
   Menu_打开(uiName,None)
#Button 'Button's Event :Command
def#Button 'Button's Event :Command
#Button 'Button's Event :Command
 Button_4_onCommand(uiName,widgetName):
def Button_4_onCommanddefdef(uiName,widgetName):
 Button_4_onCommand Button_4_onCommand (uiName,widgetName):
(uiName,widgetName):
   Menu_保存(uiName,None)
    Menu_保存(uiName,None)
  #Button 'Button's Event :Command
   Menu_保存(uiName,None)
   Menu_保存(uiName,None)
#Button 'Button's Event :Command
def#Button 'Button's Event :Command
#Button 'Button's Event :Command
 Button_5_onCommanddef(uiName,widgetName):
 Button_5_onCommanddefdef(uiName,widgetName):
 Button_5_onCommand Button_5_onCommand (uiName,widgetName):
(uiName,widgetName):
   Menu_运行(uiName,None)
    Menu_运行(uiName,None)
 def    Menu_运行(uiName,None)
 Menu_新建   Menu_运行(uiName,None)
def(uiName,itemName):
 Menu_新建def(uiName,itemName):
def Menu_新建  Menu_新建(uiName,itemName):
   content = (uiName,itemName):
 Fun.   content = GetText Fun.(    content = GetText'RightTextBar'   content = Fun.(,Fun.GetText'RightTextBar''Text_2'GetText(,)
('RightTextBar''Text_2''RightTextBar',)
,'Text_2' 'Text_2')
   )
 if    if len     (content) > 0    lenifandif(content) > 0   content != andlen'\n'len content !=(content) > 0 :
(content) > 0 '\n'andand:
 content != content !='\n' '\n':
   :
        result =   Fun.    result =    AskBox   Fun. ( AskBox   result = '提示'   result = (Fun.,Fun.'提示'AskBox'是否保存当前文件？'AskBox,()
('是否保存当前文件？''提示''提示')
,,'是否保存当前文件？' '是否保存当前文件？')
   )
          if        result    if ==  result        ==ifTrueif  result :
 result True====:
  True True:
   :
                          if           if 'CurrentFile'         'CurrentFile'ifnotif    not'CurrentFile'in'CurrentFile'   Fun.G_UserVarDict:
 innotnot Fun.G_UserVarDict:
   inin    Fun.G_UserVarDict:
 Fun.G_UserVarDict:
                                  savePath =        Fun.     savePath = SaveFile      Fun.(title=  SaveFile"保存Python文件"   savePath =    savePath = (title=,filetypes=Fun.Fun."保存Python文件"[SaveFileSaveFile,filetypes=((title=(title=["保存Python文件"'Python File'"保存Python文件"(,filetypes=,,filetypes='Python File'['*.py'[,(),(('*.py''Python File''All files''Python File'),(,,,'All files''*.py''*''*.py',),()],initDir = os.path.abspath(),('*''All files''.''All files')],initDir = os.path.abspath(,),defaultextension=,'.''*''py''*'),defaultextension=)],initDir = os.path.abspath()
)],initDir = os.path.abspath('py''.''.')
),defaultextension=),defaultextension= 'py''py'   )
)
                                         if      savePath !=       ifNone   savePath !=        Noneandifif   savePath !=  savePath != andlenNoneNone (savePath) > 0:
  lenandand(savePath) > 0:
   lenlen   (savePath) > 0:
(savePath) > 0:
                                                         if            ifTrue    == Fun.WriteToFile(savePath,content)      True:
ifif == Fun.WriteToFile(savePath,content)  :
TrueTrue  == Fun.WriteToFile(savePath,content) == Fun.WriteToFile(savePath,content)   :
:
                                                                           Fun.         SetTextFun.  (uiName,SetText      "root"(uiName,Fun.Fun.,"root"SetTextSetText"PythonEditor:",(uiName,(uiName, + fileName)
"PythonEditor:""root""root" + fileName)
,,"PythonEditor:""PythonEditor:"  + fileName)
 + fileName)
                                                                           Fun.G_UserVarDict[   'CurrentFile'   Fun.G_UserVarDict[      ]  = savePath
'CurrentFile'  ]  = savePath
   Fun.G_UserVarDict[   Fun.G_UserVarDict['CurrentFile''CurrentFile' ]  = savePath
]  = savePath
                                                                              Fun.         MessageBoxFun.  (MessageBox      '保存成功'(Fun.Fun.)
'保存成功'MessageBoxMessageBox)
(('保存成功''保存成功' )
)
                                                           else:
      else:
            else:
   else:
                                                                                 Fun.      Fun.MessageBox  MessageBox(      ('保存失败'Fun.Fun.'保存失败')
MessageBoxMessageBox)
(('保存失败''保存失败' )
)
                                            Fun.G_UserVarDict[     Fun.G_UserVarDict['CurrentFile'      'CurrentFile']  = savePath
  ]  = savePath
   Fun.G_UserVarDict[   Fun.G_UserVarDict['CurrentFile''CurrentFile' ]  = savePath
]  = savePath
                            else:
     else:
            else:
   else:
                                              if          if  False        == Fun.WriteToFile(Fun.G_UserVarDict['CurrentFile'] ,content)Falseifif:
 == Fun.WriteToFile(Fun.G_UserVarDict['CurrentFile'] ,content)  :
FalseFalse == Fun.WriteToFile(Fun.G_UserVarDict['CurrentFile'] ,content) == Fun.WriteToFile(Fun.G_UserVarDict['CurrentFile'] ,content) :
:
                                                              Fun.         MessageBox  Fun.(      MessageBox'保存失败'Fun.Fun.()
MessageBoxMessageBox'保存失败'(()
'保存失败''保存失败' )
)
                                                           return
            return
      return
   return
   Fun. SetText     (Fun.      'RightTextBar'SetTextFun.Fun.,(SetTextSetText'Text_2''RightTextBar'((,,'RightTextBar''RightTextBar''''Text_2',,)
,'Text_2''Text_2''',,)
''def'')
 Menu_打开)
(uiName,itemName):
def Menu_打开defdef(uiName,itemName):
 Menu_打开  Menu_打开(uiName,itemName):
   openPath = (uiName,itemName):
Fun.    openPath = OpenFile  Fun.(title=   openPath =    openPath = OpenFile"打开Python文件"Fun.Fun.(title=,filetypes=OpenFileOpenFile"打开Python文件"[(title=(title=,filetypes=("打开Python文件""打开Python文件"['Python File',filetypes=,filetypes=(,[['Python File''*.py'((,),('Python File''Python File''*.py''All files',,),(,'*.py''*.py''All files''*'),(),(,)],initDir = os.path.abspath('All files''All files''*''.',,)],initDir = os.path.abspath())
'*''*''.')],initDir = os.path.abspath()],initDir = os.path.abspath())
'.''.' ))
))
    if    openPath !=   ifNone       openPath !=  ififNoneand openPath !=  openPath !=   NoneNoneandlen   (openPath) > 0:
andandlen  (openPath) > 0:
lenlen (openPath) > 0:
(openPath) > 0:
            content =      Fun.   content =     ReadFromFileFun.    content = (openPath)
ReadFromFile   content = Fun.(openPath)
Fun.ReadFromFileReadFromFile(openPath)
 (openPath)
            Fun.G_UserVarDict[     'CurrentFile'   Fun.G_UserVarDict[    ] = openPath
'CurrentFile'    Fun.G_UserVarDict[] = openPath
   Fun.G_UserVarDict['CurrentFile''CurrentFile' ] = openPath
] = openPath
              Fun.         SetText Fun. (   SetText   'RightTextBar'Fun.(Fun.,SetText'RightTextBar'SetText'Text_2'(,(,content)
'RightTextBar''Text_2''RightTextBar',,content)
,'Text_2''Text_2'def,content)
,content)
 Menu_保存def(uiName,itemName):
 Menu_保存def(uiName,itemName):
def Menu_保存  Menu_保存(uiName,itemName):
   (uiName,itemName):
 if    if 'CurrentFile'         'CurrentFile'ifnotif    not'CurrentFile'in'CurrentFile'   Fun.G_UserVarDict:
 innotnot Fun.G_UserVarDict:
  in in Fun.G_UserVarDict:
    Fun.G_UserVarDict:
        savePath =       savePath =    Fun.   Fun. SaveFile SaveFile   savePath = (title=   savePath = (title=Fun."保存Python文件"Fun."保存Python文件",filetypes=SaveFileSaveFile,filetypes=[(title=(title=[("保存Python文件""保存Python文件"('Python File',filetypes=,filetypes='Python File',[[,'*.py'(('*.py'),('Python File''Python File'),('All files',,'All files','*.py''*.py','*'),(),('*')],initDir = os.path.abspath('All files''All files')],initDir = os.path.abspath('.',,'.'),defaultextension='*''*'),defaultextension='py')],initDir = os.path.abspath()],initDir = os.path.abspath('py')
'.''.')
),defaultextension=),defaultextension='py''py' )
)
                       ifif   savePath !=  savePath !=       NoneNoneifif   savePath !=  savePath != andandNoneNone    lenlenandand(savePath) > 0:
(savePath) > 0:
  lenlen(savePath) > 0:
(savePath) > 0:
                               content =    content =       Fun.Fun.  GetTextGetText   content =    content = ((Fun.Fun.'RightTextBar''RightTextBar'GetTextGetText,,(('Text_2''Text_2''RightTextBar''RightTextBar')
)
,,'Text_2''Text_2')
)
                                        ifif          TrueTrueifif == Fun.WriteToFile(savePath,content) == Fun.WriteToFile(savePath,content)  :
:
TrueTrue == Fun.WriteToFile(savePath,content) == Fun.WriteToFile(savePath,content):
:
                                                        Fun.Fun.  SetTextSetText      (uiName,(uiName,Fun.Fun."root""root"SetTextSetText,,(uiName,(uiName,"PythonEditor:""PythonEditor:""root""root" + fileName)
 + fileName)
,,"PythonEditor:""PythonEditor:" + fileName)
 + fileName)
                                               Fun.G_UserVarDict[   Fun.G_UserVarDict[      'CurrentFile''CurrentFile'  ] = savePath
] = savePath
   Fun.G_UserVarDict[   Fun.G_UserVarDict['CurrentFile''CurrentFile'] = savePath
] = savePath
                                                        Fun.Fun.  MessageBoxMessageBox      ((Fun.Fun.'保存成功''保存成功'MessageBoxMessageBox)
)
(('保存成功''保存成功')
)
                               else:
   else:
           else:
     else:
                                                   Fun.Fun.    MessageBoxMessageBox    ((   Fun.'保存失败''保存失败'Fun.MessageBox)
)
MessageBox(('保存失败''保存失败')
 )
    else:
   else:
     else:
    else:
             content =     content =    Fun.   Fun. GetText GetText   content = (   content = (Fun.'RightTextBar'Fun.'RightTextBar'GetText,GetText,('Text_2'('Text_2''RightTextBar')
'RightTextBar')
,,'Text_2''Text_2')
 )
                    if    if      True   ifTrue == Fun.WriteToFile(Fun.G_UserVarDict['CurrentFile'],content)if  == Fun.WriteToFile(Fun.G_UserVarDict['CurrentFile'],content):
 True:
True == Fun.WriteToFile(Fun.G_UserVarDict['CurrentFile'],content) == Fun.WriteToFile(Fun.G_UserVarDict['CurrentFile'],content):
 :
                                 Fun.       MessageBoxFun.    (MessageBox   Fun.'保存成功'(Fun.MessageBox)
'保存成功'MessageBox()
('保存成功''保存成功' )
)
           else:
         else:
         else:
   else:
                                    Fun.     MessageBoxFun.      (MessageBoxFun.Fun.'保存失败'(MessageBoxMessageBox)
'保存失败'(()
'保存失败''保存失败')
)
def Menu_另存为def(uiName,itemName):
 Menu_另存为defdef(uiName,itemName):
 Menu_另存为 Menu_另存为(uiName,itemName):
 (uiName,itemName):
   savePath =  Fun.   savePath =  SaveFile Fun.   savePath = (title=   savePath = SaveFileFun."保存Python文件"Fun.(title=SaveFile,filetypes=SaveFile"保存Python文件"(title=[(title=,filetypes="保存Python文件"("保存Python文件"[,filetypes='Python File',filetypes=([,['Python File'('*.py'(,'Python File'),('Python File''*.py','All files',),('*.py','*.py''All files'),('*'),(,'All files')],initDir = os.path.abspath('All files''*','.',)],initDir = os.path.abspath('*'),defaultextension='*''.')],initDir = os.path.abspath('py')],initDir = os.path.abspath(),defaultextension='.')
'.''py'),defaultextension=),defaultextension=)
'py''py')
 )
    if     savePath !=  if   None    savePath != if:
ifNone savePath !=  savePath != :
NoneNone:
 :
            content =      Fun.   content =     GetTextFun.    content = (GetText   content = Fun.'RightTextBar'(Fun.GetText,'RightTextBar'GetText('Text_2',('RightTextBar')
'Text_2''RightTextBar',)
,'Text_2''Text_2')
 )
                 if        if    True    if == Fun.WriteToFile(savePath,content)Trueif :
 == Fun.WriteToFile(savePath,content) True:
True == Fun.WriteToFile(savePath,content) == Fun.WriteToFile(savePath,content):
 :
                                 Fun.       SetTextFun.    (uiName,SetText   Fun."root"(uiName,Fun.SetText,"root"SetText(uiName,"PythonEditor:",(uiName,"root" + fileName)
"PythonEditor:""root", + fileName)
,"PythonEditor:""PythonEditor:"  + fileName)
 + fileName)
                           Fun.G_UserVarDict[   'CurrentFile'      Fun.G_UserVarDict[   ] = savePath
 'CurrentFile'    Fun.G_UserVarDict[] = savePath
   Fun.G_UserVarDict['CurrentFile''CurrentFile' ] = savePath
] = savePath
                              Fun.         Fun.MessageBox  MessageBox(      ('保存成功'Fun.Fun.'保存成功')
MessageBoxMessageBox)
(('保存成功''保存成功' )
)
            else:
     else:
            else:
   else:
                                 Fun.      Fun.MessageBox  MessageBox(      ('保存失败'Fun.Fun.'保存失败')
MessageBoxMessageBox)
(('保存失败''保存失败'def)
def)
 Menu_退出 Menu_退出(uiName,itemName):
(uiName,itemName):
defdef Menu_退出 Menu_退出 (uiName,itemName):
 (uiName,itemName):
      Fun.Fun.DestroyUI  DestroyUI(uiName)
      (uiName)
Fun.Fun.DestroyUIdefDestroyUI(uiName)
def Menu_剪切(uiName)
 Menu_剪切(uiName,itemName):
(uiName,itemName):
defdef Menu_剪切 Menu_剪切(uiName,itemName):
  (uiName,itemName):
      Fun.Fun. G_UserVarDict['CutContent'] = Fun.GetSelectText G_UserVarDict['CutContent'] = Fun.GetSelectText   (uiName,   (uiName,Fun.'Text_2'Fun.'Text_2'G_UserVarDict['CutContent'] = Fun.GetSelectText)
G_UserVarDict['CutContent'] = Fun.GetSelectText)
(uiName,(uiName,'Text_2''Text_2')
 )
       Fun. Fun.DelSelectText    DelSelectText(uiName,   Fun.(uiName,'Text_2'Fun.DelSelectText'Text_2')
DelSelectText(uiName,)
(uiName,'Text_2''Text_2')
def)
def Menu_拷贝 Menu_拷贝(uiName,itemName):
def(uiName,itemName):
def Menu_拷贝 Menu_拷贝(uiName,itemName):
(uiName,itemName):
        Fun.  Fun.G_UserVarDict['CutContent'] = Fun.GetSelectText      G_UserVarDict['CutContent'] = Fun.GetSelectText(uiName,Fun.Fun.(uiName,'Text_2'G_UserVarDict['CutContent'] = Fun.GetSelectTextG_UserVarDict['CutContent'] = Fun.GetSelectText'Text_2')
(uiName,(uiName,)
'Text_2''Text_2')
)
def Menu_粘贴def(uiName,itemName):
 Menu_粘贴defdef(uiName,itemName):
 Menu_粘贴 Menu_粘贴(uiName,itemName):
(uiName,itemName):
     if      if      'CutContent' ifif 'CutContent'  in 'CutContent''CutContent' Fun.G_UserVarDict:
in   Fun.G_UserVarDict:
inin Fun.G_UserVarDict:
 Fun.G_UserVarDict:
                     Fun.     AddLineTextFun.      (uiName,AddLineTextFun.Fun.'Text_2'(uiName,AddLineTextAddLineText,Fun.G_UserVarDict['Text_2'(uiName,(uiName,'CutContent',Fun.G_UserVarDict['Text_2''Text_2'],'CutContent',Fun.G_UserVarDict[,Fun.G_UserVarDict['insert'],'CutContent''CutContent')
'insert'],],)
'insert''insert')
def)
 Menu_运行def(uiName,itemName):
 Menu_运行def(uiName,itemName):
def Menu_运行 Menu_运行(uiName,itemName):
 (uiName,itemName):
             TextContent =        TextContent = Fun.    Fun.GetText    TextContent = GetText(   TextContent = Fun.('RightTextBar'Fun.GetText'RightTextBar',GetText(,'Text_2'('RightTextBar''Text_2')
'RightTextBar',)
,'Text_2''Text_2')
 )
             OutputText =        OutputText = Fun.    Fun.GetElement    OutputText = GetElement(uiName,   OutputText = Fun.(uiName,'Text_7'Fun.GetElement'Text_7')
GetElement(uiName,)
(uiName,'Text_7''Text_7')
 )
             tempFileName = os.path.       tempFileName = os.path.join    join   tempFileName = os.path. (Fun.G_ExeDir,join   tempFileName = os.path.(Fun.G_ExeDir,"temp.py"join"temp.py")
(Fun.G_ExeDir,)
"temp.py"(Fun.G_ExeDir,)
"temp.py" )
            f = open(tempFileName,mode=     'w'   f = open(tempFileName,mode= ,encoding=   'w'   f = open(tempFileName,mode='utf-8' ,encoding='w')
   f = open(tempFileName,mode='utf-8',encoding='w')
'utf-8',encoding= )
'utf-8'   )
        f.write(TextContent.strip(  '\n'       f.write(TextContent.strip())
    '\n'   f.write(TextContent.strip( ))
'\n'   f.write(TextContent.strip( ))
'\n'    ))
         #coding=utf-8
        #coding=utf-8
        #coding=utf-8
        #coding=utf-8
      f.close()
        f.close()
      f.close()
            f.close()
      projpath, projfile = os.path.  split      projpath, projfile = os.path.(tempFileName)
  split   projpath, projfile = os.path.   (tempFileName)
split  (tempFileName)
   projpath, projfile = os.path.   split  (tempFileName)
   cmdText = r    'cd '    +projpath + r   cmdText = r  '&&python -u ''cd '   cmdText = r   +projfile
+projpath + r'cd ' '&&python -u '+projpath + r   cmdText = r+projfile
'&&python -u ' 'cd '+projfile
   +projpath + r '&&python -u '    run_thread = threading.Thread(target=handle_output, args=[cmdText,OutputText])
+projfile
            run_thread = threading.Thread(target=handle_output, args=[cmdText,OutputText])
     run_thread = threading.Thread(target=handle_output, args=[cmdText,OutputText])
            run_thread.Daemon = True
    run_thread = threading.Thread(target=handle_output, args=[cmdText,OutputText])
           run_thread.Daemon = True
    run_thread.Daemon = True
              run_thread.start()
   run_thread.Daemon = True
           run_thread.start()
   run_thread.start()
def  Menu_关于   (uiName,itemName):
def def Menu_关于   run_thread.start()
 Menu_关于(uiName,itemName):
 (uiName,itemName):
   defFun. Menu_关于MessageBox (uiName,itemName):
 (      '欢迎使用PyMe'Fun.Fun.) MessageBoxMessageBox   ((Fun.'欢迎使用PyMe''欢迎使用PyMe'MessageBox))('欢迎使用PyMe')
