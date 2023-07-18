class Pessoa:
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade 
        self.cpf = cpf
        
    def apresentar(self):
        print("Olá, meu nome é: ", self.nome)
        
    def envelhecer(self,anos):
        self.idade += anos
        
    def mostrarcpf(self):
        print("Este é o meu cpf: ", self.cpf)
    
        
pessoal = Pessoa("Danilo", 18, '538743513')

pessoal.apresentar()
pessoal.envelhecer(5)
