document.getElementById('gerar').addEventListener('click', () => {

  // --- 1. Ler os parâmetros escolhidos pelo usuário ---
  const tamanho = parseInt(document.getElementById('tamanho').value);
  const usarMinusculas = document.getElementById('minusculas').checked;
  const usarMaiusculas = document.getElementById('maiusculas').checked;
  const usarNumeros = document.getElementById('numeros').checked;
  const usarSimbolos = document.getElementById('simbolos').checked;

  // --- 2. Montar o alfabeto disponível ---
  let alfabeto = '';
  if (usarMinusculas) alfabeto += 'abcdefghijklmnopqrstuvwxyz';
  if (usarMaiusculas) alfabeto += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  if (usarNumeros) alfabeto += '0123456789';
  if (usarSimbolos) alfabeto += '!@#$%^&*()_+-=[]{}|;:,.<>?';

  if (alfabeto === '') {
    document.getElementById('resultado').textContent = 'Selecione ao menos um tipo de caractere.';
    return;
  }

  // --- 3. Espaço de busca (E = c^n), usando BigInt para números grandes ---
  const c = BigInt(alfabeto.length);
  const n = BigInt(tamanho);
  const espacoBusca = c ** n;

  // --- 4. Classificação do nível de segurança ---
  let nivel;
  if (espacoBusca < 1_000_000n) nivel = 'Muito baixo';
  else if (espacoBusca < 1_000_000_000n) nivel = 'Baixo';
  else if (espacoBusca < 1_000_000_000_000n) nivel = 'Médio';
  else if (espacoBusca < 1_000_000_000_000_000n) nivel = 'Alto';
  else nivel = 'Muito alto';

  // --- 5. Tempo estimado de força bruta ---
  const TENTATIVAS_POR_SEGUNDO = 1_000_000_000;
  const tempoSegundos = Number(espacoBusca) / TENTATIVAS_POR_SEGUNDO;

  function formatarTempo(segundos) {
    const MINUTO = 60, HORA = 60 * MINUTO, DIA = 24 * HORA, ANO = 365.25 * DIA;
    if (segundos < 1) return 'menos de 1 segundo';
    if (segundos < MINUTO) return `${Math.floor(segundos)} segundos`;
    if (segundos < HORA) return `${Math.floor(segundos / MINUTO)} minutos`;
    if (segundos < DIA) return `${Math.floor(segundos / HORA)} horas`;
    if (segundos < ANO) return `${Math.floor(segundos / DIA)} dias`;
    const anos = segundos / ANO;
    if (!isFinite(anos)) return 'tempo praticamente infinito';
    return `${anos.toLocaleString('pt-BR', {maximumFractionDigits: 0})} anos`;
  }
  const tempoFormatado = formatarTempo(tempoSegundos);

  // --- 6. Gerar as 3 sugestões de senha ---
  function gerarSenha() {
  const valores = new Uint32Array(tamanho);
  crypto.getRandomValues(valores);
  let senha = '';
  for (let i = 0; i < tamanho; i++) {
    senha += alfabeto[valores[i] % alfabeto.length];
  }
  return senha;
}
  const senhas = [gerarSenha(), gerarSenha(), gerarSenha()];

  // --- 7. Exibir tudo na tela ---
  document.getElementById('resultado').innerHTML = `
    <h4>Sugestões</h4>
    <ul>${senhas.map(s => `<li><code>${s}</code></li>`).join('')}</ul>
    <p><b>Espaço de busca:</b> ${espacoBusca.toLocaleString('pt-BR')} combinações</p>
    <p><b>Nível de segurança:</b> ${nivel}</p>
    <p><b>Tempo estimado (força bruta):</b> ${tempoFormatado}</p>
  `;

});