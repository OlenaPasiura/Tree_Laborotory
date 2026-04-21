def pre_order(node):
    if node is None:
        return []
    our_lst = [node.data]
    our_lst += pre_order(node.left)
    our_lst += pre_order(node.right)
    return our_lst

def in_order(node):
    if node is None:
        return []
    our_lst = in_order(node.left)
    our_lst += [node.data]
    our_lst += in_order(node.right)
    return our_lst

def post_order(node):
    if node is None:
        return []
    our_lst = post_order(node.left)
    our_lst += post_order(node.right)
    our_lst += [node.data]
    return our_lst
