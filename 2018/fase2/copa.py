# https://olimpiada.ic.unicamp.br/pratique/pj/2018/f2/copa/

K = input()
L = input()

oitavas = []
for i in range(1,17,2):
    oitavas.append((i,i+1))

if ((K,L) in oitavas or (L,K) in oitavas)
