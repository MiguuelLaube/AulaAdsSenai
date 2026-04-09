class Pessoa:
    def __init__(self, nome=None, idade=None):
        if nome is None:
            nome = input("Digite o nome da pessoa: ") 
        if idade is None:
            idade = int(input("Digite a idade da pessoa: ")) 
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("João", 30)
pessoa1.apresentar()
aluno = Pessoa("Ana", 21)
aluno.apresentar()
pessoa2 = Pessoa()
pessoa2.apresentar()