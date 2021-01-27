class Category:
    def __init__(self, id_, name):
        self.id = id_
        self.name = name
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)

    def search_or_add_group(self, searched_group):
        for group in self.groups:
            if searched_group.id == group.id:
                return group
        self.groups.append(searched_group)
        return searched_group
