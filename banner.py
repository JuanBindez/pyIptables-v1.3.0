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

