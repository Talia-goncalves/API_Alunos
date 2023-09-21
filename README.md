# API_Alunos
Esta API serve para fazer o controle de Alunos, disciplinas e tarefas de uma escola fictícia.
Aqui em cada um destes controles você pode fazer a criação, atualização, deletagem e listagem de um ou mais itens dentre elas.

# Alunos
Um exemplo de input que você pode inserir para fazer a criação de um aluno é a seguinte: (método POST)
{
    "nome": "Pedro Augusto",
    "email": "pedroLima@gmail.com"
}

desta forma, você terá criado um aluno que retornará com um id já correspondente a ele:
{
    "id": 1,
    "nome": "Pedro Augusto",
    "email": "pedroLima@gmail.com"
}

para você fazer por exemplo a atualização, e a deletagem de determinado item em sua aquisição mensione o id do item que deleja fazer tal ação.

# Disciplina
O exemplo dado a cima serve da mesma maneira para a disciplina, porém irei fornecer mais um exemplo de inserção para criação de uma disciplina:
{
    "nome": "IA",
    "descricao": "Inteligência Artifícial"
}

Para você efetuar a atualização deste item, basta informar na url o id correspondente ao item, e descrever a mudança que deseja fazer ao utilizar o metodo PUT, um exemplo de atualização:
{
    "nome": "IA",
    "descricao": "Inteligência Artifícial atua na reprodução de padrões de comportamento semelhantes ao humano por dispositivos e programas computacionais"
}

# Tarefa
Para você criar uma tarefa, precisa inserir dados compativeis com os dados que a API necessita, pois alem dos dados da propria tarefa em si, precisa também adicionar os dados de qual disciplina ela pertence (podendo ser uma tarefa sendo atribuida a mais disciplinas) e ao aluno pela qual ela foi atribuida. Um exemplo de inserção válida a seguir:
{
  "titulo": "Criar um API",
  "descricao": "Criar uma API com a funcionalidade básica de ToDo",
  "data_entrega": "2023-09-26",
  "concluida": false,
  "alunos_tarefas": 1,
  "disciplinas": [1, 1]
}

O padrão para as inserções dos 3 itens(alunos, disciplinas e tarefas) é o mesmo, então para você deletar cada qualquer uma delas, basta colocar o id do item desejado na URL e utilizar o método DELETE.

Para atualizar alem de colocar ao id correspondente na URL, precisa colocar o conteudo do item com a modificação que se deseja efetuar e utilizar o método PUT