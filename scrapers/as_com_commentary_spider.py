import scrapy

valid_urls = [
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_1_179512/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_1_179519/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_1_179513/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_1_179515/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_1_179514/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_1_179518/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_1_179516/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_1_179510/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_1_179511/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_1_179517/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_30_179801/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_30_179802/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_30_179805/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_30_179803/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_30_179800/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_30_179804/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_30_179807/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_30_179809/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_30_179808/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_30_179806/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_29_179791/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_29_179797/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_29_179798/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_29_179795/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_29_179793/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_29_179792/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_29_179794/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_29_179796/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_29_179799/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_29_179790/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_28_179786/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_28_179788/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_28_179781/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_28_179780/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_28_179785/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_28_179789/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_28_179782/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_28_179784/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_28_179787/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_28_179783/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_26_179764/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_26_179769/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_26_179768/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_26_179766/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_26_179763/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_26_179767/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_26_179762/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_26_179765/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_26_179761/narracion",
    "http://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_26_179760/narracion"
]

class ASCommentarySpider(scrapy.Spider):
  name = 'as_com_commentary'
  start_urls = [valid_urls[0]]

  def __init__(self):
      self.current_index = 0

  def parse(self, response):

    for commentary_container in response.xpath('//*[@id="comments-live-es"]'): #css('#comments-live-es'):
        for commentary_el in commentary_container.css('.cnt-comentario::text'):
            commentary = commentary_el.extract().replace('.', ' ').strip()
            if len(commentary) > 1: 
                yield {"text": commentary}
    
    self.current_index += 1
    yield scrapy.Request(valid_urls[self.current_index], callback=self.parse)
