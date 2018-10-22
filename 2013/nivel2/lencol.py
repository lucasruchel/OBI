
h0,L0,h1,L1,h,L = [ int(x) for x in input().split() ]

#verifica se cabe em apenas um tecido
if ((h0 >= h and L0 >= L) or (L0 >= h  and h0 >= L) or (h1 >= h and L1 >=L) or (L1 >= h  and (h1 >= L))):
    print("S")
# verifica os dois lados deitados
elif (((h0 >= h) and (h1 >= h) and ((L0+L1) >= L)) or ((h0 >= L) and (h1 >= L) and ((L0+L1) >= h))):
    print("S")
# verifica os primeira deitada e outra de pé
elif (((L0 >= L) and (h1 >= L) and ((h0+L1) >= h)) or  ((L0 >= h) and (h1 >= h) and ((h0+L1) >= L))):
    print("S")
# verifica as duas de pé
elif ((((h0+h1) >= h) and (L0 >= L) and (L1 >= L)) or (((h0+h1) >= L) and (L0 >= h) and (L1 >= h))):
    print("S")
# verifica a primeira deitada e a segunda de pé
elif ((((L0+h1) >= h) and (L1 >= L) and (h0 >= L)) or ((L0+h1 >= L) and (L1 >= h) and (h0 >= h))):
    print("S")

else:
    print("N")


