import PySimpleGUI as sg
import os,threading,time,re
isFileTxt=os.path.isfile('lastBackup.txt')
arr=['','','']
if isFileTxt:
    myfile = open("lastBackup.txt","r")
    valueFile = myfile.read()
    myfile.close()
    if valueFile.split("*")!=['']:
        arr = valueFile.split("*")
        
    else:
        myfile = open("lastBackup.txt","w")
        myfile = myfile.write("null*"+"null*"+"null")
        arr = ["null","null","null"]
else:
    myfile = open("lastBackup.txt","w")
    myfile = myfile.write("null*"+"null*"+"null")
    arr = ["null","null","null"]


isEceptionFileTxt=os.path.isfile('exception.txt')

if isEceptionFileTxt:
    myfile = open("exception.txt","r")
    valueFile = myfile.read()
    myfile.close()
else:
    myfile = open("exception.txt","w")
    myfile = myfile.write("null")
    valueFile="null"
    

sg.theme("DarkAmber")
if arr[2]=="one":
    layout = [
        [sg.T("")],
        [sg.Text("Backup from : ",text_color='white',key="backupfromText"), sg.Input(key="-IN1-" ,change_submits=True,default_text=arr[0],size=(50,50)), sg.FolderBrowse(key="-IN2-")],
        [sg.Text("Save to :        ",text_color='white'), sg.InputText(key="-IN3-" ,change_submits=True,default_text=arr[1],size=(50,50)), sg.FolderBrowse(key="-IN4-")],
        [sg.Radio('multiple Select', "RADIO1", default=False,key="radio",enable_events=True),sg.Radio('one path', "RADIO1",default=True,enable_events=True)],
        [sg.Text("exception path:",text_color='red'),sg.T(""),sg.Multiline("",key="Exception",auto_size_text=True,change_submits=True,text_color='pink',size=(50,5))],
        [sg.Text("                                    ",text_color='white',key="multipleText"),sg.Multiline("",key="multiple",auto_size_text=True,change_submits=True,text_color='white',size=(50,20),visible =False)],
        [sg.Text("Results :            ",text_color='white'),sg.Multiline(" ",key="-run-",auto_size_text=True,text_color='white',size=(50,1))],
        [sg.T("")],[sg.T("")],
        [sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.Button("Submit", button_color=('white', 'green'),border_width=5) , sg.Button("Cancel",button_color=('white', 'red'),border_width=5)],
        [sg.T("")],
        [sg.T("")],
        [sg.Text("produce by norouzy_mohamad    16/7/2021",text_color='white', font='Courier 8')]
    ]
elif arr[2]=="mul":
    layout = [
        [sg.T("")],
        [sg.Text("Find easy :     ",text_color='white',key="backupfromText"), sg.Input(key="-IN1-" ,change_submits=True,default_text="",size=(50,50)), sg.FolderBrowse(key="-IN2-")],
        [sg.Text("Save to :        ",text_color='white'), sg.InputText(key="-IN3-" ,change_submits=True,default_text=arr[1],size=(50,50)), sg.FolderBrowse(key="-IN4-")],
        [sg.Radio('multiple Select', "RADIO1", default=True,key="radio",enable_events=True),sg.Radio('one path', "RADIO1",enable_events=True)],
        [sg.Text("exception path:",text_color='red'),sg.T(""),sg.Multiline("",key="Exception",auto_size_text=True,change_submits=True,text_color='pink',size=(50,5))],
        [sg.Text("Multiple path     : ",text_color='white',key="multipleText"),sg.Multiline("",key="multiple",auto_size_text=True,text_color='white',size=(50,20))],
        [sg.Text("Results :            ",text_color='white'),sg.Multiline(" ",key="-run-",auto_size_text=True,text_color='white',size=(50,1))],
        [sg.T("")],[sg.T("")],
        [sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.Button("Submit", button_color=('white', 'green')) , sg.Button("Cancel",button_color=('white', 'red'))],
        [sg.T("")],
        [sg.T("")],
        [sg.Text("produce by norouzy    16/7/2021",text_color='white', font='Courier 8')]
    ]
else:
    layout = [
        [sg.T("")],
        [sg.Text("Backup from : ",text_color='white',key="backupfromText"), sg.Input(key="-IN1-" ,change_submits=True,size=(50,50)), sg.FolderBrowse(key="-IN2-")],
        [sg.Text("Save to :        ",text_color='white'), sg.InputText(key="-IN3-" ,change_submits=True,size=(50,50)), sg.FolderBrowse(key="-IN4-")],
        [sg.Radio('multiple Select', "RADIO1", default=False,key="radio",enable_events=True),sg.Radio('one path', "RADIO1",default=True,enable_events=True)],
        [sg.Text("exception path:",text_color='red'),sg.T(""),sg.Multiline("$RECYCLE.BIN,System Volume Information",key="Exception",auto_size_text=True,change_submits=True,text_color='pink',size=(50,5))],
        [sg.Text("                                    ",text_color='white',key="multipleText"),sg.Multiline("",key="multiple",auto_size_text=True,change_submits=True,text_color='white',size=(50,20),visible =False)],
        [sg.Text("Results :            ",text_color='white'),sg.Multiline(" ",key="-run-",auto_size_text=True,text_color='white',size=(50,1))],
        [sg.T("")],[sg.T("")],
        [sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.T(""),sg.Button("Submit", button_color=('white', 'green')) , sg.Button("Cancel",button_color=('white', 'red'))],
        [sg.T("")],
        [sg.T("")],
        [sg.Text("produce by norouzy_mohamad    16/7/2021",text_color='white', font='Courier 8')]
    ]
flag=0

###Building Window
window = sg.Window('Backup', layout,icon='backup_icon-icons.com_72047.ico', resizable=True, finalize=True)
if arr[2]=="mul":
    window['multiple'].update(arr[0])
else:
    window['multiple'].update("")
if valueFile != None and valueFile !=" " and valueFile!="null":
    window['Exception'].update(valueFile)

def checkFileName(paths):
    if len(paths)>259:
        arrPath = paths.split("/")
        checkName = arrPath[len(arrPath)-1]
        checkName= checkName[len(checkName)-42:len(checkName)]
        return checkName
    return paths

def exppload(text):
    my_Paths=text.split(",")
    while "" in my_Paths:
        my_Paths.remove("")
    for index,path in enumerate(my_Paths):
        my_Paths[index] = path.replace("\n","")
    return my_Paths

def removeEnter(my_Paths):
    my_Paths = my_Paths.replace("\n","")
    return my_Paths

def calculate(backupPaths,savePath,exceptionPaths):
    start_time = time.time()

    for p in backupPaths:
        if p=='' or savePath=='':
            window['-run-'].update('Input is Empty !')
            window['Submit'].update(visible =True)
            return 
        if p==savePath:
            window['-run-'].update('Backup location and storage location cant be same !')
            window['Submit'].update(visible =True)
            return 
        checkRes=savePath.find(p)
        if checkRes==0:
            window['-run-'].update('Change the file storage location.\nBackup and storage cannot be in one place')
            window['Submit'].update(visible =True)
            return 

   
    try:
        exceptionPath= exceptionChange(exceptionPaths)
        flag2=0
        counter = 1
        mypath =savePath +"/"
        for backupPath in backupPaths:
            backupPath = backupPath.replace('\\','/')
            arrPath=backupPath.split("/")
            mainPathFolderName=arrPath[len(arrPath)-1]
            for root, dirs, files in os.walk(backupPath, topdown=False):
                if exceptionPath!=['']:
                    for checkException in exceptionPath:
                        findRes = re.search(checkException,root)
                        if findRes:
                            window['-run-'].update('we jump this file '+checkException)
                            flag2=1
                            break
                    if flag2==1:
                        flag2=0
                        continue
                for name in files:
                    path = os.path.join(root, name)
                    path=path.replace('\\','/')
                    test=path.split(backupPath)
                    mypaths=mypath+mainPathFolderName+test[len(test)-1]
                    myDir=os.path.dirname(mypaths)
                    res=os.path.exists(myDir)

                    if not res:
                        os.makedirs(myDir)
                        file=open(mypaths,'a')
                        counter=counter+1
                        file.close()
                    else:
                        res=os.path.exists(mypaths)
                        if not res:
                            file=open(mypaths,'a')
                            counter=counter+1
                            window['-run-'].update(mypaths)
                            file.close()
                        else:
                            window['-run-'].update('file exist !')
                    if flag==1:
                        break 
                if flag==1:
                    break
            if flag==1:
                break
    except OSError as err:
        window['-run-'].update("OS error: {0}".format(err))
    except ValueError:
        window['-run-'].update("Could not convert data to an integer.")
    except:
        window['-run-'].update("Unexpected error:", sys.exc_info()[0])
        raise
    
    end_time = time.time()
    totTime= end_time - start_time
    if(totTime>=1):
        totTime=int(totTime)
        totTime=str(totTime)
    else:
        totTime=str(totTime)
    window['-run-'].update('Finish !\ntime :'+totTime+" S\nFiles : "+str(counter))
    window['Submit'].update(visible =True)
    # balloon_tip("Backup","finished successfully")

def calculate_one_path(backupPath,savePath,exceptionPaths):
    start_time = time.time()

    if backupPath=='' or savePath=='':
        window['-run-'].update('Input is Empty !')
        window['Submit'].update(visible =True)
        return 
    if backupPath==savePath:
        window['-run-'].update('Backup location and storage location cant be same !')
        window['Submit'].update(visible =True)
        return 

    checkRes=savePath.find(backupPath)
    if checkRes==0:
        window['-run-'].update('Change the file storage location.\nBackup and storage cannot be in one place')
        window['Submit'].update(visible =True)
        return 
   
    try:
        exceptionPath= exceptionChange(exceptionPaths)
        counter = 1
        mypath =savePath +"/"
        flag3=0
        backupPath = backupPath.replace('\\','/')
        arrPath=backupPath.split("/")
        mainPathFolderName=arrPath[len(arrPath)-1]
        for root, dirs, files in os.walk(backupPath, topdown=False):
            if exceptionPath!=['']:
                for checkException in exceptionPath:
                    findRes = re.search(checkException,root)
                    if findRes:
                        window['-run-'].update('we jump this file '+checkException)
                        flag3=1
                        break
                if flag3==1:
                    flag3=0
                    continue
            
            for name in files:
                path = os.path.join(root, name)
                path=path.replace('\\','/')
                test=path.split(backupPath)
               
                mypaths=mypath+mainPathFolderName+test[len(test)-1]
                myDir=os.path.dirname(mypaths)
                res=os.path.exists(myDir)
                checkFileName(mypaths)
               
                if flag==1:
                    break 
                if not res:
                    os.makedirs(myDir)
                    file=open(mypaths,'a')
                    counter=counter+1
                    file.close()
                else:
                    res=os.path.exists(mypaths)
                    if not res:
                        file=open(mypaths,'a')
                        counter=counter+1
                        window['-run-'].update(mypaths)
                        file.close()
                    else:
                        window['-run-'].update('file exist !')
                if flag==1:
                    break 
            if flag==1:
                window['Submit'].update(visible =False)
                break

    except OSError as err:
        window['-run-'].update("OS error: {0}".format(err))
    except ValueError:
        window['-run-'].update("Could not convert data to an integer.")
    except:
        window['-run-'].update("Unexpected error:", sys.exc_info()[0])
        raise
    
    end_time = time.time()
    totTime= end_time - start_time
    if(totTime>=1):
        totTime=int(totTime)
        totTime=str(totTime)
    else:
        totTime=str(totTime)
    window['-run-'].update('Finish !\ntime :'+totTime+" S\nFiles : "+str(counter))
    window['Submit'].update(visible =True)
    # balloon_tip("Backup","finished successfully")

def exceptionChange(exceptions):
    for index,exp in enumerate(exceptions):
        exceptions[index]=exp.replace("\\","\\\\")
    for index,exp in enumerate(exceptions):
        exceptions[index]=exp.replace("/","\\\\")
    return exceptions


while True:
    event, values = window.read()


    if event == sg.WIN_CLOSED or event=="Exit" or event =="Cancel":
        flag=1                                                                                          
        window.close()
        break
    elif event == "Submit":
        window['Submit'].update(visible =False)
        myfile = open("lastBackup.txt","w")
        myExceptionFile = open("exception.txt","w")
        exceptionPath = exppload(values['Exception'])
        
        if values['radio']==True:
            myfile.write(removeEnter(values['multiple'])+"*"+removeEnter(values['-IN3-'])+"*"+"mul")
            myExceptionFile.write(removeEnter(values['Exception']))
            myExceptionFile.close()
            values['multiple'] = exppload(values['multiple'])
            mypos=threading.Thread(target=calculate,args=(values['multiple'],values['-IN3-'],exceptionPath,))
            mypos.start()
            myfile.close()
        elif values['radio']==False:
            myfile.write(removeEnter(values['-IN1-'])+"*"+removeEnter(values['-IN3-'])+"*"+"one")
            myExceptionFile.write(removeEnter(values['Exception']))
            myExceptionFile.close()
            mypos=threading.Thread(target=calculate_one_path,args=(values['-IN1-'],values['-IN3-'],exceptionPath,))
            mypos.start()
            myfile.close()
    if values['radio']==False:
        window['multiple'].update(visible =False)
        window['multipleText'].update('')
        window['backupfromText'].update('Backup from : ')

    if values['radio']==True:
        window['multiple'].update(visible =True)
        window['multipleText'].update('Multiple path     : ')
        window['backupfromText'].update('Find easy :     ')