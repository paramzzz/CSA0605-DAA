import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_tree(characters, frequencies):
    
    pq = []
    for char, freq in zip(characters, frequencies):
        node = Node(char, freq)
        heapq.heappush(pq, node)

    while len(pq) > 1:
        node1 = heapq.heappop(pq)
        node2 = heapq.heappop(pq)
        merged_node = Node(None, node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(pq, merged_node)

    huffman_codes = []
    def generate_codes(node, code):
        if node.char is not None:
            huffman_codes.append((node.char, code))
        if node.left:
            generate_codes(node.left, code + '0')
        if node.right:
            generate_codes(node.right, code + '1')

    root = pq[0]
    generate_codes(root, '')

    return huffman_codes


n = 4
characters = ['a', 'b', 'c', 'd']
frequencies = [5, 9, 12, 13]
print("The Huffman Codes for each character are:", huffman_tree(characters, frequencies))
