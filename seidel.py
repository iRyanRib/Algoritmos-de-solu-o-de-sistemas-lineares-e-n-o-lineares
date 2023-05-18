import numpy as np

#define matrix
mat = np.array([[10.0, 2.0, 1.0, 7.0],
                [1.0, 5.0, 2.0, -8.0],
                [2.0, 3.0, 10.0, 6.0],])
dimensions = mat.shape
matA = mat.copy()
matA = np.delete(matA,(dimensions[1]-1),1)
matG = mat[:,dimensions[1]-1]
print(mat)
print(matA)
print(matG)

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

#inicializa matriz A
def makeAmatrix(matA,pivos):
    for i in range(0,len(pivos)):
        matA[i] = (-1/pivos[i])*matA[i]
        matA[i,i] = 0
#inicializa matriz B
def makeGmatrix(matG,pivos):
    for i in range(0,len(pivos)):
        matG[i] = matG[i]/pivos[i]
#encontra os novos valores de g a cada iteração
def newX(matA,matG,matB,pivos):
    list = []
    for i in range(0,len(pivos)):
        x = 0
        for j in range(0,len(pivos)): 
            x = x +  matA[i,j]*matG[j]
        x = x + matB[i]
        matG[i] = x#alteração para usar gauss seidel, usando os valores de x calculados como novos de G para a próxima iteração
    return matG


def main():
  global matG
  #pega pivos
  pivos = findPivos(mat)
  #pega matriz A
  makeAmatrix(matA,pivos)
  #pega matriz g
  makeGmatrix(matG,pivos)
  #pega matriz b
  matB = matG.copy()
  erro = 0.0
  #enquanto erro não for menor que 0.05 continua processo
  while(True):
    matGnovo = newX(matA,matG,matB,pivos)
    matVerif = []
    for i in range(0,len(matGnovo)):
            aux =  abs(matGnovo[i]) - abs(matG[i])
            matVerif.append(aux)
    print("MATv\n",matVerif)
    print("MATgnv\n",matGnovo)
    print("maxVer",max(matVerif),"matGn",max(abs(matGnovo)))
    erro = max(matVerif)/max(abs(matGnovo))
    if(erro < 0.05):
        break
    print("erro:",erro)
    matG = matGnovo
  print("MATa\n",matA)
  #na ultima iteração aqui estará o resultado
  print("MATg\n",matG)
  
 


if __name__ == "__main__":
    main()
