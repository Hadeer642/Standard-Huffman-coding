filein = open("input.txt", "r")
fileout = open("output.txt", 'w')

seq = filein.readline()
filein.close()
frequency = {}
# Calculating frequency
for char in seq:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# First step
# print(frequency)
frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
# print(frequency)

nodes = frequency


# Second Step
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def nodes(self):
        return self.left, self.right

    def __str__(self):
        return '%s_%s' % self.left, self.right


while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)


# For each non-leaf node, assign 0 to the left edge and 1 to the right edge

def huffman_code_tree(node, left=True, binstring=''):
    if type(node) is str:
        return {node: binstring}

    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binstring + '0'))
    d.update(huffman_code_tree(r, False, binstring + '1'))

    return d


huffmanCode = huffman_code_tree(nodes[0][0])

Compression = 0
fileout.write("symbol==> code:" + '\n')
for (char, frequency) in frequency:
    Compression += frequency * len(huffmanCode[char])
    fileout.write(char+ "     ==> " + huffmanCode[char] + '\n')

h = str(len(seq) * 8)
y = str(Compression)
fileout.write('\n' + "Size before compression: " + h + " bits")
fileout.write('\n' + "Size after compression: " + y + " bits")

"""
The priority queue is an advanced type of the queue data structure. 
Instead of dequeuing the oldest element, a priority queue sorts and dequeues elements based on their priorities.
"""
