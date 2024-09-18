class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def calculate_frequency(characters, frequencies):
    frequency_dict = {}
    for char, freq in zip(characters, frequencies):
        frequency_dict[char] = freq
    return frequency_dict

def build_huffman_tree(characters, frequencies):
    frequency_dict = calculate_frequency(characters, frequencies)
    nodes = [Node(char, freq) for char, freq in frequency_dict.items()]
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        node1 = nodes.pop(0)
        node2 = nodes.pop(0)
        merged_node = Node(None, node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2
        nodes.append(merged_node)
    return nodes[0]

def build_huffman_codes_helper(root, current_code, codes):
    if root == None:
        return
    if root.char != None:
        codes[root.char] = current_code
    build_huffman_codes_helper(root.left, current_code + "0", codes)
    build_huffman_codes_helper(root.right, current_code + "1", codes)

def build_huffman_codes(root):
    codes = {}
    build_huffman_codes_helper(root, "", codes)
    return codes

def huffman_decode(encoded_string, root):
    decoded_string = ""
    current_node = root
    for bit in encoded_string:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char != None:
            decoded_string += current_node.char
            current_node = root
    return decoded_string

# Test Case 1
n = 4
characters = ['a', 'b', 'c', 'd']
frequencies = [5, 9, 12, 13]
encoded_string = '1101100111110'

root = build_huffman_tree(characters, frequencies)
codes = build_huffman_codes(root)
decoded_string = huffman_decode(encoded_string, root)

print("Decoded String:", decoded_string)
