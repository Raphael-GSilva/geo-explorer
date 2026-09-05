from mcp.server.mcpserver import MCPServer
import json

# Inicializa o nosso servidor MCP (versão 2.x)
mcp = MCPServer("Geo-Explorer")

def carregar_trilhas():
    with open('data/trilhas.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        return dados['trilhas']

@mcp.tool()
def consultar_trilha(tecnologia: str) -> str:
    """Consulta os módulos de uma trilha específica (ex: Python, JavaScript)."""
    trilhas = carregar_trilhas()
    for trilha in trilhas:
        if trilha['tecnologia'].lower() == tecnologia.lower():
            modulos_str = ", ".join(trilha['modulos'])
            return f"Trilha de {tecnologia.upper()} (Nível {trilha['nivel']}): {modulos_str}"
    return f"Trilha de {tecnologia} não encontrada no banco de dados."

@mcp.tool()
def gerar_desafio(tecnologia: str) -> str:
    """Gera um desafio prático de programação para a tecnologia informada."""
    return f"Desafio de {tecnologia.upper()}: Crie uma função que receba uma lista de números e retorne apenas os pares."

if __name__ == "__main__":
    mcp.run()
