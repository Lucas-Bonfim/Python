import pandas as pd

#lê a lista de colunas definida pelo cliente
minha_lista = pd.read_csv('lista_de_colunas.txt')
minha_lista = list(minha_lista)
print(minha_lista)



df = pd.read_excel('testeDados.xlsx')

# Verifica se o dataframe possui todas as colunas da lista
if set(df.columns) == set(minha_lista):
    print("Estrutura de colunas do excel correta!")
else:
    raise ValueError("O dataframe possui colunas não identificadas")
# Verifica se existe pelo menos uma célula nula em cada linha do dataframe
if df.isnull().any(axis=1).any():
    print("Existem linhas com pelo menos uma célula nula")
    # Identifica o nome e a linha da célula que está nula
    null_cell = df.isnull().stack()
    null_cell = null_cell[null_cell]
    raise ValueError("Valor nulo encontrado na coluna:", null_cell.index[0])

else:
    print("Não existem linhas com células nulas")
    
