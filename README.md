# baraholka_monitoring
collection and analysis of statistics http://baraholka.onliner.by/

## pagescan package
Getting statistics about a product
Example: 
``` python
    import pagescan
    page = pagescan.BaraholkaPage()
    page.download('http://baraholka.onliner.by/viewtopic.php?t=18922805')
    page.is_nice_page() 
    page.data()
```

## sectionscan package
Getting all references to goods
Example:
``` python
    import sectionscan
    sectionscan.get_goods_urls('http://baraholka.onliner.by/viewforum.php?f=2')
```

