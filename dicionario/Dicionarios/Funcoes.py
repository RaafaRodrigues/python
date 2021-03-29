def perguntar():
    return input("O que deseja realizar? \n" +
                 "<I> - Para inserir um usario\n" +
                 "<P> - Para pesquisar um usuario\n" +
                 "<E> - Para excluir um usario\n" +
                 "<L> - Para listar um usuario\n"
                 "<Q> - Para sair \n"
                 ).upper()

def listar(dicionario):
    if dicionario:
        return dicionario
    else:
        return "Dicionario vazio \n"


def exluir(dicionario,chave):
    exist =dicionario.get(chave)
    if(exist):
        dicionario.pop(chave)
        return "Excluido \n"
    else:
        return "Não encontrado \n"



def pesquisar(dicionario,chave):
    exist = dicionario.get(chave)
    if exist:
        return exist
    else:
        return "Não encontrado"

def inserir(dicionario):
    login = input("Digite o login: ").upper()
    dicionario[login] = [input("Digite o nome: ").upper(),
                                                     input("Digite a ultima data de acesso: "),
                                                     input("Qual a ultima estação acessada: ").upper()]
    salvar(dicionario)


def salvar(dicionario):
    with open("bd.txt","w") as arquivo:
        for chave,valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor)+"\n")




def lerArquivo(chave):
    with open("bd.txt","r") as arquivo:
        for linha in arquivo.readlines():
            registroLinha = linha.split(":")
            if(registroLinha[0] == chave ):
                return linha
    return "Não encontrado"


def listarBd():

    with open("bd.txt","r") as arquivo:
        for linha in arquivo.readlines():
            if(linha):
                print(linha)



def excluirDoArquivo(chave):
    contador =0
    with open("bd.txt","r") as arq:
        dicionario={}
        for linha in arq.readlines():
            if(len(linha.strip())>0):
                registro = linha.split(":")
                if (registro[0].strip() != chave.strip()):
                    dicionario[registro[0]] = registro[1]
                else:
                    contador = contador + 1


        if(contador>0):
            salvar(dicionario)
            return "Apagado com sucesso"
        else:
            return "Chave não encontrada"