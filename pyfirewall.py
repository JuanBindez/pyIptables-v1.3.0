'''
Copyright (c) 2022 Juan Carlos Bindez
"This project is licensed under the MIT License."
'''

try:
    import os
    from colors import Color
    from banner import header_banner
    from ipv4.logica_ipv4 import LogicasMenu1
    from ipv4.logica_ipv4 import RegrasList
    from ipv4.logica_ipv4 import DeleteRegra


    # MENU PRINCIPAL
    ver_regras = LogicasMenu1("sudo iptables -L --line-numbers")
    delete = LogicasMenu1("sudo iptables -D INPUT")



    def menu_main():
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
            os.system("clear")
            ver_regras.start_command()
            header_banner()
            # deleta id de regra no firewall
            print(

                '''                       
                                           deletar de qual tabela?

                                                 *[1]INPUT
                                                 *[2]FORWARD
                                                 *[3]OUTPUT
                
                '''
            )

            choice_delete = str(input(">>"))

            if choice_delete == "1":
                DeleteRegra.delete_INPUT.delete_id()
                menu_main()

            elif choice_delete == "2":
                DeleteRegra.delete_FORWARD.delete_id()
                menu_main()

            elif choice_delete == "3":
                DeleteRegra.delete_OUTPUT.delete_id()
                menu_main()

            os.system("clear")
            ver_regras.start_command()
            delete.delete_id()
            menu_main()

        elif choice == "3":
            # regras de portas
            def header_regra_port():
                os.system("clear")
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
                    menu_main()

                elif choice_regra == "2":
                    RegrasList.ports_tab_input_drop.port_change()
                    menu_main()

            def regra_port_FORWARD():
                header_regra_port()
                choice_regra = str(input(">>"))

                if choice_regra == "1":
                    RegrasList.ports_tab_forward_accept.port_change()
                    menu_main()

                elif choice_regra == "2":
                    RegrasList.ports_tab_forward_drop.port_change()
                    menu_main()

            def regra_port_OUTPUT():
                header_regra_port()
                choice_regra = str(input(">>"))

                if choice_regra == "1":
                    RegrasList.ports_tab_output_accept.port_change()
                    menu_main()

                elif choice_regra == "2":
                    RegrasList.ports_tab_output_drop.port_change()
                    menu_main()


            os.system("clear")
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

            if choice_tab == "2":
                regra_port_FORWARD()

            if choice_tab == "3":
                regra_port_OUTPUT()



        else:
            print("algo deu errado")
            


    if __name__ == "__main__":
        menu_main()

except KeyboardInterrupt:
    os.system("clear")
    print("Obrigado Por Usar Este Programa!")