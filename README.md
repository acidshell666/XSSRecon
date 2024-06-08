
# XSSRecon

Este é um script Python simples para testar vulnerabilidades de XSS (Cross-Site Scripting) em uma URL específica. Ele faz isso injetando payloads XSS comuns e verificando se eles são executados com sucesso na página alvo.

## Funcionamento

O script segue estes passos para testar uma URL em busca de vulnerabilidades de XSS:

1. O usuário insere a URL alvo.
2. O script carrega uma lista de payloads XSS comuns de um arquivo de texto.
3. Para cada payload, o script injeta o payload na URL e faz uma solicitação GET.
4. Se o payload for executado com sucesso na página, o script o marca como bem-sucedido.
5. No final do teste, o script exibe os payloads XSS bem-sucedidos e pergunta ao usuário se deseja salvá-los em um arquivo.

## Modo de Uso

1. Clone o repositório para o seu ambiente local.
2. Abra um terminal e navegue até o diretório do script.
3. Execute o script usando o comando `python3 xsstest.py`.
4. Quando solicitado, insira a URL alvo.
5. O script testará automaticamente a URL em busca de vulnerabilidades de XSS e exibirá os resultados.

## Requisitos

O script requer a biblioteca `requests` para fazer solicitações HTTP. Você pode instalá-lo executando o comando `pip install requests`.

## Como Contribuir

Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request. Seu feedback é bem-vindo!
