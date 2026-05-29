# ============================================================
# Gerador e Analisador de Senhas
# Trabalho Acadêmico - Matemática Computacional Aplicada
# ============================================================

import random
import string

# --- Configurações do usuário ---
print('=== Gerador e Analisador de Senhas ===')
print()

# Tamanho da senha
tamanho = int(input('Informe a quantidade de caracteres desejado da senha: '))

# Escolha dos tipos de caracteres
usar_minusculas = input('Usar letras minúsculas? (s/n): ').strip().lower() == 's'
usar_maiusculas = input('Usar letras maiúsculas? (s/n): ').strip().lower() == 's'
usar_numeros    = input('Usar números? (s/n): ').strip().lower() == 's'
usar_simbolos   = input('Usar símbolos? (s/n): ').strip().lower() == 's'

# --- Montagem do alfabeto disponível ---
alfabeto = ''

if usar_minusculas:
    alfabeto += string.ascii_lowercase   # a-z (26 caracteres)

if usar_maiusculas:
    alfabeto += string.ascii_uppercase   # A-Z (26 caracteres)

if usar_numeros:
    alfabeto += string.digits            # 0-9 (10 caracteres)

if usar_simbolos:
    alfabeto += string.punctuation       # !@#$... (32 caracteres)

# Verificação: ao menos um tipo deve ser escolhido
if not alfabeto:
    print('Erro: selecione ao menos um tipo de caractere.')
    exit()

# --- Cálculo do espaço de busca (E = c^n) ---
c = len(alfabeto)      # tamanho do alfabeto
n = tamanho            # comprimento da senha
espaco_busca = c ** n  # Princípio Fundamental da Contagem

# --- Classificação do nível de segurança ---
if espaco_busca < 1_000_000:
    nivel = 'Muito baixo'
elif espaco_busca < 1_000_000_000:
    nivel = 'Baixo'
elif espaco_busca < 1_000_000_000_000:
    nivel = 'Médio'
elif espaco_busca < 1_000_000_000_000_000:
    nivel = 'Alto'
else:
    nivel = 'Muito alto'

# --- Geração de 3 sugestões de senha ---
senhas = [''.join(random.choices(alfabeto, k=tamanho)) for _ in range(3)]

# --- Função auxiliar para o contorno ---
largura = 52

def linha(caracter='─'):
    return '─' * largura

def linha_dados(rotulo, valor):
    conteudo = f'  {rotulo:<22} {valor}'
    # preenche com espaços até a largura e fecha com │
    return f'│{conteudo:<{largura}}│'

# ╔══════════════════════════════════════════════════════╗
# ║           SUGESTÕES DE SENHA                         ║
# ╚══════════════════════════════════════════════════════╝
print()
print('╔' + '═' * largura + '╗')
print('║' + '  SUGESTÕES DE SENHA'.center(largura) + '║')
print('╠' + '═' * largura + '╣')
for i, senha in enumerate(senhas, 1):
    print(linha_dados(f'Sugestão {i}:', senha))
print('╚' + '═' * largura + '╝')

# ╔══════════════════════════════════════════════════════╗
# ║        ANÁLISE DO ESPAÇO DE BUSCA                    ║
# ╚══════════════════════════════════════════════════════╝
print()
print('╔' + '═' * largura + '╗')
print('║' + '  ANÁLISE DO ESPAÇO DE BUSCA'.center(largura) + '║')
print('╠' + '═' * largura + '╣')
print(linha_dados('Alfabeto utilizado:', f'{c} caracteres'))
print(linha_dados('Tamanho da senha:', f'{n} caracteres'))
print(linha_dados('Espaço de busca:', f'{espaco_busca:,} combinações'))
print('╠' + '═' * largura + '╣')
print(linha_dados('Nível de segurança:', nivel))
print('╚' + '═' * largura + '╝')
print()