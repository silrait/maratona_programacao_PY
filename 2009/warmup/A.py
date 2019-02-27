import sys


def bubblesort(q, v):
    jogador = ["marcelo", "carlos"]
    turno = -1
    for i in range(0, q):
        for j in range(0, q - i - 1):
            if(v[j] > v[j + 1]):
                v[j], v[j + 1] = v[j + 1], v[j]
                turno += 1
    
    return jogador[turno % 2]
    

def main():
    for linha in sys.stdin:
        tokens = linha.strip().split(" ")
        quantidade = int(tokens[0])
        if(quantidade == 0):
            break
            
        vetor = list(map(int, tokens[1:]))
        
        print(bubblesort(quantidade, vetor))
        
        
if(__name__ == '__main__'):
    main()