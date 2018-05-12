#add 404 check in requests version where you can get status code

from selenium import webdriver
import unittest

allSites = ['http://ericervin.org',
            'http://ericervin.com',
            'http://ericcervin.github.io',
            'http://noiselife.org',
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
      counts = []
      urls = ['http://ericervin.org/destiny/cards?',
              'http://ericervin.com/destiny/cards?']

      for u in urls:
          self.browser.get(u)
          self.assertIn('Destiny', self.browser.title)
          table = self.browser.find_element_by_id('id_card_table')
          rows = table.find_elements_by_tag_name('tr')
          counts.append(len(rows))

      self.assertEqual(counts[0],counts[1])

  def test_discogs_releases(self):
      counts = []
      urls = ['http://www.ericervin.org/discogs/releases?',
              'http://www.ericervin.com/discogs/releases?']

      for u in urls:
          self.browser.get(u)
          self.assertIn('Discogs', self.browser.title)
          table = self.browser.find_element_by_id('id_release_table')
          rows = table.find_elements_by_tag_name('tr')
          counts.append(len(rows))

      self.assertEqual(counts[0],counts[1])

  def test_discogs_reports(self):
      counts = []
      urls = ['http://www.ericervin.org/discogs/reports?rpt=artist_count',
              'http://www.ericervin.com/discogs/reports?rpt=artist_count']

      for u in urls:
          self.browser.get(u)
          self.assertIn('Discogs', self.browser.title)
          table = self.browser.find_element_by_id('id_release_table')
          rows = table.find_elements_by_tag_name('tr')
          counts.append(len(rows))

      self.assertEqual(counts[0],counts[1])
      

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

  def test_ericervin_dot_org_discogs(self):
    url = "http://ericervin.org/discogs"
    self.browser.get(url)
    self.assertIn('Discogs', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('My Record Collection', header_text) 
    
  def test_ericervin_dot_org_gematria(self):
    url = 'http://ericervin.org/gematria'
    self.browser.get(url)
    self.assertIn('Gematria', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Gematria', header_text)

    inputbox1 = self.browser.find_element_by_id('id_word_input')
    self.assertEqual(inputbox1.get_attribute('name'),'word')

    inputbox2 = self.browser.find_element_by_id('id_value_input')
    self.assertEqual(inputbox2.get_attribute('name'),'value')

    #then add Keys input for fields and submit
    
  def test_ericervin_dot_org_philosophy(self):
    url = "http://ericervin.org/philosophy"
    self.browser.get(url)
    self.assertIn('Philosophy USA', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Philosophy USA', header_text) 

  def test_ericervin_dot_org_powerball(self):
    url = "http://ericervin.org/powerball"
    self.browser.get(url)
    self.assertIn('Powerball', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Powerball', header_text)

  def test_ericervin_dot_org_serialism(self):
    url = "http://ericervin.org/serialism"
    self.browser.get(url)
    self.assertIn('Serialism', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Serialism', header_text)
    
    
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

  def test_ericervin_dot_com_discogs(self):
    url = "http://ericervin.com/discogs"
    self.browser.get(url)
    self.assertIn('Discogs', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('My Record Collection', header_text)
    
  def test_ericervin_dot_com_powerball(self):
    url = "http://ericervin.com/powerball"
    self.browser.get(url)
    self.assertIn('Powerball', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Powerball', header_text)

  def test_ericervin_dot_com_serialism(self):
    url = "http://ericervin.com/serialism"
    self.browser.get(url)
    self.assertIn('Serialism', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Serialism', header_text)
    
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
