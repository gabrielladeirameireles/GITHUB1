def validar_titulo():
    while True:
        titulo = input("Digite o titulo da tarefa: ").strip()
        if titulo:
            return titulo
        print("[ERRO] O titulo e obrigatorio e nao pode conter apenas espacos. Tente novamente.")

def validar_prioridade():
    opcoes_validas = ["alta", "média", "media", "baixa"]
    while True:
        prioridade = input("Digite a prioridade (Alta, Media, Baixa): ").strip()
        if prioridade.lower() in opcoes_validas:
            if prioridade.lower() in ["média", "media"]:
                return "Media"
            return prioridade.capitalize()
        print("[ERRO] Prioridade invalida! Escolha apenas entre Alta, Media ou Baixa.")

def cadastrar_tarefa(tarefas):
    print("\n--- CADASTRAR NOVA TAREFA ---")
    titulo = validar_titulo()
    descricao = input("Digite a descricao da tarefa: ").strip()
    prioridade = validar_prioridade()
    data_limite = input("Digite a data limite (ex: DD/MM/AAAA): ").strip()
    status = "Pendente"

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": status
    }
    tarefas.append(tarefa)
    print("[SUCESSO] Tarefa cadastrada com sucesso!")

def listar_tarefas(tarefas):
    print("\n--- LISTA DE TAREFAS ---")
    if not tarefas:
        print("[INFO] Nenhuma tarefa cadastrada no momento.")
        return

    for idx, t in enumerate(tarefas, start=1):
        print(f"\n[Tarefa #{idx}]")
        print(f"  - Titulo:      {t['titulo']}")
        print(f"  - Descricao:   {t['descricao']}")
        print(f"  - Prioridade:  {t['prioridade']}")
        print(f"  - Data Limite: {t['data_limite']}")
        print(f"  - Status:      {t['status']}")
        print("-" * 35)

def main():
    tarefas = []
    while True:
        print("\n==============================")
        print("    TASKTRACKER - MENU        ")
        print("==============================")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicacao")
        
        opcao = input("Escolha uma opcao (1-3): ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("\nSaindo da aplicacao...")
            break
        else:
            print("[ERRO] Opcao invalida! Escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
