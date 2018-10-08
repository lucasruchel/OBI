# https://olimpiada.ic.unicamp.br/pratique/pj/2018/f1/album/

q_album = int(input())
q_compradas = int(input())

fig_compradas = []

for i in range(q_compradas):
    fig_compradas.append(int(input()))

fig_preenchidas = set(fig_compradas)
total_faltante = q_album - len(fig_preenchidas)

print(total_faltante)
