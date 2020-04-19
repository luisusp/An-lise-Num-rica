def print_formatted_vector(X, label = "X"):
    
    _last_index = len(X) - 1
    print("{} = [".format(label), end="")

    for i in range(0, len(X)):
        if i != _last_index:
            print(" {:.3f},".format(X[i]), end="")
        else:
            print(" {:.3f}".format(X[i]), end="")
    print(" ]")

def print_result(L, D):
    print_formatted_vector(L, label = "L")
    print_formatted_vector(D, label = "D")

def print_step(i, ai, bi, li, d_i_1, di):

    print("L{} = b{}/x{} = {:.3f}/{:.3f} = {:.3f}".format(i, i , i, bi,  d_i_1, li))
    print("X{} = a{} - l{} * b{} = {:.3f} - {:.3f} * {:.3f} = {:.3f}\n".format(i, i, i, i, ai, li, bi, di))

def linear_system_solver_th(vector_a, vector_b, r):
    """ Esta função resolve um sistema linear tridiagonal Ax = r
    
    Arguments:
        vector_a {[array]} -- diagonal princial de A
        vector_b {[array]} -- subdiagonal de A
        r {[array]} -- array com os resultados

    Returns:
        {[array]} -- array com os valores de x
    """

    Y    = [r[0]]
    N    = len(vector_a)
    L, D = thomas_algorithm(vector_a, vector_b)
    Z    = [r[0]/D[0]]

    for i in range(1, N):
        yi = r[i] - L[i - 1] * Y[i - 1]
        Y.append(yi)
    
    for i in range(1, N):
        zi = (r[i] - L[i - 1] * Y[i - 1])/D[i]
        Z.append(zi)

    X        = [0] * N          # inicializa o array X com zeros
    X[N - 1] = Z[N - 1]         # Xn = Zn
    i        = N - 2                   

    while i >= 0:
        xi = (Z[i] - L[i] * X[i + 1])
        X[i] = xi
        i = i - 1

    return X

def thomas_algorithm(vector_a, vector_b):
    """Esta função faz a decomposição de uma matriz tridiagonal A em LDL^T
    
    Arguments:
        vector_a {[array]} -- diagonal princial de A
        vector_b {[array]} -- subdiagonal de A
    
    Returns:
        [tuple] -- O primeiro elemento é a matriz L e o segundo a matriz D
    """

    L = []
    D = [vector_a[0]]
    N = len(vector_a)

    for i in range(1, N):
        
        li = vector_b[i - 1]/D[i -1]
        di = vector_a[i] - li * vector_b[i - 1]

        print_step(i, vector_a[i], vector_b[i - 1], li, D[i -1], di)

        L.append(li)
        D.append(di)
    return L, D

def parse_input_vector(str):
    return eval(str)

print("\nSolução do Sistema Linear Ax = r")
print("\nDigite os vetores no formato: [a1, a2, a3, ..., an]")
vector_a = parse_input_vector(input("Vetor diagonal principal de A: "))

print("\nDigite os vetores no formato: [b1, b2, b3, ..., b_(n-1)]")
vector_b = parse_input_vector(input("Vetor subdiagonal de A: "))

print("\nDigite os vetores no formato: [r1, r2, r3, ..., rn]")
r        = parse_input_vector(input("Vetor r: "))
print()
# vector_a = [2, 2, 2, 2]
# vector_b = [1, 1, 1]

# r        = [1, 1, 1, 1]

X        = linear_system_solver_th(vector_a, vector_b, r)
print_formatted_vector(X)

# L, D = thomas_algorithm(vector_a, vector_b)
# print_result(L, D)


    
