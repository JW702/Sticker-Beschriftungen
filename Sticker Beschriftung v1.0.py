import json
import pyautogui
import keyboard

def intzuStringausgabe(i, minl):
    s = ""
    dl = minl-len(i)
    if dl > 0:
        for item in range(0, dl, 1):
            s = s + "0"
    s = s + i
    return s

def deletefield():
    for item in range(0, 6, 1):
        pyautogui.press('backspace')
        pyautogui.press('delete')

b = True

with open('Settings.json') as f:
    data = json.load(f)

while(b):

    

    if keyboard.is_pressed('F7'):
        b = False
    elif keyboard.is_pressed('+'):
        deletefield()
        pyautogui.typewrite(intzuStringausgabe(data["number"], int(data["length number"])))

        print(data["number"])
        if int(data["iteration"]) == int(data["numberofiterrations"]):
            data["number"] = str(int(data["number"]) + 1)
            data["iteration"] = "1"
        else:
            data["iteration"] = str(int(data["iteration"])+1)
        
        datadump = json.dumps(data)

        with open('Settings.json', "w") as outfile:
            outfile.write(datadump)