# encoding:utf-8

from cgitb import text
from cmath import e
import os
from re import M
try:
    import PySimpleGUI as sg
except:
    os.system('pip install PySimpleGUI')
    import PySimpleGUI as sg
from tkinter import Button, Scrollbar
from turtle import back
import webbrowser
import ctypes
import locale
import json
try:
    import clipboard
except:
    os.system('pip install clipboard')
    import clipboard
from pathlib import Path
icon = b'iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAYAAAD0eNT6AAAACXBIWXMAAAsTAAALEwEAmpwYAABMoUlEQVR4nO3deXxU1cE+8OfOPpM9ISEQtoSwCFgWkWUEt7rUFfel1b7ltYu2tdXW2rrU3Wrr1tba9qevtbVa9wX3XXQUCAoiAkJIQggJISH7ZDL73N8fkJRAZr8zZ+be5/v59PO+JDNnnizmPHPPvedKsiyDiIiItEUnOgARERGlHwsAERGRBrEAEBERaRALABERkQaxABAREWkQCwAREZEGsQAQERFpEAsAERGRBrEAEBERaRALABERkQaxABAREWkQCwAREZEGsQAQERFpEAsAERGRBrEAEBERaRALABERkQaxABAREWkQCwAREZEGsQAQERFpEAsAERGRBrEAEBERaRALABERkQaxABAREWkQCwAREZEGsQAQERFpEAsAERGRBrEAEBERaRALABERkQaxABAREWkQCwAREZEGsQAQERFpEAsAERGRBrEAEBERaRALABERkQaxABAREWkQCwAREZEGsQAQERFpEAsAERGRBrEAEBERaRALABERkQaxABAREWkQCwAREZEGsQAQERFpEAsAERGRBrEAEBERaRALABERkQaxABAREWkQCwAREZEGsQAQERFpEAsAERGRBrEAEBERaZBBdAClSJIkOkLWe/iWRbpup1xmNkqjZKAUwKhQCMUhWS4MhlAYCqEwGEKeLMMoOisRjUjW6TBg0KFPp0OvTkKXTid1S0CXJKFDBjoGPHL7DX+s6RMdVA1kWRYdISlStn8Bg1gAYvfn6xdNDQRxjMcnH+HyYIZzQJ7Y65JHdfTKVn8A/EYSqVy+TQoW50u9BTlozbFK9TYzNpqN0mpfQHb86p4ap+h82SLb508WAJX7152LZ3b1ycv39srfbO0KTezqk/PdXuhF5yKizCNJQFGu5BlVIHWWF0sbi/OllyaM1v3n9J+uconOlomyff5kAVCZP/5m0WFun/y9nn75xNZOefqeLtkqOhMRZS+zCfL4Ul17aaH0Wb5Nesnrl5+6/oEat+hcmSDb508WgCznWbVU9/g7/h/uaJWX72wLzerolW2iMxGRepkMCFWU6toqy6WVlWN0d134q9Vfic4kSrbPnywAWeqhGxed1tYtX1vXElrU0SubROchIu3R64DqCl3buFLp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6AhEYbV1yWM9q5YaLHZHQHQWJajuCECvi+v/RESkvM4+Wf/ppqBqrgZQXQHY0yVPFp2BiIjUqbY5pJqbA6mqABxxxBFS8165UHQOIiJSpz1d6jkPQFUF4PTFhiNdHllVXxMREWWO9m65WnQGpahqsvQHcKLoDEREpF5t3XKp6AxKUVUBADBTdAAiIlIvl0c2L7/gSIvoHEpQVQEIBuUq0RmIiEi9ZBnSvGq9KvagVlUB8PpRIToDERGpm04HVZwIqKoCMOBFsegMRESkbsEQDhedQQmqKQCeVUuNvS7ZJjoHERGpm9enjv1mVFMAaneFinv7ZdExiIhI5XoHMEp0BiWopgB8silYGeL8T0REKdbnkvNFZ1CCagoAbwFMRETp0OuSc0RnUIJq7gZ4xmJDx7KjVPPlJMxSH4CpORTTY0M2Cf1HGlOciIhIXWQZrf96XnSK5Klmxjxsok41RzOS4dsF+AdiKwCSUYeK8fy2ERHFSRVzp5r++ueJDkBERJqgivmGBYCIiCg+qphvWACIiIjikys6gBJYAIiIiOKj86xamvVXAqipAPB0diIiSpesn3PUVACIiIgoRiwAREREGsQCQEREpEEsAERERBrEAkBERKRBLABEREQaxAJARESkQSwAREREGsQCQEREpEEsAERERBrEAkBERKRBLABEREQaxAJARESkQSwAREREGsQCQEREpEEsAERERBrEAkBERKRBLABEREQaxAJARESkQSwAREREGsQCQEREpEEsAERERBrEAkBERKRBLABEREQaxAJARESkQSwAREREGsQCQEREpEEsAERERBrEAkBERKRBLABEREQaxAJARESkQSwAREREGsQCQEREpEEG0QGIMo07mItj1l4vOoamPTHrSUzN25zW11yw+ndpfT01uHLsF7h04nOiY1CCeASAiIhIg1gAiIiINIgFgIiISINYAIiIiDSIBYCIiEiDWACIiIg0iAWAiIhIg1gAiIiINIgFgIiISIO4EyDRQSx6F96ffw+6fcXo9heiy1eANm8hmj1FaHQXotaTj56gUXTMrGOQZEwxO1Fp6cVocz9KjP0oMfWh0OhEntEFm34AVr0bFv0ArHpX2vOtXHAXBgI5cAdz4ArY4ApY4Qra0OvPQZu3AK3efDR789DgzUNvUBt/OscaPZhq7cEESw/GWbpRZu5GgbEfuYZ+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'

"""
from datetime import datetime


clock = datetime.now()

clock = clock.strftime("%H")
"""

try:
    windll = ctypes.windll.kernel32
    windll.GetUserDefaultUILanguage()
    lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]
    print('Windows')
except:
    lang = locale.getdefaultlocale()
    lang = str(lang[0])
print(lang)

try:
    with open('settings.file', 'r') as f:
        config = f.readlines()
        f.close()

    if config[2] == 'dynamic':
        pass
    elif config[2] == 'static':
        lang = config[0]
    else:
        pass

    if config[1] == 'white\n':
        theme = 'white'
    elif config[1] == 'black\n':
        theme = 'black'
    else:
        theme = 'white'

except FileNotFoundError:
    with open('settings.file', 'w') as f:
        f.write(lang+'\n')
        f.write('white\n')
        f.write('dynamic')
        f.close()
    theme = 'white'
except:
    try:
        with open('settings.file', 'w') as f:
            f.write(lang+'\n')
            f.write('white\n')
            f.write('dynamic')
            f.close()
        theme = 'white'
    except:
        theme = 'white'

if theme == 'white':
    color2 = 'black'
elif theme == 'black':
    theme = '#1D1D1D'
    color2 = 'white'
else:
    color2 = 'black'
try:
    print('Config File:', config)
except:
    print('First Start')
try:
    if lang == 'en_US' or lang == 'en_US\n' or lang == 'en_GB' or lang == 'en_GB\n':
        f = open('en.json', encoding='utf-8')
    elif lang == 'tr_TR' or lang == 'tr_TR\n':
        f = open('tr.json', encoding='utf-8')
    else:
        f = open('en.json', encoding='utf-8')
    data = json.load(f)
    f.close()
except:
    sg.popup_error("Notepad can't find language files or corrupted while loading",background_color=theme,text_color=color2)
    exit()

sdata = ''

nofile = True

use_custom_titlebar = True if sg.running_trinket() else False

sg.SystemTray.notify('XNotepad', data["launchinfo"])
right_click_menu = ['None',[data["paste"],data["undo"]]]
menu_def = sg.MenubarCustom([[data["file"], [data["newfile"],data["openfile"], data["savefile"], '---', data["settings"],data["exit"]  ]],
            [data["edit"], [data["paste"], data["undo"]],],
            [data["help"], data["about"]],],background_color=theme, text_color=color2, bar_background_color=theme, bar_text_color=color2)
"""
utf-8 bug fix update

def setText(Text):
    decodedText = Text.read().decode("utf-8")
    window['textElement'].update(value=decodedText)
"""
layout = [[menu_def],[sg.Multiline(text_color=color2,background_color=theme,change_submits=True,expand_x=True,expand_y=True,key='notedata',k="textElement",)]]

window = sg.Window('XNotepad',layout,element_justification="l",size=(690, 400),no_titlebar=False,background_color=theme,enable_close_attempted_event=True,resizable=True,finalize=True, return_keyboard_events=True,right_click_menu=right_click_menu,icon=icon)
window.TKroot.minsize(250,120)

while True:
    event, values = window.Read()

    if values['notedata'] == '':
        nofile = True
    else:
        nofile = False

    if sdata == values['notedata']:
        saved = True
    else:
        saved = False
    
    if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == data["exit"]:
        
        if nofile == True or saved == True:
            window.close()
            break
        else:
            asklayout = [[sg.Text(data["exitwithoutsave"],background_color=theme,text_color=color2)],[sg.Button(data["yes"],button_color=('white','red'),size=(16,1)),sg.Button(data["no"],button_color=('white','green'),size=(16,1))]]
            askwindow = sg.Window(data["saveas"], asklayout, finalize=True,background_color=theme,icon=icon)
            while True:
                askevent, askvalues = askwindow.read()
                if askevent is None:
                    break
                elif askevent == data["yes"]:
                    exit()
                elif askevent == data["no"]:
                    askwindow.close()
                    break
    
    elif event == data["about"]:
        layoutabout = [[sg.Text(data["aboutapp"],background_color=theme,font=(20),text_color=color2)],[sg.Text(data["aboutwho"],background_color=theme, text_color=color2),sg.Text('@Eta06', click_submits=True, key='https://github.com/eta06/',background_color=theme,text_color="blue")],[sg.Text('GitHub Link', click_submits=True, key='https://github.com/eta06/xnotepad',background_color=theme,text_color="blue")]]
        windowabout = sg.Window(data["about"],layoutabout,background_color=theme,element_justification="c",keep_on_top=True,icon=icon) 
        while True:
            eventabout, valuesabout = windowabout.Read()
            if eventabout == sg.WINDOW_CLOSED or None:
                windowabout.Close()
                break
            if eventabout == 'https://github.com/eta06/':
                webbrowser.open('https://github.com/eta06/')
            elif eventabout == 'https://github.com/eta06/xnotepad':
                webbrowser.open('https://github.com/eta06/xnotepad')
            else:
                windowabout.Close()
                break
        window.TKroot.wm_attributes("-topmost", 1)
        window.TKroot.wm_attributes("-topmost", 0)
        
    elif event == data["newfile"]:
        if nofile == True or saved == True:
            window.FindElement('notedata').Update('')
        else:
            asklayout = [[sg.Text(data["asktosave"],background_color=theme,text_color=color2)],[sg.Button(data["yes"],button_color=('white','green'),size=(16,1)),sg.Button(data["no"],button_color=('white','red'),size=(16,1))]]
            askwindow = sg.Window(data["saveas"], asklayout, finalize=True,background_color=theme,icon=icon)
            while True:
                askevent, askvalues = askwindow.read()
                if askevent is None:
                    break
                elif askevent == data["yes"]:
                    savelayout = [[sg.InputText(visible=False, enable_events=True, key='fig_path'), sg.FileSaveAs(data["savelocal"],button_color=(color2,theme), key='fig_save', default_extension='.xpad')]]
                    savewindow = sg.Window(data["saveas"], savelayout, finalize=True,background_color=theme,icon=icon)  
                    fig_canvas_agg = None
                    while True:  # Event Loop
                        saveevent, savevalues = savewindow.Read()
                        if (saveevent == 'fig_path') and (savevalues['fig_path'] != ''):
                            print('Saving to:', savevalues['fig_path'])
                            with open(savevalues['fig_path'], 'w') as f:
                                f.write(values['notedata'])
                                f.close
                            saved = True
                            sdata = values['notedata']
                            savewindow.close()
                            break
                        if saveevent is None:
                            savewindow.close()
                            break
                    askwindow.close()
                    break
                elif askevent == data["no"]:
                    askwindow.close()
                    window.FindElement('notedata').Update('')
                    break
            if saved == True:
                window.FindElement('notedata').Update('')
    elif event == data["savefile"] or event == "s:83":
        if values["notedata"] == '' or saved == True:
            pass
        else:
            savelayout = [[sg.InputText(visible=False, enable_events=True, key='fig_path'), sg.FileSaveAs(data["savelocal"],button_color=(color2,theme), key='fig_save', default_extension='.xpad')]]
            savewindow = sg.Window(data["saveas"], savelayout, finalize=True,background_color=theme,icon=icon)
            
            fig_canvas_agg = None
            while True:  # Event Loop
                saveevent, savevalues = savewindow.Read()
                if (saveevent == 'fig_path') and (savevalues['fig_path'] != ''):
                    print('Saving to:', savevalues['fig_path'])
                    with open(savevalues['fig_path'], 'w') as f:
                        f.write(values['notedata'])
                        f.close
                    saved = True
                    sdata = values['notedata']
                    savewindow.close()
                    break
                if saveevent is None:
                    savewindow.close()
                    break
            window.TKroot.wm_attributes("-topmost", 1)
            window.TKroot.wm_attributes("-topmost", 0)
    elif event == data["paste"]:
        try:                        # Delete selection before paste
            window['notedata'].Widget.delete("sel.first", "sel.last")
        except:                     # Exception if no selection
            pass
        text = clipboard.paste()    # Text to paste
        window['notedata'].Widget.insert("insert", text)
    elif event == data["openfile"]:
        openlayout = [[
        sg.Input(key='-INPUT-',background_color=theme,text_color=color2,border_width=2,font=(16)),
        sg.FileBrowse(file_types=(("XPAD Files", "*.xpad"), ("ALL Files", "*.*")),button_color=(color2,theme),button_text=data["selectfile"]),
        sg.Button(data["openchosen"], button_color=(color2,theme)),
        ]]
        openwindow = sg.Window(data["openfile"], openlayout,background_color=theme,icon=icon)
        while True:
            openevent, openvalues = openwindow.read()
            if openevent == sg.WINDOW_CLOSED:
                openwindow.close()
                break
            elif openevent == data["openchosen"]:
                chosen = openvalues['-INPUT-']
                if chosen == '':
                    pass
                else:
                    try:
                        with open(chosen,mode='r',encoding="utf-8") as f:
                            filedata = f.read()
                            f.close()
                        if saved == True:
                            window.FindElement('notedata').Update(filedata)
                            openwindow.close()
                            break
                        else:
                            asklayout = [[sg.Text(data["asktosave"],background_color=theme,text_color=color2)],[sg.Button(data["yes"],button_color=('white','green'),size=(16,1)),sg.Button(data["no"],button_color=('white','red'),size=(16,1))]]
                            askwindow = sg.Window(data["saveas"], asklayout, finalize=True,background_color=theme,icon=icon)
                            while True:
                                askevent, askvalues = askwindow.read()
                                if askevent is None:
                                    break
                                elif askevent == data["yes"]:
                                    savelayout = [[sg.InputText(visible=False, enable_events=True, key='fig_path'), sg.FileSaveAs(data["savelocal"],button_color=(color2,theme), key='fig_save', default_extension='.xpad')]]
                                    savewindow = sg.Window(data["saveas"], savelayout, finalize=True,background_color=theme,icon=icon)  
                                    fig_canvas_agg = None
                                    while True:  # Event Loop
                                        saveevent, savevalues = savewindow.Read()
                                        if (saveevent == 'fig_path') and (savevalues['fig_path'] != ''):
                                            print('Saving to:', savevalues['fig_path'])
                                            with open(savevalues['fig_path'], 'w') as f:
                                                f.write(values['notedata'])
                                                f.close
                                            saved = True
                                            sdata = values['notedata']
                                            savewindow.close()
                                            break
                                        if saveevent is None:
                                            savewindow.close()
                                            break
                                    askwindow.close()
                                    break
                                elif askevent == data["no"]:
                                    askwindow.close()
                                    window.FindElement('notedata').Update(filedata)
                                    break
                            openwindow.close()
                            window.FindElement('notedata').Update(filedata)
                            break
                    except FileNotFoundError:
                        pass
                    except:
                        pass
                        