# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <21/11/2015>
"""
from time import strftime
import pandas as pd
import threading

class ThConversor(threading.Thread):
    def __init__ (self, dadosArquivo, diretorioArqOrigem, controlador):
        super(ThConversor, self).__init__()
        self.dados = dadosArquivo
        self.origem = diretorioArqOrigem
        self.controlador = controlador

    def run(self):
        Converte(self.origem, self.dados, self.controlador)


class Converte(object):
    def __init__(self, diretorioArqOrigem, dados, controlador):
        super(Converte, self).__init__()
        self.start(diretorioArqOrigem, dados, controlador)

    def start(self, diretorioArqOrigem, lstdados, controlador):
        # Abrindo o arquivo xlsx
        xlsx = pd.ExcelFile(diretorioArqOrigem)

        # Pegando a primeira coluna
        sheet1 = xlsx.parse(0)

        parsed = pd.ExcelFile.parse(xlsx, "sheet1")
        nomes_coluna = []

        for coluna in (parsed.columns):
            nomes_coluna.append(coluna)

        dados = []
        lstdados.append(parsed[nomes_coluna[0]].size)
        tamanho = parsed[nomes_coluna[0]].size
        controlador[1]+=tamanho
        for i in range(tamanho):
            for coluna in (nomes_coluna):
                row = parsed[coluna].iloc[i]
                dados.append(str(row))
                controlador[0] += 1
            lstdados.append(dados)
            dados = []

class SalvaArquivo(object):
    def __init__(self, diretorioArqDestino, lst_dados, obj):
        super(SalvaArquivo, self).__init__()
        self._objeto = obj
        self.salva(diretorioArqDestino, lst_dados)

    def salva(self, diretorioArqDestino, lst_dados):
        aux = ''
        arq = open(diretorioArqDestino, "w")
        del(lst_dados[0])
        for i in range(len(lst_dados)):
            for j in range(len(lst_dados[i])):
                if j == len(lst_dados[i])-1:
                    aux+=str((lst_dados[i][j]))+"\n"
                else:
                    aux+=str((lst_dados[i][j]))+("\t")
            arq.write(aux) # Transformando o conteudo da primeira posicao da lista em string e escrevendo no arquivo
            aux = ''
        arq.close()
        self._objeto.insertPlainText(strftime('[%H:%M:%S]') + " Arquivo salvo com sucesso!!!")
# dados = []
# controlador = [0]
# c = Converte("dados.xlsx", dados, controlador)