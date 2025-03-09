# 🧪 Calculadora com PyQt6 em Python

## 📚 Descrição
Este projeto consiste em uma **calculadora gráfica** desenvolvida com **Python** e **PyQt6**, oferecendo uma interface intuitiva e interativa para realizar operações matemáticas básicas.

## 🔢 Funcionalidades
✔️ **Soma (+)**  
✔️ **Subtração (-)**  
✔️ **Multiplicação (X)**  
✔️ **Divisão (/)** (com tratamento de erro para divisão por zero)  
✔️ **Porcentagem (%)**  
✔️ **Alternar sinal (+/-)**  
✔️ **Entrada de números e formatação via interface gráfica**  

---

## 📂 Passo a Passo da Implementação  

### 🔹 1️⃣ Instalar as Dependências  
Antes de iniciar o desenvolvimento, instale o **PyQt6** caso ainda não tenha instalado:  
```bash
pip install PyQt6
```
---

### 🔹 2️⃣ Importar as Bibliotecas  
No início do código, as seguintes bibliotecas são importadas:

```python
import sys  # Para manipulação do sistema e saída do programa
from PyQt6.QtWidgets import *  # Importa todos os componentes do PyQt6
```
📌 A biblioteca `sys` é necessária para gerenciar a execução da aplicação, e `PyQt6.QtWidgets` contém os elementos gráficos usados na interface.  

---

### 🔹 3️⃣ Criar a Aplicação PyQt6  
A aplicação **PyQt6** deve ser inicializada antes de criar a interface:  
```python
app = QApplication(sys.argv)  # Cria a aplicação
```
O **QApplication** é essencial para gerenciar eventos e a interface da calculadora.  

---

### 🔹 4️⃣ Criar a Interface Gráfica  
#### Criando a Janela Principal:  
```python
janela = QWidget()  # Cria a janela principal
janela.resize(290, 450)  # Define o tamanho da janela
janela.setWindowTitle("Calculadora")  # Define o título da janela
```
📌 O **QWidget** é o contêiner principal que suporta os botões e a entrada de texto.  

---

### 🔹 5️⃣ Carregar Estilos do Arquivo CSS  
Para personalizar a aparência da calculadora, um arquivo **CSS externo** pode ser importado:  
```python
with open("style.css", "r") as style_file:
    styles = style_file.read()  # Lê o conteúdo do CSS
janela.setStyleSheet(styles)  # Aplica o estilo na janela
```
📌 Certifique-se de ter um arquivo `style.css` na mesma pasta do código para estilizar a interface.  

---

### 🔹 6️⃣ Criar o Campo de Entrada  
```python
inputCalculadora = QLineEdit("", janela)  # Campo de entrada da calculadora
inputCalculadora.resize(270, 40)
inputCalculadora.move(10, 40)
inputCalculadora.setReadOnly(True)  # Impede que o usuário digite diretamente
```
📌 O **QLineEdit** permite exibir e manipular os números digitados.  

---

### 🔹 7️⃣ Criar os Botões  
Os botões são criados usando **QPushButton** e conectados às funções:  
```python
btnAC = QPushButton("AC", janela)
btnAC.setGeometry(10, 80, 60, 60)
btnAC.setObjectName("botaoAC")
btnAC.clicked.connect(limpar)
```
📌 Cada botão é posicionado com `setGeometry(x, y, largura, altura)` e vinculado a uma função com `clicked.connect(funcao)`.  

---

### 🔹 8️⃣ Definir Funções para os Botões  
As funções principais incluem:  

✅ **Limpar a tela:**  
```python
def limpar():
    inputCalculadora.setText("")
    lista.clear()
```
✅ **Executar cálculos com `eval()`:**  
```python
def calcularResultado():
    try:
        conteudoInput = inputCalculadora.text()
        resultado = eval(conteudoInput)  # Avalia a expressão matemática
        inputCalculadora.setText(str(resultado))
    except Exception:
        inputCalculadora.setText("Error")
```
📌 A função `eval()` interpreta a string como uma expressão matemática, permitindo cálculos dinâmicos.  

---

### 🔹 9️⃣ Exibir a Janela  
No final do código, chamamos `show()` para exibir a interface:  
```python
janela.show()
sys.exit(app.exec())  # Mantém a aplicação rodando até ser fechada
```
📌 O `sys.exit(app.exec())` garante que a aplicação continue em execução até o usuário fechá-la.  

---

## 🚀 Como Executar o Projeto  
1️⃣ Certifique-se de ter o **Python 3.x** instalado.  
2️⃣ Instale a biblioteca **PyQt6** com:  
   ```bash
   pip install PyQt6
   ```
3️⃣ Salve o código como `calculadora.py` e execute:  
   ```bash
   python calculadora.py
   ```
4️⃣ A calculadora abrirá com a interface gráfica funcionando corretamente! 🎉  

---

## 📀 Melhorias Futuras  
🔹 Adicionar suporte para **teclado físico**.  
🔹 Criar um **histórico de cálculos**.  
🔹 Implementar **atalhos de teclado** para operações rápidas.  

---

📌 *Este projeto pode ser expandido conforme necessário!*  

