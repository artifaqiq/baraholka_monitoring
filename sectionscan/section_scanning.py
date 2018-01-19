import urllib.request
import urllib.parse
from furl import furl

from lxml import html as html

_GOODS_PER_PAGE = 50


def get_goods_urls(section_url, cat=1):
    """
    Return list of goods urls on current section
    Example:  >>> urls = get_goods_urls('http://baraholka.onliner.by/viewforum.php?f=2')
              >>> len(urls)
              13800

    Cat is ad filter constant:
    1 - sale
    2 - buying
    3 - service
    4 - rent
    5 - closed
    """

    url = str(furl(section_url).add({'cat': cat}))
    page = str(urllib.request.urlopen(url).read().decode('utf-8'))
    root = html.fromstring(page)

    count_pages = len(root.find_class('wraptxt'))

    urls = []
    for i in range(0, count_pages - 1):
        url = str(furl(section_url).add({'start' : i * _GOODS_PER_PAGE}))
        urls += _get_goods_urls_one_page(url, cat)

    return urls


def _get_goods_urls_one_page(section_url, cat=1):
    url = str(furl(section_url).add({'cat':cat}))
    page = str(urllib.request.urlopen(url).read().decode('utf-8'))
    root = html.fromstring(page)

    if len(root.find_class('onliner-outer')) == 0:
        raise Exception('{} is not baraholka onliner section url'.format(url))

    urls = []

    table = root.find_class('ba-tbl-list__table').pop()

    for tr in table:
        if 'class' not in tr.keys():
            try:
                relative_href = tr.find_class('wraptxt').pop().find('a').get('href')
            except IndexError:
                next

            absolute_url = urllib.parse.urljoin(url, relative_href)
            urls.append(absolute_url)

    return urls





