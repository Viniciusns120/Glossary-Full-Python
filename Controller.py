from Models import *
from DAO import *
from datetime import datetime


class controllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = daoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
            
        if not existe:
            daoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso')
        else:
            print('A categoria já existe')

    def removerCategoria(self, categoriaRemover):
        x = daoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
        if len(cat) <= 0:
            print('A categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso')

            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
        
        estoque = daoEstoque.ler()
        
        est = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, 'Sem categoria'), x.quantidade)
                                         if(x.produto.categoria == categoriaRemover) else(x), estoque))
        
        with open('estoque.txt', 'w') as arq:
            for i in est:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = daoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada)if(x.categoria == categoriaAlterar) else(x), x))
                print('A alteração foi efetuada com sucesso')
                
            else:
                print('A categoria para a qual deseja alterar já existe')

        else:
            print('A categoria que deseja alterar não existe')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

        estoque = daoEstoque.ler()

        est = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoriaAlterada), x.quantidade)
                       if(x.produto.categoria == categoriaAlterar) else(x), estoque))
        
        with open('estoque.txt', 'w') as arq:
            for i in est:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = daoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria vazia')
        else:
            print('='* 5 + 'Categorias' + '=' *5)
            for i in categorias:
                print(f'Categoria: {i.categoria}')
                print('-' * 20)


class controllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = daoEstoque.ler()
        y = daoCategoria.ler()

        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                daoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso')
            
            else:
                print('Produto já existe em estoque')
        else:
            print('Categoria Inexistente')
    
    def removerProduto(self, nome):
        x = daoEstoque.ler()

        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print('Produto foi removido com sucesso.')
        else:
            print('O produto que deseja remover não exite.')

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = daoEstoque.ler()
        y = daoCategoria.ler()
        
        h = list(filter(lambda x: x.categoria == novaCategoria, y))

        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) 
                                 if(x.produto.nome == nomeAlterar) else (x), x ))
                    print('Produto alterado com sucesso')
                else:
                    print('produto já cadastrado')
            else:
                print('O produto que deseja alterar não existe')
            
            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                    arq.writelines('\n')

        else:
            print('A categoria informada não existe')

    def mostrarEstoque(self):
        estoque = daoEstoque.ler()
        if len(estoque) == 0:
            print('Não há produtos em estoque')
        else:
            print('=' * 5 , 'Produto', '=' * 5)
            for i in estoque:
                print(f'Nome: {i.produto.nome}\n'
                      f'Preco: {i.produto.preco}\n'
                      f'Categoria: {i.produto.categoria}\n'
                      f'Quantidade: {i.quantidade}'
                      )
                print('-' * 20)


class controllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = daoEstoque.ler()
        
        temp = []

        existe = False
        quantidade = False

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)

                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)

                        daoVenda.salvar(vendido)

            temp.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])

        arq = open('estoque.txt', 'w')
        arq.write('')

        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i[0].nome + '|' + i[0].preco + '|' + i[0].categoria + '|' + str(i[1]))
                arq.writelines('\n')
            
        if existe == False:
            print('O produto não existe')
            return None
        elif not quantidade:
            print('A quantiade vendida não contém em estoque')
            return None
        else:
            print('Venda realizada com sucesso')
            return valorCompra

    def relatorioProdutos(self):
        vendas = daoVenda.ler()

        produtos = []

        for i in vendas:
            nome = i.itensVendido.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)}
                                    if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': quantidade})

        ordenado = sorted(produtos, key = lambda k: ['quantidade'], reverse = True)

        print('Esses são os produtos mais vendidos')

        a = 1

        for i in ordenado:
            print(f'==========Produto [{a}]==========\n' )
            print(f'Produto: {i['produto']}\n')
            print(f'Quantidade: {i['quantidade']}\n')

            a += 1

    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = daoVenda.ler()

        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1 and 
                                         datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas))
        
        cont = 1
        total = 0

        for i in vendasSelecionadas:
            print(f'==========Venda [{cont}]==========')
            print(f'Nome: {i.itensVendido.nome}\n'
                f'Categoria: {i.itensVendido.categoria}\n'
                f'Data: {i.data}\n'
                f'Quantidade: {i.quantidadeVendida}\n'
                f'Cliente: {i.comprador}\n'
                f'Vendedor: {i.vendedor}\n')
            
            total += int(i.itensVendido.preco) * int(i.quantidadeVendida)
            cont += 1
        
        print(f'Total vendido: {total}')


class controllerFornecedor:
    def  cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = daoFornecedor.ler()

        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.telefone == telefone, x))

        if len(listaCnpj) > 0:
            print('O Cnpj no qual você deseja cadastrar já existe')
        elif len(listaTelefone) > 0:
            print('O telefone no qual você deseja cadastrar já existe')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                daoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
                print('Fornecedor cadastrado com sucesso.')
            else:
                print('Digite um cnpj ou telefone válido')

    def removerFornecedor(self, nome):
        x = daoFornecedor.ler()

        forn = list(filter(lambda x: x.nome == nome, x))

        if len(forn) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
            print('Fonecedor removido com sucesso')
        else:
            print('O Fornecedor que deseja remover não existe')

        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + i.categoria)
                arq.writelines('\n')
        
    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria):
        x = daoFornecedor.ler()

        forn = list(filter(lambda x: x.nome == nomeAlterar, x))

        if len(forn) > 0:
            x = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria) if(x.nome == nomeAlterar) else (x), x))
            print('Fornecedor alterado com sucesso')
        else:
            print('O Forncedor que deseja alterar não existe')

        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + i.categoria)
                arq.writelines('\n')

    def mostrarFornecedor(self):
        x = daoFornecedor.ler()

        if len(x) == 0:
            print('Não há fornecedores cadastrados')
        
        else:
            print('=' * 5 , 'Fornecedores', '=' * 5)
            for i in x:
                print(f'Nome: {i.nome}\n'
                      f'Cnpj: {i.cnpj}\n'
                      f'Telefone: {i.telefone}\n'
                      f'Categoria: {i.categoria}')
                print('-' * 20 + '\n')
                

class controllerCliente:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x = daoPessoa.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))

        if len(listaCpf) > 0:
            print('O cpf que deseja cadastrar já existe')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                daoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('Cliente cadastrado com sucesso.')
            else:
                print('Digite um cpf ou telefone válido.')
    
    def removerCliente(self, cpf):
        x = daoPessoa.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))

        if len(listaCpf) > 0:
            for i in range(len(x)):
                if x[i].cpf == cpf:
                    del x[i]
                    print(f'Cpf: {cpf}, removido com sucesso')
                    break
        else:
            print('O cliente que você deseja remover não existe')

        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')

    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = daoPessoa.ler()

        client = list(filter(lambda x: x.nome == nomeAlterar, x))

        if len(client) > 0:
            list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if(x.nome == nomeAlterar) else(x), x))
            print('Cliente alterado com sucesso')
        else:
            print('O cliente que deseja alterar não existe')
        
        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')

    def mostrarCliente(self):
        x = daoPessoa.ler()

        if len(x) > 0:
            print('=' * 5 , 'Clientes', '=' * 5)
            for i in x:
                print(f'Nome: {i.nome}\n'
                      f'Telefone: {i.telefone}\n'
                      f'Cpf: {i.cpf}\n'
                      f'Email: {i.email}\n'
                      f'Endereço: {i.endereco}')
                print('-' * 20)
        else:
            print('Lista de clientes vazia')


class controllerFuncionario:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = daoFuncionario.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaClt = list(filter(lambda x: x.clt == clt, x))

        if len(listaCpf) > 0:
            print('cpf já consta no banco de dados da empresa')
        elif len(listaClt) > 0:
            print('Já existe um funcionário com essa clt')
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                daoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print('Funcionario cadastrado com sucesso')
            else:
                print('Digite um telefone ou cpf válido')

    def removerFuncionario(self,nome):
        x = daoFuncionario.ler()

        func = list(filter(lambda x: x.nome == nome, x))

        if len(func) > 0:
            for i in range(len(x)):
                if x[i].nome == nome :
                    del x[i]
                    print(f'Funcionário {nome} removido com sucesso')
                    break
        else:
            print('O funcionário que deseja remover não está cadastrado')

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + '|' + i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')
            
    def alterarFuncionario(self, nomeAlterar, novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = daoFuncionario.ler()

        func = list(filter(lambda x: x.nome == nomeAlterar, x))

        if len(func) > 0:
            list(map(lambda x: Funcionario(novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if(x.nome == nomeAlterar) else(x), x))
            print(f'Funcionario {nomeAlterar} alterado com sucesso')
        else:
            print('O funcionário não existe')

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + '|' + i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')

    def mostrarFuncionario(self):
        x = daoFuncionario.ler()

        if len(x) > 0:
            print('='*10 + 'Funcionarios' + '=' *10)
            for i in x:
                print(f'Clt: {i.clt}\n'
                      f'Nome: {i.nome}\n'
                      f'Telefone: {i.telefone}\n'
                      f'Cpf: {i.cpf}\n'
                      f'Email: {i.email}\n'
                      f'Endereço: {i.endereco}')
                print('-' * 32)
        else:
            print('Não existe funcionários cadastrados')


