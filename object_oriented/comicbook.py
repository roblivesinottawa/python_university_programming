class ComicBook:
    def __init__(self, title, publisher):
        self.title = title
        self.publisher = publisher

    def __repr__(self):
        return f"{self.title} by {self.publisher}"

comic = ComicBook("The Punisher War Zone", "Marvel Comics")

print(comic)
print(comic.title)