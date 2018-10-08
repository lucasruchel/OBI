# https://olimpiada.ic.unicamp.br/pratique/pj/2018/f2/capsulas/

def moedas_dias(ciclo,dia):
    return int(dia/ciclo)

n_capsulas, n_aproduzir = input().split()

ciclo_capsulas = input().split()

capsulas = []
for i in range(len(ciclo_capsulas)):
    capsulas.append(int(ciclo_capsulas[i]))


n = 0
while True:
    total = 0
    n = n + 1
    for i in range(len(capsulas)):
        total += moedas_dias(capsulas[i],n)

    if (total >= int(n_aproduzir)):
        break

print(n)
