class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Author name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        return self._name  # immutable

    def articles(self):
        from .article import Article
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        return list(set([a.magazine for a in self.articles()]))

    def add_article(self, magazine, title):
        from .article import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set([a.magazine.category for a in self.articles()]))
