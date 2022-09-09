'''
MIT License

Copyright (c) 2022 Juan Carlos Bindez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Author: https://github.com/JuanBindez
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
        id = int(input(Color.VERMELHO + " digite numero da regra a ser deletada \n>>"))
        os.system(self.command.format(id))


    # Altera porta especifica no iptables.
    def port_change(self):
        port = str(input(Color.VERMELHO + "Digite a Porta Escolhida \n PORT >> "))
        os.system(self.command.format(port))


    # Executa comandos de regras de ip.
    def ip_func_regra(self):
        ip = str(input(Color.VERMELHO + "Digite o ip Escolhido \n IP >> "))
        os.system(self.command.format(ip))

    # Executa comandos de regras de Mac.
    def mac_func_regra(self):
        mac = str(input(Color.VERMELHO + "Digite o MacAddress Escolhido \n Mac >> "))
        os.system(self.command.format(mac))


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


class MacRegras:
    '''
        Aqui as regras especificas para Mac
    '''
    mac_ACCEPT_tab_INPUT = LogicasMenu1("sudo iptables -A INPUT -m mac --mac-source {} -j ACCEPT")
    mac_DROP_tab_INPUT = LogicasMenu1("sudo iptables -A INPUT -m mac --mac-source {} -j DROP")

    mac_ACCEPT_tab_FORWARD = LogicasMenu1("sudo iptables -A FORWARD -m mac --mac-source {} -j ACCEPT")
    mac_DROP_tab_FORWARD = LogicasMenu1("sudo iptables -A FORWARD -m mac --mac-source {} -j DROP")

    mac_ACCEPT_tab_OUTPUT = LogicasMenu1("sudo iptables -A OUTPUT -m mac --mac-source {} -j ACCEPT")
    mac_DROP_tab_OUTPUT = LogicasMenu1("sudo iptables -A OUTPUT -m mac --mac-source {} -j DROP")