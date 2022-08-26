'''
    Aqui esta o banner da interface do usuario.
'''

'''
Copyright (c) 2022 Juan Carlos Bindez
"This project is licensed under the MIT License."
'''


from colors import Color

def header_banner():
    print(Color.AMARELO +
                '''
                            
                                                                             
                                           ,,                                                ,,   ,,  
                              `7MM"""YMM   db                                              `7MM  7MM  
                                MM    `7                                                     MM   MM  
        `7MMpdMAo. `7M'   `MF'  MM   d   `7MM  `7Mb,od8  .gP"Ya  `7M'    ,A    `MF' ,6"Yb.   MM   MM  
          MM   `Wb   VA   ,V    MM""MM     MM    MM' "' ,M'   Yb   VA   ,VAA   ,V  8)   MM   MM   MM  
          MM    M8    VA ,V     MM   Y     MM    MM     8M""""""    VA ,V  VA ,V    ,pm9MM   MM   MM  
          MM   ,AP     VVV      MM         MM    MM     YM.    ,     VVV    VVV    8M   MM   MM   MM  
          MMbmmd'      ,V     .JMML.     .JMML..JMML.    `Mbmmd'      W      W     `Moo9^Yo.JMML.JMML. v1.1.2
          MM          ,V                                                                                
        .JMML.     OOb"                             
                                                                                    
                                    Copyright (c) 2022 Juan Carlos Bindez
                                    
                                      *[Ctrl + C] Para Sair do Programa               
                '''
    + Color.RESET)

