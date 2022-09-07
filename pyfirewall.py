'''
Copyright (c) 2022 Juan Carlos Bindez
"This project is licensed under the MIT License."

Todas as funções desse script buscam comandos embutidos
nas classes do arquivo logica_ipv4.py e os executam,
conforme solicitado na interface do usuario.
'''


try:
    import os
    import time

    from banner import header_banner
    from colors import Color
    from ipv4.logica_ipv4 import DeleteRegra, LogicasMenu1, RegrasList, IpRegras


    ver_regras = LogicasMenu1("sudo iptables -L --line-numbers")# variaveis para ver regras numeradas
    delete = LogicasMenu1("sudo iptables -D INPUT")# regra para deletar tabela


    #### INCIO DO BLOCO DE MENU IPV4 ####
    

    #### escolha 1 ####
    def Ver_regras_firewall():
        # ve regras existentes no firewall
        os.system("clear")
        ver_regras.start_command()
        menu_main_ipv4()

    #### escolha 2 ####
    def deletar_regras_firewall():
        os.system("clear")
        ver_regras.start_command()
        header_banner()
        # deleta id de regra no firewall
        print(Color.AMARELO +

                '''                       
                                         Deletar de qual tabela?

                                *[0]Voltar
                                *[1]INPUT     
                                *[2]FORWARD
                                *[3]OUTPUT
                                                 
                '''
        + Color.RESET)

        choice_delete = str(input(">>"))

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
        #### fim do menu de escolha 2 ####

    #### escolha 3 ####
    def regras_de_ports_firewall():

        #### func menu de escolha 3 ####
        def regra_port_INPUT():
            header_regra_port()
            choice_regra = str(input(">>"))

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

        #### func menu de escolha 3 ####
        def header_regra_port():
            os.system("clear")
            header_banner()
            print(Color.AMARELO +
                '''
                                *[0]Voltar
                                *[1]ACCEPT
                                *[2]DROP
                
                '''
            + Color.RESET)
            ### header ####

        #### func menu de escolha 3 ####
        def regra_port_FORWARD():
            header_regra_port()
            choice_regra = str(input(">>"))

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

        #### func menu de escolha 3 ####
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

                                *[0]Voltar
                                *[1]INPUT
                                *[2]FORWARD
                                *[3]OUTPUT

                '''
        + Color.RESET)

        choice_tab = str(input(">>"))

        if choice_tab == "0":
            os.system("clear")
            menu_main_ipv4()

        elif choice_tab == "1":
            regra_port_INPUT()

        elif choice_tab == "2":
            regra_port_FORWARD()

        elif choice_tab == "3":
            regra_port_OUTPUT()
        #### fim do menu de escolha 3 ####
    ######################################################################


    #### escolha 4 ####
    def salva_regras_firewall():
        os.system("sudo service netfilter-persistent save")
        time.sleep(2)
        os.system("sudo systemctl restart netfilter-persistent.service")
        time.sleep(2)
        os.system("sudo systemctl status netfilter-persistent.service")
        os.system("clear")
        menu_main_ipv4()

    #### escolha 5 ####
    def netfilter_install():
        os.system("sudo apt-get install netfilter-persistent.service")
        os.system("sudo apt-get install iptables-persistent")
        time.sleep(2)
        os.system("clear")
        menu_main_ipv4()

    #### escolha 6 ####
    def exclui_tab_firewall():
        os.system("clear")
        ver_regras.start_command()
        header_banner()

        print(Color.AMARELO +

                '''    
                                        Escolha a Tabela a ser Excluída

                                *[0]Voltar
                                *[1]INPUT
                                *[2]FORWARD
                                *[3]OUTPUT
                                *[4]Todas as tabelas
                
                '''
        + Color.RESET)

        escolha = str(input(">>"))

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
        #### fim do menu de escolha 6 ####


    #### escolha 7 ####
    def ip_regras():

        def header_escolha7():
            os.system("clear")
            header_banner()

            print(Color.AMARELO +
                    '''
                                    *[0]Voltar
                                    *[1]ACCEPT
                                    *[2]DROP

                    
                    '''
            + Color.RESET)

        ### fuc escolha 7 ###
        def ip_regra_INPUT_ACCEPT():
            IpRegras.ip_ACCEPT_tab_INPUT.ip_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        ### func escolha 7 ###
        def ip_regra_FORWARD_ACCEPT():
            IpRegras.ip_ACCEPT_tab_FORWARD.ip_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()


        ### func escolha 7 ###
        def ip_regra_OUTPUT_ACCEPT():
            IpRegras.ip_ACCEPT_tab_OUTPUT.ip_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()


        ### fuc escolha 7 ###
        def ip_regra_INPUT_DROP():
            IpRegras.ip_DROP_tab_INPUT.ip_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        ### func escolha 7 ###
        def ip_regra_FORWARD_DROP():
            IpRegras.ip_DROP_tab_FORWARD.ip_func_regra()
            os.system("clear")
            ver_regras.start_command()
            menu_main_ipv4()

        ### func escolha 7 ###
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

                                 *[0]Voltar   
                                 *[1]INPUT
                                 *[2]FORWARD   
                                 *[3]OUTPUT
                '''
        + Color.RESET)

        escolha7 = str(input(">>"))

        if escolha7 == "0":
            os.system("clear")
            menu_main_ipv4()

        elif escolha7 == "1":
            header_escolha7()
            escolha = str(input(">>"))

            if escolha == "0":
                os.system("clear")
                menu_main_ipv4()

            elif escolha == "1":
                ip_regra_INPUT_ACCEPT()

            elif escolha == "2":
                ip_regra_INPUT_DROP()


        elif escolha7 == "2":
            header_escolha7()
            escolha = str(input(">>"))

            if escolha == "0":
                os.system("clear")
                menu_main_ipv4()

            elif escolha == "1":
                ip_regra_FORWARD_ACCEPT()

            elif escolha == "2":
                ip_regra_FORWARD_DROP()

        elif escolha7 == "3":
            header_escolha7()
            escolha = str(input(">>"))

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
    #### fim do menu de escolha 7 ####


    ### escolha 8 ###
    ### fim do menu de escolha 8 ###



    ###### MENU INICIAL PRINCIPAL IPV4 ######
    def menu_main_ipv4():
        header_banner()
        print(Color.AMARELO +
                '''
                                    *[1]Ver regras
                                    *[2]Delete regra
                                    *[3]Ports
                                    *[4]Salvar
                                    *[5]Instalar o netfilter-persistent.service
                                    *[6]Excluir tabelas
                                    *[7]Ip (regras para IPs especificos)

                '''
        + Color.RESET)

        choice = str(input(">>"))

        if choice == "1":
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
            
        else:
            os.system("clear")
            print("Digite Apenas os Números Listados!")
            menu_main_ipv4()
    #### FIM DO BLOCO DO MENU PRINCIPAL IPV4
            

    if __name__ == "__main__":
        menu_main_ipv4()

except KeyboardInterrupt:
    os.system("clear")
    print("Obrigado Por Usar Este Programa!")
