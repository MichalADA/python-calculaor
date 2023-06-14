# import operations
# powoduje to pewne problemy ze zmienymi 

# def handle_standard_calculator(window , event , values):
#     input_str_standard = ''
#     current_op = ''

#     if event is not None and event in '0123456789':
#         input_str_standard += event
#         window['-DISPLAY-STANDARD-'].update(input_str_standard)
#     elif event in '+-*/^':
#         input_str_standard += event
#         current_op = event
#         window['-DISPLAY-STANDARD-'].update(input_str_standard)
#     elif event == 'sqrt':
#         input_str_standard = str(operations.calculate(f'{current_op}{input_str_standard}'))
#         window['-DISPLAY-STANDARD-'].update(input_str_standard)
#     elif event == 'C':
#         input_str_standard = ''
#         current_op = ''
#         window['-DISPLAY-STANDARD-'].update(input_str_standard)
#     elif event == '=':
#         if input_str_standard:
#             input_str_standard = str(operations.calculate(input_str_standard))
#             window['-DISPLAY-STANDARD-'].update(input_str_standard)


# def handle_programmer_calculator(window, event, values):
#     if event is not None and (event in '0123456789' or (event in 'ABCDEF' and values['-DISPLAY-PROGRAMMER-'].startswith(('0x', '0X')))):
#         values['-DISPLAY-PROGRAMMER-'] += event
#         window['-DISPLAY-PROGRAMMER-'].update(values['-DISPLAY-PROGRAMMER-'])
#     elif event == 'Bin->Dec':
#         result = operations.to_dec(values['-DISPLAY-PROGRAMMER-'])
#         window['-DISPLAY-PROGRAMMER-'].update(result)
#     elif event == 'Dec->Bin':
#         result = operations.to_binary(values['-DISPLAY-PROGRAMMER-'])
#         window['-DISPLAY-PROGRAMMER-'].update(result)
#     elif event == 'Hex->Dec':
#         result = operations.to_dec(values['-DISPLAY-PROGRAMMER-'], base=16)
#         window['-DISPLAY-PROGRAMMER-'].update(result)
#     elif event == 'Dec->Hex':
#         result = operations.to_hex(values['-DISPLAY-PROGRAMMER-'])
#         window['-DISPLAY-PROGRAMMER-'].update(result)
#     elif event == 'Oct->Dec':
#         result = operations.to_dec(values['-DISPLAY-PROGRAMMER-'], base=8)
#         window['-DISPLAY-PROGRAMMER-'].update(result)
#     elif event == 'Dec->Oct':
#         result = operations.to_oct(values['-DISPLAY-PROGRAMMER-'])
#         window['-DISPLAY-PROGRAMMER-'].update(result)
#     elif event == 'C':
#         window['-DISPLAY-PROGRAMMER-'].update('')