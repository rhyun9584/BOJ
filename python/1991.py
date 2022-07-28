N = int(input())

def get_idx(char):
    return ord(char) - ord('A')

tree = [[-1, -1] for _ in range(N)]
for _ in range(N):
    now, left, right = map(get_idx, input().split())
    if left >= 0:
        tree[now][0] = left
    if right >= 0:
        tree[now][1] = right

def preorder(idx):
    print(chr(idx+ord('A')), end='')

    if tree[idx][0] >= 0:
        preorder(tree[idx][0])
    if tree[idx][1] >= 0:
        preorder(tree[idx][1])

def inorder(idx):
    if tree[idx][0] >= 0:
        inorder(tree[idx][0])
    
    print(chr(idx+ord('A')), end='')

    if tree[idx][1] >= 0:
        inorder(tree[idx][1])
    
def postorder(idx):
    if tree[idx][0] >= 0:
        postorder(tree[idx][0])
    if tree[idx][1] >= 0:
        postorder(tree[idx][1])

    print(chr(idx+ord('A')), end='')

preorder(0)
print()

inorder(0)
print()

postorder(0)
