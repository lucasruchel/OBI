# https://olimpiada.ic.unicamp.br/pratique/pj/2018/f1/basquete/

d1p = 0
d2p = 800
d3p = 1400

d_robo = int(input())

if d_robo <= d2p:
    p = 1
elif d_robo > d2p and d_robo <= d3p:
    p = 2
elif d_robo <= 2000:
    p = 3

print(p)
