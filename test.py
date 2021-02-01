class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        ans=[]
        if root:
            
            cache=collections.defaultdict(list)
            stack=collections.deque()
            stack.append((root,0))
            while stack:
                temp=collections.defaultdict(list)
                for _ in range(len(stack)):
                    node,x=stack.popleft()
                    temp[x].append(node.val)
                    if node.left:
                        stack.append((node.left,x-1))   
                    if node.right:
                        stack.append((node.right,x+1))
                for k in temp.keys():
                    cache[k].extend(sorted(temp[k]))
            for x in sorted(cache.keys()):
                ans.append(cache[x])
            #print(cache)
        return ans

ans = []
        if root:
            vertical_dic = dict()
            node_stack = collections.deque()
            node_stack.append((root, 0, 0))
            while node_stack:
                for _ in range(len(node_stack)):
                    node, x, y = node_stack.popleft()
                    if x not in vertical_dic:
                        vertical_dic[x] = []
                    vertical_dic[x].append(node.val)
                    vertical_dic[x].sort()
                    if node.left:
                        node_stack.append((node.left, x-1))
                    if node.right:
                        node_stack.append((node.right, x+1))
            for key in sorted(vertical_dic.keys()):
                ans.append(vertical_dic[key])
        return ans

