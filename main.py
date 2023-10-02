#!/usr/bin/env python3
"""Hello World multi linguas.

Dependendo da lingua configurada o programa exibe a correspondente

Como usar:

Tenha a variável LANG devidamente configurada no seu sistema operacional:

$ export LANG=pt_BR

execução:

$ python3 main.py
ou
$ ./main.py
"""
import os
__version__ = '0.1'
__author__ = 'Adeilton da Silva'
__license__ = 'Unlicense'

current_language = os.getenv('LANG', 'en_US')[:5]

msg =("Hello world")

if current_language=="pt_BR":
    msg=("Olá Mundo")


elif current_language=="it_IT":
     msg=("Ciao Mondo")



print(msg) 
