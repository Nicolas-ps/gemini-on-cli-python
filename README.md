# Python — Assistente de Linha de Comando com Google GenAI

Este projeto é um assistente simples de linha de comando que utiliza o SDK `google-genai` para conversar com um modelo da família Gemini, opcionalmente com a Ferramenta de Pesquisa do Google ativada. As configurações são carregadas via `.env`.

## Requisitos
- Python 3.9+ (recomendado 3.10 ou 3.11)
- Uma chave de API válida do Google AI Studio (variável de ambiente `GOOGLE_API_KEY`)
- Um ID de modelo Gemini (por exemplo: `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-1.5-pro`, etc.)

## Instalação
1. Clone o repositório e acesse a pasta do projeto.
2. Crie um ambiente virtual (opcional, mas recomendado):
   - Linux/macOS: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows (PowerShell): `py -m venv .venv; .\.venv\Scripts\Activate.ps1`
3. Instale as dependências:
   - `pip install -r requirements.txt`

## Configuração (.env)
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
GOOGLE_API_KEY=coloque_sua_chave_aqui
MODEL_ID=gemini-2.0-flash
```

- `GOOGLE_API_KEY`: sua chave do Google AI Studio (ou variável de ambiente equivalente aceita pelo SDK `google-genai`).
- `MODEL_ID`: o modelo que você deseja usar. Exemplos: `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-1.5-flash`, `gemini-1.5-pro`.

Observação: o script habilita a ferramenta de Pesquisa do Google via `types.Tool(google_search=types.GoogleSearch)`. Verifique se sua conta/chave possui acesso a esse recurso no momento do uso.

## Como executar
Execute o script principal:

```
python index.py
```

Você verá o prompt:

```
Oque te apetece? (Digite 'q' para encerrar):
```

- Digite sua pergunta/comando e pressione Enter.
- Para encerrar, digite `q` ou use `Ctrl+C`/`Ctrl+\` (o script captura o sinal e sai com uma mensagem de encerramento).

## Estrutura do projeto
- `index.py`: loop de interação no terminal com o cliente `google.genai`. Lê `MODEL_ID` do ambiente, e imprime `response.text`.
- `requirements.txt`: dependências do projeto (`python-dotenv`, `google-genai`, `keyboard`).
- `README.md`: este arquivo.

## Exemplo de uso
Entrada:
```
Explique resumidamente o que é aprendizado de máquina.
```
Saída (exemplo):
```
Aprendizado de máquina é uma área da inteligência artificial que permite que sistemas aprendam padrões a partir de dados para fazer previsões ou tomar decisões sem serem explicitamente programados para cada tarefa.
```

## Solução de problemas
- Erro de autenticação / 401:
  - Confirme que `GOOGLE_API_KEY` está definido no `.env` e é válido.
  - Garanta que o ambiente virtual está ativado e que o `python-dotenv` está instalado.
- Erro ao importar `google.genai` ou `google-genai`:
  - Reinstale as dependências: `pip install -r requirements.txt`.
  - Verifique conflitos de versões e se está usando o Python correto (ex.: `which python` / `where python`).
- Respostas vazias (`response.text` vazio):
  - Verifique se o `MODEL_ID` é válido e suportado pela sua chave.
  - Remova momentaneamente a ferramenta de pesquisa se suspeitar de problemas de permissão.
- Problemas de encoding no terminal:
  - Configure o terminal para UTF-8.

## Notas
- Este projeto é um exemplo simples para experimentação com a API do Google GenAI em modo interativo no terminal. Adapte conforme necessário (histórico de conversa, parâmetros de geração, controle fino de ferramentas, etc.).
- Consulte a documentação oficial para modelos e recursos atualizados: https://ai.google.dev/

## Licença
Este repositório não especifica uma licença. Caso pretenda distribuí-lo, adicione um arquivo `LICENSE` apropriado.