#!/usr/bin/env python
"""
A equacao da reta e dada por y = mx + b

Onde:
m e o coeficiente angular da reta (determina a sua inclinacao)
b e o coeficiente linear da reta e determina o ponto onde a
reta corta o eixo y (isto e, b determina o valor de y quando x for zero)

"""
from fractions import Fraction

if __name__ == "__main__":
    print("Determinacao da equacao da reta a partir de 2 pontos:")

    print(__doc__)

    p1 = raw_input("Ponto (x1,y1): ")# necessario que as coordenadas sejam enviadas até aqui
    p2 = raw_input("Ponto (x2,y2): ")# tentar substituir isso por event.x e event.y, respectivamente

    print(p1, p2)#apenas para fins de verificacao

    # separa os elementos recebidos em suas respectivas variáveis
    # talvez isso seja desnecessario
    x1 = p1.split(",")[0].strip()
    y1 = p1.split(",")[1].strip()
    x2 = p2.split(",")[0].strip()
    y2 = p2.split(",")[1].strip()

    print("(x1, y1) = (%s, %s)" % (x1, y1))# novamente, apenas para fins de comprovação
    print("(x2, y2) = (%s, %s)" % (x2, y2))

    x1Frac = Fraction(x1)
    y1Frac = Fraction(y1)
    x2Frac = Fraction(x2)
    y2Frac = Fraction(y2)
    mFrac = (y2Frac - y1Frac) / (x2Frac - x1Frac)
    bFrac = y1Frac - (mFrac*x1Frac)

    print("Equacao geral da reta: y = mx+b")

    # Determina o sinal a ser apresentado no texto da equacao da reta
    sign = ""
    if bFrac > 0:
        sign = "+"

    # Monta m e b em formato string levando em consideracao se o
    # denominador for igual a 1 (se denominador=1, nao mostra fracao)
    if mFrac.denominator == 1:
        mStr = "%d" % mFrac.numerator
    else:
        mStr = "(%d/%d)" % (mFrac.numerator, mFrac.denominator)

    if bFrac.denominator == 1:
        bStr = "%d" % bFrac.numerator
    else:
        bStr = "(%d/%d)" % (bFrac.numerator, bFrac.denominator)

    print("\nEquacao da reta proposta: y=%sx%s%s" % (mStr, sign,bStr))
    print("Coeficiente angular: %s" % mStr.strip("(").strip(")"))
    print("Coeficiente linear:  %s" % bStr.strip("(").strip(")")
