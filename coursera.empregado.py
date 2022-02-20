class Empregado:
    def __init__(self, nome, CPF, RG):
        self.nome = nome
        self.CPF = CPF
        self.RG = RG

class EmpregadoHorista(Empregado):
    def __init__(self, nome, CPF, RG, horasTrabalhadas, pagamentoPorHora):
        super().__init__(nome, CPF, RG)
        self.horasTrabalhadas = horasTrabalhadas
        self.pagamentoPorHora = pagamentoPorHora

    def pagamento(self):
        return self.horasTrabalhadas * self.pagamentoPorHora 

class EmpregadoCLT(Empregado):
    def __init__(self, nome, CPF, RG, salario):
        super().__init__(nome, CPF, RG)
        self.salario = salario 

    def pagamento(self):
        return 13.3 * self.salario

class PrestadordeServico(Empregado):
    def __init__(self, nome, CPF, RG, pagamentoAvulso):
        super().__init__(nome, CPF, RG)
        self.pagamentoAvulso = pagamentoAvulso

    def pagamento(self):
        return self.pagamentoAvulso 