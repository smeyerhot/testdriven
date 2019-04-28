describe('Swagger', () => {
  it('should display the swagger docs correctly', () => {
    cy
      .visit('/')
      .get('.navbar-burger').click()
      .get('a').contains('Swagger').click();
      });
  });