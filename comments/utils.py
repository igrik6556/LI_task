# -*- coding: utf-8 -*-


def create_tree(items):
    """
    Creates a tree comments.
    """
    tree = []
    for item in items:
        item.children = []
        item.level = 1
        if item.parent is None:
            tree.append(item)
        else:
            try:
                parent = [p for p in items if p.id == item.parent_id][0]
                parent.children.append(item)
                item.level = parent.level + 1
            except ValueError:
                tree.append(item)
    return tree
