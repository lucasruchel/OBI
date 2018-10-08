
M,N = [ int(x) for x in input().split() ]

moradores = []
total_cheques = 0
valor_minimo = 0

for i in range(N):
    moradores.append(0)

for i in range(M):
    f,v,t = [ int(x) for x in input().split() ]
    total_cheques += v
    moradores[f-1] -= v
    moradores[t-1] += v


for i in range(N):
    if (moradores[i] > 0):
        valor_minimo += moradores[i]

if (valor_minimo < total_cheques):
    print('S')
else:
    print('N')

print(valor_minimo)
