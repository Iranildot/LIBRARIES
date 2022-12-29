def linear(l:list, escolhido):
    for i in range(len(l)):
        if escolhido == l[i]:
            return i
    return -1

def binary(l:list, escolhido):

    multi = 1
    # Tamanho da lista
    tamanho = len(l)

    # Ajuda a definir os extremos
    inicio = 0
    meio = int(tamanho/2)
    fim = tamanho

    while (True):
        if (escolhido == l[meio]):
            return meio

        elif (escolhido < l[meio]):
            fim = meio
            meio = int((inicio + fim)/2)

        elif (escolhido > l[meio]):
            inicio = meio
            meio = int((inicio + fim)/2)
        
        if (multi >= tamanho):
            return -1
        
        multi *= 2