
describe('empty spec', () => {
    it('permite visualizar um evento', () => {
      cy.visit('http://127.0.0.1:3000');
      cy.wait(3000);
      cy.contains('Atlético-MG x Flamengo').first().click()
      cy.url()
      .should('be.equal', 'http://127.0.0.1:3000/eventos/0036e757-dd9c-40ee-bae8-07f13f8f5236')
      
      cy.contains('Detalhes do Evento - Atlético-MG x Flamengo').should('exist');
      cy.contains('Jogo de ida das oitavas de final da Copa do Brasil 2022').should('exist');
      cy.contains('Mineirão - Belo Horizonte/MG').should('exist');
      cy.contains('Atlético-MG').should('exist');
      cy.contains('14/07/2022 18:40').should('exist');
      cy.contains('Flamengo').should('exist');
      
      cy.get('button[aria-label="voltar"]').click()
      cy.url()
      .should('be.equal', 'http://127.0.0.1:3000/')

    })
    
    it('permite apostar', () => {
        cy.visit('http://127.0.0.1:3000');
        cy.wait(3000);
        cy.contains('Apostar', {matchCase: false}).first().click();
        cy.url().should('be.equal', 'http://127.0.0.1:3000/apostar/0036e757-dd9c-40ee-bae8-07f13f8f5236')

        cy.get('#result')
            .parent()
            .click()
            .get('ul > li[data-value="1"]')
            .click();
        cy.contains('Betar!', {matchCase: false}).click();
        cy.wait(250);
        cy.contains('Preencha todos os campos para realizar a aposta!', {matchCase: false}).should('exist');
    })
  })