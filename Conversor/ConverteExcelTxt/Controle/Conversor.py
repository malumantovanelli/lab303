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
    def __init__ (self, dadosArquivo, diretorioArqOrigem):
        super(ThConversor, self).__init__()
        self.dados = dadosArquivo
        self.origem = diretorioArqOrigem

    def run(self):
        (Converte(self.origem, self.dados))


class Converte(object):
    def __init__(self, diretorioArqOrigem, dados):
        super(Converte, self).__init__()
        #self.start(diretorioArqOrigem, dados)

    def start(self, diretorioArqOrigem, dados):
        # Abrindo o arquivo xlsx
        xlsx = pd.ExcelFile(diretorioArqOrigem)


        # Pegando a primeira coluna
        sheet1 = xlsx.parse(0)

        parsed = pd.ExcelFile.parse(xlsx, "sheet1")
        lst = []
        print(parsed.columns[1])
        print(parsed["Untitled.1"][0])

        nomes_coluna = []
        for coluna in (parsed.columns):
            nomes_coluna.append(coluna)

        print(nomes_coluna)
        print(parsed[nomes_coluna[0]].size)
        for i in range(parsed[nomes_coluna[0]].size):
            for coluna in (nomes_coluna):
                row = parsed[coluna].irow(i)
                dados.append(str(row))
            lst.append(dados)
            dados = []

        aux = ''
        arq = open("teste.txt", "w")
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if str((lst[i][j])) != "nan":
                    if j == len(lst[i])-1:
                        aux+=str((lst[i][j]))+"\n"
                    else:
                        aux+=str((lst[i][j]))+("\t")
                else:
                    aux+="\t\t"
            arq.write(aux) # Transformando o conteudo da primeira posicao da lista em string e escrevendo no arquivo
            #arq.write("\n")  # Pulando uma linha no arquivo
            aux = ''


        # for coluna in (parsed.columns):
        #     size_coluna = parsed[coluna].size
        #     dados.append(size_coluna)
        #     for i in range(size_coluna):
        #          row = parsed[coluna].irow(i)  # Transformando o dado da linha em uma lista
        #          dados.append(str(row))
        #     lst.append(dados)
        #     dados = []

        # dic = {"size" :[]}
        # for coluna in (parsed.columns):
        #     size_coluna = parsed[coluna].size
        #     dic["size"].append(size_coluna)
        #     for i in range(size_coluna):
        #         if i not in list(dic.keys()):
        #             dic[i] = []
        #             dic[i].append(parsed[coluna].irow(i))
        #         else:
        #             dic[i].append(parsed[coluna].irow(i))
        # #print(dic)
        # aux = ''
        # arq = open("teste.txt", "w")
        # for i in range(dic["size"]):
        #     for j in range(len(dic[i])):
        #         aux+=str((dic[i][j]))+"\t"
        #     arq.write(aux) # Transformando o conteudo da primeira posicao da lista em string e escrevendo no arquivo
        #     arq.write("\n")  # Pulando uma linha no arquivo

        # arq = open("teste.txt", "w")
        # for i in range(len(lst)):
        #     tamanho = lst[i][0]
        #     print(tamanho)
        #     del(lst[i][0])
        #     for j in range(tamanho):
        #         arq.write(str(lst[i][j]))  # Transformando o conteudo da primeira posicao da lista em string e escrevendo no arquivo
        #         arq.write("\n")  # Pulando uma linha no arquivo
        #     arq.write("Coluna")

        # for coluna in (parsed.colums):
        #     size_coluna = parsed.icol(i).size
        #
        #     print(size_coluna)
        #     # size_coluna a coluna
        #     dados.append(size_coluna)
        #     for i in range(50):
        #         row = parsed.irow(i).tolist()  # Transformando o dado da linha em uma lista
        #         dados.append(str(row[0]))
        #     print(dados)
        #     print("\n")
        #     lst.append(dados)
        #     dados = []
        # arq  = open("teste", "w")
        # for i in range(len(lst)):
        #     tamanho = lst[i][0]
        #     print(tamanho)
        #     del(lst[i][0])
        #     for j in range(tamanho):
        #         arq.write(str(lst[i][j]))  # Transformando o conteudo da primeira posicao da lista em string e escrevendo no arquivo
        #         arq.write("\n")  # Pulando uma linha no arquivo
        #     arq.write("Coluna")
        #
        # arq.close()


        # Pegando o tamanho do numero de linha da primeira coluna
        #size_coluna = sheet1.icol(0).size

        # # Varrendo a coluna
        # dados.append(size_coluna)
        # for i in range(size_coluna):
        #     row = sheet1.irow(i).tolist()  # Transformando o dado da linha em uma lista
        #     dados.append(str(row[0]))

class SalvaArquivo(object):
    def __init__(self, diretorioArqDestino, lst_dados, obj):
        super(SalvaArquivo, self).__init__()
        self.objeto = obj
        self.salva(diretorioArqDestino, lst_dados)

    def salva(self, diretorioArqDestino, lst_dados):
        # Abrindo arquivo para salvar em txt
        arq  = open(diretorioArqDestino, "w")
        tamanho = lst_dados[0]
        del(lst_dados[0])
        for i in range(tamanho):
            arq.write(str(lst_dados[i]))  # Transformando o conteudo da primeira posicao da lista em string e escrevendo no arquivo
            arq.write("\n")  # Pulando uma linha no arquivo

        self.objeto.CxTexto.insertPlainText(strftime('[%H:%M:%S]')+ " Arquivo salvo com sucesso!!!\n")
        arq.close()  # Fechando o arquivo
dados = []
diretorio = "dados.xlsx"
teste = Converte(diretorio, dados)

teste.start(diretorio, dados)