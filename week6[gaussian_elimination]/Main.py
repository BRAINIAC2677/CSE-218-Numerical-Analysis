import numpy as np

def GaussianElimination(A, B, pivot = True, showall = True):
    n = A.shape[0]
    A = np.float64(A)
    B = np.float64(B)
    if showall is True:
        print("Start of Forward Elimination:\n")
    for i in range(n-1):
        if pivot is True:
            max_row_index = np.argmax(np.abs(A[i:, i])) + i
            A[[i, max_row_index]] = A[[max_row_index, i]]
            B[[i, max_row_index]] = B[[max_row_index, i]]
        
        for j in range(i+1, n):
            multiplier = A[j, i] / A[i,i]
            subtracted_term = A[i, i:] * multiplier
            A[j, i:] = A[j, i:] - subtracted_term
            subtracted_term = B[i]*multiplier
            B[j] = B[j] - subtracted_term
            if showall is True:
                print(f'Step: {i+1} Substep: {j-i}\nA:\n{A}\nB:\n{B}\n')
    if showall is True:
        print("End of Forward Elimination\n")
    X = np.zeros((n,1))
    for i in range(n-1, -1, -1):
        X[i] = B[i]
        tempA = A[i, i+1:]
        tempX = X[i+1:, 0]
        tempA = tempA.reshape(1, tempA.shape[0])
        tempX = tempX.reshape(tempX.shape[0], 1)
        X[i] = X[i] - np.matmul(tempA, tempX)
        X[i] = X[i] / A[i, i]
    return X

def take_input():
    n = int(input())
    A = np.zeros((n,n))
    B = np.zeros((n,1))
    for i in range(n):
        row = list(map(float, input().strip().split()[:n]))
        A[i] = row
    for i in range(n):
        row = float(input().strip())
        B[i] = row
    return n,A, B

def Main():
    n = 3
    A = np.array([[-2, 0, 1], [-1, 7, 1], [5,-1, 1]])
    B = np.array([[-4], [-50], [-26]])
    #n,A, B = take_input()
    np.set_printoptions(formatter={'float': lambda x: "{0:0.4f}".format(x)})
    X = GaussianElimination(A, B)
    print("The Solution Vector:")
    for i in range(n):
        print(f'{X[i][0]:0.4f}')
    

Main()