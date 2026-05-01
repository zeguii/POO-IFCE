# Herança e Sobrescrita/Sobreposição do método construtor (Override)
class Funcionario:
    def __init__(self, cargo, nome, salario):
        self._cargo = cargo
        self._nome = nome
        self._salario = salario

class Analista(Funcionario):
    def __init__(self, nome, salario):
        super().__init__("Analista", nome, salario)
        self.certificacoes = []
        self._chamados = []

class Caixa(Funcionario):
    def __init__(self, nome, salario):
        super().__init__("Caixa", nome, salario)
        self.guiche = None
        self._turno_atendimento = None
        self._limite_operacao = None
        self.__meta_anual = None

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__("Gerente", nome, salario)
        self._equipe = []
        self._meta_anual = None
        self.__clientes_vip = []
        self.__bonus = None