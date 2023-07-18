class Aluno:
    def __init__(self,primeira,segunda, terceira,nome):
        self.nome = nome
        self.primeira = primeira 
        self.segunda = segunda
        self.terceira = terceira
        
    def verificar(self):
        media = (self.primeira + self.segunda + self.terceira)/3
        if media >= 7:
            print("Aluno aprovado")
            
        else: 
            print("Aluno reprovado")
