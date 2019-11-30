

class TreeGraph:

    def __init__(self):
        self.root = Node(Vertex("C:\""))

    def add(self, value, current=None):
        if not current:
            current = self.root
            return current.children.add(value)
        else:
            

    def search(self):
