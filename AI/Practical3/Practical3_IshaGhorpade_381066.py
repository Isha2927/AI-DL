class FamilyMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_children_names(self):
        return ", ".join([c.name for c in self.children])

def print_tree(member, indent=""):
    print(f"{indent}{member.name} ({member.age})")
    for child in member.children:
        print_tree(child, indent + "  ")

if __name__ == "__main__":
    # creating family members
    grandparent = FamilyMember("Grandparent", 75)
    parent1 = FamilyMember("Parent1", 50)
    parent2 = FamilyMember("Parent2", 48)
    child1 = FamilyMember("Child1", 20)
    child2 = FamilyMember("Child2", 18)
    child3 = FamilyMember("Child3", 15)

    # building family relation
    grandparent.add_child(parent1)
    grandparent.add_child(parent2)
    parent1.add_child(child1)
    parent1.add_child(child2)
    parent2.add_child(child3)

    # print hierarchical tree
    print_tree(grandparent)

    print(f"{parent1.name}'s children: {parent1.get_children_names()}")
    print(f"{child1.name}'s parent: {child1.parent.name if child1.parent else 'Unknown'}")
