import Controller
import os.path

def criarArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write('')

criarArquivos('categoria.txt', 'clientes.txt', 'estoque.txt', 'fornecedores.txt', 'funcionarios.txt', 'venda.txt')

if __name__ == '__main__':
    while True:
        local = int(input('Digite 1 para acessar ( Categorias )\n'
                          'Digite 2 para acessar ( Estoque )\n'
                          'Digite 3 para acessar ( Fornecedores )\n'
                          'Digite 4 para acessar ( Clientes )\n'
                          'Digite 5 para acessar ( Funcionarios )\n'
                          'Digite 6 para acessar ( Vendas )\n'
                          'Digite 7 para ver os produtos mais vendidos\n'
                          'Digite 8 para sair\n> '))
        
        if local == 1:
            cat = Controller.controllerCategoria()
            while True:
                decidir = int(input('Digite 1 para cadastrar uma categoria\n'
                                    'Digite 2 para remover uma categoria\n'
                                    'Digite 3 para alterar uma categoria\n'
                                    'Digite 4 para mostrar as categorias cadastradas\n'
                                    'Digite 5 para sair\n> '))
                
                if decidir == 1:
                    categoria = input('Digite a categoria que deseja cadastrar\n> ')
                    cat.cadastrarCategoria(categoria)
                elif decidir == 2:
                    categoria = input('Digite a categoria que deseja remover\n> ')
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input('Digite a categoria que deseja alterar\n> ')
                    categoriaAlterada = input('Digite para qual categoria que deseja alterar\n> ')
                    cat.alterarCategoria(categoria, categoriaAlterada)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    break

        if local == 2:
            cat = Controller.controllerEstoque()
            while True:
                decidir = int(input('Digite 1 para cadastrar um produto\n'
                                    'Digite 2 para remover um produto\n'
                                    'Digite 3 para alterar um produto\n'
                                    'Digite 4 para mostrar o estoque\n'
                                    'Digite 5 para sair\n> '))
                
                if decidir == 1:
                    nome = input('Digite o nome do produto que deseja cadastrar\n> ')
                    preco = input('Digite o preço do produto que deseja cadastrar\n> ')
                    categoria = input('Digite a categoria do produto que deseja cadastrar\n> ')
                    quantidade = input('Digite a quantidade do produto que deseja cadastrar\n> ')
                    cat.cadastrarProduto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    produto = input('Digite o nome do produto que deseja remover\n> ')
                    cat.removerProduto(produto)
                elif decidir == 3:
                    antigoNome = input('Digite o nome do produto que deseja alterar\n> ')
                    nome = input('Digite o nome do novo produto que deseja cadastrar\n> ')
                    preco = input('Digite o preço do novo produto que deseja cadastrar\n> ')
                    categoria = input('Digite a nova categoria do produto que deseja cadastrar\n> ')
                    quantidade = input('Digite a nova quantidade do produto que deseja cadastrar\n> ')
                    cat.alterarProduto(antigoNome, nome, preco, categoria, quantidade)
                elif decidir == 4:
                    cat.mostrarEstoque()
                
                else:
                    break

        if local == 3:
            cat = Controller.controllerFornecedor()
            while True:
                decidir = int(input('Digite 1 para cadastrar um fornecedor\n'
                                    'Digite 2 para remover um fornecedor\n'
                                    'Digite 3 para alterar um fornecedor\n'
                                    'Digite 4 para mostrar todos os fornecedores\n'
                                    'Digite 5 para sair\n> '))
                
                if decidir == 1:
                    nome = input('Digite o nome do fornecedor que deseja cadastrar\n> ')
                    cnpj = input('Digite o cnpj do fornecedor que deseja cadastrar\n> ')
                    telefone = input('Digite o telefone do fornecedor que deseja cadastrar\n> ')
                    categoria = input('Digite a categoria do fornecedor que deseja cadastrar\n> ')
                    cat.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    nome = input('Digite o nome do fornecedor que deseja remover\n> ')
                    cat.removerFornecedor(nome)
                elif decidir == 3:
                    antigoNome = input('Digite o nome do fornecedor que deseja alterar\n> ')
                    nome = input('Digite o nome do novo fornecedor que deseja cadastrar\n> ')
                    cnpj = input('Digite o novo cnpj do fornecedor que deseja cadastrar\n> ')
                    telefone = input('Digite o novo telefone do fornecedor que deseja cadastrar\n> ')
                    categoria = input('Digite a nova categoria do fornecedor que deseja cadastrar\n> ')
                    cat.alterarFornecedor(antigoNome, nome, cnpj, telefone, categoria)
                elif decidir == 4:
                    cat.mostrarFornecedor()

                else:
                    break

        if local == 4:
            cat = Controller.controllerCliente()
            while True:
                decidir = int(input('Digite 1 para cadastrar um cliente\n'
                                    'Digite 2 para remover um cliente\n'
                                    'Digite 3 para alterar um cliente\n'
                                    'Digite 4 para mostrar todos os clientes\n'
                                    'Digite 5 para sair\n> '))
                
                if decidir == 1:
                    nome = input('Digite o nome do cliente que deseja cadastrar\n> ')
                    telefone = input('Digite o telefone do cliente que deseja cadastrar\n> ')
                    cpf = input('Digite o cpf do cliente que deseja cadastrar\n> ')
                    email = input('Digite e-mail do cliente que deseja cadastrar\n> ')
                    endereco = input('Digite o endereço do cliente que deseja cadastrar\n> ')
                    cat.cadastrarCliente(nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    nome = input('Digite o nome do cliente que deseja remover\n> ')
                    cat.removerCliente(nome)
                elif decidir == 3:
                    nomeAlterar = input('Digite o nome do cliente que deseja alterar\n> ')
                    nome = input('Digite o nome do novo cliente que deseja cadastrar\n> ')
                    telefone = input('Digite o novo telefone do cliente que deseja cadastrar\n> ')
                    cpf = input('Digite o novo cpf do cliente que deseja cadastrar\n> ')
                    email = input('Digite o novo email do cliente que deseja cadastrar\n> ')
                    endereco = input('Digite o novo endereço do cliente que deseja cadastrar\n> ')
                    cat.alterarCliente(nomeAlterar, nome, telefone, cpf, email, endereco)
                elif decidir == 4:
                    cat.mostrarCliente()

                else:
                    break

        if local == 5:
            cat = Controller.controllerFuncionario()
            while True:
                decidir = int(input('Digite 1 para cadastrar um funcionario\n'
                                    'Digite 2 para remover um funcionario\n'
                                    'Digite 3 para alterar um funcionario\n'
                                    'Digite 4 para mostrar todos os funcionarios\n'
                                    'Digite 5 para sair\n> '))
                
                if decidir == 1:
                    clt = input('Digite a clt do funcionario que deseja cadastrar\n> ')
                    nome = input('Digite o nome do funcionario que deseja cadastrar\n> ')
                    telefone = input('Digite o telefone do funcionario que deseja cadastrar\n> ')
                    cpf = input('Digite o cpf do funcionario que deseja cadastrar\n> ')
                    email = input('Digite e-mail do funcionario que deseja cadastrar\n> ')
                    endereco = input('Digite o endereço do funcionario que deseja cadastrar\n> ')
                    cat.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    nome = input('Digite o nome do funcionario que deseja remover\n> ')
                    cat.removerFuncionario(nome)
                elif decidir == 3:
                    antigoNome = input('Digite o nome do funcionario que deseja alterar\n> ')
                    clt = input('Digite a nova clt do funcionario que deseja cadastrar\n> ')
                    nome = input('Digite o nome do novo funcionario que deseja cadastrar\n> ')
                    telefone = input('Digite o novo telefome do funcionario que deseja cadastrar\n> ')
                    cpf = input('Digite o novo cpf do funcionario que deseja cadastrar\n> ')
                    email = input('Digite o novo email do funcionario que deseja cadastrar\n> ')
                    endereco = input('Digite o novo endereço do funcionario que deseja cadastrar\n> ')
                    cat.alterarFuncionario(antigoNome, clt, nome, telefone, cpf, email, endereco)
                elif decidir == 4:
                    cat.mostrarFuncionario()

                else:
                    break

        if local == 6:
            cat = Controller.controllerVenda()
            while True:
                decidir = int(input('Digite 1 para realizar uma venda\n'
                                    'Digite 2 para mostrar as vendas com base em datas específicas\n'
                                    'Digite 3 para sair\n> '))
                
                if decidir == 1:
                    nome = input('Digite o nome do produto vendido\n> ')
                    nomeVendedor = input('Digite o nome do vendedor responsável\n> ')
                    nomeComprador = input('Digite o nome do cliente\n> ')
                    quantidade = input('Digite a quantidade vendida\n> ')
                    cat.cadastrarVenda(nome, nomeVendedor, nomeComprador, int(quantidade))
                elif decidir == 2:
                    dataInicio = input('Digite a data de início (ex:01/01/2001)\n> ')
                    dataTermino = input('Digite a data de término (ex:01/01/2001)\n> ')
                    cat.mostrarVenda(dataInicio, dataTermino)

                else:
                    break
        
        elif local == 7:
            a = Controller.controllerVenda()
            a.relatorioProdutos()

        else:
            break

                   