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
        BufferString = ''
        qtnCasaDecimais = 8
        arquivo = open(diretorioArqDestino, "w")

        del(lstDados[0])

        for lstLinhas in lstDados:
            for conteudoColuna in lstLinhas:
                qtnZeros = qtnCasaDecimais - len(conteudoColuna)
                conteudoColunaMenor = str(conteudoColuna) + (("0")*qtnZeros)
                conteudoColunaMenor = conteudoColunaMenor[:6]
                BufferString += conteudoColunaMenor + ("\t")
                controlador[2]+=1
            BufferString += "\n"
            arquivo.write(BufferString)
            BufferString = ''

        arquivo.close()