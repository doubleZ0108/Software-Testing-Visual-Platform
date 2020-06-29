# -*- coding: utf-8 -*-
from app.common.commonUtil import df_update, df_read
from app.csv.index import printer as printer_index

'''
@program: question6.py

@description: 

@author: doubleZ

@modify: dasein

@create: 2020/06/29 
'''
from state_machine import State, Event, acts_as_state_machine, after, before, InvalidStateTransition

state_dir = {
    'Empty': 1,
    'Printing': 2,
    'Alarming': 3,
    'End': 'End',
    'Failure': 'Failure'
}


@acts_as_state_machine
class Printer:
    initial = State(initial=True)
    empty = State()
    printing = State()
    alarming = State()
    end = State()
    failure = State()

    # initial event
    initialize = Event(from_states=initial, to_state=empty)

    # delete event
    empty_delete = Event(from_states=empty, to_state=end)
    other_delete = Event(from_states=(printing, alarming), to_state=failure)

    # ask for print event
    general_ask_for_print = Event(from_states=(empty, printing), to_state=printing)
    alarm_ask_for_print = Event(from_states=alarming, to_state=failure)

    # print end event
    general_print_end = Event(from_states=(empty, alarming), to_state=failure)
    printing_print_end = Event(from_states=printing, to_state=empty)

    # check printer event
    empty_check_printer = Event(from_states=empty, to_state=failure)
    general_check_printer = Event(from_states=(printing, alarming), to_state=alarming)

    # check printer end event
    alarm_check_printer_end = Event(from_states=alarming, to_state=printing)
    general_check_printer_end = Event(from_states=(empty, printing), to_state=failure)


def transition(printer, event):
    try:
        event()
    except InvalidStateTransition as err:
        print("Failure")


def printer_atom(arg_list):
    command = arg_list[0]

    printer = Printer()

    for cmd in command:
        if cmd == 'S':
            transition(printer, printer.initialize)
        elif cmd == '1':
            if printer.current_state == printer.alarming:
                transition(printer, printer.alarm_ask_for_print)
            else:
                transition(printer, printer.general_ask_for_print)
        elif cmd == '2':
            if printer.current_state == printer.printing:
                transition(printer, printer.printing_print_end)
            else:
                transition(printer, printer.general_print_end)
        elif cmd == '3':
            if printer.current_state == printer.empty:
                transition(printer, printer.empty_check_printer)
            else:
                transition(printer, printer.general_check_printer)
        elif cmd == '4':
            if printer.current_state == printer.alarming:
                transition(printer, printer.alarm_check_printer_end)
            else:
                transition(printer, printer.general_check_printer_end)
        elif cmd == 'E':
            if printer.current_state == printer.empty:
                transition(printer, printer.empty_delete)
            else:
                transition(printer, printer.other_delete)
    final_state = printer.current_state
    return final_state


class question6:
    def __init__(self):
        pass

    @staticmethod
    def printer(method_type):
        csv_path = printer_index[method_type]
        df, arg_start, arg_end = df_read(csv_path=csv_path)
        output1 = []
        for i in range(0, len(df)):
            arg_list = df.iloc[i, arg_start:arg_end].values.tolist()
            output1.append(state_dir[printer_atom(arg_list).capitalize()])
        return df_update(df=df, csv_path=csv_path, actual_outputs=[output1], tester_name='anonymous')

    @staticmethod
    def printer_method_test(request):
        arg_list = request['command']
        state = printer_atom(arg_list)
        return {'state': state}

question6.printer('printer')