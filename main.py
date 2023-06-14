import PySimpleGUI as sg
import operations
from layout import get_layout_standard, get_layout_programmer
# from event_handlers import handle_standard_calculator , handle_programmer_calculator
# Tworzenie okien
layout_standard = get_layout_standard()
layout_programmer = get_layout_programmer()


window_standard = sg.Window('Kalkulator', layout_standard, finalize=True)
window_programmer = sg.Window('Kalkulator', layout_programmer, location=window_standard.current_location(), finalize=True)

window_programmer.hide()

current_window = window_standard
input_str_standard = ''
current_op = ''

while True:
    window, event, values = sg.read_all_windows()
    if window == sg.WINDOW_CLOSED:
        break

    if event == '-CALCULATOR-':
        if values['-CALCULATOR-'] == 'Standardowy':
            current_window.hide()
            current_window = window_standard
            current_window.un_hide()
        elif values['-CALCULATOR-'] == 'Programista':
            current_window.hide()
            current_window = window_programmer
            current_window.un_hide()

    # Obsługa zdarzeń dla kalkulatora standardowego:
    if current_window == window_standard:
        if event is not None and event in '0123456789':
                input_str_standard += event
                window['-DISPLAY-STANDARD-'].update(input_str_standard)
        elif event in '+-*/^':
                input_str_standard += event
                current_op = event
                window['-DISPLAY-STANDARD-'].update(input_str_standard)
        elif event == 'sqrt':  # Zmiana warunku dla operatora pierwiastka
                input_str_standard = str(operations.calculate(f'{current_op}{input_str_standard}'))
                window['-DISPLAY-STANDARD-'].update(input_str_standard)
        elif event == 'C':
                input_str_standard = ''
                current_op = ''
                window['-DISPLAY-STANDARD-'].update(input_str_standard)
        elif event == '=':
                if input_str_standard:
                    input_str_standard = str(operations.calculate(input_str_standard))
                    window['-DISPLAY-STANDARD-'].update(input_str_standard)


    # Obsługa zdarzeń dla kalkulatora programisty:
    elif current_window == window_programmer:
        if event is not None and (event in '0123456789' or (event in 'ABCDEF' and values['-DISPLAY-PROGRAMMER-'].startswith(('0x', '0X')))):
            values['-DISPLAY-PROGRAMMER-'] += event
            window['-DISPLAY-PROGRAMMER-'].update(values['-DISPLAY-PROGRAMMER-'])
        
        
        if event == 'Bin->Dec':
            result = operations.to_dec(values['-DISPLAY-PROGRAMMER-'])
            window['-DISPLAY-PROGRAMMER-'].update(result)
        elif event == 'Dec->Bin':
            result = operations.to_binary(values['-DISPLAY-PROGRAMMER-'])
            window['-DISPLAY-PROGRAMMER-'].update(result)
        elif event == 'Hex->Dec':
            result = operations.to_dec(values['-DISPLAY-PROGRAMMER-'], base=16)
            window['-DISPLAY-PROGRAMMER-'].update(result)
        elif event == 'Dec->Hex':
            result = operations.to_hex(values['-DISPLAY-PROGRAMMER-'])
            window['-DISPLAY-PROGRAMMER-'].update(result)
        elif event == 'Oct->Dec':
            result = operations.to_dec(values['-DISPLAY-PROGRAMMER-'], base=8)
            window['-DISPLAY-PROGRAMMER-'].update(result)
        elif event == 'Dec->Oct':
            result = operations.to_oct(values['-DISPLAY-PROGRAMMER-'])
            window['-DISPLAY-PROGRAMMER-'].update(result)
        elif event == 'C':
            window['-DISPLAY-PROGRAMMER-'].update('')




window_standard.close()
window_programmer.close()
