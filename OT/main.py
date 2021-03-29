from Funcoes.IdentificacaoDeFuncoes import *


minhaLista=[]
print("Preenchendo...")
preencherInventario(minhaLista)

print("Exibindo")
exibirInventario(minhaLista)

print("pesquisando...")
localizarPorNome(minhaLista)

print("Alterando...")
depreciarPorNome(minhaLista,0.5)

print("EXcluindo...")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("Resumindo")
exibirValores(minhaLista)
