class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be a string 2-16 chars.")
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise Exception("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        from .article import Article
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list(set([a.author for a in self.articles()]))

    def article_titles(self):
        if not self.articles():
            return None
        return [a.title for a in self.articles()]

    def contributing_authors(self):
        authors = [a.author for a in self.articles()]
        result = [a for a in set(authors) if authors.count(a) > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        from .article import Article
        if not Article.all:
            return None
        return max(cls.all, key=lambda m: len(m.articles()))
