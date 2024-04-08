"""
Problem link: https://leetcode.com/problems/lru-cache/

Idea:
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    - Use Double LinkedList: since we have to move back or forward to find the recent used node
    - Store value to a dict() - key: cacheNode --> Get O(1)
    - lruNode: track least recent used node
    - current: track current node (for added)

Time complexity:

Space Complexity:
"""
class CacheNode:
    def __init__(self, key, val, prev=None, next=None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
    def __str__(self) -> str:
        return f"{self.val}"


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity

        self.left = CacheNode(-1, -1) # sentinel
        self.right = CacheNode(-1, -1) # sentinel
        self.left.next, self.right.prev = self.right, self.left

    # O(1)
    def get(self, key: int) -> int:
        if key in self.cache:
            # Update most recent node
            cacheNode = self.cache[key]
            print(cacheNode.next)
            self.remove(cacheNode) 
            self.insertRight(cacheNode)
            return self.cache[key].val
        return -1

    # O(1)
    def put(self, key: int, value: int) -> None:
        newNode = CacheNode(key, value)
        if key in self.cache:
            # Update it and move to right
            cacheNode = self.cache[key]
            self.remove(cacheNode) 
            self.insertRight(newNode)
            return

        if len(self.cache) == self.capacity:
            print("ABC: ", self.left.next)
            self.remove(self.left.next)
        self.insertRight(newNode)

    def remove(self, node) -> None:
        nodeBefore, nodeAfter = node.prev, node.next
        nodeBefore.next = nodeAfter
        nodeAfter.prev = nodeBefore
        self.cache.pop(node.key)
        

    def insertRight(self, node) -> None:
        currentLastNode = self.right.prev
        node.prev = currentLastNode
        node.next = self.right
        currentLastNode.next = node
        self.right.prev = node
        self.cache[node.key] = node

    def getLeft(self):
        print(self.left.next)

    def getRight(self):
        print(self.right.prev)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
        
lru = LRUCache(4)
lru.put(1, 1)
lru.put(2, 2)
lru.get(2)
# lru.put(3, 3)
# lru.put(4, 4)
# lru.put(1, 11)
# lru.getLeft() #2
# lru.getRight() # 11
# lru.get(2)
# lru.getLeft() #3
# lru.get(1)
