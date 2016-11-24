#-*- coding: utf-8 -*-
# novos comentários aqui
from pygraphviz import *
from random import *
from threading import Thread
import Image
import os

LIMPAR = "clear"

class Dijkstra(Thread):

   def menorCaminho(self, rede, origem):

      #Inicialização
      dist = {}

      for node in rede:
         if node in rede.neighbors(origem):
            dist[node] = (float(rede.get_edge(origem, node).attr['label']), origem)
         else:
            dist[node] = (float('+inf'), None)

      N = dist.keys()
      Nl = [origem]
      distCopy = dist.copy()
      listaDist = [distCopy]


      #Iteração principal
      while (len(N) > len(Nl)):
         items = dist.items()
         itemsAux = []
         for el in items:
            if el[0] not in Nl:
               itemsAux += [el]

         menor = itemsAux[0]
         for el in itemsAux:
            if el[1][0]<menor[1][0]:
               menor = el

         Nl += [menor[0]]

         for node in rede.neighbors(menor[0]):
            if node not in Nl:
               if dist[node][0] > (menor[1][0]+float(rede.get_edge(menor[0], node).attr['label'])):
                  dist[node] = (menor[1][0]+float(rede.get_edge(menor[0], node).attr['label']), menor[0])

         #del dist[origem]
         distCopy = dist.copy()
         listaDist += [distCopy]


      return (Nl, dist, listaDist)


def gerarGrafo(n):
   grafo = AGraph(strict=False)
   nodeC = randint(97,122)
   nodeD = randint(97,122)
   for i in range(n):
      nodeA = randint(97,122)
      nodeB = randint(97,122)

      while nodeA==nodeB or grafo.has_edge(chr(nodeA), chr(nodeB)):
         nodeB = randint(97,122)

      custo = randint(1,20)
      grafo.add_edge(chr(nodeA), chr(nodeB), label=str(custo))

      while nodeA==nodeC or grafo.has_edge(chr(nodeA), chr(nodeC)):
         nodeC = randint(97,122)

      custo = randint(1,20)
      grafo.add_edge(chr(nodeA), chr(nodeC), label=str(custo))

      while nodeB==nodeD or grafo.has_edge(chr(nodeB), chr(nodeD)):
         nodeD = randint(97,122)

      custo = randint(1,20)
      grafo.add_edge(chr(nodeB), chr(nodeD), label=str(custo))

      nodeC = nodeB
      nodeD = nodeA

   return grafo


def desenharMenorCaminho(grafo, dist, origem, destino):

   for el in grafo.edges():
      el.attr['color'] = 'black'

   destinoAux = destino

   while True:
      ptr = dist.get(destinoAux)[1]
      grafo.get_edge(destinoAux, ptr).attr['color'] = 'red'
      destinoAux = ptr
      if ptr == origem:
         break


   grafo.draw("grafo.jpg", "jpg", "dot")
   Image.open("grafo.jpg").show();


def calcularRotas(grafo):
   dicResultados = {}
   for el in grafo:
      o = Dijkstra()
      r = o.menorCaminho(grafo, el)
      dicResultados[el] = r

   return dicResultados


def tabelaRota(resultado):

   print ("\nDestino | (Menor distância/antecessor)")
   lista = resultado.items()
   lista.sort()
   for el in lista:
      print (str(el[0]) + " | " + str(el[1]))

   raw_input("\nPressione ENTER para continuar...")

# ele reconhece como a função principal?
# isto, é, main é palavra reservada?
def main():

   grafo = gerarGrafo(5)
   grafo.draw("grafo.jpg", "jpg", "dot")

   dicResultados = None

   opcao = -1

   while opcao != 6:
      os.system(LIMPAR)
      print ("ALGORITMO DE DIJKSTRA")
      print ("1. Gerar novo grafo")
      print ("2. Visualizar grafo")
      print ("3. Calcular caminhos")
      print ("4. Visualizar tabela de menor caminho")
      print ("5. Visualizar iterações de tabela de menor caminho")
      print ("6. Sair")
      opcao = input("\nEscolha uma opção: ")

      if opcao==1:
         grafo = gerarGrafo(5)
         grafo.draw("grafo.jpg", "jpg", "dot")
         raw_input("Grafo gerado!")

      if opcao==2:
         Image.open("grafo.jpg").show();

      if opcao==3:
         dicResultados = calcularRotas(grafo)
         raw_input("Cálculos encerrados...")

      if opcao==4:
         if dicResultados:
            origem = raw_input("\nEscolha um nó de origem: ")
            resultado = dicResultados.get(origem)
            print ("Vetor N' = " + str(resultado[0]))
            tabelaRota(resultado[1])
            destino = raw_input("Escolha um nó destino para visualizar o menor caminho: ")
            desenharMenorCaminho(grafo, dicResultados[origem][1], origem, destino)
         else:
            raw_input("Caminhos não calculados, escolha a opção 3 para calculá-los...")

      if opcao==5:
         if dicResultados:
            origem = raw_input("\nEscolha um nó de origem: ")
            resultado = dicResultados.get(origem)
            print (resultado)
            for el in resultado[2]:
               tabelaRota(el)
         else:
            raw_input("Caminhos não calculados, escolha a opção 3 para calculá-los...")


main()
