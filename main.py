import os
import abc

class Autenticavel(abc.ABC):
    @abc.abstractmethod
    def autenticar(self, senha):
        pass

class Voo():
    def __init__(self, sigla, origem, destino, aviao, piloto, comissarios):
        self._sigla = sigla
        self._origem = origem
        self._destino = destino
        self._aviao = aviao
        self._assentos = []
        self._reservados = []
        self._piloto = piloto
        self._comissarios = comissarios

    @property
    def sigla(self):
        return self._sigla
    
    @sigla.setter
    def set_sigla(self, sigla):
        self._sigla = sigla

    @property
    def origem(self):
        return self._origem
    
    @origem.setter
    def set_origem(self, origem):
        self._origem = origem

    @property
    def destino(self):
        return self._destino
    
    @destino.setter
    def set_destino(self, destino):
        self._destino = destino

    @property
    def aviao(self):
        return self._aviao
    
    @aviao.setter
    def set_aviao(self, aviao):
        self._aviao = aviao

    def add_assento(self):
        for i in range(int(self._aviao.quantidade_assentos)):
            self._assentos.append(i)

    def reservar_assento(self, assento):
        if assento in self._assentos:
            self._assentos.remove(assento)
            self._reservados.append(assento)
            return True, "Assento reservado com sucesso!"
        return False, "Assento indisponível!"

    def cancelar_reserva(self, assento):
        if assento in self._reservados:
            self._assentos.append(assento)
            self._reservados.remove(assento)
            self._assentos.sort()
            return True, "Reserva cancelada com sucesso!"
        return False, "Assento não reservado!"
    
    def listar_disp(self):
        print("Assentos disponíveis:")
        print(self._assentos)

    def listar_reservados(self):
        print("Assentos reservados:")
        print(self._reservados)

class Aviao():
    def __init__(self, modelo, quantidade_assentos, siglaav):
        self._modelo = modelo
        self._quantidade_assentos = quantidade_assentos
        self._siglaav = siglaav

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def set_modelo(self, modelo):
        self._modelo = modelo

    @property
    def quantidade_assentos(self):
        return self._quantidade_assentos
    
    @quantidade_assentos.setter
    def set_quantidade_assentos(self, quantidade_assentos):
        self._quantidade_assentos = quantidade_assentos

    @property
    def siglaav(self):
        return self._siglaav

    @siglaav.setter
    def set_siglaav(self, siglaav):
        self._siglaav = siglaav

class Passageiro():
    def __init__(self, nome, cpf, telefone):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def set_nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def set_cpf(self, cpf):
        self._cpf = cpf

    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def set_telefone(self, telefone):
        self._telefone = telefone

class Funcionario():
    def __init__(self, nome, cpf, salario, senha):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._senha = senha

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def set_nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def set_cpf(self, cpf):
        self._cpf = cpf

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def set_salario(self, salario):
        self._salario = salario

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def set_senha(self, senha):
        self._senha = senha

class Piloto(Funcionario):
    def __init__(self, nome, cpf, salario, senha, horas_voo):
        super().__init__(nome, cpf, salario, senha)
        self._horas_voo = horas_voo

    @property
    def horas_voo(self):
        return self._horas_voo
    
    @horas_voo.setter
    def set_horas_voo(self, horas_voo):
        self._horas_voo = horas_voo

    @abc.abstractmethod
    def autenticar(self, senha):
        if senha == self._senha:
            return True, "Senha correta"
        return False, "Senha incorreta"

class Comissario(Funcionario):
    def __init__(self, nome, cpf, salario, senha, idiomas):
        super().__init__(nome, cpf, salario, senha)
        self._idiomas = idiomas

    @property
    def idiomas(self):
        return self._idiomas
    
    @idiomas.setter
    def set_idiomas(self, idiomas):
        self._idiomas = idiomas

    @abc.abstractmethod
    def autenticar(self, senha):
        if senha == self._senha:
            return True
        return False

class Atendente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, terminal):
        super().__init__(nome, cpf, salario, senha)
        self._terminal = terminal

    @property
    def terminal(self):
        return self._terminal
    
    @terminal.setter
    def set_terminal(self, terminal):
        self._terminal = terminal
    
    @abc.abstractmethod
    def autenticar(self, senha):
        if senha == self._senha:
            return True, "Senha correta"
        return False, "Senha incorreta"

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, expediente):
        super().__init__(nome, cpf, salario, senha)
        self._expediente = expediente

    @property
    def expediente(self):
        return self._expediente
    
    @expediente.setter
    def set_expediente(self, expediente):
        self._expediente = expediente
    
    @abc.abstractmethod
    def autenticar(self, senha):
        if senha == self._senha:
            return True, "Senha correta"
        return False, "Senha incorreta"

class ControleAutenticacao():
    def __init__(self):
        pass

    def acessoPiloto(self, piloto, senha):
        if isinstance(piloto, Piloto):
            booleano, mensagem = piloto.autenticar(senha)
            return booleano, mensagem
        return False, "Piloto inválido!"
    
    def acessoComissario(self, comissario, senha):
        if isinstance(comissario, Comissario):
            return comissario.autenticar(senha), "Acesso permitido!"
        return False, "Comissário inválido!"
    
    def acessoAtendente(self, atendente, senha):
        if isinstance(atendente, Atendente):
            booleano, mensagem = atendente.autenticar(senha)
            return booleano, mensagem
        return False, "Atendente inválido!"
    
    def acessoGerente(self, gerente, senha):
        if isinstance(gerente, Gerente):
            booleano, mensagem = gerente.autenticar(senha)
            return booleano, mensagem
        return False, "Gerente inválido!"

class CiaAerea():
    def __init__(self, nome, cnpj, telefone, endereco):
        self._nome = nome
        self._cnpj = cnpj
        self._telefone = telefone
        self._endereco = endereco
        self._avioes = {}
        self._voos = {}
        self._passageiros = {}
        self._funcionarios = {}

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def set_nome(self, nome):
        self._nome = nome

    @property
    def cnpj(self):
        return self._cnpj
    
    @cnpj.setter
    def set_cnpj(self, cnpj):
        self._cnpj = cnpj

    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def set_telefone(self, telefone):
        self._telefone = telefone

    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def set_endereco(self, endereco):
        self._endereco = endereco

    def add_aviao(self, aviao):
        if isinstance(aviao, Aviao):
            if aviao._siglaav not in self._avioes.keys():
                self._avioes[aviao.siglaav] = aviao
                return True, "Avião cadastrado com sucesso!"
            else:
                return False, "Avião já cadastrado!"
        return False, "Avião inválido!"

    def alterar_aviao(self, sigla):
        if sigla in self._avioes.keys():
            print("Avião encontrado!")
            print("Qual dado deseja alterar?: ")
            print("1. Modelo")
            print("2. Quantidade de assentos")
            print("3. Cancelar")
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao < 1 or opcao > 3:
                    raise ValueError
            except ValueError:
                return False, "Opção inválida!"

            if opcao == 1:
                modelo = input("Modelo: ")
                self._avioes[sigla]._modelo = modelo
                return True, "Modelo alterado com sucesso!"
            elif opcao == 2:
                quantidade_assentos = input("Quantidade de assentos: ")
                self._avioes[sigla]._quantidade_assentos = quantidade_assentos
                return True, "Quantidade de assentos alterada com sucesso!"
            elif opcao == 3:
                return False, "Operação cancelada!"
            else:
                return False, "Opção inválida!"
        return False, "Avião não encontrado!"
    
    def excluir_aviao(self, sigla):
        if sigla in self._avioes.keys():
            del self._avioes[sigla]
            return True, "Avião excluído com sucesso!"
        return False, "Avião não encontrado!"
    
    def listar_avioes(self):
        print("\nAVIÕES:")
        print(f"{'SIGLA':<10}{'MODELO':<20}{'QUANTIDADE DE ASSENTOS':<10}")
        for sigla, aviao in self._avioes.items():
            sigla_str = str(sigla)
            modelo_str = str(aviao.modelo)
            quantidade_assentos_str = str(aviao.quantidade_assentos)
            print(f"{sigla_str:<10}{modelo_str:<20}{quantidade_assentos_str:<10}")
        print("\n")

    def add_voo(self, voo):
        if isinstance(voo, Voo):
            if voo.sigla not in self._voos:
                self._voos[voo.sigla] = voo
                return True, "Voo cadastrado com sucesso!"
            else:
                return False, "Voo já cadastrado!"
        return False, "Voo inválido!"
    
    def alterar_voo(self, sigla):
        if sigla in self._voos.keys():
            print("Voo encontrado!")
            print("Qual dado deseja alterar?: ")
            print("1. Origem")
            print("2. Destino")
            print("3. Avião")
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao < 1 or opcao > 3:
                    raise ValueError
            except ValueError:
                return False, "Opção inválida!"

            if opcao == 1:
                origem = input("Origem: ")
                self._voos[sigla]._origem = origem
                return True, "Origem alterada com sucesso!"
            elif opcao == 2:
                destino = input("Destino: ")
                self._voos[sigla]._destino = destino
                return True, "Destino alterado com sucesso!"
            elif opcao == 3:
                aviao = input("Já possui avião cadastrado? (sim/não): ").lower()
                if aviao == 'sim':
                    cont = 0
                    for i in range(3):
                        siglaav = input("Digite a sigla do avião: ")
                        if siglaav in self._avioes.keys():
                            aviao = self._avioes[siglaav]
                            break
                        else:
                            print("Avião não encontrado! Cadastre primeiro.")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        print("3 tentativas falhas! Tente novamente...")
                else:
                    modelo = input("Modelo: ")
                    # <- Quantidade de assentos ->
                    cont = 0
                    for i in range(3):
                        try:
                            quantidade_assentos = int(input("Quantidade de assentos: "))
                            if quantidade_assentos < 0:
                                raise ValueError
                            break
                        except ValueError:
                            print("Quantidade inválida! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        return False, "3 tentativas falhas! Tente novamente..."

                    # <- Sigla ->
                    cont = 0
                    for i in range(3):
                        try:
                            siglaav = input("Sigla do avião: ")
                            if siglaav in self._avioes.keys():
                                raise ValueError
                            break
                        except ValueError:
                            print("Sigla inválida ou já existe! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        return False, "3 tentativas falhas! Tente novamente..."
                    aviao = Aviao(modelo, quantidade_assentos, quantidade_bagagens, sigla)
                self._voos[sigla]._aviao = aviao
                return True, "Avião alterado com sucesso!"
            else:
                return False, "Opção inválida!"
        return False, "Voo não encontrado!"
    
    def excluir_voo(self, sigla):
        if sigla in self._voos.keys():
            del self._voos[sigla]
            return True, "Voo excluído com sucesso!"
        return False, "Voo não encontrado!"

    def listar_voos(self):
        print("\nVOOS:")
        print(f"{'SIGLA':<10}{'ORIGEM':<20}{'DESTINO':<20}{'AVIÃO':<10}")
        for sigla, voo in self._voos.items():
            sigla_str = str(sigla)
            origem_str = str(voo.origem)
            destino_str = str(voo.destino)
            aviao_sigla_str = str(voo.aviao.siglaav)
            print(f"{sigla_str:<10}{origem_str:<20}{destino_str:<20}{aviao_sigla_str:<10}")
        print("\n")

    def add_passageiro(self, passageiro):
        if isinstance(passageiro, Passageiro):
            if passageiro.cpf not in self._passageiros:
                self._passageiros[passageiro.cpf] = passageiro
                return True, "Passageiro cadastrado com sucesso!"
            else:
                return False, "Passageiro já cadastrado!"
        return False, "Passageiro inválido!"
    
    def alterar_passageiro(self, cpf):
        if cpf in self._passageiros.keys():
            print("Passageiro encontrado!")
            print("Qual dado deseja alterar?: ")
            print("1. Nome")
            print("2. Telefone")
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao < 1 or opcao > 2:
                    raise ValueError
            except ValueError:
                return False, "Opção inválida!"

            if opcao == 1:
                nome = input("Nome: ")
                self._passageiros[cpf]._nome = nome
                return True, "Nome alterado com sucesso!"
            elif opcao == 2:
                telefone = input("Telefone: ")
                self._passageiros[cpf]._telefone = telefone
                return True, "Telefone alterado com sucesso!"
            else:
                return False, "Opção inválida!"
        return False, "Passageiro não encontrado!"
    
    def excluir_passageiro(self, cpf):
        if cpf in self._passageiros.keys():
            del self._passageiros[cpf]
            return True, "Passageiro excluído com sucesso!"
        return False, "Passageiro não encontrado!"
    
    def listar_passageiros(self):
        print("\nPASSAGEIROS")
        print(f"{'CPF':<15}{'NOME':<20}{'TELEFONE':<15}")
        for cpf, passageiro in self._passageiros.items():
            cpf_str = str(cpf)
            nome_str = str(passageiro.nome)
            telefone_str = str(passageiro.telefone)
            print(f"{cpf_str:<15}{nome_str[:20]:<20}{telefone_str:<15}")
        print("\n")

    def add_funcionario(self, funcionario):
        if isinstance(funcionario, Funcionario):
            if funcionario.cpf not in self._funcionarios:
                self._funcionarios[funcionario.cpf] = funcionario
                return True, "Funcionário cadastrado com sucesso!"
            else:
                return False, "Funcionário já cadastrado!"
        return False, "Funcionário inválido!"
    
    def alterar_funcionario(self, cpf):
        if cpf in self._funcionarios.keys():
            print("Funcionário encontrado!")
            print("Qual dado deseja alterar?: ")
            print("1. Nome")
            print("2. Salário")
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao < 1 or opcao > 2:
                    raise ValueError
            except ValueError:
                return False, "Opção inválida!"

            if opcao == 1:
                nome = input("Nome: ")
                self._funcionarios[cpf]._nome = nome
                return True, "Nome alterado com sucesso!"
            elif opcao == 2:
                salario = input("Salário: ")
                self._funcionarios[cpf]._salario = salario
                return True, "Salário alterado com sucesso!"
            else:
                return False, "Opção inválida!"
        return False, "Funcionário não encontrado!"
    
    def excluir_funcionario(self, cpf):
        if cpf in self._funcionarios.keys():
            del self._funcionarios[cpf]
            return True, "Funcionário excluído com sucesso!"
        return False, "Funcionário não encontrado!"
    
    def listar_funcionarios(self):
        print("\nFUNCIONÁRIOS")
        print(f"{'CPF':<15}{'NOME':<20}{'SALÁRIO':<10}")
        for cpf, funcionario in self._funcionarios.items():
            cpf_str = str(cpf)
            nome_str = str(funcionario.nome)
            salario_str = str(funcionario.salario)
            print(f"{cpf_str:<15}{nome_str[:20]:<20}{salario_str:<10}")

    def listar_pilotos(self):
        valido = False
        for cpf, funcionario in self._funcionarios.items():
            if isinstance(funcionario, Piloto):
                valido = True
                break
        if not valido:
            return False, "Não há pilotos cadastrados!"
        print("\nPILOTOS")
        print(f"{'CPF':<15}{'NOME':<20}{'SALÁRIO':<10}{'HORAS DE VOO':<10}")
        for cpf, funcionario in self._funcionarios.items():
            if isinstance(funcionario, Piloto):
                cpf_str = str(cpf)
                nome_str = str(funcionario.nome)
                salario_str = str(funcionario.salario)
                horas_voo_str = str(funcionario.horas_voo)
                print(f"{cpf_str:<15}{nome_str[:20]:<20}{salario_str:<10}{horas_voo_str:<10}")
        return True, "Pilotos listados com sucesso!"

    def listar_comissarios(self):
        valido = False
        for cpf, funcionario in self._funcionarios.items():
            if isinstance(funcionario, Comissario):
                valido = True
                break
        if not valido:
            return False, "Não há comissários cadastrados!"
        print("\nCOMISSÁRIOS")
        print(f"{'CPF':<15}{'NOME':<20}{'SALÁRIO':<10}{'IDIOMAS':<10}")
        for cpf, funcionario in self._funcionarios.items():
            if isinstance(funcionario, Comissario):
                cpf_str = str(cpf)
                nome_str = str(funcionario.nome)
                salario_str = str(funcionario.salario)
                idiomas_str = str(funcionario.idiomas)
                print(f"{cpf_str:<15}{nome_str[:20]:<20}{salario_str:<10}{idiomas_str:<10}")
        return True, "Comissários listados com sucesso!"

    def listar_atendentes(self):
        valido = False
        for cpf, funcionario in self._funcionarios.items():
            if isinstance(funcionario, Atendente):
                valido = True
                break
        if not valido:
            return False, "Não há atendentes cadastrados!"
        print("\nATENDENTES")
        print(f"{'CPF':<15}{'NOME':<20}{'SALÁRIO':<10}{'TERMINAL':<10}")
        for cpf, funcionario in self._funcionarios.items():
            if isinstance(funcionario, Atendente):
                cpf_str = str(cpf)
                nome_str = str(funcionario.nome)
                salario_str = str(funcionario.salario)
                terminal_str = str(funcionario.terminal)
                print(f"{cpf_str:<15}{nome_str[:20]:<20}{salario_str:<10}{terminal_str:<10}")
        return True, "Atendentes listados com sucesso!"

    def listar_gerentes(self):
        valido = False
        for cpf, funcionario in self._funcionarios.items():
            if isinstance(funcionario, Gerente):
                valido = True
                break
        if not valido:
            return False, "Não há gerentes cadastrados!"
        print("\nGERENTES")
        print(f"{'CPF':<15}{'NOME':<20}{'SALÁRIO':<10}{'EXPEDIENTE':<10}")
        for cpf, funcionario in self._funcionarios.items():
            if isinstance(funcionario, Gerente):
                cpf_str = str(cpf)
                nome_str = str(funcionario.nome)
                salario_str = str(funcionario.salario)
                expediente_str = str(funcionario.expediente)
                print(f"{cpf_str:<15}{nome_str[:20]:<20}{salario_str:<10}{expediente_str:<10}")
        return True, "Gerentes listados com sucesso!"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def lertxt():
    if os.path.exists('cia.txt'):
        with open('cia.txt', 'r') as f:
            nome = f.readline().strip()
            cnpj = f.readline().strip()
            telefone = f.readline().strip()
            endereco = f.readline().strip()
            cia = CiaAerea(nome, cnpj, telefone, endereco)
    else:
        clear()
        print("Bem-vindo ao sistema de gerenciamento de companhias aéreas!")
        print("Para começar, preencha os dados da companhia aérea.")
        nome = input("Nome: ")
        cnpj = input("CNPJ: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")
        cia = CiaAerea(nome, cnpj, telefone, endereco)
        
        with open('cia.txt', 'w') as f:
            f.write(f"{cia.nome}\n{cia.cnpj}\n{cia.telefone}\n{cia.endereco}")

    return cia

ca = ControleAutenticacao()

def main():
    clear()
    cia = lertxt()

    while True:
        clear()
        print(f"\nBem-vindo à {cia.nome}!")
        print("1. Gerenciar voos")
        print("2. Gerenciar aviões")
        print("3. Gerenciar passageiros")
        print("4. Gerenciar funcionários")
        print("5. Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao < 1 or opcao > 5: 
                raise ValueError
        except ValueError:
            input("Opção inválida! Tente novamente...")
            continue

        # Gerenciar voos
        if opcao == 1:
            if not cia._funcionarios.keys():
                input("Não existe funcionários cadastrados! Cadastre primeiro...")
                continue
            p = 0
            c = 0
            for key in cia._funcionarios.keys():
                if isinstance(cia._funcionarios[key], Piloto):
                    p = 1
                if isinstance(cia._funcionarios[key], Comissario):
                    c = 1
            if c == 0 or p == 0:
                input("Deve haver ao menos 1 piloto e 1 comissário para essa área! Cadastre primeiro...")
                continue

            while True:
                clear()
                print("\nGerenciar voos")
                print("1. Cadastrar voo")
                print("2. Alterar voo")
                print("3. Excluir voo")
                print("4. Listar voos")
                print("5. Realizar voo")
                print("6. Reservar assento")
                print("7. Cancelar reserva")
                print("0. Voltar")
                try:
                    opcao = int(input("Escolha uma opção: "))
                    if opcao < 0 or opcao > 7: 
                        raise ValueError
                except ValueError:
                    input("Opção inválida! Tente novamente...")
                    continue

                # Cadastrar voo
                if opcao == 1:
                    comissarios = []
                    print("Cadastrar voo")
                    # Autenticar o gerente
                    cont = 0
                    for i in range(3):
                        try:
                            cpf = int(input("CPF do Gerente: "))
                            senha = input("Senha: ")
                            if cpf not in cia._funcionarios.keys():
                                raise KeyError
                            gerente = cia._funcionarios[cpf]
                            booleano, _ = ca.acessoGerente(gerente, senha)
                            if booleano == False:
                                raise ValueError
                            break
                        except ValueError:
                            print("Senha inválida! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                        except KeyError:
                            print("Gerente não encontrado! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue

                    # <- Sigla ->
                    cont = 0
                    for i in range(3):
                        try:
                            sigla = input("Sigla: ")
                            if sigla in cia._voos.keys(): 
                                raise ValueError
                            break
                        except ValueError:
                            print("Sigla inválida ou já existe! Tente novamente...")
                            if i == 2: 
                                cont = 1
                            continue
                    if cont == 1: 
                        input("3 tentativas falhas! Tente novamente..."); 
                        continue

                    # <- Origem ->
                    cont = 0
                    for i in range(3):
                        try:
                            origem = str(input("Origem: "))
                            if any(char.isdigit() for char in origem):
                                raise ValueError
                            break
                        except ValueError:
                            print("Origem inválida! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    
                    # <- Destino ->
                    cont = 0
                    for i in range(3):
                        try:
                            destino = str(input("Destino: "))
                            if any(char.isdigit() for char in destino):
                                raise ValueError
                            break
                        except ValueError:
                            print("Destino inválido! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    
                    # <- Piloto ->
                    cont = 0
                    for i in range(3):
                        try:
                            cpfpiloto = int(input("CPF do piloto: "))
                            if cpfpiloto not in cia._funcionarios.keys():
                                raise KeyError
                            break
                        except ValueError:
                            print("Piloto inválido! Tente novamente.")
                            if i == 2:
                                cont = 1
                            continue
                        except KeyError:
                            print("Piloto não encontrado! Cadastre ou tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue

                    # <- Quantidade de comissários ->
                    cont = 0
                    for i in range(3):
                        try:
                            quantcomissarios = int(input("Quantidade de comissários: "))
                            if quantcomissarios < 0:
                                raise ValueError
                            break
                        except ValueError:
                            print("Quantidade inválida! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue

                    # <- Comissários ->
                    cont = 0
                    for i in range(3):
                        try:
                            for j in range(quantcomissarios):
                                try:
                                    cpfcomissario = int(input(f"Comissário {j + 1}: "))
                                    if not isinstance(cia._funcionarios[cpfcomissario], Comissario):
                                        raise ValueError
                                    if cpfcomissario not in cia._funcionarios.keys():
                                        raise KeyError
                                except ValueError:
                                    print("Comissário inválido! Tente novamente...")
                                    if i == 2:
                                        cont = 1
                                    continue
                                comissarios.append(cpfcomissario)
                            break
                        except KeyError:
                            print("Comissário não encontrado! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue

                    # <- Avião ->
                    cont = 0
                    for i in range(3):
                        try:
                            possui = str(input("Já possui avião cadastrado? (sim/não): ")).lower()
                            if possui not in ['sim', 'não'] or any(char.isdigit() for char in possui):
                                raise ValueError
                            break
                        except ValueError:
                            print("Opção inválida! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    
                    # Se possuir avião cadastrado, escolher avião
                    if possui == 'sim':
                        siglaav = input("Digite a sigla do avião: ")
                        if siglaav in cia._avioes.keys():
                            aviao = cia._avioes[siglaav]
                        else:
                            print("Avião não encontrado! Cadastre primeiro.")
                    # Se não possuir avião cadastrado, cadastrar avião
                    else:
                        # <- Modelo ->
                        cont = 0
                        for i in range(3):
                            try:
                                modelo = input("Modelo: ")
                                if any(char.isdigit() for char in modelo):
                                    raise ValueError
                                break
                            except ValueError:
                                print("Modelo inválido! Tente novamente...")
                                if i == 2:
                                    cont = 1
                                continue
                        if cont == 1:
                            input("3 tentativas falhas! Tente novamente...")
                            continue

                        # <- Quantidade de assentos ->
                        cont = 0
                        for i in range(3):
                            try:
                                quantidade_assentos = int(input("Quantidade de assentos: "))
                                if quantidade_assentos < 0:
                                    raise ValueError
                                break
                            except ValueError:
                                print("Quantidade inválida! Tente novamente...")
                                if i == 2: 
                                    cont = 1
                                continue
                        if cont == 1:
                            input("3 tentativas falhas! Tente novamente...")
                            continue

                        # <- Sigla ->
                        cont = 0
                        for i in range(3):
                            try:
                                siglaav = input("Sigla do avião: ")
                                if siglaav in cia._avioes.keys():
                                    raise ValueError
                                break
                            except ValueError:
                                print("Sigla inválida ou já existe! Tente novamente...")
                                if i == 2:
                                    cont = 1
                                continue
                        if cont == 1:
                            input("3 tentativas falhas! Tente novamente...")
                            continue
                        aviao = Aviao(modelo, quantidade_assentos, siglaav)
                    voo = Voo(sigla, origem, destino, aviao, cpfpiloto, comissarios)

                    print(f"\nVOO {voo.sigla}")
                    print(f"{'SIGLA':<10}{'ORIGEM':<20}{'DESTINO':<20}{'AVIÃO':<10}{'PILOTO':<10}{'COMISSÁRIOS':<10}")
                    sigla_str = str(sigla)
                    origem_str = str(voo.origem)
                    destino_str = str(voo.destino)
                    aviao_sigla_str = str(voo.aviao.siglaav)
                    piloto_str = str(voo._piloto)
                    comissarios_str = str(voo._comissarios)
                    print(f"{sigla_str:<10}{origem_str:<20}{destino_str:<20}{aviao_sigla_str:<10}{piloto_str:<10}{comissarios_str:<10}")
                    cia.add_voo(voo)
                    voo.add_assento()
                    print("\nVoo cadastrado com sucesso!...")

                # Alterar voo
                elif opcao == 2:
                    if not cia._voos.keys():
                        input("Não existe voos cadastrados! Cadastre um voo primeiro...")
                        continue

                    cont = 0
                    for i in range(3):
                        try:
                            sigla = input("Sigla: ")
                            if sigla not in cia._voos.keys():
                                raise ValueError
                            break
                        except ValueError:
                            print("Sigla inválida! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    booleano, mensagem = cia.alterar_voo(sigla)
                    if booleano == False:
                        input(mensagem)
                        continue
                    print("Voo alterado com sucesso!")

                # Excluir voo
                elif opcao == 3:
                    if not cia._voos.keys():
                        input("Não existe voos cadastrados! Cadastre um voo primeiro...")
                        continue
                    for i in range(3):
                        try:
                            sigla = input("Sigla: ")
                            if sigla not in cia._voos.keys():
                                raise ValueError
                            break
                        except ValueError:
                            print("Sigla inválida! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    booleano, mensagem = cia.excluir_voo(sigla)
                    if booleano == False:
                        input(mensagem)
                        continue
                    input("Voo excluído com sucesso!...")

                # Listar voos
                elif opcao == 4:
                    if not cia._voos.keys():
                        input("Não existe voos cadastrados! Cadastre um voo primeiro...")
                        continue
                    cia.listar_voos()
                    print("Voos listados com sucesso!")

                # Realizar voo
                elif opcao == 5:
                    # <- Blindagens ->
                    if not cia._voos.keys():
                        input("Não existe voos cadastrados! Cadastre um voo primeiro...")
                        continue
                    p = 0
                    for key in cia._funcionarios.keys():
                        if isinstance(cia._funcionarios[key], Piloto):
                            p = 1
                            break
                    if p == 0:
                        input("Deve haver ao menos 1 piloto cadastrado para essa área! Cadastre primeiro...")
                        continue
                    # <- Autenticar ->
                    cont = 0
                    for i in range(3):
                        try:
                            cpf = int(input("CPF do Piloto: "))
                            senha = input("Senha: ")
                            if cpf not in cia._funcionarios.keys():
                                raise KeyError
                            piloto = cia._funcionarios[cpf]
                            booleano, _ = ca.acessoPiloto(piloto, senha)
                            if booleano == False:
                                raise ValueError
                            break
                        except ValueError:
                            print("Senha inválida! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                        except KeyError:
                            print("Piloto não encontrado! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    else:
                        # <- Sigla ->
                        cont = 0
                        for i in range(3):
                            try:
                                sigla = input("Sigla: ")
                                if sigla not in cia._voos.keys():
                                    raise KeyError
                                break
                            except KeyError:
                                print("Voo não encontrado! Tente novamente...")
                                if i == 2:
                                    cont = 1
                                continue
                        if cont == 1:
                            input("3 tentativas falhas! Tente novamente...")
                            continue

                        if cia._voos[sigla]._piloto != cpf:
                            input("Piloto não é desse voo! Tente novamente...")
                            continue

                        # <- Voo ->
                        cont = 0
                        try:
                            if sigla not in cia._voos.keys():
                                raise KeyError
                            voo = cia._voos[sigla]
                        except KeyError:
                            input("Voo não encontrado! Tente novamente...")
                            continue
                        # Voo atual
                        print("VOO")
                        print("Origem:", voo._origem)
                        print("Destino:", voo._destino)
                        print("Avião:", voo._aviao.siglaav)

                        cia._voos[sigla].listar_reservados()
                        
                        voo._origem, voo._destino = voo._destino, voo._origem

                        # Voo de retorno
                        voo._assentos = []
                        voo._reservados = []
                        print("\nVOO DE VOLTA SERÁ: ")
                        print("Origem:", voo._origem)
                        print("Destino:", voo._destino)
                        print("Avião:", voo._aviao.siglaav)
                        voo.add_assento()
                        print("Voo realizado com sucesso!")

                # Reservar assento
                elif opcao == 6:
                    if not cia._voos.keys():
                        input("Não existe voos cadastrados! Cadastre um voo primeiro...")
                        continue
                    if len(voo._reservados) == len(voo._assentos):
                        input("Todos os assentos estão reservados! Tente novamente...")
                        continue
                    # <- Sigla ->
                    cont = 0
                    for i in range(3):
                        try:
                            sigla = input("Sigla: ")
                            if sigla not in cia._voos.keys():
                                raise KeyError
                            break
                        except KeyError:
                            input("Voo não encontrado! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue        

                    voo = cia._voos[sigla]
                    # <- CPF do cliente ->
                    cont = 0
                    for i in range(3):
                        try:
                            cpfcliente = int(input("CPF do cliente: "))
                            if cpfcliente in cia._passageiros.keys():
                                print("Cliente encontrado!")
                            else:
                                raise KeyError
                            break
                        except ValueError:
                            input("CPF inválido! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                        except KeyError:
                            input("Cliente não encontrado! Tente novamente ou cadastre o cliente.")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue

                    voo.listar_disp()
                    for i in range(3):
                        try:
                            assento = int(input("Assento: "))
                            if assento < 0 or assento >= len(voo._assentos) or assento in voo._reservados:
                                raise ValueError
                            break
                        except ValueError:
                            input("Assento inválido ou não pode ser reservado! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    booleano, mensagem = voo.reservar_assento(assento)
                    if booleano == False:
                        input(mensagem)
                        continue
                    print("Assento reservado com sucesso!")

                # Cancelar reserva
                elif opcao == 7:
                    cont = 0
                    for i in range(3):
                        try:
                            sigla = input("Sigla: ")
                            if sigla not in cia._voos.keys():
                                raise KeyError
                            break
                        except KeyError:
                            print("Voo não encontrado! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    voo = cia._voos[sigla]
                    voo.listar_reservados()

                    # <- Assento ->
                    cont = 0
                    for i in range(3):
                        try:
                            assento = int(input("Assento: "))
                            if assento not in voo._reservados:
                                raise ValueError
                            break
                        except ValueError:
                            print("Assento inválido! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    booleano, mensagem = voo.cancelar_reserva(assento)
                    if booleano == False:
                        input(mensagem)
                        continue
                    print("Reserva cancelada com sucesso!")

                # Voltar
                elif opcao == 0:
                    print("Voltar")
                    break
                input("Pressione Enter para continuar...")
        
        # Gerenciar aviões
        elif opcao == 2:
            if not cia._funcionarios.keys():
                input("Não existe funcionários cadastrados! Cadastre primeiro...")
                continue
            # Autenticar o gerente
            cont = 0
            for i in range(3):
                try:
                    cpf = int(input("CPF do Gerente: "))
                    senha = input("Senha: ")
                    if cpf not in cia._funcionarios.keys():
                        raise KeyError
                    gerente = cia._funcionarios[cpf]
                    booleano, _ = ca.acessoGerente(gerente, senha)
                    if booleano == False:
                        raise ValueError
                    break
                except ValueError:
                    print("Senha inválida! Tente novamente...")
                    if i == 2:
                        cont = 1
                    continue
                except KeyError:
                    print("Gerente não encontrado! Tente novamente...")
                    if i == 2:
                        cont = 1
                    continue
            if cont == 1:
                input("3 tentativas falhas! Tente novamente...")
                continue

            while True:
                clear()
                print("\nGerenciar aviões")
                print("1. Cadastrar avião")
                print("2. Alterar avião")
                print("3. Excluir avião")
                print("4. Listar aviões")
                print("5. Voltar")
                try:
                    opcao = int(input("Escolha uma opção: "))
                    if opcao < 1 or opcao > 5:
                        raise ValueError
                except ValueError:
                    input("Opção inválida! Tente novamente...")
                    continue
                
                # Cadastrar avião
                if opcao == 1:
                    print("Cadastrar avião")
                    # <- Modelo ->
                    modelo = input("Modelo: ")
                    
                    # <- Quantidade de assentos ->
                    cont = 0
                    for i in range(3):
                        try:
                            quantidade_assentos = int(input("Quantidade de assentos: "))
                            if quantidade_assentos < 0:
                                raise ValueError
                            break
                        except ValueError:
                            input("Quantidade inválida! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue

                    # <- Sigla ->
                    cont = 0
                    for i in range(3):
                        try:
                            sigla = input("Sigla: ")
                            if sigla in cia._avioes.keys():
                                raise ValueError
                            break
                        except ValueError:
                            input("Sigla inválida! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    aviao = Aviao(modelo, quantidade_assentos, sigla)
                    booleano, mensagem = cia.add_aviao(aviao)
                    if booleano == False:
                        input(mensagem)
                        continue
                    print("Avião cadastrado com sucesso!")

                # Alterar avião
                elif opcao == 2:
                    if not cia._avioes.keys():
                        input("Não existe aviões cadastrados! Cadastre um avião primeiro...")
                        continue
                    # <- Sigla ->
                    cont = 0
                    for i in range(3):
                        try:
                            sigla = input("Sigla: ")
                            if sigla not in cia._avioes.keys():
                                raise KeyError
                            break
                        except KeyError:
                            print("Sigla inválida! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    booleano, mensagem = cia.alterar_aviao(sigla)
                    if booleano == False:
                        input(mensagem)
                        continue
                    print("Avião alterado com sucesso!")

                # Excluir avião
                elif opcao == 3:
                    if not cia._avioes.keys():
                        input("Não existe aviões cadastrados! Cadastre um avião primeiro...")
                        continue
                    # <- Sigla ->
                    cont = 0
                    for i in range(3):
                        try:
                            sigla = input("Sigla: ")
                            if sigla not in cia._avioes.keys():
                                raise KeyError
                            break
                        except KeyError:
                            print("Sigla inválida! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    cia.excluir_aviao(sigla)
                    print("Avião excluído com sucesso!")

                # Listar aviões
                elif opcao == 4:
                    if not cia._avioes.keys():
                        input("Não existe aviões cadastrados! Cadastre um avião primeiro...")
                        continue
                    cia.listar_avioes()
                    print("Aviões listados com sucesso!")

                # Voltar
                elif opcao == 5:
                    print("Voltar")
                    break
                input("Pressione Enter para continuar...")

        # Gerenciar passageiros
        elif opcao == 3:
            if not cia._funcionarios.keys():
                input("Não existe funcionários para gerenciar! Cadastre primeiro...")
                continue

            # Autenticar o atendente
            cont = 0
            for i in range(3):
                try:
                    cpf = int(input("CPF do Atendente: "))
                    senha = input("Senha: ")
                    if cpf not in cia._funcionarios.keys():
                        raise KeyError
                    gerente = cia._funcionarios[cpf]
                    booleano, _ = ca.acessoAtendente(gerente, senha)
                    if booleano == False:
                        raise ValueError
                    break
                except ValueError:
                    print("Senha inválida! Tente novamente...")
                    if i == 2:
                        cont = 1
                    continue
                except KeyError:
                    print("Atendente não encontrado! Tente novamente...")
                    if i == 2:
                        cont = 1
                    continue
            if cont == 1:
                input("3 tentativas falhas! Tente novamente...")

            while True:
                clear()
                print("\nGerenciar passageiros")
                print("1. Cadastrar passageiro")
                print("2. Alterar passageiro")
                print("3. Excluir passageiro")
                print("4. Listar passageiros")
                print("0. Voltar")
                try:
                    opcao = int(input("Escolha uma opção: "))
                    if opcao < 0 or opcao > 4:
                        raise ValueError
                except ValueError:
                    input("Opção inválida! Tente novamente...")
                    continue

                # Cadastrar passageiro
                if opcao == 1:
                    print("Cadastrar passageiro")
                    # <- Nome ->
                    cont = 0
                    for i in range(3):
                        try:
                            nome = str(input("Nome: "))
                            if any(char.isdigit() for char in nome):
                                raise ValueError
                            break
                        except ValueError:
                            print("Nome inválido! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    
                    # <- CPF ->
                    cont = 0
                    for i in range(3):
                        try:
                            cpf = int(input("CPF: "))
                            if cpf in cia._passageiros.keys():
                                raise ValueError
                            break
                        except ValueError:
                            print("CPF inválido ou já cadastrado! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue

                    # <- Telefone ->
                    for i in range(3):
                        try:
                            telefone = int(input("Telefone: "))
                            break
                        except ValueError:
                            print("Telefone inválido! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue

                    passageiro = Passageiro(nome, cpf, telefone)
                    cia.add_passageiro(passageiro)

                # Alterar passageiro
                elif opcao == 2:
                    if not cia._passageiros.keys():
                        input("Não existe passageiros cadastrados! Cadastre um passageiro primeiro...")
                        continue
                    # <- CPF ->
                    cont = 0
                    for i in range(3):
                        try:
                            cpf = int(input("CPF: "))
                            break
                        except ValueError:
                            print("CPF inválido! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue

                    booleano, mensagem = cia.alterar_passageiro(cpf)
                    if booleano == False:
                        input(mensagem)
                        continue
                    print("Passageiro alterado com sucesso!")

                # Excluir passageiro
                elif opcao == 3:
                    if not cia._passageiros.keys():
                        input("Não existe passageiros cadastrados! Cadastre um passageiro primeiro...")
                        continue
                    # <- CPF ->
                    cont = 0
                    for i in range(3):
                        try:
                            cpf = int(input("CPF: "))
                            break
                        except ValueError:
                            print("CPF inválido! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    booleano, mensagem = cia.excluir_passageiro(cpf)
                    if booleano == False:
                        input(mensagem)
                        continue
                    print("Passageiro excluído com sucesso!")

                # Listar passageiros
                elif opcao == 4:
                    if not cia._passageiros.keys():
                        input("Não existe passageiros cadastrados! Cadastre um passageiro primeiro...")
                        continue
                    cia.listar_passageiros()
                    print("Passageiros listados com sucesso!")
                
                # Voltar
                elif opcao == 0:
                    print("Voltar")
                    break
                input("Pressione Enter para continuar...")

        # Gerenciar funcionários
        elif opcao == 4:
            while True:
                clear()
                print("\nGerenciar funcionários")
                print("1. Cadastrar funcionário")
                print("2. Alterar funcionário")
                print("3. Excluir funcionário")
                print("4. Listar funcionários")
                print("5. Listar pilotos")
                print("6. Listar comissários")
                print("7. Listar atendentes")
                print("8. Listar gerentes")
                print("0. Voltar")
                try:
                    opcao = int(input("Escolha uma opção: "))
                    if opcao < 0 or opcao > 8:
                        raise ValueError
                except ValueError:
                    input("Opção inválida! Tente novamente...")
                    continue

                if opcao == 1:
                    print("Cadastrar funcionário")
                    # <- Nome ->
                    cont = 0
                    for i in range(3):
                        try:
                            nome = str(input("Nome: "))
                            if any(char.isdigit() for char in nome):
                                raise ValueError
                            break
                        except ValueError:
                            input("Nome inválido! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue

                    # <- CPF ->
                    cont = 0
                    for i in range(3):
                        try:
                            cpf = int(input("CPF: "))
                            if cpf in cia._funcionarios.keys():
                                raise ValueError
                            break
                        except ValueError:
                            print("CPF inválido ou já cadastrado! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    
                    # <- Salário ->
                    cont = 0
                    for i in range(3):
                        try:
                            salario = float(input("Salário: "))
                            if salario < 0:
                                raise ValueError
                            break
                        except ValueError:
                            input("Salário inválido! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue

                    # <- Senha ->
                    cont = 0
                    for i in range(3):
                        try:
                            senha = input("Senha: ")
                            if len(senha) < 4:
                                raise ValueError
                            break
                        except ValueError:
                            input("Senha inválida ou não possui tamanho mínimo de 4 dígitos! Tente novamente...")
                            continue

                    # <- Tipo ->
                    print("\nTipo de funcionário:")
                    print("1. Piloto")
                    print("2. Comissário")
                    print("3. Atendente")
                    print("4. Gerente")
                    cont = 0
                    for i in range(3):
                        try:
                            opcao = int(input("Escolha uma opção: "))
                            if opcao < 1 or opcao > 4:
                                raise ValueError
                            break
                        except ValueError:
                            input("Opção inválida! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue

                    # <- Piloto ->
                    if opcao == 1:
                        # <- Horas de voo ->
                        cont = 0
                        for i in range(3):
                            try:
                                horas_voo = int(input("\nHoras de voo: "))
                                if horas_voo < 0:
                                    raise ValueError
                                break
                            except ValueError:
                                input("Quantidade de horas inválida! Tente novamente...")
                                if i == 2:
                                    cont = 1
                                continue
                        if cont == 1:
                            input("3 tentativas falhas! Tente novamente...")
                            continue
                
                        funcionario = Piloto(nome, cpf, salario, senha, horas_voo)

                    # <- Comissário ->
                    elif opcao == 2:
                        idiomas = []
                        # <- Quantidade de idiomas ->
                        cont = 0
                        for i in range(3):
                            try:
                                quant = int(input("Quantidade de idiomas: "))
                                if quant < 0:
                                    raise ValueError
                                break
                            except ValueError:
                                input("Quantidade de idiomas inválida! Tente novamente...")
                                if i == 2:
                                    cont = 1
                                continue
                        if cont == 1:
                            input("3 tentativas falhas! Tente novamente...")
                            continue
                            
                        # <- Idiomas ->
                        for i in range(quant):
                            while True:
                                try:
                                    ind = str(input(f"Idioma {i + 1}: "))
                                    if any(char.isdigit() for char in ind):
                                        raise ValueError
                                    break
                                except ValueError:
                                    input("Idioma inválido! Tente novamente...")
                                    continue
                            idiomas.append(ind)

                        funcionario = Comissario(nome, cpf, salario, senha, idiomas)

                    # <- Atendente ->
                    elif opcao == 3:
                        # <- Terminal ->
                        cont = 0
                        for i in range(3):
                            try:
                                terminal = int(input("Terminal: "))
                                if terminal < 0:
                                    raise ValueError
                                break
                            except ValueError:
                                input("Terminal inválido! Tente novamente...")
                                if i == 2:
                                    cont = 1
                                continue
                        if cont == 1:
                            input("3 tentativas falhas! Tente novamente...")
                            continue
                        funcionario = Atendente(nome, cpf, salario, senha, terminal)

                    # <- Gerente ->
                    elif opcao == 4:
                        # <- Expediente ->
                        cont = 0
                        for i in range(3):
                            try:
                                expediente = str(input("Expediente: "))
                                if any(char.isdigit() for char in expediente):
                                    raise ValueError
                                break
                            except ValueError:
                                input("Expediente inválido! Tente novamente...")
                                if i == 2:
                                    cont = 1
                                continue
                        if cont == 1:
                            input("3 tentativas falhas! Tente novamente...")
                            continue
                        funcionario = Gerente(nome, cpf, salario, senha, expediente)
                    booleano, mensagem = cia.add_funcionario(funcionario)
                    if booleano == False:
                        input(mensagem)
                        continue
                    print("Funcionário cadastrado com sucesso!")

                # Alterar funcionário
                elif opcao == 2:
                    if not cia._funcionarios.keys():
                        input("Não existe funcionários cadastrados! Cadastre um funcionário primeiro...")
                        continue
                    # <- CPF ->
                    cont = 0
                    for i in range(3):
                        try:
                            cpf = int(input("CPF: "))
                            if cpf not in cia._funcionarios.keys():
                                raise KeyError
                            break
                        except ValueError:
                            print("CPF inválido! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                        except KeyError:
                            print("CPF não encontrado! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    booleano, mensagem = cia.alterar_funcionario(cpf)
                    if booleano == False:
                        input(mensagem)
                        continue
                    print("Funcionário alterado com sucesso!")

                # Excluir funcionário
                elif opcao == 3:
                    if not cia._funcionarios.keys():
                        input("Não existe funcionários cadastrados! Cadastre um funcionário primeiro...")
                        continue
                    # <- CPF ->
                    cont = 0
                    for i in range(3):
                        try:
                            cpf = int(input("CPF: "))
                            break
                        except ValueError:
                            print("CPF inválido! Tente novamente...")
                            if i == 2:
                                cont = 1
                            continue
                    if cont == 1:
                        input("3 tentativas falhas! Tente novamente...")
                        continue
                    booleano, mensagem = cia.excluir_funcionario(cpf)
                    if booleano == False:
                        input(mensagem)
                        continue
                    print("Funcionário excluído com sucesso!")

                # Listar funcionários
                elif opcao == 4:

                    if not cia._funcionarios.keys():
                        input("Não existe funcionários cadastrados! Cadastre um funcionário primeiro...")
                        continue
                    cia.listar_funcionarios()
                    print("\nFuncionários listados com sucesso!")

                # Listar pilotos
                elif opcao == 5:
                    if not cia._funcionarios.keys():
                        input("Não existe funcionários cadastrados! Cadastre um funcionário primeiro...")
                        continue
                    b, m = cia.listar_pilotos()
                    if b == False:
                        input(m)
                        continue
                    print("\nPilotos listados com sucesso!")

                # Listar comissários
                elif opcao == 6:
                    if not cia._funcionarios.keys():
                        input("Não existe funcionários cadastrados! Cadastre um funcionário primeiro...")
                        continue
                    b, m = cia.listar_comissarios()
                    if b == False:
                        input(m)
                        continue
                    print("\nComissários listados com sucesso!")

                # Listar atendentes
                elif opcao == 7:
                    if not cia._funcionarios.keys():
                        input("Não existe funcionários cadastrados! Cadastre um funcionário primeiro...")
                        continue
                    b, m = cia.listar_atendentes()
                    if b == False:
                        input(m)
                        continue
                    print("\nAtendentes listados com sucesso!")

                # Listar gerentes
                elif opcao == 8:
                    if not cia._funcionarios.keys():
                        input("Não existe funcionários cadastrados! Cadastre um funcionário primeiro...")
                        continue
                    b, m = cia.listar_gerentes()
                    if b == False:
                        input(m)
                        continue
                    print("\nGerentes listados com sucesso!")

                # Voltar
                elif opcao == 0:
                    print("Voltar")
                    break
                input("Pressione Enter para continuar...")

        # Sair
        elif opcao == 5:
            print("Saindo...")
            break

if __name__ == "__main__":
    main()