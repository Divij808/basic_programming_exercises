import PySimpleGUI as Sg
import math

times = '\u00D7'
divided = '\u00F7'
percentage = '%'

layout = [[Sg.InputText(key='input_box', disabled=True, size=(40, 1), default_text='0')],
          [Sg.Button('7', key='seven', size=(5, 2)),
           Sg.Button('8', key='eight', size=(5, 2)),
           Sg.Button('9', key='nine', size=(5, 2)),
           Sg.Button(divided, key='div', size=(5, 2)),
           Sg.Button('off', key='off', size=(5, 2))],
          [Sg.Button('4', key='four', size=(5, 2)),
           Sg.Button('5', key='five', size=(5, 2)),
           Sg.Button('6', key='six', size=(5, 2)),
           Sg.Button('+', key='add', size=(5, 2)),
           Sg.Button('^', key='power', size=(5, 2))],
          [Sg.Button('1', key='one', size=(5, 2)),
           Sg.Button('2', key='two', size=(5, 2)),
           Sg.Button('3', key='three', size=(5, 2)),
           Sg.Button(percentage, key='percentage', size=(5, 2)),
           Sg.Button('\u00D7', key='times', size=(5, 2))],
          [Sg.Button('0', key='zero', size=(5, 2)),
           Sg.Button('c', key='restart', size=(5, 2)),
           Sg.Button('_', key='minus', size=(5, 2)),
           Sg.Button('.', key='dot', size=(5, 2)),
           Sg.Button('=', key='equal', size=(5, 2))]]

window = Sg.Window("calculator", layout)
first_numb = ''
second_numb = ''
operator_pressed = False
operator = ''
while True:
    event, values = window.read()
    if event in (None, 'off'):
        window.close()
        break
    elif event in 'restart':
        window.Element('input_box').update('0')
        second_numb = ''
        first_numb = ''
        operator = ''
        operator_pressed = False
    elif event in 'zero':
        if not operator_pressed:
            first_numb = first_numb + '0'
            window.Element('input_box').update(first_numb)
        else:
            second_numb = second_numb + '0'
            window.Element('input_box').update(second_numb)

    elif event in 'one':
        if not operator_pressed:
            first_numb = first_numb + '1'
            window.Element('input_box').update(first_numb)
        else:
            second_numb = second_numb + '1'
            window.Element('input_box').update(second_numb)
    elif event in 'two':
        if not operator_pressed:
            first_numb = first_numb + '2'
            window.Element('input_box').update(first_numb)
        else:
            second_numb = second_numb + '2'
            window.Element('input_box').update(second_numb)

    elif event in 'three':
        if not operator_pressed:
            first_numb = first_numb + '3'
            window.Element('input_box').update(first_numb)
        else:
            second_numb = second_numb + '3'
            window.Element('input_box').update(second_numb)
    elif event in 'four':
        if not operator_pressed:
            first_numb = first_numb + '4'
            window.Element('input_box').update(first_numb)
        else:
            second_numb = second_numb + '4'
            window.Element('input_box').update(second_numb)
    elif event in 'five':
        if not operator_pressed:
            first_numb = first_numb + '5'
            window.Element('input_box').update(first_numb)
        else:
            second_numb = second_numb + '5'
            window.Element('input_box').update(second_numb)
    elif event in 'six':
        if not operator_pressed:
            first_numb = first_numb + '6'
            window.Element('input_box').update(first_numb)
        else:
            second_numb = second_numb + '6'
            window.Element('input_box').update(second_numb)
    elif event in 'seven':
        if not operator_pressed:
            first_numb = first_numb + '7'
            window.Element('input_box').update(first_numb)
        else:
            second_numb = second_numb + '7'
            window.Element('input_box').update(second_numb)
    elif event in 'eight':
        if not operator_pressed:
            first_numb = first_numb + '8'
            window.Element('input_box').update(first_numb)
        else:
            second_numb = second_numb + '8'
            window.Element('input_box').update(second_numb)
    elif event in 'nine':
        if not operator_pressed:
            first_numb = first_numb + '9'
            window.Element('input_box').update(first_numb)
        else:
            second_numb = second_numb + '9'
            window.Element('input_box').update(second_numb)
    elif event in 'dot':
        if not "." in first_numb:
            if not operator_pressed:
                first_numb = first_numb + '.'
                window.Element('input_box').update(first_numb)
        if not "." in second_numb:
            if not operator_pressed:
                second_numb = second_numb + '.'
                window.Element('input_box').update(second_numb)

    elif event in 'equal':
        if operator == 'add':
            window.Element('input_box').update(int(first_numb) + int(second_numb))
        elif operator == 'times':
            window.Element('input_box').update(int(first_numb) * int(second_numb))
        elif operator == 'divided':
            window.Element('input_box').update(int(first_numb) / int(second_numb))
        elif operator == 'minus':
            window.Element('input_box').update(int(first_numb) - int(second_numb))
        elif operator == 'percentage':
            window.Element('input_box').update(int(first_numb) / int(second_numb) * 100)
        elif operator == 'power':
            window.Element('input_box').update(math.pow(int(first_numb), int(second_numb)))
    elif event in 'add':
        operator_pressed = True
        operator = 'add'
        window.Element('input_box').update(second_numb)
    elif event in 'percentage':
        operator_pressed = True
        operator = 'percentage'
        window.Element('input_box').update(second_numb)
    elif event in 'times':
        operator_pressed = True
        operator = 'times'
        window.Element('input_box').update(second_numb)
    elif event in 'minus':
        operator_pressed = True
        operator = 'minus'
        window.Element('input_box').update(second_numb)
    elif event in 'divided':
        operator_pressed = True
        operator = 'divided'
        window.Element('input_box').update(second_numb)
    elif event in 'power':
        operator_pressed = True
        operator = 'power'
        window.Element('input_box').update(second_numb)
