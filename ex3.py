class Calculadora:
    def adicionar(self, a, b):
        return a + b
    def subtrair(self, a, b):
        return a - b
    def multiplicar(self, a, b):
        return a * b
    def dividir(self, a, b):
        if b != 0: 
            return a / b
        else:
            return "Erro: Divisão por zero não é permitida."
    
calc = Calculadora()
print(calc.adicionar(5, 3))   # Saída: 8
print(calc.subtrair(5, 3))    # Saída: 2
print(calc.multiplicar(5, 3)) # Saída: 15
print(calc.dividir(5, 3))     # Saída: 1.666...
print(calc.dividir(5, 0))     # Saída: Erro: Divisão por zero não é permitida.