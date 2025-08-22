def Criar_um_cadastro():
    nome = input("Qual seu nome: ")
    idade = input("Qual sua idade: ")
    genero = input("Qual seu genero: [Masculino/Feminino/Outro]")
    return {"nome": nome, "idade": idade, "genero": genero}
print(Criar_um_cadastro())
def Escolher_opcao():
    print("Você gosta de ler?")
    print("1- Sim")
    print("2-Não")
    leitura = int(input("Digite o número da opção: "))
    if leitura == 1:
        print("Perfeito, este app é para você!")
        print("De quais generos você gosta?")
        generos = input("Digite os gêneros que você gosta, separados por vírgula: ")
        print("Ótimo, você gosta dos seguintes gêneros:")
        generos_dict = {"Ação": True, "Aventura": True, "Ficção Científica": True, "Romance": True, "Comédia": True, "Drama": True, "Terror": True, "Fantasia": True, "Mistério": True, "Biografia": True}
        for genero, gosta in generos_dict.items():
            if gosta and genero == "Drama":
                print(lista_de_dramas := ["A Culpa é das Estrelas, John Green", "As Vantagens de ser Invisível, Stephen Chbosky", "Mil Beijos de Garoto, Tillie Cole"])
            elif gosta and genero == "Fantasia":
                print(lista_de_fantasia := ["Harry Potter (7 livros), J.K. Rowling"])

    else:
        print("Que pena, posso te mostrar alguns livros que te farão mudar de ideia?")
        print("1- Sim")
        print("2- Não")
        Escolher_opcao = int(input("Digite o número da opção: "))
        if Escolher_opcao == 1:
            print("Ótimo, vamos lá!")
        else:
            print("Tudo bem, talvez em outra hora.")
        return Escolher_opcao
        print(Escolher_opcao())
Escolher_opcao()

