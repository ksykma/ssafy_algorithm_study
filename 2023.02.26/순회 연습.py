tree = [0, 'A', 'B', 'C', 'D', 'E', 'F']

def inorder(v):
    if v > 6:
        return
    else:
        inorder(v*2)
        inorder(v*2+1)
        print(tree[v], end = ' ')
inorder(1)
