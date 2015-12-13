# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <10/12/2015>
"""

class GravaArquivo(object):

    @staticmethod
    def startGravacao(diretorioArqDestino, lstDados, controlador):
        try:
            BufferString = ''
            arquivo = open(diretorioArqDestino, "w")

            del(lstDados[0])

            for lstLinhas in lstDados:
                for conteudoColuna in lstLinhas:
                    BufferString += str(conteudoColuna) + "/t"
                    controlador[2]+=1
                BufferString += "\n"
                arquivo.write(BufferString)
                BufferString = ''

            arquivo.close()
        except:
            print("Não achei")