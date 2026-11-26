# sistema de sku para comércios do ramo alimentício

produto = ''
produtos = []
quantidade = ''
quantidade_geral_produtos = []
preco = ''
preco_geral_produtos = []
estoque_geral = produtos

while True:

    print('\n------ |SISTEMA DE ORGANIZAÇÃO DE ESTOQUE| ------')
    print('1 - Cadastrar produto')
    print('2 - Excluir produto')
    print('3 - Inserir quantidade')
    print('4 - Inserir preço')  
    print('5 - Consultar estoque')
    print('6 - Consultar produto')
    print('7 - Voltar ao menu')
    print('8 - Sair')

    opcao = input(f'Escolha uma opção: ')

    if opcao == '1':
        produto = str(input('Cadastre o produto: '))
        produtos.append(produto)
        print(f'Produto {produto} cadastrado com sucesso!')

    elif opcao == '2':
        produto = str(input('Digite o produto a ser excluído: '))

        if produto not in produtos:
            print('Produtos não cadastrados não podem sem excluídos.')
        else:
            produtos.remove(produto)
            print(f'Produto {produto} removido com sucesso!')

    elif opcao == '3':
        quantidade = int(input('Insira a quantidade do produto: ')) 
        quantidade_geral_produtos.append(quantidade)
        print(f'Quantidade inserida com sucesso! ({quantidade})')

    elif opcao == '4':
        preco = float(input('Digite o preço definido ao produto: '))
        if produto not in produtos:
            print('Produto não cadastrado.')
        else:
            preco_geral_produtos.append(preco)
            print(f'Preço do produto {produto} un. = R$ {preco:.2f}')

    elif opcao == '5':
        print('Consultando estoque...')
        print(f'Produtos no estoque: {estoque_geral}')
        print(f'Quantidade: {quantidade_geral_produtos}')

    elif opcao == '6':
        consulta = input('Consulta de produto: ')

        if consulta.lower() == produto.lower():
            print('\n----- INFORMAÇÕES DO PRODUTO -----')
            print(f'Produto: {produto}')
            print(f'Quantidade: {quantidade}')
            print(f'Preço: R$ {preco:.2f}')
            print((f'Valor estoque: ({preco * quantidade})'))
        else:
          print('Produto não encontrado')

    elif opcao == '7':
        print('Sair para menu')

    elif opcao == '8':
        break 
    else:
        print('Opção inválida. Tente novamente.')    
        


# inserir um if para somente inserir o valor do produto se ele estiver
# cadastrado no sistema

# definir uma condicao para especificamente qual produto sera precificado OU
# mostrar na barra de menu qual produto está sendo precificado
