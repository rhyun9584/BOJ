import sys
sys.setrecursionlimit(10**6)

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

preorder = []

# 특정 값이 node일 때 inorder에서의 그 위치
index = [0] * (N+1)
for i in range(N):
    index[inorder[i]] = i

def solve(i_s, i_e, p_s, p_e):
    if i_s > i_e:
        return
        
    # postorder의 마지막 노드가 최상위노드
    preorder.append(postorder[p_e])
    # inorder에서의 최상위노드 위치
    node_idx = index[postorder[p_e]]

    # 리스트에 노드가 하나뿐이므로 더이상 탐색할 필요가 없음
    if i_s == i_e:
        return

    # 왼쪽 노드부터 재귀 호출
    solve(i_s, node_idx-1, p_s, p_s+(node_idx-1 - i_s))
    solve(node_idx+1, i_e, p_s+(node_idx-1 - i_s)+1, p_e-1)

solve(0, N-1, 0, N-1)

print(" ".join(map(str, preorder)))
