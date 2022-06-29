
describe('Visualização de evento', () => {
  it('permite visualizar detalhes de um evento', () => {
    cy.visit('http://127.0.0.1:3000');
    cy.wait(3000);
    cy.contains('Atlético-MG x Flamengo').first().click()
    cy.url()
      .should('match', /http:\/\/127.0.0.1:3000\/eventos\/[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}/)

    cy.contains('Detalhes do Evento - Atlético-MG x Flamengo').should('exist');
    cy.contains('Jogo de ida das oitavas de final da Copa do Brasil 2022').should('exist');
    cy.contains('Mineirão - Belo Horizonte/MG').should('exist');
    cy.contains('Atlético-MG').should('exist');
    cy.contains('Flamengo').should('exist');

    cy.get('button[aria-label="voltar"]').click()
    cy.url()
      .should('be.equal', 'http://127.0.0.1:3000/')
  })
})