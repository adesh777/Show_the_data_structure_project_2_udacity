import sys
from collections import Counter, namedtuple

Pair = namedtuple('Pair', 'frequency char')


class Node:
    def __init__(self, value, char=None):
        self.value = value
        self.char = char
        self.left = None
        self.right = None

    def get_pair(self):
        return Pair(frequency=self.value, char=self.char)

    def __repr__(self):
        return str(self.value)


class HuffmanTree:
    def __init__(self, pair=None, node=None):
        self.root = Node(None)
        self.root.left = node if node else Node(pair.frequency, pair.char)

    def append(self, pair):
        if self.root.left and self.root.right:
            new_tree = HuffmanTree(node=self.root)
            new_tree.append(pair)
            self.re_assign_root(new_tree)
        else:
            self.root.right = Node(pair.frequency, pair.char)
            self.root.value = self.root.left.value + self.root.right.value

    def mix_with_tree(self, tree):
        mixed_tree = HuffmanTree(node=self.root)

        mixed_tree.root.right = tree.root
        mixed_tree.root.value = mixed_tree.root.left.value + mixed_tree.root.right.value
        self.re_assign_root(mixed_tree)

    def re_assign_root(self, sub_tree):
        self.root = sub_tree.root

    def traverse_dfs(self):
        visit_order = list()
        root = self.root

        def traverse(node):
            if node:
                if node.get_pair().char is not None:
                    visit_order.append(node.get_pair())

                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return visit_order

    def __repr__(self):
        # return '\n'.join(self.traverse_dfs())
        return str(self.root.left) + ' - \'' + str(self.root.value) + '\' - ' + str(self.root.right)


def lowest_frequencies(frequencies):
 
    lowest_freq = min(frequencies, key=lambda x: x.frequency).frequency
    lowest_freq_pairs = [pair for pair in frequencies if pair.frequency == lowest_freq]
    new_frequencies = [pair for pair in frequencies if pair.frequency != lowest_freq]
    return lowest_freq_pairs, new_frequencies


def create_subtrees_in_pairs(trees, lowest_freq_pairs):
 
    if len(lowest_freq_pairs) == 1 and len(trees) == 0:
        sub_tree = HuffmanTree(lowest_freq_pairs[0])
        trees.append(sub_tree)
        return

    for i in range(1, len(lowest_freq_pairs), 2):
        sub_tree = HuffmanTree(lowest_freq_pairs[i - 1])
        sub_tree.append(lowest_freq_pairs[i])
        trees.append(sub_tree)

    if len(lowest_freq_pairs) % 2 == 1:
        trees[0].append(lowest_freq_pairs[-1])


def add_one_freq_to_each_tree(trees, lowest_freq_pairs):
   
    for i, tree in enumerate(trees):
        if i + 1 <= len(lowest_freq_pairs):
            tree.append(lowest_freq_pairs[i])
    if len(lowest_freq_pairs) > len(trees):
        lowest_freq_pairs = lowest_freq_pairs[len(trees):]
        create_subtrees_in_pairs(trees, lowest_freq_pairs)


def build_final_tree_from_trees(trees):

    trees = sorted(trees, key=lambda x: x.root.value)
    while len(trees) > 1:
        trees[0].mix_with_tree(trees[1])
        del trees[1]

    return trees[0]


def find_path_to_char(char, node, previous_path_found=""):
    if node:
        if node.get_pair().char == char:
            return previous_path_found

        found_left = find_path_to_char(char, node.left, previous_path_found + "0")
        if found_left:
            return found_left

        found_right = find_path_to_char(char, node.right, previous_path_found + "1")
        if found_right:
            return found_right


def get_encoded_data(root_node, data):
    return ' '.join([find_path_to_char(c, root_node) for c in data])


def huffman_encoding(data):
    trees = []

    frequencies = [Pair(freq, char) for char, freq in Counter(sorted(data)).items()]

    while len(frequencies) > 0:

        lowest_freq_pairs, frequencies = lowest_frequencies(frequencies)

        if len(trees) == 0:
           
            create_subtrees_in_pairs(trees, lowest_freq_pairs)
        else:
            
            add_one_freq_to_each_tree(trees, lowest_freq_pairs)

    
    final_tree = build_final_tree_from_trees(trees)
    data_encoded = get_encoded_data(final_tree.root, data)

    return data_encoded, final_tree


def find_char_from_path(path, node):
  
    if node:
        if node.get_pair().char is not None:
            return node.get_pair().char

        if len(path) > 0:
            direction = path[0]
            char = None
            if direction == "0":
                char = find_char_from_path(path[1:], node.left)
            elif direction == "1":
                char = find_char_from_path(path[1:], node.right)

            return char


def huffman_decoding(data, codified_tree):
   
    return ''.join([find_char_from_path(path, codified_tree.root) for path in data.split()])


def test_case(data):
    if data is None or len(str(data)) == 0:
        print('Empty data!')
        return

    if type(data) != str:
        print('Invalid data!', data)
        return

    print("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print("The content of the data is: {}\n".format(data))

    encoded_data, t = huffman_encoding(data)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data.replace(' ', ''), base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, t)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


if __name__ == "__main__":
    test_case('The bird is the word')
    test_case('aaaaa')
    test_case('')
    test_case(123)