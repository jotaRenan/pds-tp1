# BETinho, o site de apostas

Projeto relacionado à disciplina Prática em Desenvolvimento de Software 2022/01 da UFMG
<details>

  <summary>Proposta </summary>

Inspirado em plataformas como o [bet365](https://pt.wikipedia.org/wiki/Bet365) e o [sportsBet](https://en.wikipedia.org/wiki/Sportsbet), a equipe desenvolverá um site que permite aos seus usuários realizarem apostas online. O nosso site permitirá o cadastro de cenários de aposta (e.g.: cadastrar um cenário referente a um jogo entre Cruzeiro e Atlético) e registrar as apostas de usuários (e.g: apostar $50 que o Cruzeiro será vencedor). Além disso, cuidará do cálculo das chances e prêmios envolvidos nas apostas.

O site **não** realizará sorteios. Ele apenas permitirá apostas.
</details>

## Equipe

- Bárbara Ribeiro (@barbaragribeiro) - Desenvolvedora Fullstack
- Jean George (@jeanGeorge) - Desenvolvedor Fullstack
- João Pedro Renan (@jotarenan) - Desenvolvedor Fullstack
- Luiz Berto (@luiz787) - Desenvolvedor Fullstack

## Tecnologias

Backend: Python (Django Framework)
Frontend: React + Typescript

<details>
  <summary>
    <h2>User stories - backlog do produto</h2>
  </summary>  
  
  ### Listagem de eventos

- **Como** usuário do BETinho
- **Quero** ver a listagem dos eventos disponíveis para aposta
- **Para** verificar eventos de interesse e escolher eventos para realizar apostas.

### Detalhes do evento

- **Como** usuário do BETinho
- **Quero** poder visualizar detalhes de um evento específico como data, hora, local, participantes envolvidos e _odds_
- **Para** me informar acerca do evento, saber qual o retorno potencial de uma aposta e decidir se vou ou não apostar (e em qual resultado).

### Apostar

- **Como** usuário do BETinho
- **Quero** poder apostar em um resultado de um evento
- **Para** obter retorno financeiro _fictício_ caso o resultado se concretize.

### Cadastro de eventos

- **Como** administrador do BETinho
- **Quero** poder cadastrar novos eventos
- **Para** permitir que os usuários do BETinho consigam fazer apostas nesses eventos.

### Edição e deleção de eventos

- **Como** administrador do BETinho
- **Quero** poder editar e deletar eventos
- **Para** poder adaptar a plataforma à mudanças externas (ex.: cancelamento de jogo, mudança de horário), e dessa manter a qualidade do conteúdo do BETinho.

### Cálculo de odds

- **Como** administrador do BETinho
- **Quero** que o sistema calcule automaticamente as _odds_ de cada possível resultado de um evento, baseado na proporção de apostas em cada resultado
- **Para** que os usuários saibam o potencial de ganho em cada possível resultado de um evento, e para que isso não tenha que ser feito manualmente pelos administradores do BETinho.

### Atualização de resultados de eventos

- **Como** administrador do BETinho
- **Quero** que o sistema permita lançar o resultado de um evento
- **Para** que o evento seja encerrado e o pagamento para os vencedores possa ser feito.

### Pagamento aos vencedores

- **Como** usuário do BETinho
- **Quero** que o sistema realize o pagamento para os vencedores de forma automática quando um evento for encerrado (resultado lançado)
- **Para** que eu possa desfrutar dos meus gains 💪 🤑

### Cadastro, edição e deleção de conta

- **Como** usuário do BETinho
- **Quero** que o sistema permita criar uma conta, editar o perfil e deletar a conta
- **Para** que eu possa utilizar o sistema de forma autenticada e ter controle sob meus dados.

### Agrupamento/filtragem de eventos por categoria

- **Como** usuário do BETinho
- **Quero** que o sistema agrupe eventos em categorias (ex.: Futebol, Fórmula 1, Basquete)
- **Para** que eu possa visualizar e achar os eventos do meu interesse com maior facilidade.

### Cadastro, edição e deleção de categorias

- **Como** administrador do BETinho
- **Quero** que o sistema possibilite cadastrar, editar e deletar categorias
- **Para** que as categorias de eventos possam ser mantidas pelos administradores.
  
</details>


