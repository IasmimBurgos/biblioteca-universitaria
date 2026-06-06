======================================================================
              📚 SISTEMA DE GESTÃO DE BIBLIOTECA 🚀
======================================================================

Este é um sistema de gerenciamento de biblioteca desenvolvido em Django 
e Django REST Framework. O projeto conta com rotas para administração 
de acervos, gerenciamento de alunos, autores e livros, além de incluir 
um script automatizado para povoamento inicial do banco de dados com 
dados fictícios e livros reais. ✨

----------------------------------------------------------------------
1. 🛠️ TECNOLOGIAS UTILIZADAS
----------------------------------------------------------------------
* 🐍 Python 3.x
* ⚡ Django 6.0.6
* 🔌 Django REST Framework 3.17.1
* 🖼️ Pillow 12.2.0 (Processamento de imagens/capas de livros)
* 🗄️ SQLite 3 (Banco de dados padrão)
* 🐳 Docker & Docker Compose

----------------------------------------------------------------------
2. 🚀 COMO EXECUTAR O PROJETO
----------------------------------------------------------------------
Você pode rodar o projeto localmente utilizando um ambiente virtual 
Python tradicional ou através do Docker. 💻

🐳 OPÇÃO 1: Utilizando Docker (Recomendado)
Certifique-se de ter o Docker e o Docker Compose instalados.

1. Instale as dependências e suba o container:
   docker compose up --build

2. O servidor estará acessível em: http://localhost:8000 🌐

📦 OPÇÃO 2: Instalação Local (Ambiente Virtual)

1. Crie e ative o seu ambiente virtual (venv):
   python -m venv venv
   
   # No Linux/macOS:
   source venv/bin/activate
   
   # No Windows (Prompt de comando):
   venv\Scripts\activate

2. Instale as dependências listadas no projeto:
   pip install -r requirements.txt 📥

3. Execute as migrações para estruturar o banco de dados:
   python manage.py migrate ⚙️

4. Inicie o servidor de desenvolvimento:
   python manage.py runserver 🔥

----------------------------------------------------------------------
3. 📊 POVOANDO O BANCO DE DADOS (SEED)
----------------------------------------------------------------------
O projeto possui um script utilitário para cadastrar automaticamente 
100 livros reais (divididos entre literatura brasileira, ficção 
científica, tecnologia, terror, entre outros) e 100 alunos fictícios 
de diversos cursos. 🧪

Para rodar o povoamento e preencher o seu banco de dados, execute:

python popular_banco.py 🏃‍♂️

(Caso esteja utilizando Docker, você pode rodar o comando de seed 
de dentro do container utilizando o comando: 
docker compose exec web python popular_banco.py 🐳)

----------------------------------------------------------------------
4. 📁 ESTRUTURA DE ARQUIVOS PRINCIPAIS
----------------------------------------------------------------------
* 📂 biblioteca_config/ : Configurações centrais do ecossistema Django.
* 📂 core/              : App principal com modelos (Livro, Autor, Aluno).
* 📜 popular_banco.py   : Script responsável por gerar a massa de dados.
* 🐳 docker-compose.yml : Orquestração do ambiente conteinerizado.
* 📋 requirements.txt   : Lista de dependências do Python.
======================================================================