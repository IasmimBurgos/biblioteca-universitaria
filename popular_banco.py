import os
import django
import random
from datetime import date, timedelta

# Configuração do ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_config.settings')
django.setup()

from core.models import Livro, Autor

def gerar_data_aleatoria():
    """Gera uma data aleatória nos últimos 20 anos"""
    start_date = date(2000, 1, 1)
    end_date = date.today()
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)

# Lista curada de 100 Livros Reais (Título, Autor, Gênero)
# Os gêneros estão combinados para testar a lógica de múltipla seleção
dados_livros = [
    # Literatura Brasileira
    ("Dom Casmurro", "Machado de Assis", "Romance,Clássico"),
    ("Memórias Póstumas de Brás Cubas", "Machado de Assis", "Romance,Clássico"),
    ("O Cortiço", "Aluísio Azevedo", "Romance,Naturalismo"),
    ("Grande Sertão: Veredas", "João Guimarães Rosa", "Romance,Literatura Brasileira"),
    ("Vidas Secas", "Graciliano Ramos", "Romance,Drama"),
    ("Capitães da Areia", "Jorge Amado", "Romance,Aventura"),
    ("A Hora da Estrela", "Clarice Lispector", "Romance,Filosófico"),
    ("O Tempo e o Vento", "Erico Verissimo", "Romance,História"),
    ("Triste Fim de Policarpo Quaresma", "Lima Barreto", "Sátira,Clássico"),
    ("O Guarani", "José de Alencar", "Romance,Indigenista"),
    
    # Fantasia e Ficção Científica
    ("O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", "Fantasia,Aventura"),
    ("O Hobbit", "J.R.R. Tolkien", "Fantasia,Aventura"),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia,Jovem Adulto"),
    ("Harry Potter e o Prisioneiro de Azkaban", "J.K. Rowling", "Fantasia,Mistério"),
    ("Duna", "Frank Herbert", "Sci-Fi,Aventura"),
    ("Neuromancer", "William Gibson", "Sci-Fi,Cyberpunk"),
    ("Fundação", "Isaac Asimov", "Sci-Fi,Clássico"),
    ("O Guia do Mochileiro das Galáxias", "Douglas Adams", "Sci-Fi,Humor"),
    ("1984", "George Orwell", "Distopia,Sci-Fi"),
    ("Admirável Mundo Novo", "Aldous Huxley", "Distopia,Sci-Fi"),
    ("Fahrenheit 451", "Ray Bradbury", "Distopia,Sci-Fi"),
    ("O Nome do Vento", "Patrick Rothfuss", "Fantasia,Aventura"),
    ("A Guerra dos Tronos", "George R.R. Martin", "Fantasia,Política"),
    ("Deuses Americanos", "Neil Gaiman", "Fantasia,Mistério"),
    ("Eu, Robô", "Isaac Asimov", "Sci-Fi,Contos"),
    
    # Tecnologia e Negócios
    ("Código Limpo", "Robert C. Martin", "Técnico,Programação"),
    ("O Programador Pragmático", "Andrew Hunt", "Técnico,Carreira"),
    ("Padrões de Projeto", "Erich Gamma", "Técnico,Engenharia"),
    ("Arquitetura Limpa", "Robert C. Martin", "Técnico,Arquitetura"),
    ("Refatoração", "Martin Fowler", "Técnico,Programação"),
    ("Entendendo Algoritmos", "Aditya Bhargava", "Técnico,Educação"),
    ("Python Fluente", "Luciano Ramalho", "Técnico,Python"),
    ("Use a Cabeça! Padrões de Projetos", "Eric Freeman", "Técnico,Educação"),
    ("O Design do Dia a Dia", "Don Norman", "Design,Negócios"),
    ("A Startup Enxuta", "Eric Ries", "Negócios,Empreendedorismo"),
    ("De Zero a Um", "Peter Thiel", "Negócios,Empreendedorismo"),
    ("Rápido e Devagar", "Daniel Kahneman", "Psicologia,Negócios"),
    ("Sapiens: Uma Breve História da Humanidade", "Yuval Noah Harari", "História,Antropologia"),
    ("Homo Deus", "Yuval Noah Harari", "Futurismo,Filosofia"),
    ("Steve Jobs", "Walter Isaacson", "Biografia,Tecnologia"),
    
    # Terror e Suspense
    ("O Iluminado", "Stephen King", "Terror,Suspense"),
    ("It: A Coisa", "Stephen King", "Terror,Fantasia"),
    ("O Exorcista", "William Peter Blatty", "Terror,Sobrenatural"),
    ("Drácula", "Bram Stoker", "Terror,Clássico"),
    ("Frankenstein", "Mary Shelley", "Terror,Sci-Fi"),
    ("O Silêncio dos Inocentes", "Thomas Harris", "Suspense,Policial"),
    ("Garota Exemplar", "Gillian Flynn", "Suspense,Drama"),
    ("O Código Da Vinci", "Dan Brown", "Suspense,Mistério"),
    ("Anjos e Demônios", "Dan Brown", "Suspense,Mistério"),
    ("Bird Box", "Josh Malerman", "Terror,Distopia"),
    
    # Romance e Drama Internacional
    ("Orgulho e Preconceito", "Jane Austen", "Romance,Clássico"),
    ("Razão e Sensibilidade", "Jane Austen", "Romance,Clássico"),
    ("O Morro dos Ventos Uivantes", "Emily Brontë", "Romance,Gótico"),
    ("Jane Eyre", "Charlotte Brontë", "Romance,Drama"),
    ("A Culpa é das Estrelas", "John Green", "Romance,Jovem Adulto"),
    ("Como Eu Era Antes de Você", "Jojo Moyes", "Romance,Drama"),
    ("O Grande Gatsby", "F. Scott Fitzgerald", "Drama,Clássico"),
    ("Cem Anos de Solidão", "Gabriel García Márquez", "Realismo Mágico,Clássico"),
    ("O Amor nos Tempos do Cólera", "Gabriel García Márquez", "Romance,Drama"),
    ("A Menina que Roubava Livros", "Markus Zusak", "Drama,História"),
    ("O Caçador de Pipas", "Khaled Hosseini", "Drama,História"),
    ("A Cidade do Sol", "Khaled Hosseini", "Drama,História"),
    ("Os Miseráveis", "Victor Hugo", "Drama,História"),
    ("Anna Karenina", "Liev Tolstói", "Romance,Clássico"),
    ("Crime e Castigo", "Fiódor Dostoiévski", "Romance,Psicológico"),
    
    # Desenvolvimento Pessoal e Outros
    ("O Poder do Hábito", "Charles Duhigg", "Autoajuda,Psicologia"),
    ("Como Fazer Amigos e Influenciar Pessoas", "Dale Carnegie", "Autoajuda,Negócios"),
    ("O Milagre da Manhã", "Hal Elrod", "Autoajuda,Produtividade"),
    ("Mindset", "Carol S. Dweck", "Psicologia,Educação"),
    ("Essencialismo", "Greg McKeown", "Produtividade,Negócios"),
    ("Pai Rico, Pai Pobre", "Robert Kiyosaki", "Finanças,Autoajuda"),
    ("Os Segredos da Mente Milionária", "T. Harv Eker", "Finanças,Autoajuda"),
    ("O Homem Mais Rico da Babilônia", "George S. Clason", "Finanças,História"),
    ("A Arte da Guerra", "Sun Tzu", "Estratégia,Filosofia"),
    ("Meditações", "Marco Aurélio", "Filosofia,Estoicismo"),
    
    # Variados / Mais Vendidos Recentes
    ("Torto Arado", "Itamar Vieira Junior", "Drama,Literatura Brasileira"),
    ("O Avesso da Pele", "Jeferson Tenório", "Drama,Social"),
    ("Tudo é Rio", "Carla Madeira", "Romance,Drama"),
    ("A Biblioteca da Meia-Noite", "Matt Haig", "Fantasia,Drama"),
    ("Os Sete Maridos de Evelyn Hugo", "Taylor Jenkins Reid", "Romance,Drama"),
    ("Verity", "Colleen Hoover", "Suspense,Romance"),
    ("É Assim que Acaba", "Colleen Hoover", "Romance,Drama"),
    ("Daisy Jones & The Six", "Taylor Jenkins Reid", "Música,Drama"),
    ("Mulheres Que Correm Com os Lobos", "Clarissa Pinkola Estés", "Psicologia,Feminismo"),
    ("Pequeno Manual Antirracista", "Djamila Ribeiro", "Sociedade,Filosofia"),
    
    # Fechando a lista com Clássicos Infanto-Juvenis e HQs
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Infantil,Filosofia"),
    ("Alice no País das Maravilhas", "Lewis Carroll", "Fantasia,Clássico"),
    ("As Crônicas de Nárnia", "C.S. Lewis", "Fantasia,Aventura"),
    ("Percy Jackson e o Ladrão de Raios", "Rick Riordan", "Fantasia,Aventura"),
    ("Jogos Vorazes", "Suzanne Collins", "Distopia,Aventura"),
    ("Maus", "Art Spiegelman", "HQ,História"),
    ("Persépolis", "Marjane Satrapi", "HQ,Biografia"),
    ("Watchmen", "Alan Moore", "HQ,Super-heróis"),
    ("Batman: O Cavaleiro das Trevas", "Frank Miller", "HQ,Ação"),
    ("V de Vingança", "Alan Moore", "HQ,Distopia"),
    ("Sandman: Prelúdio", "Neil Gaiman", "HQ,Fantasia"),
    ("Diário de um Banana", "Jeff Kinney", "Infantil,Humor"),
    ("Extraordinário", "R.J. Palacio", "Drama,Infantil"),
    ("Malala: A Menina que Queria Ir para a Escola", "Adriana Carranca", "Biografia,Jornalismo"),
    ("Anne de Green Gables", "L.M. Montgomery", "Romance,Infantil")
]

def povoar_banco():
    print("Iniciando o povoamento do banco de dados...")
    print(f"Total de livros para inserir: {len(dados_livros)}")

    # Opcional: Limpar banco antes de povoar (cuidado em produção!)
    # Livro.objects.all().delete()
    # Autor.objects.all().delete()

    contador_livros = 0
    contador_autores = 0

    for titulo, nome_autor, genero in dados_livros:
        # 1. Lógica "Get or Create" para o Autor
        autor_obj, created = Autor.objects.get_or_create(nome=nome_autor)
        if created:
            contador_autores += 1

        # 2. Criar o Livro
        # Verificamos se o livro já existe para não duplicar se rodar o script 2x
        if not Livro.objects.filter(titulo=titulo).exists():
            Livro.objects.create(
                titulo=titulo,
                autor=autor_obj,
                genero=genero,
                estoque=random.randint(0, 50),
                paginas=random.randint(100, 900),
                data_publicacao=gerar_data_aleatoria(),
                descricao=f"Uma obra fascinante de {nome_autor} que explora temas de {genero.split(',')[0]}. Leitura indispensável.",
                capa_do_livro=None # Deixamos null para usar o placeholder do Frontend
            )
            contador_livros += 1
            print(f"[+] Livro criado: {titulo}")
        else:
            print(f"[!] Livro já existe: {titulo}")

    print("-" * 40)
    print("Povoamento concluído com sucesso!")
    print(f"Novos Autores cadastrados: {contador_autores}")
    print(f"Novos Livros cadastrados: {contador_livros}")

if __name__ == '__main__':
    povoar_banco()