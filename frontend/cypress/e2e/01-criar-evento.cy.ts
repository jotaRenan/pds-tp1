
describe('Criação de evento', () => {
  it('funciona com valores preenchidos válidos', () => {
    cy.visit('http://127.0.0.1:3000/cadastrar-evento');
    cy.wait(3000);
    cy.contains('Jogo de ida das oitavas de final da Copa do Brasil 2022').should('not.exist');
    cy.contains('Cadastrar Evento').should('exist');
    cy.contains('Insira os dados do evento a ser criado nos campos abaixo.').should('exist');
    cy.get('[data-testid="descricao"]').type('Jogo de ida das oitavas de final da Copa do Brasil 2022');
    cy.get('[data-testid="time-a"]').type('Atlético-MG');
    cy.get('[data-testid="time-b"]').type('Flamengo');
    cy.get('[data-testid="localizacao"]').type('Mineirão - Belo Horizonte/MG');
    cy.contains('Criar evento', { matchCase: false }).click()
    cy.wait(250);
    cy.url()
      .should('be.equal', 'http://127.0.0.1:3000/eventos/')
    cy.contains('Atlético-MG x Flamengo').should('exist');
  });
});