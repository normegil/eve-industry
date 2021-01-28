class Category:
    def __init__(self, id_, name):
        self.id = id_
        self.name = name
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)

    def group(self, searched_group_id):
        for group in self.groups:
            if searched_group_id == group.id:
                return group
        return None
