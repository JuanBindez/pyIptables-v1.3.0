'''
Copyright (c) 2022 Juan Carlos Bindez
"This project is licensed under the MIT License."
'''


import os
from colors import Color
from banner import header_banner
from ipv4.logica_ipv4 import LogicasMenu1
from ipv4.logica_ipv4 import RegrasList


# MENU PRINCIPAL
ver_regras = LogicasMenu1("sudo iptables -L --line-numbers")
delete = LogicasMenu1("sudo iptables -D INPUT")


try:
    def menu_main():
        os.system("clear")
        header_banner()
        print(Color.BRANCO +
            '''
                                                *[1]Ver Regras
                                                *[2]Delete Regra
                                                *[3]Ports

            '''
        + Color.RESET)

        choice = str(input(">>"))

        if choice == "1":
            # ve regras existentes no firewall
            os.system("clear")
            ver_regras.start_command()
            menu_main()

        elif choice == "2":
            # deleta id de regra no firewall
            os.system("clear")
            ver_regras.start_command()
            delete.delete_id()
            menu_main()

        elif choice == "3":
            # regras de portas
            def header_regra_port():
                header_banner()
                print(
                '''
                                                    *[1]ACCEPT
                                                    *[2]DROP
                
                '''
                )

    
            def regra_port_INPUT():
                header_regra_port()
                choice_regra = str(input(">>"))

                if choice_regra == "1":
                    RegrasList.ports_tab_input_accept.port_change()


            header_banner()
            print(Color.BRANCO +
                '''           
                        Escolha a Tabela

                                                    *[1]INPUT
                                                    *[2]FORWARD
                                                    *[3]OUTPUT
                '''
            + Color.RESET)

            choice_tab = str(input(">>"))

            if choice_tab == "1":
                regra_port_INPUT()



        else:
            print("algo deu errado")
            
except KeyboardInterrupt:
    os.system("clear")


if __name__ == "__main__":
    menu_main()