from passageiro import Passageiro

class Topic():

    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade
        self.qtdPrioritarios = qtdPrioritarios
        self.assentosNormais = []
        self.assentosPrioritarios = []
        self.vagasDisponiveis = self.capacidade - (len(self.assentosPrioritarios) + len(self.assentosNormais))

    def getNumeroAssentosPrioritarios(self):
        return self.qtdPrioritarios

    def getNumeroAssentosNormais(self):
        return self.capacidade - self.qtdPrioritarios

    def getPassageiroAssentoNormal(self, lugar):
        if len(self.assentosNormais) == 0:
            return None
        return self.assentosNormais[lugar]

    def getPassageiroAssentoPrioritario(self, lugar):
        if len(self.assentosPrioritarios) == 0:
            return None
        return self.assentosPrioritarios[lugar]

    def getVagas(self):
        return self.vagasDisponiveis

    def subir(self, passageiro: Passageiro):
        if self.getVagas() > 0:
            if passageiro.ePrioridade():
                if self.getNumeroAssentosPrioritarios() > len(self.assentosPrioritarios):
                    self.assentosPrioritarios.append(passageiro)
                    self.vagasDisponiveis -= 1
                    return True
                else:
                    self.assentosNormais.append(passageiro)
                    self.vagasDisponiveis -= 1
                    return True
            else:
                if self.getNumeroAssentosNormais() > len(self.assentosNormais):
                    self.assentosNormais.append(passageiro)
                    self.vagasDisponiveis -= 1
                    return True
                else:
                    self.assentosPrioritarios.append(passageiro)
                    self.vagasDisponiveis -= 1
                    return True
        return False

    def descer(self, nome):
        for passageiroPrioritario in self.assentosPrioritarios:
            if passageiroPrioritario.getNome() == nome:
                self.assentosPrioritarios.remove(passageiroPrioritario)
                self.vagasDisponiveis += 1
                return True

        for passageiroNormal in self.assentosNormais:
            if passageiroNormal.getNome() == nome:
                self.assentosNormais.remove(passageiroNormal)
                self.vagasDisponiveis += 1
                return True
        return False

    def toString(self):
        topic = '['
        for passageiroPrioritario in self.assentosPrioritarios:
            topic += '@' + passageiroPrioritario.getNome() + ' '
        topic += '@ ' * (self.qtdPrioritarios - len(self.assentosPrioritarios))

        for passageiroNormal in self.assentosNormais:
            topic += '=' + passageiroNormal.getNome() + ' '
        topic += '= ' * (self.getNumeroAssentosNormais() - len(self.assentosNormais))
        return topic + ']'