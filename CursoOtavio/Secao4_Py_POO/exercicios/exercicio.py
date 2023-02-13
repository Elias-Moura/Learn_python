"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tenm clientes, contas e um banco.
A ideia é que o cliente tenha uma conta (poupança ou corrente) e que possa sacar/depositar
nessa conta. Contas correntes tem um limente extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Cliente -> Conta  # Cliente agraga conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Clientes TEM conta (Agregação da classe ContaCorrente o ContaPoupanca
Criar classes ContaPoupança e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método para sacar abstrato (Abstracão e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas da seguinte maneira:
Banco será responsável autenticar o cliente e as contas da se
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco

"""

