def selection_sort(l:list, type:str):
    i = 0; j = i

    # Position and length of the current smaller element analyzed in list
    length = len(l)
    position = 0

    while (i < length):
        smaller = l[i]
        j = i
        while (j < length):
            if smaller >= l[j]:
                smaller = l[j]
                position = j
            j += 1

        aux = l[i]
        l[i] = smaller
        l[position] = aux

        i += 1
    
    if type == "reverse" or type == "r" or type == "R":
        tmp = [None] * length
        i = length - 1
        j = 0
        while (i >= 0):
            tmp[i] = l[j]

            i -= 1
            j += 1
        l = tmp

    return l

def bubble_sort(l:list, type:str):

    v = 0
    i = 0
    length = len(l)

    while (True):
        # Change position of items list if the left item is less than next value in list
        if l[i] > l[i + 1]:
            aux = l[i]
            l[i] = l[i + 1]
            l[i + 1] = aux
            v = i
        
        # If not occur any change while program have iterated over the entire list the program ends
        if i == length - 2  and v == 0:
            break

        # If is the end of list and there is any change the program will iterate over list again
        elif i == length - 2:
            v = 0
            i = 0
        else:
            i += 1
    
    if type == "reverse" or type == "r" or type == "R":
        tmp = [None] * length
        i = length - 1
        j = 0
        while (i >= 0):
            tmp[i] = l[j]

            i -= 1
            j += 1
        l = tmp

    return l

def merge_sort(l:list, type:str):
    # variable used to swap lists
    change = 0

    # Variable that helps in sorting non-powers of 2
    define = 1
    length = len(l)

    # auxiliary list
    aux = []
    for element in l:
        aux.append(element)
        if define < length:
            define *= 2

    multi = 2

    # Number of steps to perform sorting
    while (multi <= define):
        i = 0
        c = 0 # Loops through all elements of the new sorted list
        nod1 = 0
        nod2 = int(multi/2)
        qNodes = int(define/multi) 
        
        # Iterate over the nodes to be joined
        while (i < int(qNodes)):
            j = 0

            # Responsible for comparisons between nodes
            while (j < multi - 1):
                if nod2 < length:
                    if (change == 0):
                        if (l[nod1] > l[nod2]):
                            aux[c] = l[nod2]
                            nod2 += 1
                        else:
                            aux[c] = l[nod1]
                            nod1 += 1
                    else:
                        if (aux[nod1] > aux[nod2]):
                            l[c] = aux[nod2]
                            nod2 += 1
                        else:
                            l[c] = aux[nod1]
                            nod1 += 1
                    c += 1

                # Breaking code
                if (nod1 - i*multi >= multi/2):
                    while (nod2 - i*multi - int(multi/2) < int(multi/2)):
                        if nod2 >= length:
                            break

                        if change == 0:
                            aux[c] = l[nod2]
                        else:
                            l[c] = aux[nod2]
                        nod2 += 1
                        c += 1
                    break
                elif (nod2 - i*multi - int(multi/2) >= int(multi/2) or nod2 >= length):
                    while (nod1 - i*multi < int(multi/2)):
                        if nod1 >= length:
                            break

                        if change == 0:
                            aux[c] = l[nod1]
                        else:
                            l[c] = aux[nod1]
                        nod1 += 1
                        c += 1
                    break
                j += 1
            
            i += 1
            nod1 = i*multi
            nod2 = i*multi + int(multi/2) 

        # Manipulation of lists
        if (change == 0):
            change = 1
        else:
            change = 0

        multi *= 2 
        

    if change == 0:
        if type == "reverse" or type == "r" or type == "R":
            tmp = [None] * length
            i = length - 1
            j = 0
            while (i >= 0):
                tmp[i] = l[j]

                i -= 1
                j += 1
            l = tmp

        return l
    else:
        if type == "reverse" or type == "r" or type == "R":
            tmp = [None] * length
            i = length - 1
            j = 0
            while (i >= 0):
                tmp[i] = aux[j]

                i -= 1
                j += 1
            aux = tmp

        return aux

