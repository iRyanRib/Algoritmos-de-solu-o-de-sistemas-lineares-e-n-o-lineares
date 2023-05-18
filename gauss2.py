#import libs
import numpy as np

#define matrix
mat = np.array([[3.0, 2.0, 4.0, 1.0],
                [1.0, 1.0, 2.0, 2.0],
                [4.0, 3.0, -2.0, 3.0],])

dimensions = mat.shape#take the limits of matrix
print(dimensions)
#O determinante é diferente de 0?
def verifyMat(mat):
  #verificando determinante
  
  matVerif = mat.copy()
  matVerif = np.delete(matVerif,(dimensions[1]-1),1)
  print(matVerif)
  det = np.linalg.det(matVerif)
  print(det)
  if(det!=0):
    if(dimensions[0] == dimensions[1]-1):
      print("start elimination process")
      gaussElimination(mat)
    else:
      print("matrix isn't nxn")
  else:
    print("det == 0 error")

def gaussElimination(mat):
  pivos = findPivos(mat)
  dividePivo(mat,pivos)
  xlist = solve_linear(mat)
  print("result",xlist)

#find pivos
def findPivos(mat):
    pivos = []
    for i in range(dimensions[0]):
        if mat[i,i] != 0:
            pivos.append(mat[i,i])
        else:
            print("pivo equal to 0!")
            break
    return pivos
# Divide all of same pivot coluns  values by own pivot
def dividePivo(mat,pivos):
  matAux = mat.copy()
  for i in range(0,len(pivos)):#coluna
    matAux = mat.copy()
    for j in range(0,dimensions[0]):#linha
        if(i!=j and j >=i):#não é um pivô
           mat[j] = mat[j] - ((mat[j,i]/mat[i,i])*mat[i])
        print(mat)
        print("\n")
   # print(pivos)

#solve linear equation and find x's
def solve_linear(mat):
    x = [1]*dimensions[0]
    for i in range(dimensions[0]-1,-1,-1):
      a = 0
      for j in range(dimensions[1]-1,-1,-1):
        if (j==i):
          d = mat[i][j]
        elif( j == (dimensions[1]-1)):
          c = mat[i][j]
        else:
          a = (a + (-1*mat[i][j]))*x[j]
      result = (a + c )/d
      x[i] = round(result,4)
    return x
def main():
  verifyMat(mat)
if __name__ == "__main__":
    main()