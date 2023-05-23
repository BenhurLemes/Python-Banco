class Pessoa(object):
  def __init__(self, nome, titular, cpf, idade, gender):
    self.nome = nome
    self.titular = titular
    self.cpf = cpf
    self.idade = idade
    self.gender = gender
  
  def Adicionar_Banco(self, marca):
    self.banco = Banco(marca)
    
class ContaBancaria(object):
  def __init__(self, conta_number, titular, senha, saldo, limite):
    self.conta_number = conta_number
    self.nome = titular
    self.senha = senha
    self.balance = saldo
    self.limite = limite

class Banco(object):
  def __init__(self, marca):
    self.marca = marca
  
  def Cadastro(self, nome, titular, cpf, idade, gender):
    self.cadastro = Pessoa(nome, titular, cpf, idade, gender)
    self.nome = nome
    self.titular = titular
    self.cpf = cpf
    self.idade = idade
    self.gender = gender

  def Verificar_Pessoa(self, titular, cpf):
    print("!--Verificação de conta--!\n")
    if self.titular != titular and self.cpf != cpf and self.idade < 18:
      print("Sua conta foi banida.")
    else:
      if self.titular != titular:
        print("O titular está diferente!")
      elif self.idade < 18:
        print("Não tem idade para ter uma conta.")
      elif self.cpf != cpf:
        print("O CPF está diferente!")
      else:
        print("Verificado com Sucesso!")
        print("\n!----------------------!\n")

  def Alterar_Dados(self):
    print("\n!--Redefinir os Dados--!\n")
    nome = input("Altere seu nome: ")
    titular = input("Aletere seu Titular: ")
    idade = input("Altere sua idade: ")
    cpf = input("Altere seu CPF: ")
    if len(cpf) == 11:
      self.nome = nome
      self.titular = titular
      self.idade = idade
      self.cpf = cpf
    else:
      print("Escreva o CPF corretamente.")
    print("\n!----------------------!\n")

  def Criar_Conta(self, conta_number, titular, senha, saldo, limite):
    self.conta_number = conta_number
    self.titular = titular
    self.senha = senha
    self.balance = saldo
    self.limite = limite
    self.conta = ContaBancaria(conta_number, titular, senha, saldo, limite)
    print(f"Conta Criada: {conta_number}, {titular}")

  def Alterar_Senha(self, senha):
    print("!------------------------!\n")
    senha = input("Altere sua senha: ")
    if len(senha) >= 5:
      self.senha = senha
      print(f"Sua senha atual: {senha}")
    else:
      print("Escreva uma senha discreta.")
    print("\n!------------------------!\n")

  def Saque(self, amount):
    self.saque = amount
    if self.saque <= self.balance:
      self.balance -= amount
    else:
      print("O saque está maior que o saldo disponível")
      self.saque = 0

  def Depositar(self, amount):
    if amount > 0:
      self.balance += amount
    else:
      print("O deposito precisa ter um valor positivo.")
      amount = 0

  def Credito(self, credito):
    self.fatura = credito
    if self.fatura <= self.limite:
      self.limite -= credito
    else:
      print("A fatura está maior que o limite disponivel")
      self.fatura = 0
      
  def Debito(self, amount):
    self.debito = amount
    if self.debito <= self.balance:
      self.balance -= amount
    else:
      print("O débito está maior que o saldo disponível")
      self.debito = 0
      
  def InterfaceConta(self):
    print(f"\n!------Banco {self.marca}------!")
    resposta = 'Login: %s \nSenha: %s' % \
                (self.titular, self.senha)
    print(resposta)
    print("!------------------------!\n")

    print("!---------Dados----------!")
    identidade = 'Nome: %s \nTitular: %s \nCPF: %s\nidade: %s\nGênero: %s' % \
            (self.nome, self.titular, self.cpf, self.idade, self.gender)
    print(identidade)
    print("!------------------------!\n")

    print(f"!------Olá, {self.nome}------!")
    tela = '\nConta - %s\nSaldo disponível: R$%s\nFatura Atual R$%s\nLimite disponível de R$%s\n' % \
              (self.conta_number, self.balance, self.fatura, self.limite)
    print(tela)
    print("!------------------------!\n")

Exemplo1 = Banco("Nubank")
Exemplo1.Cadastro("Larissa","Couto", "34023460176", 18, "mulher")
Exemplo1.Verificar_Pessoa("Couto", "34023460176")
Exemplo1.Criar_Conta("1934562", "Couto", "50555", 10000, 5000)
Exemplo1.Saque(500)
Exemplo1.Depositar(600)
Exemplo1.Credito(2333)
Exemplo1.Debito(2000)
Exemplo1.InterfaceConta()

Exemplo2 = Banco("Itau")
Exemplo2.Cadastro("João","Jonas", "06503536105", 37, "homem")
Exemplo2.Verificar_Pessoa("Jonas", "06503536105")
Exemplo2.Criar_Conta("3396018", "Couto", "77441", 1000, 500)
Exemplo2.Alterar_Dados()
Exemplo2.Alterar_Senha("50555")
Exemplo2.Saque(960)
Exemplo2.Depositar(600)
Exemplo2.Credito(500)
Exemplo2.Debito(10)
Exemplo2.InterfaceConta()