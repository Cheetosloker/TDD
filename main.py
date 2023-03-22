from Bytebank import Funcionario

#maycon = Funcionario('Maycon Barboza', '21/06/1994', 2000)
#print(maycon.idade())

def teste_idade():
    funcionario_teste = Funcionario('teste', '21/06/1994', 1500)
    print(f'teste = {funcionario_teste.idade}')

teste_idade()