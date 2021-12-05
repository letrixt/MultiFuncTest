import pyautogui
import keyboard
import PySimpleGUI as sg
from pynput.mouse import Listener as M
from pynput.keyboard import Listener as K

default_status, status =\
        "NO_STATUS",[
                "Recording...",
                "Stopped!",
                "Playing..."
                ];

layout = [
        [sg.Text(default_status,size=(40,1),key='-STATUS-')],
        [sg.Button('Record'),
                sg.Button('Play'), 
                sg.Button('Stop')],
        ];

window = sg.Window('Macro Maker', layout);


m={'Record':lambda:window['-STATUS-'].update(status[0]),'Stop':lambda:window['-STATUS-'].update(status[1]),'Play':lambda:window['-STATUS-'].update(status[2])};

while True:
    event, values = window.read()
    m[event]()
window.close()
