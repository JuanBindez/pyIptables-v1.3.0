'''
    Classes usadas para armazenar comandos do iptables,
    e metodos que executam os comandos.
'''


'''
Copyright (c) 2022 Juan Carlos Bindez
"This project is licensed under the MIT License."
'''


import os
from colors import Color


class LogicasMenu1:
    '''
           Estes metodos executam comandos do os.system().
    '''
    def __init__(self, command):
        self.command = command


    # Start em comandos.
    def start_command(self):
        os.system(self.command)


    # Deleta regra de tabela especifica no iptables.
    def delete_id(self):
        id = int(input(Color.VERMELHO + " digite numero da regra a ser deletada \n>>" + Color.RESET))
        os.system(self.command.format(id))


    # Altera porta especifica no iptables.
    def port_change(self):
        port = str(input(Color.VERMELHO + "Digite a Porta Escolhida \n PORT >> " + Color.RESET))
        os.system(self.command.format(port))


    # Executa comandos de regras de ip.
    def ip_func_regra(self):
        ip = str(input(Color.VERMELHO + "Digite o ip Escolhido \n IP >> " + Color.RESET))
        os.system(self.command.format(ip))

class RegrasList:
    '''
        Aqui esta os comandos de iptables para regra de firewall,
        para desbloqueio de portas.
    '''
    ports_tab_input_accept = LogicasMenu1("sudo iptables -A INPUT -p tcp --dport {} -j ACCEPT")
    ports_tab_forward_accept = LogicasMenu1("sudo iptables -A FORWARD -p tcp --dport {} -j ACCEPT")
    ports_tab_output_accept = LogicasMenu1("sudo iptables -A OUTPUT -p tcp --dport {} -j ACCEPT")

    '''
       Aqui esta os comandos de iptables para regra de firewall,
       para bloqueio de portas.
    '''
    ports_tab_input_drop = LogicasMenu1("sudo iptables -A INPUT -p tcp --dport {} -j DROP")
    ports_tab_forward_drop = LogicasMenu1("sudo iptables -A FORWARD -p tcp --dport {} -j DROP")
    ports_tab_output_drop = LogicasMenu1("sudo iptables -A OUTPUT -p tcp --dport {} -j DROP")


class DeleteRegra:
    '''
        Aqui os comandos do iptables para deletar regras.
    
    '''
    delete_INPUT = LogicasMenu1("sudo iptables -D INPUT {}")
    delete_FORWARD = LogicasMenu1("sudo iptables -D FORWARD {}")
    delete_OUTPUT = LogicasMenu1("sudo iptables -D OUTPUT {}")


class SaveTable:
    '''
        Aqui os comandos iptables para ver o status do serviço iptables,
        restartar o serviço e iniciar o serviço.
    
    '''
    status_service = LogicasMenu1("sudo systemctl status netfilter-persistent.service")
    status_service = LogicasMenu1("sudo systemctl start netfilter-persistent.service")
    status_service = LogicasMenu1("sudo systemctl restart netfilter-persistent.service")
    

class IpRegras:
    '''
        Aqui as regras especificas para ip
    '''
    ip_ACCEPT_tab_INPUT = LogicasMenu1("sudo iptables -A INPUT -s {} -j ACCEPT")
    ip_DROP_tab_INPUT = LogicasMenu1("sudo iptables -A INPUT -s {} -j DROP")

    ip_ACCEPT_tab_FORWARD = LogicasMenu1("sudo iptables -A FORWARD -s {} -j ACCEPT")
    ip_DROP_tab_FORWARD = LogicasMenu1("sudo iptables -A FORWARD -s {} -j DROP")

    ip_ACCEPT_tab_OUTPUT = LogicasMenu1("sudo iptables -A OUTPUT -s {} -j ACCEPT")
    ip_DROP_tab_OUTPUT = LogicasMenu1("sudo iptables -A OUTPUT -s {} -j DROP")

