from selenium import webdriver
import unittest

allSites = ['http://ericervin.org','http://ericervin.com','http://ericcervin.github.io','http://noiselife.org']

class AllSitesTestForRobots(unittest.TestCase):
  
  def setUp(self):
      self.browser = webdriver.Firefox()

  def tearDown(self):
      self.browser.quit()

  def test_for_robots(self):
    for site in allSites:
        self.browser.get(site + '/robots.txt')
        self.assertIn('User-agent: *\nDisallow: /', self.browser.page_source)

    
    
class AllEricErvinSitesFirefoxTest(unittest.TestCase):
  def setUp(self):
      self.browser = webdriver.Firefox()

  def tearDown(self):
      self.browser.quit()
  
  def test_ericervin_dot_org(self):
    url = 'http://ericervin.org'
    #url = 'http://localhost'
    
    self.browser.get(url)
    self.assertIn('Eric Ervin Dot Org', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Eric Ervin Dot Org', header_text)

  def test_ericervin_dot_org_destiny(self):
    self.browser.get('http://ericervin.org/destiny')
    #self.browser.get('http://localhost/destiny')
    self.assertIn('Destiny', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Star Wars Destiny', header_text)

  def test_ericervin_dot_org_destiny_cards(self):
    self.browser.get('http://ericervin.org/destiny/cards?')
    #self.browser.get('http://localhost/destiny/cards?')
    self.assertIn('Destiny', self.browser.title)

    table = self.browser.find_element_by_id('id_card_table')
    rows = table.find_elements_by_tag_name('tr')
    #print(len(rows))
    #add code that counts rows in table.
    #maybe compare with output count from ericervin_dot_com

  
    
  def test_ericervin_dot_org_gematria(self):
    self.browser.get('http://ericervin.org/gematria')
    #add a proper title

    #add a properly sized header

    #give input fields proper ids that you can find
    #then add Keys input for field and submit
    
  def test_ericervin_dot_com(self):
    #refactor so stem of url is here. other lines build on that.

    
    
    self.browser.get('http://ericervin.com')
    self.assertIn('Eric Ervin Dot Com', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Eric Ervin Dot Com', header_text)

  def test_ericervin_dot_com_destiny(self):
    self.browser.get('http://ericervin.com/destiny')
    #self.browser.get('http://localhost/destiny')
    self.assertIn('Destiny', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Star Wars Destiny', header_text)
    
  def test_ericervin_dot_com_destiny_cards(self):
    self.browser.get('http://ericervin.com/destiny/cards?')
    #self.browser.get('http://localhost/destiny/cards?')
    self.assertIn('Destiny', self.browser.title)

    table = self.browser.find_element_by_id('id_card_table')
    rows = table.find_elements_by_tag_name('tr')
    #print(len(rows))
    #add code that counts rows in table.
    #maybe compare with output count from ericervin_dot_org
    
  def test_ericcervin_dot_github_dot_io(self):
    #refactor so stem of url is here. other lines build on that.
    
    self.browser.get('http://ericcervin.github.io')
    self.assertIn('ericcervin.github.io', self.browser.title)

  def test_noiselife_dot_org(self):
    #refactor so stem of url is here. other lines build on that.

    self.browser.get('http://noiselife.org')
    self.assertIn('noiselife-dot-org', self.browser.title)

    

if __name__ == '__main__':
    unittest.main()
