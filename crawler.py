from lxml import html
import requests

def get_english_definitions(word):

    url = 'http://www.latin-dictionary.org/%s' % (word)
    page = requests.get(url)
    tree = html.fromstring(page.content)

    definitions = tree.xpath('//div[@class="definition"]/text()')
    return definitions
