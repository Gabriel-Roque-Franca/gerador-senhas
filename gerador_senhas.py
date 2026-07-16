# ============================================================
# Gerador e Analisador de Senhas
# Trabalho Academico - Matematica Computacional Aplicada
# ============================================================
import secrets
import string

# --- Configuracoes do usuario ---
print('=== Gerador e Analisador de Senhas ===')
print()

# Tamanho da senha
tamanho = int(input('Informe a quantidade de caracteres desejado da senha: '))

# Escolha dos tipos de caracteres
usar_minusculas = input('Usar letras minusculas? (s/n): ').strip().lower() == 's'
usar_maiusculas = input('Usar letras maiusculas? (s/n): ').strip().lower() == 's'
usar_numeros    = input('Usar numeros? (s/n): ').strip().lower() == 's'
usar_simbolos   = input('Usar simbolos? (s/n): ').strip().lower() == 's'

# --- Montagem do alfabeto disponivel ---
alfabeto = ''
if usar_minusculas:
    alfabeto += string.ascii_lowercase   # a-z (26 caracteres)
if usar_maiusculas:
    alfabeto += string.ascii_uppercase   # A-Z (26 caracteres)
if usar_numeros:
    alfabeto += string.digits            # 0-9 (10 caracteres)
if usar_simbolos:
    alfabeto += string.punctuation       # !@#$... (32 caracteres)

# Verificacao: ao menos um tipo deve ser escolhido
if not alfabeto:
    print('Erro: selecione ao menos um tipo de caractere.')
    exit()

# --- Calculo do espaco de busca (E = c^n) ---
c = len(alfabeto)      # tamanho do alfabeto
n = tamanho            # comprimento da senha
espaco_busca = c ** n  # Principio Fundamental da Contagem

# --- Classificacao do nivel de seguranca ---
if espaco_busca < 1_000_000:
    nivel = 'Muito baixo'
elif espaco_busca < 1_000_000_000:
    nivel = 'Baixo'
elif espaco_busca < 1_000_000_000_000:
    nivel = 'Medio'
elif espaco_busca < 1_000_000_000_000_000:
    nivel = 'Alto'
else:
    nivel = 'Muito alto'

# --- Calculo do tempo de forca bruta ---
# Considera o pior caso: todas as combinacoes sao testadas
TENTATIVAS_POR_SEGUNDO = 1_000_000_000  # 1 bilhao de tentativas/segundo

tempo_segundos = espaco_busca / TENTATIVAS_POR_SEGUNDO

def formatar_tempo(segundos):
    """Converte segundos em uma string legivel com a unidade mais adequada."""
    MINUTO = 60
    HORA   = 60 * MINUTO
    DIA    = 24 * HORA
    ANO    = 365.25 * DIA

    if segundos < 1:
        return 'menos de 1 segundo'
    elif segundos < MINUTO:
        s = int(segundos)
        return f"{s:,} segundo{'s' if s > 1 else ''}"
    elif segundos < HORA:
        m = int(segundos / MINUTO)
        return f"{m:,} minuto{'s' if m > 1 else ''}"
    elif segundos < DIA:
        h = int(segundos / HORA)
        return f"{h:,} hora{'s' if h > 1 else ''}"
    elif segundos < ANO:
        d = int(segundos / DIA)
        return f"{d:,} dia{'s' if d > 1 else ''}"
    elif segundos < ANO * 1_000:
        a = int(segundos / ANO)
        return f"{a:,} anos"
    elif segundos < ANO * 1_000_000:
        a = int(segundos / ANO)
        return f"{a:,} anos (~{a // 1_000:,} mil anos)"
    elif segundos < ANO * 1_000_000_000:
        a = int(segundos / ANO)
        return f"{a:,} anos (~{a // 1_000_000:,} milhoes de anos)"
    else:
        a = int(segundos / ANO)
        return f"{a:,} anos (~{a // 1_000_000_000:,} bilhoes de anos)"

tempo_formatado = formatar_tempo(tempo_segundos)

# --- Geracao de 3 sugestoes de senha ---
senhas = [''.join(secrets.choice(alfabeto) for _ in range(tamanho)) for _ in range(3)]

# --- Funcoes auxiliares para o contorno ---
largura = 52

def linha_dados(rotulo, valor):
    conteudo = f'  {rotulo:<22} {valor}'
    return f'|{conteudo:<{largura}}|'

# Impressao das sugestoes de senha
print()
print('+' + '=' * largura + '+')
print('|' + '  SUGESTOES DE SENHA'.center(largura) + '|')
print('+' + '=' * largura + '+')
for i, senha in enumerate(senhas, 1):
    print(linha_dados(f'Sugestao {i}:', senha))
print('+' + '=' * largura + '+')

# Impressao da analise
print()
print('+' + '=' * largura + '+')
print('|' + '  ANALISE DO ESPACO DE BUSCA'.center(largura) + '|')
print('+' + '=' * largura + '+')
print(linha_dados('Alfabeto utilizado:', f'{c} caracteres'))
print(linha_dados('Tamanho da senha:', f'{n} caracteres'))
print(linha_dados('Espaco de busca:', f'{espaco_busca:,} combinacoes'))
print('+' + '=' * largura + '+')
print(linha_dados('Nivel de seguranca:', nivel))
print('+' + '=' * largura + '+')
print('|' + '  TEMPO ESTIMADO - FORCA BRUTA'.center(largura) + '|')
print('+' + '=' * largura + '+')
print(linha_dados('Velocidade do ataque:', '1.000.000.000 tent/s'))
print(linha_dados('Tempo maximo:', tempo_formatado))
print('+' + '=' * largura + '+')
print()
