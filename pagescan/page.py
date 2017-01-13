import urllib.request
from lxml import html as html

from .gooddata import GoodData

class BaraholkaPage:
    def __init__(self):
        self.url = None
        self.page = None
        self.correct = False

    def download(self, url):
        self.url = url
        self.page = str(urllib.request.urlopen(url).read().decode('utf-8'))
        self.correct = self.page.find('m-title') != -1

    def is_nice_page(self):
        return self.correct

    def data(self):
        if self.correct == False:
            raise Exception("{} is not baraholha good page".format(self.url))

        data = GoodData()
        data.url = self.url

        root = html.fromstring(self.page)
    
        element_with_section = root.find_class('b-path')[0]
        data.section = ""
        for x in element_with_section.itertext():
            data.section += x

        data.name = root.find_class('m-title-i title').pop().attrib['title']
        data.cost = root.find_class('price-primary').pop().text.split(',')[0]
        data.description = root.find_class('fast-desc').pop().text
        data.author_name = root.find_class('_name star-notes')[0].text
        data.ups = root.find_class('b-ba-subj-up b-ba-subj-upped').pop().find('strong').text.split()[0]
        data.last_up = [x for x in root.find_class('b-ba-subj-up b-ba-subj-upped').pop().itertext()][2].strip()
        data.date = root.find_class('msgpost-date')[0].find('span').text.strip()
        data.count_comments = len(root.find_class('b-msgpost-txt')) - 1
        return data
