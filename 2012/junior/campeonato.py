
c_v, c_e, c_saldo, f_v, f_e, f_saldo = [ int(x) for x in input().split() ]

if ((c_v * 3 + c_e ) > (f_v * 3 + f_e )):
    print("C")
elif ((c_v * 3 + c_e ) < (f_v * 3 + f_e )):
    print("F")
else:
    if ( f_saldo > c_saldo ):
        print("F")
    elif ( f_saldo < c_saldo ):
        print("C")
    else:
        print("=")


