def tree_by_levels(node):
    if node is None:
        return []
    our_lst = [node]
    l_q = []
    while our_lst:
        el = our_lst.pop(0)
        l_q.append(el.value)
        if el.left:
            our_lst.append(el.left)
        if el.right:
            our_lst.append(el.right)
    return l_q
