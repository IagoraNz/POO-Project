import os
import tkinter as tk
import abc

#Class aeroporto
#HERDAM DE AEROPORTO
#Class terminal
#Class portao
#Class pista(s) de pouso
#Class cias aereas
#HERDAM DE CIAS AEREAS
#Class aviao
#Class voo
#Class passageiro
#Class reserva
#Class bagagem

#Class Funcionario
#HERDAM DE FUNCIONARIO
#Class piloto
#Class comissario
#Class atendente
#Class gerente

#Implementação das classes e funcionalidades com tkinter
class Aeroporto():
    def __init__(self, nome, cidade, sigla):
        self.nome = nome
        self.cidade = cidade
        self.sigla = sigla
    
    @property
    def nome(self):
        return self.nome

    @nome.setter
    def set_nome(self, nome):
        self.nome = nome

    @property
    def cidade(self):
        return self.cidade
    
    @cidade.setter
    def set_cidade(self, cidade):
        self.cidade = cidade

    @property
    def sigla(self):
        return self.sigla
    
    @sigla.setter
    def set_sigla(self, sigla):
        self.sigla = sigla

class Terminal():
    def __init__(self, numero):
        self.numero = numero

    @property
    def numero(self):
        return self.numero
    
    @numero.setter
    def set_numero(self, numero):
        self.numero = numero

class Portao():
    def __init__(self, numero, terminal):
        self.numero = numero
        self.terminal = terminal

    @property
    def numero(self):
        return self.numero
    
    @numero.setter
    def set_numero(self, numero):
        self.numero = numero
        
    @property
    def terminal(self):
        return self.terminal
    
    @terminal.setter
    def set_terminal(self, terminal):
        self.terminal = terminal

class Pista():
    def __init__(self, numero, direcao, tamanho):
        self.numero = numero
        self.direcao = direcao
        self.tamanho = tamanho

    @property
    def numero(self):
        return self.numero
    
    @numero.setter
    def set_numero(self, numero):
        self.numero = numero

    @property
    def direcao(self):
        return self.direcao
    
    @direcao.setter
    def set_direcao(self, direcao):
        self.direcao = direcao

    @property
    def tamanho(self):
        return self.tamanho
    
    @tamanho.setter
    def set_tamanho(self, tamanho):
        self.tamanho = tamanho

class CiaAerea():
    def __init__(self, nome, sigla, pais, quantidade_avioes):
        self.nome = nome
        self.sigla = sigla
        self.pais = pais
        self.quantidade_avioes = quantidade_avioes

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def set_nome(self, nome):
        self.nome = nome

    @property
    def sigla(self):
        return self.sigla
    
    @sigla.setter
    def set_sigla(self, sigla):
        self.sigla = sigla

    @property
    def pais(self):
        return self.pais
    
    @pais.setter
    def set_pais(self, pais):
        self.pais = pais

    @property
    def quantidade_avioes(self):
        return self.quantidade_avioes
    
    @quantidade_avioes.setter
    def set_quantidade_avioes(self, quantidade_avioes):
        self.quantidade_avioes = quantidade_avioes

class Aviao():
    def __init__(self, modelo, quantidade_assentos, quantidade_bagagens, siglaVoo):
        self.modelo = modelo
        self.quantidade_assentos = quantidade_assentos
        self.quantidade_bagagens = quantidade_bagagens
        self.siglaVoo = siglaVoo

    @property
    def modelo(self):
        return self.modelo
    
    @modelo.setter
    def set_modelo(self, modelo):
        self.modelo = modelo

    @property
    def quantidade_assentos(self):
        return self.quantidade_assentos
    
    @quantidade_assentos.setter
    def set_quantidade_assentos(self, quantidade_assentos):
        self.quantidade_assentos = quantidade_assentos

    @property
    def quantidade_bagagens(self):
        return self.quantidade_bagagens
    
    @quantidade_bagagens.setter
    def quantidade_bagagens(self, quantidade_bagagens):
        self.quantidade_bagagens = quantidade_bagagens

    @property
    def siglaVoo(self):
        return self.siglaVoo

    @siglaVoo.setter
    def set_siglaVoo(self, siglaVoo):
        self.siglaVoo = siglaVoo

class Voo():
    def __init__(self, sigla, origem, destino, data, hora, aviao):
        self.sigla = sigla
        self.origem = origem
        self.destino = destino
        self.data = data
        self.hora = hora
        self.aviao = aviao

    @property
    def sigla(self):
        return self.sigla
    
    @sigla.setter
    def set_sigla(self, sigla):
        self.sigla = sigla

    @property
    def origem(self):
        return self.origem
    
    @origem.setter
    def set_origem(self, origem):
        self.origem = origem

    @property
    def destino(self):
        return self.destino
    
    @destino.setter
    def set_destino(self, destino):
        self.destino = destino

    @property
    def data(self):
        return self.data
    
    @data.setter
    def set_data(self, data):
        self.data = data

    @property
    def hora(self):
        return self.hora
    
    @hora.setter
    def set_hora(self, hora):
        self.hora = hora

    @property
    def aviao(self):
        return self.aviao
    
    @aviao.setter
    def set_aviao(self, aviao):
        self.aviao = aviao

class Passageiro():
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def set_nome(self, nome):
        self.nome = nome

    @property
    def cpf(self):
        return self.cpf
    
    @cpf.setter
    def set_cpf(self, cpf):
        self.cpf = cpf

    @property
    def telefone(self):
        return self.telefone
    
    @telefone.setter
    def set_telefone(self, telefone):
        self.telefone = telefone

class Reserva():
    def __init__(self, cpfpass, voo, assento, bagagem):
        self.cpfpass = cpfpass
        self.voo = voo
        self.assento = assento
        self.bagagem = bagagem

    @property
    def cpfpass(self):
        return self.cpfpass
    
    @cpfpass.setter
    def set_cpfpass(self, cpfpass):
        self.cpfpass = cpfpass

    @property
    def voo(self):
        return self.voo
    
    @voo.setter
    def set_voo(self, voo):
        self.voo = voo

    @property
    def assento(self):
        return self.assento
    
    @assento.setter
    def set_assento(self, assento):
        self.assento = assento

    @property
    def bagagem(self):
        return self.bagagem
    
    @bagagem.setter
    def set_bagagem(self, bagagem):
        self.bagagem = bagagem

class Bagagem():
    def __init__(self, peso, dimensoes):
        self.peso = peso
        self.dimensoes = dimensoes

    @property
    def peso(self):
        return self.peso
    
    @peso.setter
    def set_peso(self, peso):
        self.peso = peso

    @property
    def dimensoes(self):
        return self.dimensoes
    
    @dimensoes.setter
    def set_dimensoes(self, dimensoes):
        self.dimensoes = dimensoes

class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario, senha):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.senha = senha

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def set_nome(self, nome):
        self.nome = nome

    @property
    def cpf(self):
        return self.cpf
    
    @cpf.setter
    def set_cpf(self, cpf):
        self.cpf = cpf

    @property
    def salario(self):
        return self.salario
    
    @salario.setter
    def set_salario(self, salario):
        self.salario = salario

    @property
    def senha(self):
        return self.senha
    
    @senha.setter
    def set_senha(self, senha):
        self.senha = senha

class Piloto(Funcionario):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario, senha)

class Comissario(Funcionario):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario, senha)

class Atendente(Funcionario):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario, senha)

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario, senha)

class Usuario():
    def __init__(self, senha):
        self.senha = senha

    @property
    def senha(self):
        return self.senha
    
    @senha.setter
    def set_senha(self, senha):
        self.senha = senha

class Controle_Autenticacao():
    def __init__(self):
        pass

    def autentica(self, f, senha):
        if isinstance(f, Funcionario):
            return "Login Feito com Sucesso" if f.autenticar(senha) == True else "Senha incorreta"
        else:
            return "Usuário não é um funcionário"