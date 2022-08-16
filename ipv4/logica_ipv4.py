'''
Copyright (c) 2022 Juan Carlos Bindez
"This project is licensed under the MIT License."
'''


import os
from colors import Color


class LogicasMenu1:
    '''
           Executa Comandos.
    '''
    def __init__(self, command):
        self.command = command

    def start_command(self):
        os.system(self.command)

    def delete_id(self):
        id = int(input(Color.VERMELHO + " digite numero da regra a ser deletado \n>>" + Color.RESET))
        os.system(self.command.format(id))

    def port_change(self):
        port = str(input(Color.VERMELHO + "Digite a Porta Escolhida \n PORT >> " + Color.RESET))
        os.system(self.command.format(port))


class RegrasList:
    '''
            ACCEPTS
    '''
    ports_tab_input_accept = LogicasMenu1("sudo iptables -A INPUT -p tcp --dport {} -j ACCEPT")
    ports_tab_forward_accept = LogicasMenu1("sudo iptables -A FORWARD -p tcp --dport {} -j ACCEPT")
    ports_tab_output_accept = LogicasMenu1("sudo iptables -A OUTPUT -p tcp --dport {} -j ACCEPT")

    '''
            DROPS
    '''
    ports_tab_input_drop = LogicasMenu1("sudo iptables -A INPUT -p tcp --dport {} -j DROP")
    ports_tab_forward_drop = LogicasMenu1("sudo iptables -A FORWARD -p tcp --dport {} -j DROP")
    ports_tab_output_drop = LogicasMenu1("sudo iptables -A OUTPUT -p tcp --dport {} -j DROP")


class DeleteRegra:
    delete_INPUT = LogicasMenu1("sudo iptables -D INPUT {}")
    delete_FORWARD = LogicasMenu1("sudo iptables -D FORWARD {}")
    delete_OUTPUT = LogicasMenu1("sudo iptables -D OUTPUT {}")