from clientes import Cliente
from bancos import Banco
from contas import Conta
from contas import ContaEspecial

joão = Cliente("João da Silva", "3241-5599")
maria = Cliente("Maria Silva", "7231-9955")
josé = Cliente("José Vargas","9721-3040")
pedro = Cliente("Pedro Almeida","8888-3545")
contaJM = Conta( [joão, maria], 100)
contaJ = Conta( [josé], 10)
contaEspecial = ContaEspecial( [pedro], 15, saldo=500, limite=200)
contaJM.deposito(500)
contaJM.saque(150)
contaJ.deposito(100)
contaJM.saque(25)
contaEspecial.saque(650)
tatu = Banco("Tatú")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.abre_conta(contaEspecial)
tatu.lista_contas()
