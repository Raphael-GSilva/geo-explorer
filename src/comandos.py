import json

# Função auxiliar para ler o arquivo JSON
def carregar_trilhas():
    with open('data/trilhas.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        return dados['trilhas']

# Comando 1: Exibir a Trilha
def comando_trilha(tecnologia_buscada):
    trilhas = carregar_trilhas()
    for trilha in trilhas:
        if trilha['tecnologia'].lower() == tecnologia_buscada.lower():
            print(f"\n--- TRILHA DE {trilha['tecnologia'].upper()} ---")
            print(f"Nível: {trilha['nivel']}")
            print("Módulos para estudar:")
            for modulo in trilha['modulos']:
                print(f" 📘 {modulo}")
            return
    print("\n❌ Trilha não encontrada.")

# Comando 2: Gerar Desafio
def comando_desafio(tecnologia):
    print(f"\n💻 --- DESAFIO DE {tecnologia.upper()} ---")
    print("Missão: Crie um programa que receba uma lista de números e retorne apenas os pares.")
    print("Dica: Use o que você aprendeu nos módulos da trilha!")

# Comando 3: Gerar Certificado
def comando_certificado(nome, tecnologia):
    print("\n" + "="*40)
    print(" 🏆 CERTIFICADO DE CONCLUSÃO 🏆")
    print("="*40)
    print(f" Certificamos que {nome.upper()}")
    print(f" concluiu com maestria a trilha de {tecnologia.upper()}!")
    print("="*40 + "\n")

# O Menu Principal do Geo-Explorer
if __name__ == "__main__":
    print("\n🌍 BEM-VINDO AO GEO-EXPLORER 🌍")
    print("1 - Consultar Trilha")
    print("2 - Gerar Desafio Prático")
    print("3 - Emitir Certificado")

    opcao = input("\nEscolha uma opção (1, 2 ou 3): ")

    if opcao == '1':
        tec = input("Qual tecnologia? (ex: Python): ")
        comando_trilha(tec)
    elif opcao == '2':
        tec = input("Qual tecnologia quer praticar?: ")
        comando_desafio(tec)
    elif opcao == '3':
        nome = input("Digite o seu nome: ")
        tec = input("Qual tecnologia você concluiu?: ")
        comando_certificado(nome, tec)
    else:
        print("❌ Opção inválida!")
