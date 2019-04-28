describe('Swagger', () => {
  it('should display the swagger docs correctly', () => {
    cy
      .visit('/')
      .get('.navbar-burger').click()
      .get('a').contains('Swagger').click();

      cy.get('select > option').then((el) => {
        expect((el).text()).to.contain(Cypress.env('http://testdriven-staging-alb-1466309556.us-west-1.elb.amazonaws.com'));
      });
  });
});