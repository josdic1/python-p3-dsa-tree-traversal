class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        return self._dfs(self.root, id)

    def _dfs(self, node, id):
        if node.get('id') == id:
            return node

        for child in node.get('children', []):
            found = self._dfs(child, id)
            if found:
                return found

        return None
