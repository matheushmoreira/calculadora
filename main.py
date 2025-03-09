import sys
from turtle import color
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)

#declarando Variaveis
tamanhoBotao = 60
lista = []

#Definindo Funções
def limpar ():
    inputCalculadora.setText("")
    lista.clear()

def calcularResultado():
    #print("teste")
    try:
        
        conteudoInput = inputCalculadora.text()
        resultado = eval(conteudoInput)
        print(conteudoInput)
        print(resultado)
        inputCalculadora.setText(str (resultado))
    except Exception as e:
        # print("erro")
        inputCalculadora.setText("Error")

def calculadora(valor):
    
    if valor == "+":
        print("soma")
    if valor == "-":
        print("menos")
    if valor == "X":
        print("Multi")
    if valor == "/":
        print("Dividir")
    if valor == "=":
        print("Igual")
    if valor == ",":
        print("Virgula")
    if valor == "AC":
        print("AC")
    if valor == "%":
        print("Porcentagem")
    if valor == "+/-":
        print("MaisMenos")
        
    lista.append(valor)
    junta = "".join(lista)
    inputCalculadora.setText (junta) #chamar o valor
    
        
        
    

janela = QWidget() #cria uma janela
janela.resize(290, 450) #Define um tamanho
janela.setWindowTitle("Calculadora") #Define um titulo para a janela


with open("style.css", "r") as style_file: #importar o arquivo css
    styles = style_file.read() #lendo todo o conteudo do arquivo CSS

janela.setStyleSheet(styles) #aplicando o estilo na janela

#Entrada de dados da Calculadora
inputCalculadora = QLineEdit("", janela)
inputCalculadora.resize(270, 40)
inputCalculadora.move(10, 40)
inputCalculadora.setReadOnly(True)

#Criando os botões
btnAC = QPushButton("AC", janela)
btnAC.setGeometry(10, 80, tamanhoBotao, tamanhoBotao)
btnAC.setObjectName("botaoAC")
btnAC.clicked.connect(limpar)

btnMaisMenos = QPushButton("+/-", janela)
btnMaisMenos.setGeometry(80, 80, tamanhoBotao, tamanhoBotao)
btnMaisMenos.setObjectName("botaoAC")
btnMaisMenos.clicked.connect(lambda : calculadora("+/-"))

btnPorcentagem = QPushButton("%", janela)
btnPorcentagem.setGeometry(150, 80, tamanhoBotao, tamanhoBotao)
btnPorcentagem.setObjectName("botaoAC")
btnPorcentagem.clicked.connect(lambda : calculadora("%"))

btnDividir = QPushButton("/", janela)
btnDividir.setGeometry(220, 80, tamanhoBotao, tamanhoBotao)
btnDividir.setObjectName("botaoDividir")
btnDividir.clicked.connect(lambda : calculadora("/"))

btnSete = QPushButton("7", janela)
btnSete.setGeometry(10, 150, tamanhoBotao, tamanhoBotao)
btnSete.clicked.connect(lambda : calculadora("7"))

btnOito = QPushButton("8", janela)
btnOito.setGeometry(80, 150, tamanhoBotao, tamanhoBotao)
btnOito.clicked.connect(lambda : calculadora("8"))

btnNove = QPushButton("9", janela)
btnNove.setGeometry(150, 150, tamanhoBotao, tamanhoBotao)
btnNove.clicked.connect(lambda : calculadora("9"))

btnMulti = QPushButton("X", janela)
btnMulti.setGeometry(220, 150, tamanhoBotao, tamanhoBotao)
btnMulti.setObjectName("botaoDividir")
btnMulti.clicked.connect(lambda : calculadora("*"))

btnQua = QPushButton("4", janela)
btnQua.setGeometry(10, 220, tamanhoBotao, tamanhoBotao)
btnQua.clicked.connect(lambda : calculadora("4"))

btnCin = QPushButton("5", janela)
btnCin.setGeometry(80, 220, tamanhoBotao, tamanhoBotao)
btnCin.clicked.connect(lambda : calculadora("5"))

btnSeis = QPushButton("6", janela)
btnSeis.setGeometry(150, 220, tamanhoBotao, tamanhoBotao)
btnSeis.clicked.connect(lambda : calculadora("6"))

btnMenos = QPushButton("-", janela)
btnMenos.setGeometry(220, 220, tamanhoBotao, tamanhoBotao)
btnMenos.setObjectName("botaoDividir")
btnMenos.clicked.connect(lambda : calculadora("-"))

btnUm = QPushButton("1", janela)
btnUm.setGeometry(10, 290, tamanhoBotao, tamanhoBotao)
btnUm.clicked.connect(lambda : calculadora("1"))

btnDois = QPushButton("2", janela)
btnDois.setGeometry(80, 290, tamanhoBotao, tamanhoBotao)
btnDois.clicked.connect(lambda : calculadora("2"))

btnTres = QPushButton("3", janela)
btnTres.setGeometry(150, 290, tamanhoBotao, tamanhoBotao)
btnTres.clicked.connect(lambda : calculadora("3"))

btnMais = QPushButton("+", janela)
btnMais.setGeometry(220, 290, tamanhoBotao, tamanhoBotao)
btnMais.setObjectName("botaoDividir")
btnMais.clicked.connect(lambda : calculadora("+"))

btnZero = QPushButton("0", janela)
btnZero.setGeometry(10, 360, 130, tamanhoBotao)
btnZero.clicked.connect(lambda : calculadora("0"))

btnVirgula = QPushButton(",", janela)
btnVirgula.setGeometry(150, 360, tamanhoBotao, tamanhoBotao)
btnVirgula.clicked.connect(lambda : calculadora("."))

btnIgual = QPushButton("=", janela)
btnIgual.setGeometry(220, 360, tamanhoBotao, tamanhoBotao)
btnIgual.setObjectName("botaoDividir")
btnIgual.clicked.connect(calcularResultado)


janela.show()
sys.exit((app.exec()))