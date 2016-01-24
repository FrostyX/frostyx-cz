import markdown


class Article(object):
    def __init__(self, md):
        if not md.startswith("---"):
            return

        head = md[4:md.find("---", 3)].split("\n")[:-1]
        head = [x.lstrip() for x in head]

        for attr in head:
            split = attr.find(":")
            setattr(self, attr[:split], attr[split+1:].strip())

        self.categories = self.categories.split(", ")
        self.text = markdown.markdown(md[md.find("---", 3)+3:])
