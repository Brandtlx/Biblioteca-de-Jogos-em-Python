Biblioteca de Jogos para Zerar

Aplicação de terminal em Python para cadastrar e listar os jogos que você quer zerar. Os dados ficam salvos em um arquivo JSON, então a lista continua ali na próxima vez que o programa for aberto.

Projeto acadêmico da disciplina de Raciocínio Computacional (Atividade Somativa 2), no curso de Análise e Desenvolvimento de Sistemas da PUC-PR.

Como rodar

Requisitos: Python 3 (usa só a biblioteca padrão, não precisa instalar nada).

python Somativa2.py


Mantenha o `Memoria.json` na mesma pasta do script. Se o arquivo não existir, o programa começa com a lista vazia.

Comandos

Os comandos não diferenciam maiúsculas de minúsculas.

| Comando | O que faz |
| --- | --- |
| `ADD` | Pergunta quantos jogos você quer cadastrar e pede o nome de cada um |
| `LIST` | Mostra todos os jogos cadastrados |
| `ABOUT` | Exibe a mensagem de boas-vindas |
| `QUIT` | Salva os dados no `Memoria.json` e encerra o programa |

Importante: os dados são gravados no arquivo ao sair com `QUIT`.

O que o projeto pratica

- Loop de menu com comandos digitados pelo usuário
- Leitura e escrita de arquivo JSON (`json.load` e `json.dump`)
- Validação de entradas: nomes vazios e quantidades inválidas são recusados
- Tratamento de erros: arquivo ausente, JSON corrompido e valor que não é número
- Cores no terminal com códigos ANSI

Estrutura

```
Somativa2.py    # código principal
Memoria.json    # armazenamento dos jogos (lista em JSON)
Diario_ia.md    # diário de bordo de uso de IA exigido pela atividade
```

## Autor

Antonio Brandt · [LinkedIn](https://www.linkedin.com/in/antonio-brandt-4318533bb/)
