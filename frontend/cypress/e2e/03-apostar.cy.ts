
function selectionarAposta() {
  cy.visit('http://127.0.0.1:3000');
  cy.wait(3000);
  cy.contains('Apostar', { matchCase: false }).first().click();
  cy.url().should('match', /http:\/\/127.0.0.1:3000\/apostar\/[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}/)
}

describe('Aposta em evento', () => {
  describe('quando algum campo não é preenchido', () => {
    it('não permite realizar aposta', () => {
      selectionarAposta()
      cy.get('#result')
        .parent()
        .click()
        .get('ul > li[data-value="1"]')
        .click();
      cy.contains('Betar!', { matchCase: false }).click();
      cy.wait(250);
      cy.contains('Preencha todos os campos para realizar a aposta!', { matchCase: false }).should('exist');
    })
  })

  describe('quando todos os campos são preenchidos', () => {
    it('permite realizar aposta', () => {
      selectionarAposta()
      cy.get('#result')
        .parent()
        .click()
        .get('ul > li[data-value="1"]')
        .click();
      cy.get('[data-testid="valor"')
        .type('1200')
      cy.contains('Betar!', { matchCase: false }).click();
      cy.wait(250);
      cy.get('[data-testid="home-odd-1"]').contains('1.00')
      cy.get('[data-testid="draw-odd-1"]').contains('N/A')
      cy.get('[data-testid="away-odd-1"]').contains('N/A')
    })
  })
});