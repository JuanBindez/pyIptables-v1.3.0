# A interface of the iptables.
#
# pyIptables-v1.3.0/pyiptables.py
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
# autor: <https://github.com/juanBindez>   <juanbindez780@gmail.com>


try:
    import os
    import time

    from banner import header_banner
    from colors import Color
    from ipv4.logica_ipv4 import DeleteRegra, LogicasMenu1, RegrasList, IpRegras, MacRegras


    ver_regras = LogicasMenu1("sudo iptables -L --line-numbers")# variaveis para ver regras numeradas
    delete = LogicasMenu1("sudo iptables -D INPUT")# regra para deletar tabela


    # INCIO DO BLOCO DE MENU IPV4

    # escolha 0
    def sobre_software():
        '''exibe informações sobre o programa.'''

        os.system("clear")
        header_banner()
        print(Color.AMARELO +
            '''
                                         [0] Voltar        
        O pyIptables é um software escrito em Python3, que visa ser uma interface de usuario
            para o firewall iptables (https://g.co/kgs/9ZJDYt), este programa pode te ajudar
        a entender as regras de firewall e facilitar as configurações, ele manipula os comandos
                do iptables, para mais informações sobre o iptables acesse seu manual 
                                (https://linux.die.net/man/8/iptables)
                                Autor: https://github.com/JuanBindez
            
            '''
        + Color.RESET)

        escolha = str(input(Color.AMARELO + "Escolha Uma Opção >>"))

        if escolha == "0":
            os.system("clear")
            menu_main_ipv4()

        else:
            os.system("clear")
            print(Color.VERMELHO + "               ops, digite apenas os numeros listados!" + Color.RESET)
            time.sleep(5)
            sobre_software()

    
    # escolha 1 
    def Ver_regras_firewall():
        '''ve regras existentes no firewall'''
        
        os.system("clear")
        ver_regras.start_command()
        menu_main_ipv4()

    # escolha 2 
    def deletar_regras_firewall():
        '''deleta id de regra no firewall'''
    
        os.system("clear")
        ver_regras.start_command()
        header_banner()
        
        
        print(Color.AMARELO +

                '''                       
                                         Deletar de qual tabela?
                                [0] Voltar
                                [1] INPUT     
                                [2] FORWARD
                                [3] OUTPUT
                                                 
                '''
        + Color.RESET)

        choice_delete = str(input(Color.AMARELO + "Escolha Uma Opção>>"))

        if choice_delete == "0":
            os.system("clear")
            menu_main_ipv4()

        elif choice_delete == "1":
            DeleteRegra.delete_INPUT.delete_id()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        elif choice_delete == "2":
            DeleteRegra.delete_FORWARD.delete_id()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        elif choice_delete == "3":
            DeleteRegra.delete_OUTPUT.delete_id()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()
                
        else:
            os.system("clear")
            print("ops, digite apenas os numeros listados!")
            menu_main_ipv4()

        os.system("clear")
        ver_regras.start_command()
        delete.delete_id()
        menu_main_ipv4()
        # fim do menu de escolha 2

    # escolha 3 
    def regras_de_ports_firewall():
        '''regras de portas'''

        # função menu de escolha 3 
        def regra_port_INPUT():
            header_regra_port()
            choice_regra = str(input(Color.AMARELO + "Escolha Uma Opção >>"))

            if choice_regra == "0":
                os.system("clear")
                menu_main_ipv4()

            elif choice_regra == "1":
                RegrasList.ports_tab_input_accept.port_change()
                os.system("clear")
                ver_regras.start_command()
                menu_main_ipv4()

            elif choice_regra == "2":
                RegrasList.ports_tab_input_drop.port_change()
                os.system("clear")
                ver_regras.start_command()
                menu_main_ipv4()
                    
            else:
                os.system("clear")
                print("ops, digite apenas os numeros listados!")
                menu_main_ipv4()

        # função menu de escolha 3
        def header_regra_port():
            os.system("clear")
            header_banner()
            print(Color.AMARELO +
                '''
                                [0] Voltar
                                [1] ACCEPT
                                [2] DROP
                
                '''
            + Color.RESET)
            # header

        # função menu de escolha 3
        def regra_port_FORWARD():
            header_regra_port()
            choice_regra = str(input(Color.AMARELO + "Escolha Uma Opção >>"))

            if choice_regra == "1":
                RegrasList.ports_tab_forward_accept.port_change()
                os.system("clear")
                ver_regras.start_command()
                menu_main_ipv4()

            elif choice_regra == "2":
                RegrasList.ports_tab_forward_drop.port_change()
                os.system("clear")
                ver_regras.start_command()
                menu_main_ipv4()
                    
            else:
                os.system("clear")
                print("ops, digite apenas os numeros listados!")
                menu_main_ipv4()

        # função menu de escolha 3 ####
        def regra_port_OUTPUT():
            header_regra_port()
            choice_regra = str(input(">>"))

            if choice_regra == "1":
                RegrasList.ports_tab_output_accept.port_change()
                os.system("clear")
                ver_regras.start_command()
                menu_main_ipv4()

            elif choice_regra == "2":
                RegrasList.ports_tab_output_drop.port_change()
                os.system("clear")
                ver_regras.start_command()
                menu_main_ipv4()
                    
            else:
                os.system("clear")
                print("ops, digite apenas os numeros listados!")
                menu_main_ipv4()



        os.system("clear")
        ver_regras.start_command()
        header_banner()
        print(Color.AMARELO +
                '''           
                                         Escolha a Tabela
                                [0] Voltar
                                [1] INPUT
                                [2] FORWARD
                                [3] OUTPUT
                '''
        + Color.RESET)

        choice_tab = str(input(Color.AMARELO + "Escolha Uma Opção >>"))

        if choice_tab == "0":
            os.system("clear")
            menu_main_ipv4()

        elif choice_tab == "1":
            regra_port_INPUT()

        elif choice_tab == "2":
            regra_port_FORWARD()

        elif choice_tab == "3":
            regra_port_OUTPUT()
        # fim do menu de escolha 3
    ######################################################################


    # escolha 4
    def salva_regras_firewall():
        '''salva as regras do firewall.'''

        os.system("sudo service netfilter-persistent save")
        time.sleep(2)
        os.system("sudo systemctl restart netfilter-persistent.service")
        time.sleep(2)
        os.system("sudo systemctl status netfilter-persistent.service")
        os.system("clear")
        menu_main_ipv4()

    # escolha 5 
    def netfilter_install():
        '''faz a instalação do netfilter'''

        os.system("sudo apt-get install netfilter-persistent.service")
        os.system("sudo apt-get install iptables-persistent")
        time.sleep(2)
        os.system("clear")
        menu_main_ipv4()

    # escolha 6 
    def exclui_tab_firewall():
        '''exclui tabelas de regras do firewall.'''

        os.system("clear")
        ver_regras.start_command()
        header_banner()

        print(Color.AMARELO +

                '''    
                                        Escolha a Tabela a ser Excluída
                                [0] Voltar
                                [1] INPUT
                                [2] FORWARD
                                [3] OUTPUT
                                [4] Excluir Todas as Regras de Todas as tabelas
                
                '''
        + Color.RESET)

        escolha = str(input(Color.AMARELO + "Escolha Uma Opção >>"))

        if escolha == "0":
            os.system("clear")
            menu_main_ipv4()

        elif escolha == "1":
            os.system("sudo iptables -F INPUT")
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        elif escolha == "2":
            os.system("sudo iptables -F FORWARD")
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        elif escolha == "3":
            os.system("sudo iptables -F OUTPUT")
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        elif escolha == "4":
            os.system("sudo iptables -F")
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        else:
            os.system("clear")
            print("ops, digite apenas os numeros listados!")
            menu_main_ipv4()
        # fim do menu de escolha 6


    # escolha 7 
    def ip_regras():

        def header_escolha7():
            os.system("clear")
            header_banner()

            print(Color.AMARELO +
                    '''
                                    [0] Voltar
                                    [1] ACCEPT
                                    [2] DROP
                    
                    '''
            + Color.RESET)

        # fução escolha 7
        def ip_regra_INPUT_ACCEPT():
            IpRegras.ip_ACCEPT_tab_INPUT.ip_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        # fução escolha 7
        def ip_regra_FORWARD_ACCEPT():
            IpRegras.ip_ACCEPT_tab_FORWARD.ip_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()


        # fução escolha 7
        def ip_regra_OUTPUT_ACCEPT():
            IpRegras.ip_ACCEPT_tab_OUTPUT.ip_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()


        # fução escolha 7
        def ip_regra_INPUT_DROP():
            IpRegras.ip_DROP_tab_INPUT.ip_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        #fução escolha 7
        def ip_regra_FORWARD_DROP():
            IpRegras.ip_DROP_tab_FORWARD.ip_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        # fução escolha 7
        def ip_regra_OUTPUT_DROP():
            IpRegras.ip_DROP_tab_OUTPUT.ip_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()


        os.system("clear")
        header_banner()
        print(Color.AMARELO +
                '''    
                                        Escolha a Tabela
                                 [0] Voltar   
                                 [1] INPUT
                                 [2] FORWARD   
                                 [3] OUTPUT
                '''
        + Color.RESET)

        escolha7 = str(input(Color.AMARELO + "Escolha Uma Opção >>"))

        if escolha7 == "0":
            os.system("clear")
            menu_main_ipv4()

        elif escolha7 == "1":
            header_escolha7()
            escolha = str(input(Color.AMARELO + "Escolha Uma Opção >>"))

            if escolha == "0":
                os.system("clear")
                menu_main_ipv4()

            elif escolha == "1":
                ip_regra_INPUT_ACCEPT()

            elif escolha == "2":
                ip_regra_INPUT_DROP()


        elif escolha7 == "2":
            header_escolha7()
            escolha = str(input(Color.AMARELO + "Escolha Uma Opção >>"))

            if escolha == "0":
                os.system("clear")
                menu_main_ipv4()

            elif escolha == "1":
                ip_regra_FORWARD_ACCEPT()

            elif escolha == "2":
                ip_regra_FORWARD_DROP()

        elif escolha7 == "3":
            header_escolha7()
            escolha = str(input(Color.AMARELO + "Escolha Uma Opção >>"))

            if escolha == "0":
                os.system("clear")
                menu_main_ipv4()

            elif escolha == "1":
                ip_regra_OUTPUT_ACCEPT()

            elif escolha == "2":
                ip_regra_OUTPUT_DROP()

        else:
            os.system("clear")
            print("Ops, Digite apenas os numeros listados!")
            ip_regras()
    # fim do menu de escolha 7


    # escolha 8
    def mac_regras():
        '''regras para macaddress'''

        def header_escolha8():
            os.system("clear")
            header_banner()

            print(Color.AMARELO +
                    '''
                                    [0] Voltar
                                    [1] ACCEPT
                                    [2] DROP
                    
                    '''
            + Color.RESET)

        # função escolha 8
        def mac_regra_INPUT_ACCEPT():
            MacRegras.mac_ACCEPT_tab_INPUT.mac_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        # função escolha 8
        def mac_regra_FORWARD_ACCEPT():
            MacRegras.mac_ACCEPT_tab_FORWARD.mac_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()


        # fuçnão escolha 8
        def mac_regra_OUTPUT_ACCEPT():
            MacRegras.mac_ACCEPT_tab_OUTPUT.mac_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()


        # função escolha 8
        def mac_regra_INPUT_DROP():
            MacRegras.mac_DROP_tab_INPUT.mac_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        # função escolha 8
        def mac_regra_FORWARD_DROP():
            MacRegras.mac_DROP_tab_FORWARD.mac_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        # função escolha 8
        def mac_regra_OUTPUT_DROP():
            MacRegras.mac_DROP_tab_OUTPUT.mac_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()


        os.system("clear")
        header_banner()
        print(Color.AMARELO +
                '''    
                                        Escolha a Tabela
                                 [0] Voltar   
                                 [1] INPUT
                                 [2] FORWARD   
                                 [3] OUTPUT
                '''
        + Color.RESET)

        escolha8 = str(input(Color.AMARELO + "Escolha Uma Opção >>"))

        if escolha8 == "0":
            os.system("clear")
            menu_main_ipv4()

        elif escolha8 == "1":
            header_escolha8()
            escolha = str(input(Color.AMARELO + "Escolha Uma Opção >>"))

            if escolha == "0":
                os.system("clear")
                menu_main_ipv4()

            elif escolha == "1":
                mac_regra_INPUT_ACCEPT()

            elif escolha == "2":
                mac_regra_INPUT_DROP()


        elif escolha8 == "2":
            header_escolha8()
            escolha = str(input(Color.AMARELO + "Escolha Uma Opção >>"))

            if escolha == "0":
                os.system("clear")
                menu_main_ipv4()

            elif escolha == "1":
                mac_regra_FORWARD_ACCEPT()

            elif escolha == "2":
                mac_regra_FORWARD_DROP()

        elif escolha8 == "3":
            header_escolha8()
            escolha = str(input(Color.AMARELO + "Escolha Uma Opção >>"))

            if escolha == "0":
                os.system("clear")
                menu_main_ipv4()

            elif escolha == "1":
                mac_regra_OUTPUT_ACCEPT()

            elif escolha == "2":
                mac_regra_OUTPUT_DROP()

        else:
            os.system("clear")
            print("Ops, Digite apenas os numeros listados!")
            ip_regras()
    # fim do menu de escolha 8

    # escolha 9

    # fim do menu de escolha 9


    # MENU INICIAL PRINCIPAL IPV4
    def menu_main_ipv4():
        '''exibe as opções do menu inicial.'''

        header_banner()
        print(Color.AMARELO +
                '''
                                [0] Sobre
                                [1] Ver Regras
                                [2] Delete Regra
                                [3] Ports
                                [4] Salvar
                                [5] Instalar o netfilter-persistent.service
                                [6] Excluir Regras de Tabelas
                                [7] Ip (Regras Para IPs Especificos)
                                [8] Mac (Regras Para Mac Address)
                '''
        + Color.RESET)

        choice = str(input(Color.AMARELO + "Escolha Uma Opção >>"))

        if choice == "0":
            sobre_software()

        elif choice == "1":
            Ver_regras_firewall()
                
        elif choice == "2":
            deletar_regras_firewall()

        elif choice == "3":
            regras_de_ports_firewall()
                
        elif choice == "4":
            salva_regras_firewall()
                
        elif choice == "5":
            netfilter_install()

        elif choice == "6":
            exclui_tab_firewall()

        elif choice == "7":
            ip_regras()

        elif choice == "8":
            mac_regras()
            
        else:
            os.system("clear")
            print("Digite Apenas os Números Listados!")
            menu_main_ipv4()
    # FIM DO BLOCO DO MENU PRINCIPAL IPV4
            

    if __name__ == "__main__":
        menu_main_ipv4()

except KeyboardInterrupt:
    os.system("clear")
    print("Obrigado Por Usar Este Programa!")
    
    # Acho que acabou.
