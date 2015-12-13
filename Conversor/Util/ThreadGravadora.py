# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <12/12/2015>
"""

from Model.Gravador import GravaArquivo
import threading


class ThreadGravar(threading.Thread):
    def __init__ (self,  diretorioArqDestino, lst_dados, obj):
        super(ThreadGravar, self).__init__()
        self.dados = lst_dados
        self.diretorioDestino = diretorioArqDestino
        self._objeto = obj

    def run(self):
        GravaArquivo.startGravacao(self.diretorioDestino, self.dados, self._objeto)