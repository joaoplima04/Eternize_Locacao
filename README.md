# Projeto de Aluguel de Itens de Mesa e Cozinha

Este é um projeto de uma aplicação web para aluguel de itens de mesa e cozinha, desenvolvido utilizando Django.

## Estrutura do Projeto

projeto_django/
├── categorias/
│ ├── migrations/
│ ├── templates/
│ │ ├── base.html
│ │ ├── carrinho.html
│ │ ├── categoria.html
│ │ ├── index.html
│ │ ├── login.html
│ │ └── register.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
├── static/
│ └── ...
├── projeto_django/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
└── README.md

## Funcionalidades Implementadas

1. **Autenticação de Usuários:**
   - Login e Logout.
   - Registro de novos usuários.
   - Redirecionamento para a página de login se o usuário não estiver autenticado.

2. **Visualização de Produtos por Categoria:**
   - Lista de produtos filtrados por categoria.
   - Visualização detalhada de cada produto.

3. **Carrinho de Compras:**
   - Adicionar itens ao carrinho.
   - Remover itens do carrinho.
   - Atualizar quantidade de itens no carrinho.
   - Visualizar itens no carrinho e o preço total.

4. **Banco de Dados:**
   - Utilização do SQLite como banco de dados relacional.

## Pré-requisitos

- Python 3.x
- Django 3.x ou superior
- SQLite

## Configuração e Execução

### Clonando o Repositório

```sh
git clone https://github.com/seu_usuario/projeto_django.git
cd projeto_django

Estrutura do Banco de Dados
Modelos Principais
Cliente: Representa os usuários do sistema.
Produto: Representa os itens disponíveis para aluguel.
Carrinho: Representa o carrinho de compras dos usuários

Modelo Produto:
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=150, choices=OPCOES_CATEGORIA, default='')
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    quantidade_estoque = models.IntegerField(null=False, blank=False, default=0)
    imagem = models.ImageField(upload_to="imagens/", blank=True)
    cor = models.CharField(max_length=100)
    estilo = models.CharField(max_length=100, choices=OPCOES_ESTILO, default='')
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

Modelo Cliente:
class Cliente(AbstractUser):
    cpf = models.CharField(max_length=11, primary_key=True, default='')
    username = models.CharField(max_length=150, unique=True) 
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  
    telefone = models.CharField(max_length=20)  
    data_nascimento = models.DateField(default=timezone.now)  
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cpf', 'nome', 'telefone', 'data_nascimento']

    def __str__(self):
        return self.nome

Contribuição
Faça um fork do projeto.
Crie uma branch para sua feature (git checkout -b feature/fooBar).
Faça o commit das suas alterações (git commit -m 'Add some fooBar').
Dê um push para a branch (git push origin feature/fooBar).
Abra um Pull Request.

Contato
João Lucas - joaolucass0420@gmail.com
