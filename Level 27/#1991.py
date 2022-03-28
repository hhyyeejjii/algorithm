#1991 전위. 중위. 후위.
tree= {}
n= int(input())

def front(node): #전위순회는 루트 -> 왼쪽 -> 오른쪽
    if node == '.' :
        return
    print(node, end= '')  
    front(tree[node][0]) 
    front(tree[node][1]) 

def center(node): #중위순회는 왼쪽 ->루트 -> 오른쪽
    if node == '.' :
        return
    center(tree[node][0]) 
    print(node, end= '')
    center(tree[node][1]) 

def back(node): #후위순회는 왼쪽 ->오른쪽 ->루트
    if node == '.' :
        return
    back(tree[node][0]) 
    back(tree[node][1]) 
    print(node, end= '')

#트리함수 만들기
for _ in range (n) :
    root, left, right = input().split()
    tree[root] = (left, right)

front("A")
print()
center("A")
print()
back("A")
