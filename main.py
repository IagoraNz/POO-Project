import os

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
        if assento not in self._assentos:
            self._assentos.append(assento)
            self._reservados.remove(assento)
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
            print("3. Quantidade de bagagens")
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                modelo = input("Modelo: ")
                self._avioes[sigla]._modelo = modelo
                return True, "Modelo alterado com sucesso!"
            elif opcao == 2:
                quantidade_assentos = input("Quantidade de assentos: ")
                self._avioes[sigla]._quantidade_assentos = quantidade_assentos
                return True, "Quantidade de assentos alterada com sucesso!"
            elif opcao == 3:
                quantidade_bagagens = input("Quantidade de bagagens: ")
                self._avioes[sigla]._quantidade_bagagens = quantidade_bagagens
                return True, "Quantidade de bagagens alterada com sucesso!"
            else:
                return False, "Opção inválida!"
        return False, "Avião não encontrado!"
    
    def excluir_aviao(self, sigla):
        if sigla in self._avioes.keys():
            del self._avioes[sigla]
            return True, "Avião excluído com sucesso!"
        return False, "Avião não encontrado!"
    
    def listar_avioes(self):
        print("Aviões cadastrados:")
        print("Sigla\tModelo\tQuantidade de assentos")
        for sigla, aviao in self._avioes.items():
            print(f"{sigla}\t{aviao.modelo}\t{aviao.quantidade_assentos}")

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
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                origem = input("Origem: ")
                self._voos[sigla]._origem = origem
                return True, "Origem alterada com sucesso!"
            elif opcao == 2:
                destino = input("Destino: ")
                self._voos[sigla]._destino = destino
                return True, "Destino alterado com sucesso!"
            elif opcao == 3:
                aviao = input("Já possui avião cadastrado?: ")
                if aviao == 'sim':
                    aviao = input("Digite a sigla do avião: ")
                else:
                    modelo = input("Modelo: ")
                    quantidade_assentos = input("Quantidade de assentos: ")
                    quantidade_bagagens = input("Quantidade de bagagens: ")
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
        print("Voos cadastrados:")
        print("Sigla\tOrigem\tDestino\tAvião")
        for sigla, voo in self._voos.items():
            print(f"{sigla}\t{voo.origem}\t{voo.destino}\t{voo.aviao.siglaav}")

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
            opcao = int(input("Escolha uma opção: "))

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
        print("Passageiros cadastrados:")
        print("CPF\tNome\tTelefone")
        for cpf, passageiro in self._passageiros.items():
            print(f"{cpf}\t{passageiro.nome}\t{passageiro.telefone}")

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
            opcao = int(input("Escolha uma opção: "))

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
        print("Funcionários cadastrados:")
        print("CPF\tNome\tSalário")
        for cpf, funcionario in self._funcionarios.items():
            print(f"{cpf}\t{funcionario.nome}\t{funcionario.salario}")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
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

    while True:
        with open('cia.txt', 'r') as f:
            nome = f.readline().strip()
            cnpj = f.readline().strip()
            telefone = f.readline().strip()
            endereco = f.readline().strip()
            cia = CiaAerea(nome, cnpj, telefone, endereco)

        while True:
            clear()
            print(f"Bem-vindo à {cia.nome}!")
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

            if opcao == 1:
                while True:
                    clear()
                    print("Gerenciar voos")
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

                    if opcao == 1:
                        comissarios = []
                        print("Cadastrar voo")
                        sigla = input("Sigla: ")
                        while True:
                            try:
                                origem = str(input("Origem: "))
                                if any(char.isdigit() for char in origem):
                                    raise ValueError
                                break
                            except ValueError:
                                print("Origem inválida! Tente novamente...")
                                continue

                        while True:
                            try:
                                destino = str(input("Destino: "))
                                if any(char.isdigit() for char in destino):
                                    raise ValueError
                                break
                            except ValueError:
                                print("Destino inválido! Tente novamente...")
                                continue

                        while True:
                            try:
                                cpfpiloto = int(input("CPF do piloto: "))
                                if cpfpiloto not in cia._funcionarios.keys():
                                    raise KeyError
                                break
                            except ValueError:
                                print("Piloto inválido! Tente novamente.")
                                continue
                            except KeyError:
                                print("Piloto não encontrado! Cadastre ou tente novamente...")
                                continue
                        
                        while True:
                            try:
                                quantcomissarios = int(input("Quantidade de comissários: "))
                                if quantcomissarios < 0:
                                    raise ValueError
                                break
                            except ValueError:
                                print("Quantidade inválida! Tente novamente...")
                                continue

                        while True:
                            try:
                                for i in range(quantcomissarios):
                                    try:
                                        cpfcomissario = int(input(f"Comissário {i + 1}: "))
                                        if cpfcomissario not in cia._funcionarios.keys():
                                            raise KeyError
                                    except ValueError:
                                        print("Comissário inválido! Tente novamente...")
                                        continue
                                    comissarios.append(cpfcomissario)
                                break
                            except KeyError:
                                print("Comissário não encontrado! Tente novamente...")
                                continue

                        while True:
                            try:
                                possui = str(input("Já possui avião cadastrado? (sim/não): "))
                                if possui not in ['sim', 'não'] or any(char.isdigit() for char in possui):
                                    raise ValueError
                                break
                            except ValueError:
                                print("Opção inválida! Tente novamente...")
                                continue

                        if possui == 'sim':
                            siglaav = input("Digite a sigla do avião: ")
                            if siglaav in cia._avioes.keys():
                                aviao = cia._avioes[siglaav]
                                voo = Voo(sigla, origem, destino, aviao, cpfpiloto, comissarios)
                                cia.add_voo(voo)
                                voo.add_assento()
                            else:
                                print("Avião não encontrado! Cadastre primeiro.")
                        else:
                            modelo = input("Modelo: ")
                            while True:
                                try:
                                    quantidade_assentos = int(input("Quantidade de assentos: "))
                                    if quantidade_assentos < 0:
                                        raise ValueError
                                    break
                                except ValueError:
                                    print("Quantidade inválida! Tente novamente...")
                                    continue
                            siglaav = input("Sigla: ")
                            aviao = Aviao(modelo, quantidade_assentos, siglaav)
                            voo = Voo(sigla, origem, destino, aviao, cpfpiloto, comissarios)
                            cia.add_voo(voo)
                            voo.add_assento()

                    elif opcao == 2:
                        sigla = int(input("Sigla: "))
                        cia.alterar_voo(sigla)

                    elif opcao == 3:
                        sigla = int(input("Sigla: "))
                        cia.excluir_voo(sigla)

                    elif opcao == 4:
                        cia.listar_voos()

                    elif opcao == 5:
                        sigla = input("Sigla: ")
                        voo = cia._voos[sigla]
                        print("VOO")
                        print("Origem:", voo._origem)
                        print("Destino:", voo._destino)
                        print("Avião:", voo._aviao)
                        voo.listar_reservados()
                        
                        voo._origem, voo._destino = voo._destino, voo._origem

                        voo._assentos = []
                        voo._reservados = []
                        print("VOO DE VOLTA SERÁ: ")
                        print("Origem:", voo._origem)
                        print("Destino:", voo._destino)
                        print("Avião:", voo._aviao)
                        voo.add_assento()

                    elif opcao == 6:
                        sigla = input("Sigla: ")

                        while True:
                            try:
                                cpfcliente = int(input("CPF do cliente: "))
                                if cpfcliente in cia._passageiros.keys():
                                    print("Cliente encontrado!")
                                else:
                                    raise KeyError
                                break
                            except ValueError:
                                print("CPF inválido! Tente novamente...")
                                continue
                            except KeyError:
                                print("Cliente não encontrado! Tente novamente ou cadastre o cliente.")
                                continue

                        voo = cia._voos[sigla]
                        voo.listar_disp()
                        while True:
                            try:
                                assento = int(input("Assento: "))
                                if assento < 0 or assento >= len(voo._assentos):
                                    raise ValueError
                                break
                            except ValueError:
                                print("Assento inválido! Tente novamente...")
                                continue
                        voo.reservar_assento((assento, cpfcliente))

                    elif opcao == 7:
                        sigla = input("Sigla: ")
                        voo = cia._voos[sigla]
                        voo.listar_reservados()
                        while True:
                            try:
                                assento = int(input("Assento: "))
                                if assento < 0 or assento >= len(voo._reservados):
                                    raise ValueError
                                break
                            except ValueError:
                                print("Assento inválido! Tente novamente...")
                                continue
                        voo.cancelar_reserva(assento)

                    elif opcao == 0:
                        print("Voltar")
                        break
                    input("Pressione Enter para continuar...")
                
            elif opcao == 2:
                while True:
                    clear()
                    print("Gerenciar aviões")
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

                    if opcao == 1:
                        print("Cadastrar avião")
                        modelo = input("Modelo: ")
                        
                        while True:
                            try:
                                quantidade_assentos = int(input("Quantidade de assentos: "))
                                if quantidade_assentos < 0:
                                    raise ValueError
                                break
                            except ValueError:
                                input("Quantidade inválida! Tente novamente...")
                                continue

                        sigla = input("Sigla: ")
                        aviao = Aviao(modelo, quantidade_assentos, sigla)
                        cia.add_aviao(aviao)

                    elif opcao == 2:
                        while True:
                            try:
                                sigla = input("Sigla: ")
                                if sigla not in cia._avioes.keys():
                                    raise KeyError
                                break
                            except KeyError:
                                print("Sigla inválida! Tente novamente...")
                                continue
                        cia.alterar_aviao(sigla)

                    elif opcao == 3:
                        while True:
                            try:
                                sigla = input("Sigla: ")
                                if sigla not in cia._avioes.keys():
                                    raise KeyError
                                break
                            except KeyError:
                                print("Sigla inválida! Tente novamente...")
                                continue
                        cia.excluir_aviao(sigla)

                    elif opcao == 4:
                        cia.listar_avioes()

                    elif opcao == 5:
                        print("Voltar")
                        break
                    input("Pressione Enter para continuar...")

            elif opcao == 3:
                while True:
                    clear()
                    print("Gerenciar passageiros")
                    print("1. Cadastrar passageiro")
                    print("2. Alterar passageiro")
                    print("3. Excluir passageiro")
                    print("4. Listar passageiros")
                    print("5. Voltar")
                    try:
                        opcao = int(input("Escolha uma opção: "))
                        if opcao < 1 or opcao > 5:
                            raise ValueError
                    except ValueError:
                        input("Opção inválida! Tente novamente...")
                        continue

                    if opcao == 1:
                        print("Cadastrar passageiro")
                        while True:
                            try:
                                nome = str(input("Nome: "))
                                if any(char.isdigit() for char in nome):
                                    raise ValueError
                                break
                            except ValueError:
                                print("Nome inválido! Tente novamente...")
                                continue
                        
                        while True:
                            try:
                                cpf = int(input("CPF: "))
                                break
                            except ValueError:
                                print("CPF inválido! Tente novamente...")
                                continue

                        while True:
                            try:
                                telefone = int(input("Telefone: "))
                                break
                            except ValueError:
                                print("Telefone inválido! Tente novamente...")
                                continue

                        passageiro = Passageiro(nome, cpf, telefone)
                        cia.add_passageiro(passageiro)

                    elif opcao == 2:
                        while True:
                            try:
                                cpf = int(input("CPF: "))
                                break
                            except ValueError:
                                print("CPF inválido! Tente novamente...")
                                continue

                        cia.alterar_passageiro(cpf)

                    elif opcao == 3:
                        while True:
                            try:
                                cpf = int(input("CPF: "))
                                break
                            except ValueError:
                                print("CPF inválido! Tente novamente...")
                                continue
                        cia.excluir_passageiro(cpf)

                    elif opcao == 4:
                        cia.listar_passageiros()

                    elif opcao == 5:
                        print("Voltar")
                        break
                    input("Pressione Enter para continuar...")

            elif opcao == 4:
                while True:
                    clear()
                    print("Gerenciar funcionários")
                    print("1. Cadastrar funcionário")
                    print("2. Alterar funcionário")
                    print("3. Excluir funcionário")
                    print("4. Listar funcionários")
                    print("5. Voltar")
                    try:
                        opcao = int(input("Escolha uma opção: "))
                        if opcao < 1 or opcao > 5:
                            raise ValueError
                    except ValueError:
                        input("Opção inválida! Tente novamente...")
                        continue

                    if opcao == 1:
                        print("Cadastrar funcionário")
                        while True:
                            try:
                                nome = str(input("Nome: "))
                                if any(char.isdigit() for char in nome):
                                    raise ValueError
                                break
                            except ValueError:
                                input("Nome inválido! Tente novamente...")
                                continue

                        while True:
                            try:
                                cpf = int(input("CPF: "))
                                break
                            except ValueError:
                                print("CPF inválido! Tente novamente...")
                                continue

                        while True:
                            try:
                                salario = float(input("Salário: "))
                                if salario < 0:
                                    raise ValueError
                                break
                            except ValueError:
                                input("Salário inválido! Tente novamente...")
                                continue

                        while True:
                            try:
                                senha = input("Senha: ")
                                if len(senha) < 4:
                                    raise ValueError
                                break
                            except ValueError:
                                input("Senha inválida! Tente novamente...")
                                continue
                        print("\n1. Piloto")
                        print("2. Comissário")
                        print("3. Atendente")
                        print("4. Gerente")
                        try:
                            opcao = int(input("Escolha uma opção: "))
                            if opcao < 1 or opcao > 4:
                                raise ValueError
                        except ValueError:
                            input("Opção inválida! Tente novamente...")
                            continue

                        if opcao == 1:
                            while True:
                                try:
                                    horas_voo = int(input("\nHoras de voo: "))
                                    if horas_voo < 0:
                                        raise ValueError
                                    break
                                except ValueError:
                                    input("Quantidade de horas inválida! Tente novamente...")
                                    continue
                    
                            funcionario = Piloto(nome, cpf, salario, senha, horas_voo)
                        elif opcao == 2:
                            idiomas = []
                            while True:
                                try:
                                    quant = int(input("Quantidade de idiomas: "))
                                    if quant < 0:
                                        raise ValueError
                                    break
                                except ValueError:
                                    input("Quantidade de idiomas inválida! Tente novamente...")
                                    continue
                                
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
                        elif opcao == 3:
                            while True:
                                try:
                                    terminal = int(input("Terminal: "))
                                    if terminal < 0:
                                        raise ValueError
                                    break
                                except ValueError:
                                    input("Terminal inválido! Tente novamente...")
                                    continue
                            funcionario = Atendente(nome, cpf, salario, senha, terminal)
                        elif opcao == 4:
                            while True:
                                try:
                                    expediente = str(input("Expediente: "))
                                    if any(char.isdigit() for char in expediente):
                                        raise ValueError
                                    break
                                except ValueError:
                                    input("Expediente inválido! Tente novamente...")
                                    continue
                            funcionario = Gerente(nome, cpf, salario, senha, expediente)
                        cia.add_funcionario(funcionario)

                    elif opcao == 2:
                        while True:
                            try:
                                cpf = int(input("CPF: "))
                                break
                            except ValueError:
                                print("CPF inválido! Tente novamente...")
                                continue
                        cia.alterar_funcionario(cpf)

                    elif opcao == 3:
                        while True:
                            try:
                                cpf = int(input("CPF: "))
                                break
                            except ValueError:
                                print("CPF inválido! Tente novamente...")
                                continue
                        cia.excluir_funcionario(cpf)

                    elif opcao == 4:
                        cia.listar_funcionarios()

                    elif opcao == 5:
                        print("Voltar")
                        break
                    input("Pressione Enter para continuar...")

            elif opcao == 5:
                break

if __name__ == "__main__":
    main()