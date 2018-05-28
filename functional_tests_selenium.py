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

  def test_destiny(self):
    urls = ["http://ericervin.org/destiny", "http://ericervin.com/destiny"]
    for url in urls:
        self.browser.get(url)
        self.assertIn('Destiny', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Star Wars Destiny', header_text)
    
  def test_destiny_cards(self):
      self.browser.get('http://ericervin.org/destiny/cards?')
      self.assertIn('Destiny', self.browser.title)
      org_card_table = self.browser.find_element_by_id('id_card_table')
      org_card_table_text = org_card_table.text
      
      self.browser.get('http://ericervin.com/destiny/cards?')
      self.assertIn('Destiny', self.browser.title)
      com_card_table = self.browser.find_element_by_id('id_card_table')
      com_card_table_text = com_card_table.text

      self.assertEqual(org_card_table_text,com_card_table_text)

  def test_destiny_reports(self):
      self.browser.get('http://ericervin.org/destiny/reports?rpt=rarity_count')
      self.assertIn('Destiny', self.browser.title)

      org_result_table = self.browser.find_element_by_id('id_card_table')
      org_result_table_text = org_result_table.text
      
      self.browser.get('http://www.ericervin.com/destiny/reports/rarity_count')
      self.assertIn('Destiny', self.browser.title)

      com_result_table = self.browser.find_element_by_id('id_card_table')
      com_result_table_text = com_result_table.text

      self.assertEqual(org_result_table_text,com_result_table_text)

  def test_discogs(self):
    urls = ["http://ericervin.org/discogs", "http://ericervin.com/discogs"]
    for url in urls:
        self.browser.get(url)
        self.assertIn('Discogs', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('My Record Collection', header_text)
        
  
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
      urls = ['http://www.ericervin.org/discogs/reports/artist_count',
              'http://www.ericervin.com/discogs/reports/artist_count']

      for u in urls:
          self.browser.get(u)
          self.assertIn('Discogs', self.browser.title)
          table = self.browser.find_element_by_id('id_release_table')
          rows = table.find_elements_by_tag_name('tr')
          counts.append(len(rows))

      self.assertEqual(counts[0],counts[1])

  def test_gematria(self):
    urls = ["http://ericervin.org/gematria", "http://ericervin.com/gematria"]
    for url in urls:
        self.browser.get(url)
        self.assertIn('Gematria', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Gematria', header_text)

        inputbox1 = self.browser.find_element_by_id('id_word_input')
        self.assertEqual(inputbox1.get_attribute('name'),'word')

        inputbox2 = self.browser.find_element_by_id('id_value_input')
        self.assertEqual(inputbox2.get_attribute('name'),'value')
        
        #then add Keys input for fields and submit

  def test_gematria_words(self):
      self.browser.get('http://www.ericervin.org/gematria/word?word=eric')
      self.assertIn('Gematria', self.browser.title)

      org_word_value_table = self.browser.find_element_by_id('id_word_value_table')
      org_word_value_text = org_word_value_table.text
      
      org_other_word_table = self.browser.find_element_by_id('id_other_word_table')
      org_other_word_rows = org_other_word_table.find_elements_by_tag_name('tr')
      org_other_word_rows_count = len(org_other_word_rows)
      
      self.browser.get('http://www.ericervin.com/gematria/word?word=eric')
      self.assertIn('Gematria', self.browser.title)

      com_word_value_table = self.browser.find_element_by_id('id_word_value_table')
      com_word_value_text = com_word_value_table.text
      
      com_other_word_table = self.browser.find_element_by_id('id_other_word_table')
      com_other_word_rows = com_other_word_table.find_elements_by_tag_name('tr')
      com_other_word_rows_count = len(com_other_word_rows)

      self.assertEqual(org_other_word_rows_count,com_other_word_rows_count)
      self.assertEqual(org_word_value_text,com_word_value_text)

  def test_gematria_values(self):
      self.browser.get('http://www.ericervin.org/gematria/value?value=65')
      self.assertIn('Gematria', self.browser.title)
      
      org_word_table = self.browser.find_element_by_id('id_word_value_table')
      org_word_rows = org_word_table.find_elements_by_tag_name('tr')
      org_word_rows_count = len(org_word_rows)
      
      self.browser.get('http://www.ericervin.com/gematria/value?value=65')
      self.assertIn('Gematria', self.browser.title)
      
      com_word_table = self.browser.find_element_by_id('id_word_value_table')
      com_word_rows = com_word_table.find_elements_by_tag_name('tr')
      com_word_rows_count = len(com_word_rows)

      self.assertEqual(org_word_rows_count,com_word_rows_count)

  

  def test_philosophy(self):
    urls = ["http://ericervin.org/philosophy", "http://ericervin.com/philosophy"]
    for url in urls:
        self.browser.get(url)
        self.assertIn('Philosophy USA', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Philosophy USA', header_text)

  def test_philosophy_reports(self):
      self.browser.get('http://ericervin.org/philosophy/reports?rpt=inst_count')
      self.assertIn('Philosophy USA', self.browser.title)

      org_result_table = self.browser.find_element_by_id('id_result_table')
      org_result_table_text = org_result_table.text
      
      self.browser.get('http://ericervin.com/philosophy/reports/inst_count')
      self.assertIn('Philosophy USA', self.browser.title)

      com_result_table = self.browser.find_element_by_id('id_result_table')
      com_result_table_text = com_result_table.text

      self.assertEqual(org_result_table_text,com_result_table_text)


  def test_powerball(self):
    urls = ["http://ericervin.org/powerball", "http://ericervin.com/powerball"]
    for url in urls:
        self.browser.get(url)
        self.assertIn('Powerball', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Powerball', header_text)

  def test_ericervin_dot_org(self):
    url = 'http://ericervin.org'
    #url = 'http://localhost'
    
    self.browser.get(url)
    self.assertIn('Eric Ervin Dot Org', self.browser.title)

    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Eric Ervin Dot Org', header_text)

    
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
