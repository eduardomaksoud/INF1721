def k_select(lst, k):
    size = len(lst)
    if k > size:
        print("o valor de K excede o tamanho do vetor")
    
    S = []
    M = []
    for i in range(0, size, 5):
       S.append(lst[i:i + 5])
       
    for el in S:
        el.sort()
        print(el)
        M.append(el[len(el)//2])
        
    m = M[len(M)//2]
    print(f"m atual: {m}")

    left = []
    right = []
    l_size = 0
    r_size = 0
    for el in lst:
        if el < m:
            left.append(el)
            l_size = l_size + 1
        elif el > m:
            right.append(el)
            r_size = r_size + 1
    print(f"left: {left}")
    print(f"right: {right}")

    if l_size == k - 1 or (l_size == 0 and r_size == 0):
        return m
    elif l_size > k - 1:
        return k_select(left,k)
    else:
        return k_select(right,k - l_size - 1)
    
t = [2,5,9,19,24,54,5,87,9,10,44,32,18,13,2,4,23,26,16,19,25,39,47,56,71]
