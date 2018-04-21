#save 404 check for requests version where you can get status code

from selenium import webdriver
import unittest

allSites = ['http://ericervin.org',
            'http://ericervin.com',
            'http://ericcervin.github.io',
            'http://noiselife.org',
            'http://127.0.0.1:5000' #new AskFlapp site
            ]

class AllSitesTestForRobots(unittest.TestCase):
  
  def setUp(self):
      self.browser = webdriver.Firefox()

  def tearDown(self):
      self.browser.quit()

  def test_for_robots(self):
    for site in allSites:
        self.browser.get(site + '/robots.txt')
        self.assertIn('User-agent: *\nDisallow: /', self.browser.page_source)

class AllSitesTestFor404(unittest.TestCase):
  
  def setUp(self):
      self.browser = webdriver.Firefox()

  def tearDown(self):
      self.browser.quit()

  def test_for_robots(self):
    for site in allSites:
      if site != 'http://ericcervin.github.io':
        self.browser.get(site + '/platypus')

        self.assertIn('Error 404 Not Found', self.browser.title)
        self.assertIn('<body>404 - Not Found', self.browser.page_source)
   
class AllEricErvinSitesFirefoxTest(unittest.TestCase):
  def setUp(self):
      self.browser = webdriver.Firefox()

  def tearDown(self):
      self.browser.quit()

  def test_destiny_cards(self):
    url = 'http://ericervin.org/destiny/cards?'
    #url = 'http://localhost/destiny/cards?'
    self.browser.get(url)
    self.assertIn('Destiny', self.browser.title)

    table = self.browser.find_element_by_id('id_card_table')
    rows = table.find_elements_by_tag_name('tr')
    org_destiny_cards_count = len(rows)

    url = 'http://ericervin.com/destiny/cards?'
    #url = 'http://localhost/destiny/cards?'
    self.browser.get(url)
    self.assertIn('Destiny', self.browser.title)

    table = self.browser.find_element_by_id('id_card_table')
    rows = table.find_elements_by_tag_name('tr')
    com_destiny_cards_count = len(rows)
    self.assertEqual(org_destiny_cards_count,com_destiny_cards_count)

  def test_ask_flapp(self):
    url = 'http://localhost:5000/'

    self.browser.get(url)
    self.assertIn('Eric Ervin Dot Com', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Eric Ervin Dot Com', header_text)
    
  def test_ericervin_dot_org(self):
    url = 'http://ericervin.org'
    #url = 'http://localhost'
    
    self.browser.get(url)
    self.assertIn('Eric Ervin Dot Org', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Eric Ervin Dot Org', header_text)

  def test_ericervin_dot_org_destiny(self):
    url = "http://ericervin.org/destiny"
    #url = 'http://localhost/destiny'
    self.browser.get(url)
    self.assertIn('Destiny', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Star Wars Destiny', header_text)

 
    
  def test_ericervin_dot_org_gematria(self):
    url = 'http://ericervin.org/gematria'
    #url = 'http://localhost/gematria'
    self.browser.get(url)
    self.assertIn('Gematria', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Gematria', header_text)

    inputbox1 = self.browser.find_element_by_id('id_word_input')
    self.assertEqual(inputbox1.get_attribute('name'),'word')

    inputbox2 = self.browser.find_element_by_id('id_value_input')
    self.assertEqual(inputbox2.get_attribute('name'),'value')

    
    #then add Keys input for fields and submit
    
  def test_ericervin_dot_com(self):
    url = 'http://ericervin.com'

    self.browser.get(url)
    self.assertIn('Eric Ervin Dot Com', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Eric Ervin Dot Com', header_text)

  def test_ericervin_dot_com_destiny(self):
    url = 'http://ericervin.com/destiny'
    #url = http://localhost/destiny'
    self.browser.get(url)
    self.assertIn('Destiny', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Star Wars Destiny', header_text)
    
  
    
  def test_ericcervin_dot_github_dot_io(self):
    url = 'http://ericcervin.github.io'
    self.browser.get(url)
    self.assertIn('ericcervin.github.io', self.browser.title)

  def test_noiselife_dot_org(self):
    url = 'http://noiselife.org'
    self.browser.get(url)
    self.assertIn('noiselife-dot-org', self.browser.title)

    

if __name__ == '__main__':
    unittest.main()
