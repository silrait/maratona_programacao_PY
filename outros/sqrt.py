import sys

for linha in sys.stdin:
    valor = int(linha.strip())
    e = float(valor)
    s = 0.0
    m = 0.0
    
    while((e - s) >= 0.00001):
        m = (e + s) / 2
        if((m * m) > valor):
            e = m
        else:
            s = m
    
    print("Valor {} tem a raiz {:.3f}".format(valor, m))
    