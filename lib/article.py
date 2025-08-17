class Article:
    all = []

    def __init__(self, author, magazine, title):
        from .author import Author
        from .magazine import Magazine

        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string 5-50 chars.")
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance.")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance.")

        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title  # immutable

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        from .author import Author
        if not isinstance(value, Author):
            raise Exception("Author must be an Author instance.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        from .magazine import Magazine
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be a Magazine instance.")
        self._magazine = value
