import flask_testing import TestCase
from flask import current_app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTInG'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app
    
    def test_app_exist(self):
        self.assertIsNotNone(current_app)
        
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
        
    def test_index_redirect(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))
        
    def test_hello_get(self):
        response = self.client.get(url_for('hello'))
        self.assert200(response)
        
    def test_hello_post(self):
        fake_form = {
            'username':'fake',
            'password':'fake-password'
        }
        response = self.client.post(url_for('hello'), data=fake_form)
        self.assertRedirect(response, url_for('index'))