import json
import pyautogui
import keyboard

def intzuStringausgabe(i, minl):
    dl = minl-len(i)
    if dl == 1:
        return "0"+i
    elif dl == 2: 
        return "00"+i
    elif dl == 3:
        return "000"+i
    else: 
        s = ""
        for item in range(1, dl , 1):
            s = s + "0"
        return s+i


def deletefield(b, d):
    pyautogui.press('backspace', b)
    pyautogui.press('delete', d)

def writenextnumber():
    #delete previous number
    deletelen = int(data["length number"])
    deletefield(deletelen, deletelen)
    
    #write current number
    pyautogui.typewrite(intzuStringausgabe(data["number"], int(data["length number"])))

    #go to next logicstep
    intlogicstep = int(data["logicstep"])
    if intlogicstep == len(data["logic"].split(","))-1:
        data["logicstep"] = "0"
    else:
        data["logicstep"] = str(intlogicstep+1)

    #execute new logicstep
    data["number"] = str(int(data["number"]) + int(data["logic"].split(",")[intlogicstep]))
    
    #write to json file
    datadump = json.dumps(data)
    with open('Settingsv1.1.json', "w") as outfile:
        outfile.write(datadump)

b = True

with open('Settingsv1.1.json') as f:
    data = json.load(f)

while(b):
    if keyboard.is_pressed('F7'):
        b = False
    elif keyboard.is_pressed('+'):
        pyautogui.press("backspace")
        writenextnumber()