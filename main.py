# Sistema Clínica Vida+
# Cadastro e consulta de pacientes pelo terminal.


def cadastrar_paciente(pacientes):
    """Cadastra um novo paciente validando nome, idade e telefone."""
    nome = input("\nDigite o nome do paciente: ").strip()

    if nome == "":
        print("\nO nome é obrigatório.")
        return

    try:
        idade = int(input("Digite a idade do paciente: "))

        if idade <= 0:
            print("\nIdade inválida.\n")
            return

        telefone = input("Digite o número de telefone do paciente: ").strip()

        if telefone == "" or not telefone.isdigit():
            print("\nNúmero de telefone inválido.")
            return

        paciente = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone,
        }

        pacientes.append(paciente)

        print("\nPaciente cadastrado com sucesso!\n")

    except ValueError:
        print("\nErro! Digite apenas números inteiros.")


def visualizar_estatisticas(pacientes):
    """Mostra total, média de idades, paciente mais jovem e mais velho."""
    if len(pacientes) == 0:
        print("\nNão há pacientes cadastrados.\n")
        return

    total_pacientes_cadastrados = len(pacientes)
    soma_idades = 0

    paciente_mais_jovem = pacientes[0]
    paciente_mais_velho = pacientes[0]

    for paciente in pacientes:
        soma_idades += paciente["idade"]

        if paciente["idade"] < paciente_mais_jovem["idade"]:
            paciente_mais_jovem = paciente
        if paciente["idade"] > paciente_mais_velho["idade"]:
            paciente_mais_velho = paciente

    media_idades = soma_idades / total_pacientes_cadastrados

    print(
        "\n=== ESTATÍSTICAS ===\n"
        f"\nTotal de pacientes cadastrados: {total_pacientes_cadastrados}\n"
        f"Média de idades dos pacientes: {media_idades:.1f}\n"
        f"Paciente mais jovem: {paciente_mais_jovem['nome']}\n"
        f"Paciente mais velho: {paciente_mais_velho['nome']}\n"
    )


def buscar_paciente(pacientes):
    """Busca pacientes pelo nome (ignora maiúsculas e minúsculas)."""
    if len(pacientes) == 0:
        print("\nNão há pacientes cadastrados.\n")
        return

    busca_paciente = input("\nDigite o nome do paciente que deseja buscar: ").strip().lower()

    if busca_paciente == "":
        print("\nO nome é obrigatório.\n")
        return

    encontrado = False

    print("\n=== PACIENTES ENCONTRADOS ===\n")

    for paciente in pacientes:
        if busca_paciente in paciente["nome"].lower():
            encontrado = True

            print(
                f"Nome: {paciente['nome']}\n"
                f"Idade: {paciente['idade']}\n"
                f"Telefone: {paciente['telefone']}\n"
                "--------------------"
            )

    if not encontrado:
        print("Paciente não encontrado")


def listar_pacientes(pacientes):
    """Lista todos os pacientes cadastrados."""
    if len(pacientes) == 0:
        print("\nNão há pacientes cadastrados.\n")
        return

    print("\n=== PACIENTES ===\n")

    for paciente in pacientes:
        print(
            f"Nome: {paciente['nome']}\n"
            f"Idade: {paciente['idade']}\n"
            f"Telefone: {paciente['telefone']}\n"
            "--------------------"
        )


def main():
    """Menu principal do sistema."""
    # Lista onde ficam armazenados os pacientes cadastrados
    pacientes = []

    while True:
        print(
            "\n=== SISTEMA CLÍNICA VIDA+ ===\n"
            "\n1. Cadastrar paciente\n"
            "2. Ver estatísticas\n"
            "3. Buscar paciente\n"
            "4. Listar todos os pacientes\n"
            "5. Sair\n"
        )

        opcao = input("Escolha uma das opções: ")

        if opcao == "1":
            cadastrar_paciente(pacientes)
        elif opcao == "2":
            visualizar_estatisticas(pacientes)
        elif opcao == "3":
            buscar_paciente(pacientes)
        elif opcao == "4":
            listar_pacientes(pacientes)
        elif opcao == "5":
            print("\nEncerrando sistema...\n")
            break
        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    main()
