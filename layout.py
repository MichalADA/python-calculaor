import PySimpleGUI as sg
import operations


def get_layout_standard(): 
       return  [
    [[sg.Combo(['Standardowy', 'Programista'], enable_events=True, key='-CALCULATOR-', default_value='Standardowy')]], 
    [sg.Input(size=(18, 2), key='-DISPLAY-STANDARD-', justification='right', font=("Helvetica", 20), readonly=True)],
    [sg.Button('7', size=(4, 2), font=("Helvetica", 20)), sg.Button('8', size=(4, 2), font=("Helvetica", 20)), 
     sg.Button('9', size=(4, 2), font=("Helvetica", 20)), sg.Button('/', size=(4, 2), font=("Helvetica", 20), button_color=('black', 'orange'))],
    [sg.Button('4', size=(4, 2), font=("Helvetica", 20)), sg.Button('5', size=(4, 2), font=("Helvetica", 20)), 
     sg.Button('6', size=(4, 2), font=("Helvetica", 20)), sg.Button('*', size=(4, 2), font=("Helvetica", 20),
                                                                     button_color=('black', 'orange'))],
    [sg.Button('1', size=(4, 2), font=("Helvetica", 20)), sg.Button('2', size=(4, 2), font=("Helvetica", 20)),
      sg.Button('3', size=(4, 2), font=("Helvetica", 20)), sg.Button('-', size=(4, 2), font=("Helvetica", 20), 
                                                                     button_color=('black', 'orange'))],
    [sg.Button('0', size=(4, 2), font=("Helvetica", 20)), sg.Button('^', size=(4, 2), font=("Helvetica", 20)), 
     sg.Button('sqrt', size=(4, 2), font=("Helvetica", 20)), sg.Button('+', size=(4, 2), font=("Helvetica", 20), 
                                                                       button_color=('black', 'orange'))],
    [sg.Button('C', size=(10, 2), font=("Helvetica", 20), button_color=('black', 'red')), sg.Button('=', size=(10, 2), font=("Helvetica", 20), 
                                                                                                    button_color=('black', 'green'))]
]

def get_layout_programmer():
    return [
        [sg.Combo(['Standardowy', 'Programista' , 'Data'] , enable_events=True, key='-CALCULATOR-', default_value='Standardowy')],
        [sg.Input(size=(18, 2), key='-DISPLAY-PROGRAMMER-', justification='right', font=("Helvetica", 20), readonly=True)],
        [sg.Button(str(i), size=(4, 2), font=("Helvetica", 20)) for i in range(0, 10)],
        [sg.Button(chr(ord('A')+i), size=(4, 2), font=("Helvetica", 20)) for i in range(6)],
        [sg.Button('Bin->Dec', size=(8, 2), font=("Helvetica", 20)), sg.Button('Dec->Bin', size=(8, 2), font=("Helvetica", 20))],
        [sg.Button('Oct->Dec', size=(8, 2), font=("Helvetica", 20)), sg.Button('Dec->Oct', size=(8, 2), font=("Helvetica", 20))],
        [sg.Button('Hex->Dec', size=(8, 2), font=("Helvetica", 20)), sg.Button('Dec->Hex', size=(8, 2), font=("Helvetica", 20))],
        [sg.Button('C', size=(16, 2), font=("Helvetica", 20), button_color=('black', 'red'))]
    ]


# def get_layout_date():
#       return [
            
#       ]