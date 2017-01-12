class GoodData:
    def __init__(self,
                 name = None,
                 url = None,
                 count_comments = None,
                 ups = None,
                 description = None,
                 cost = None,
                 date = None,
                 section = None,
                 last_up = None,
                 author_name = None):
        self.url = url
        self.count_comments = count_comments
        self.ups = ups
        self.description = description
        self.cost = cost
        self.date = date
        self.section = section
        self.last_up = last_up
        self.author_name = author_name
        self.name = name

