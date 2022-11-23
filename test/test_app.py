from unittest import TestCase

from app import app

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class ConverterViewsTestCase(TestCase):
    """Examples of intergration tests: testing Flask app"""
    def test_home_route(self):
        """Test home page route"""    
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h3 class="title">Forex Converter</h3>', html)

    def test_show_result_page(self):
        """Test result page route"""
        with app.test_client() as client:
            resp = client.get('/results')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)   
            self.assertIn('<div class="results-container">', html)
    

    def test_form_submit(self):
        """Test if the results were submitted and posted to the page"""
        with app.test_client() as client:
            resp = client.post('/results', data={"from", "USD"})
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("$100", html)
    
    
        




            