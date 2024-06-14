import streamlit as st
st.title(":rainbow[Calculadora]")
n1 = st.number_input("Primeiro número:")
n2 = st.number_input("Segundo número: ")
def soma(n1, n2 ):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

def potencia(n1,n2):
    return n1 ** n2

def modulo(n1,n2):
    return n1 // n2

op = st.radio(
    "Escolha uma operação:",
    [":rainbow[Adição]", ":rainbow[Subtração]", ":rainbow[Multiplicação]", ":rainbow[Divisão]", ":rainbow[Potenciação]", ":rainbow[Módulo]"],
)
if st.button("Calcular"):
    resultado = float
    if op == ":rainbow[Adição]":
        resultado = soma(n1, n2)
    elif op == ":rainbow[Subtração]":
        resultado = subtracao(n1, n2)
    elif op == ":rainbow[Multiplicação]":
        resultado = multiplicacao(n1, n2)
    elif op == ":rainbow[Divisão]":
        resultado = divisao(n1, n2)
    elif op == ":rainbow[Potenciação]":
        resultado = potencia(n1, n2)
    elif op == ":rainbow[Módulo]":
        resultado = modulo(n1,n2)
    st.write('Resultado: ',resultado)
