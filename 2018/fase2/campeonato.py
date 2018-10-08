p_chave = [ int (x) for x in input().split() ]

niveis = ['oitavas','quartas','semifinal','final']

K = 1
L = 9

nivel = 0
def verifica(chave,nivel):
    n_chave = []

    for i in range(0,len(chave),2):
        if ((chave[i] == L and chave[i+1] == K) or (chave[i] == K and chave[i+1] == L)):
            return nivel

        if (chave[i] == K or chave[i+1] == K):
            n_chave.append(K)
        elif (chave[i] == L or chave[i+1] == L):
            n_chave.append(L)
        else:
            n_chave.append(0)

    nivel += 1

    return verifica(n_chave,nivel)


encontro = verifica(p_chave,0)

print(niveis[encontro])
