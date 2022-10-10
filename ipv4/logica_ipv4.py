# A interface of the iptables written in Python.
#
# Copyright (c) 2022  Juan Carlos Bindez
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#  
# autor: https://github.com/juanBindez
# e-mail: juanbindez780@gmail.com


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
