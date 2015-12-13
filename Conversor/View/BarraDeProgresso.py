# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <12/12/2015>
"""
from PyQt4 import QtGui

class ProgressBar(object):
    def __init__(self, objetoInterface):
        super(ProgressBar, self).__init__()
        self.creatProgressBar(objetoInterface)

    def creatProgressBar(self, objInter):
        objInter.progressBar = QtGui.QProgressBar(self)             # Criando uma barra de progresso
        objInter.LayoutConversao.addWidget(self.progressBar)        # Adicionando a barra de progresso no layout do widget
        objInter.timer = QtCore.QBasicTimer()                # Criando o objeto tempo
        objInter.step = 0                                    # Controlador do tempo
        objInter.inicio = 0                                  # Controla o relogio

    def timerEvent(self, e):
        if objInter.step >= 100:
            objInter.timer.stop()
            objInter.CxTexto.insertPlainText(strftime('[%H:%M:%S]') + " Arquivo salvo com sucesso\n")

        if objInter.dadosArquivo != [] and objInter.step < 50:
            objInter.tamanho = objInter.dadosArquivo[0] * objInter.controlador[1]
            if objInter.controlador[0] <= (objInter.dadosArquivo[0] * objInter.controlador[1]):
                objInter.step = ((len(objInter.dadosArquivo)-1)*50)//objInter.dadosArquivo[0]
                objInter.progressBar.setValue(objInter.step)

        if objInter.step >= 50:
            if objInter.controlador[2] <= (objInter.tamanho):
                objInter.step = (objInter.controlador[2]*50)/objInter.tamanho + 50
                objInter.progressBar.setValue(objInter.step)

        if objInter.step == 50:
            objInter.CxTexto.insertPlainText(strftime('[%H:%M:%S]') + " Conversão concluida com sucesso...\n")
            objInter.CxTexto.insertPlainText(strftime('[%H:%M:%S]') + " Salvando arquivo...\n")
            Conversor.starThreadGravadora(objInter.nome_arquivoDestino, objInter.dadosArquivo, objInter.controlador)

    def doAction(self):
        objInter.timer.isActive()
        objInter.timer.start(100, objInter)