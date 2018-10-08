# *-* coding: utf-8 -*-

#1: número total de fileiras do avião
#2: número de posições por fileira
#3: número da fileira de classe econômica
#4: posição do sr. zuki

nro_fileiras, qtd_by_fileira, nro_in_eco, p_zuki  = [ int(x) for x in input().split() ]

t = ((nro_fileiras * qtd_by_fileira)-((nro_in_eco-1) * qtd_by_fileira) ) 


if (((nro_fileiras-(nro_in_eco-1)) * qtd_by_fileira) < p_zuki):
    print("PROXIMO VOO")
else:
    if (p_zuki % qtd_by_fileira == 0):
        fileira = (p_zuki /  qtd_by_fileira ) + nro_in_eco - 1
        cadeira = qtd_by_fileira
    else:
        fileira = (p_zuki /  qtd_by_fileira ) + nro_in_eco
        cadeira = p_zuki % qtd_by_fileira

    print("%i %c" % (fileira,chr(cadeira+64)))

