# LockGate — Gerador de Senhas

Extensão de navegador que gera senhas seguras a partir de parâmetros
escolhidos pelo usuário, exibindo o nível de segurança e o tempo estimado
para quebrá-la por força bruta — aplicando Análise Combinatória
(Princípio Fundamental da Contagem, E = c^n) na prática.

![Screenshot do LockGate](screenshot.png)

## Funcionalidades

- Geração de 3 sugestões de senha por vez
- Controle de tamanho (slider) e tipos de caractere (maiúsculas,
  minúsculas, números, símbolos)
- Cálculo do espaço de busca (combinações possíveis) usando `BigInt`,
  sem perda de precisão mesmo em senhas longas
- Classificação de nível de segurança (Muito baixo → Muito alto)
- Estimativa de tempo de quebra por força bruta
- Botão de copiar senha com um clique
- Geração de números aleatórios criptograficamente segura
  (`crypto.getRandomValues` no JS / `secrets` no Python)

## Tecnologias

- JavaScript (Chrome Extension, Manifest V3)
- HTML / CSS
- Python (versão original em linha de comando)

## Fundamentação e decisões técnicas

- **Análise Combinatória aplicada à segurança**: o espaço de busca de uma
  senha é calculado pelo Princípio Fundamental da Contagem (E = c^n, onde
  c é o tamanho do alfabeto disponível e n o tamanho da senha),
  demonstrando na prática como o crescimento exponencial das combinações
  impacta a resistência a ataques de força bruta
- **`BigInt` em vez de `Number`**: o espaço de busca de senhas longas
  ultrapassa o limite seguro de precisão do JavaScript, então todo o
  cálculo combinatório usa `BigInt`
- **`crypto.getRandomValues` em vez de `Math.random`**: `Math.random` usa
  um algoritmo pseudo-aleatório previsível, inadequado para geração de
  dados sensíveis a segurança; a API `crypto` usa uma fonte de
  aleatoriedade adequada para esse fim
- Nenhuma senha gerada é armazenada ou enviada para qualquer servidor —
  toda a lógica roda localmente no navegador, sem permissões de rede

## Autor

**Gabriel Roque França**
Estudante de Ciência da Computação | Cibersegurança & Redes
