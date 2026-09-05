# geo-explorer
Desafio prático da plataforma DIO com foco em desenvolver o Geo-Explorer, um projeto que usa o IBM Bob como apoio para criar, testar e documentar uma solução completa.

🌍 Geo-Explorer
Projeto desenvolvido como parte de um desafio prático da DIO, com apoio de Inteligência Artificial (IBM Bob). O Geo-Explorer é uma ferramenta de exploração de trilhas de aprendizagem que permite consultar planos de estudo, receber desafios de código e gerar certificados fictícios de conclusão — tudo via linha de comando em Python.

🧠 O que é o Geo-Explorer?
O Geo-Explorer simula uma plataforma de aprendizagem interativa. A pessoa usuária escolhe uma tecnologia e pode:

Consultar a trilha de estudos (módulos e nível) para aquela tecnologia.
Receber um desafio de código prático para praticar.
Gerar um certificado fictício de conclusão personalizável.
O projeto também expõe esses recursos como um Servidor MCP (Model Context Protocol), permitindo que agentes de IA acessem os dados de forma programática.

📁 Estrutura do Projeto

geo-explorer/
 ├── data/
 │    └── trilhas.json       # Base de dados fictícia com trilhas de aprendizagem
 ├── src/
 │    ├── comandos.py        # Menu interativo com os 3 comandos principais
 │    └── mcp_server.py      # Servidor MCP para integração com IAs
 ├── docs/                   # Pasta reservada para documentação adicional
 ├── tests/
 │    └── test_comandos.py   # Testes automatizados do projeto
 └── README.md
▶️ Como Executar o Projeto
Pré-requisitos
Python 3.10 ou superior instalado
Terminal (PowerShell, CMD ou terminal integrado do VS Code)
Instalação das dependências
bash

pip install mcp
Rodando o menu interativo
Dentro da pasta geo-explorer, execute:

bash

python src/comandos.py
🛠️ Como Usar os Comandos
Ao rodar o programa, você verá o menu:


🌍 BEM-VINDO AO GEO-EXPLORER 🌍
1 - Consultar Trilha
2 - Gerar Desafio Prático
3 - Emitir Certificado
Opção 1 — Consultar Trilha
Digite o número 1 e informe a tecnologia desejada (ex: Python ou JavaScript). O programa exibirá o nível e os módulos da trilha.

Opção 2 — Gerar Desafio Prático
Digite o número 2 e informe a tecnologia. O programa exibirá um desafio de código para você praticar.

Opção 3 — Emitir Certificado
Digite o número 3, informe seu nome e a tecnologia concluída. O programa gerará um certificado fictício de conclusão personalizado.

🧪 Como Executar os Testes
O projeto usa o módulo nativo unittest do Python. Para rodar os testes automatizados, execute:

bash

python -m unittest tests/test_comandos.py
Resultado esperado:


✅ Teste aprovado: O banco de dados JSON foi lido com sucesso!
.
----------------------------------------------------------------------
Ran 1 test in 0.002s
OK
🤖 Servidor MCP (Integração com IAs)
O arquivo src/mcp_server.py transforma o Geo-Explorer em um servidor MCP (Model Context Protocol), permitindo que agentes de IA consumam os recursos do projeto de forma autônoma.

Ferramentas disponíveis via MCP:
consultar_trilha(tecnologia) — retorna os módulos e o nível de uma trilha.
gerar_desafio(tecnologia) — retorna um desafio de código prático.
Como rodar o servidor:
bash

python src/mcp_server.py
⚠️ O terminal ficará parado aguardando conexões. Isso é o comportamento correto! O servidor está ativo e aguardando que um agente de IA se conecte. Pressione Ctrl + C para encerrar.

🚀 Melhorias Realizadas
Estrutura de projeto organizada em pastas por responsabilidade (data, src, tests, docs).
Menu interativo com validação de opção inválida.
Servidor MCP implementado e atualizado para a versão 2.x da biblioteca (MCPServer).
📚 O que Aprendi Durante o Desafio
Como organizar um projeto Python de forma profissional, com separação de responsabilidades.
Como ler e manipular dados de um arquivo JSON com Python.
Como criar e rodar testes automatizados com o módulo unittest.
O que é o Model Context Protocol (MCP) e como expor funções Python para que agentes de IA possam consumi-las.
Como diagnosticar e resolver um erro de breaking change de biblioteca (a migração de FastMCP para MCPServer na versão 2.x da lib mcp).

Autor: Raphael Gustavo da Silva 

[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raphael-silva-ab5051208)
