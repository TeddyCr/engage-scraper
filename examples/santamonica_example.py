from __future__ import absolute_import
from engage_scraper.scraper_logics.santamonica_scraper_logic import SantaMonicaScraper

smscraper = SantaMonicaScraper()
smscraper.get_available_agendas()
smscraper.scrape()