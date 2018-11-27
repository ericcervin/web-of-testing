import requests, unittest
from bs4 import BeautifulSoup

allSites = ['http://ericervin.org',
            'http://ericervin.com',
            'http://ericcervin.github.io',
            'http://noiselife.org',
            ]

class AllSitesTestForRobots(unittest.TestCase):

  def test_for_robots(self):
    for site in allSites:
        page = requests.get(site + '/robots.txt')
        self.assertIn('User-agent: *\nDisallow: /', page.text)

class AllSitesTestFor404(unittest.TestCase):

  def test_for_404(self):
    for site in allSites:
      if site != 'http://ericcervin.github.io':
        page = requests.get(site + '/platypus')
        soup = BeautifulSoup(page.text,'html.parser')
        
        self.assertEqual(page.status_code,404)
        self.assertIn('Error 404 Not Found', soup.find_all('title')[0])
        self.assertIn('<body>404 - Not Found', page.text)

class AllEricErvinSitesTest(unittest.TestCase):

  def test_destiny(self):
    urls = ["http://ericervin.org/destiny", "http://ericervin.com/destiny"]
    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        
        self.assertEqual(page.status_code,200)
        self.assertIn('Destiny', soup.find_all('title')[0])
        self.assertIn('Star Wars Destiny', soup.find_all('h1')[0])

  def test_destiny_cards(self):
      page = requests.get('http://ericervin.org/destiny/cards?')
      soup = BeautifulSoup(page.text,'html.parser')
      self.assertEqual(page.status_code,200)
      self.assertIn('  Cards', soup.find_all('title')[0])

      org_card_table = soup.find_all(id='id_card_table')[0]

      page = requests.get('http://ericervin.com/destiny/cards?')
      soup = BeautifulSoup(page.text,'html.parser')
      self.assertEqual(page.status_code,200)
      self.assertIn('  Cards', soup.find_all('title')[0])

      com_card_table = soup.find_all(id='id_card_table')[0]
      
      self.assertEqual(org_card_table,com_card_table)

  def test_destiny_reports(self):
      page = requests.get('http://ericervin.org/destiny/reports/rarity_count')
      soup = BeautifulSoup(page.text,'html.parser')
      self.assertEqual(page.status_code,200)
      self.assertIn('Count by Rarity', soup.find_all('title')[0])

      org_result_table = soup.find_all(id='id_card_table')[0]

      page = requests.get('http://ericervin.com/destiny/reports/rarity_count')
      soup = BeautifulSoup(page.text,'html.parser')
      self.assertEqual(page.status_code,200)
      self.assertIn('Count by Rarity', soup.find_all('title')[0])

      com_result_table = soup.find_all(id='id_card_table')[0]
      
      self.assertEqual(org_result_table,com_result_table)
        
  def test_discogs(self):
     urls = ["http://ericervin.org/discogs", "http://ericervin.com/discogs"]
     for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        
        self.assertEqual(page.status_code,200)
        self.assertIn('Discogs', soup.find_all('title')[0])
        self.assertIn('My Record Collection', soup.find_all('h1')[0])

  def test_discogs_releases(self):
     counts = []
     urls = ['http://www.ericervin.org/discogs/releases?',
             'http://www.ericervin.com/discogs/releases?']
     for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        
        self.assertEqual(page.status_code,200)
        self.assertIn('Releases by Artist,Title', soup.find_all('title')[0])
        rows = soup.find_all('td')
        counts.append(len(rows))

     self.assertEqual(counts[0],counts[1])

  def test_discogs_reports(self):
     counts = []
     urls = ['http://www.ericervin.org/discogs/reports/artist_count',
              'http://www.ericervin.com/discogs/reports/artist_count']
     for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        
        self.assertEqual(page.status_code,200)
        self.assertIn('Count by Artist', soup.find_all('title')[0])
        rows = soup.find_all('td')
        counts.append(len(rows))

     self.assertEqual(counts[0],counts[1])

  def test_gematria(self):
     urls = ["http://ericervin.org/gematria", "http://ericervin.com/gematria"]
     for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        
        self.assertEqual(page.status_code,200)
        self.assertIn('Gematria', soup.find_all('title')[0])
        self.assertIn('Gematria', soup.find_all('h1')[0])

  def test_gematria_search_word(self):
     texts = []
     urls = ['http://www.ericervin.org/gematria/search?word=fish',
             'http://www.ericervin.com/gematria/search?word=fish']
     for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        
        self.assertEqual(page.status_code,200)
        self.assertIn('Gematria', soup.find_all('title')[0])
        
        texts.append(soup.find_all(id='id_other_word_table')[0])
        texts.append(soup.find_all(id='id_word_value_table')[0])

     self.assertEqual(texts[0],texts[2])
     self.assertEqual(texts[1],texts[3])

  def test_gematria_search_value(self):
     texts = []
     urls = ['http://www.ericervin.org/gematria/search?value=65',
             'http://www.ericervin.com/gematria/search?value=65']
     for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        
        self.assertEqual(page.status_code,200)
        self.assertIn('Gematria', soup.find_all('title')[0])
        
        texts.append(soup.find_all(id='id_word_value_table')[0])

     self.assertEqual(texts[0],texts[1])

  def test_philosophy(self):
     urls = ["http://ericervin.org/philosophy", "http://ericervin.com/philosophy"]
     for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        
        self.assertEqual(page.status_code,200)
        self.assertIn('Philosophy USA', soup.find_all('title')[0])
        self.assertIn('Philosophy USA', soup.find_all('h1')[0])
  
  def test_philosophy_reports(self):
      texts = []
      urls = ['http://ericervin.org/philosophy/reports/inst_count',
             'http://ericervin.com/philosophy/reports/inst_count']
      for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        
        self.assertEqual(page.status_code,200)
        self.assertIn('Philosophy Degrees Completed by Institution', soup.find_all('title')[0])
        
        texts.append(soup.find_all(id='id_result_table')[0])

      self.assertEqual(texts[0],texts[1])

  def test_powerball(self):
     urls = ["http://ericervin.org/powerball", "http://ericervin.com/powerball"]
     for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        
        self.assertEqual(page.status_code,200)
        self.assertIn('Powerball', soup.find_all('title')[0])
        self.assertIn('Powerball', soup.find_all('h1')[0])

  def test_serialism(self):
     urls = ["http://ericervin.org/serialism", "http://ericervin.com/serialism"]
     for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        
        self.assertEqual(page.status_code,200)
        self.assertIn('Serialism', soup.find_all('title')[0])
        self.assertIn('Serialism', soup.find_all('h1')[0])

  def test_wh_champions(self):
    urls = ["http://ericervin.org/wh_champions", "http://ericervin.com/wh_champions"]
    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        
        self.assertEqual(page.status_code,200)
        self.assertIn('Warhammer Champions', soup.find_all('title')[0])
        self.assertIn('Warhammer Champions', soup.find_all('h1')[0])

  def test_ericervin_dot_org(self):
      page = requests.get('http://ericervin.org')
      soup = BeautifulSoup(page.text,'html.parser')

      self.assertEqual(page.status_code,200)
      self.assertIn('Eric Ervin Dot Org', soup.find_all('title')[0])
      self.assertIn('Eric Ervin Dot Org', soup.find_all('h1')[0])

  def test_ericervin_dot_com(self):
      page = requests.get('http://ericervin.com')
      soup = BeautifulSoup(page.text,'html.parser')

      self.assertEqual(page.status_code,200)
      self.assertIn('Eric Ervin Dot Com', soup.find_all('title')[0])
      self.assertIn('Eric Ervin Dot Com', soup.find_all('h1')[0])

  def test_ericcervin_dot_github_dot_io(self):
      page = requests.get('http://ericcervin.github.io')
      soup = BeautifulSoup(page.text,'html.parser')

      self.assertEqual(page.status_code,200)
      self.assertIn('ericcervin.github.io', soup.find_all('title')[0])

  def test_noiselife_dot_org(self):
      page = requests.get('http://noiselife.org')
      soup = BeautifulSoup(page.text,'html.parser')

      self.assertEqual(page.status_code,200)
      self.assertIn('noiselife-dot-org', soup.find_all('title')[0])
      
        
if __name__ == '__main__':
    unittest.main()
