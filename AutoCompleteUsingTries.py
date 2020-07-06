class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.flag = False


def addData(root, word):
    current = root
    for w in word:
        if root.children[ord(w) - ord('a')] == None:
            root.children[ord(w) - ord('a')] = TrieNode()
        root = root.children[ord(w) - ord('a')]
    root.flag = True
    return current


def search(word, root):
    for w in word:
        if root.children[ord(w) - ord('a')] != None:
            root = root.children[ord(w) - ord('a')]
        else:
            return None
    return root


def autoComplete(root, word, prefix):
    if root.flag == True and len(word) != 0:
        print(prefix, end="")
        for j in word:
            print(j, end="")
        print()
    for i in range(26):
        if root.children[i] is not None:
            word.append(chr(ord('a') + i))
            autoComplete(root.children[i], word, prefix)
            word.pop()


def permutation(word):
    l = []
    for i in word:
        l.append(i)
    permutation = []
    permHelper(l, 0, permutation)
    return permutation


def permHelper(word, i, permutation):
    if i == len(word)-1:
        str1 = ""
        str1 = str1.join(word)
        permutation.append(str1)
    else:
        for j in range(i,len(word)):
            word[i], word[j] = word[j], word[i]
            permHelper(word, i+1, permutation)
            word[i], word[j] = word[j], word[i]


root = TrieNode()
f = open('/Users/arnab/Desktop/bonga.txt', 'r')
for line in f.readlines():
    line = line.strip()
    root = addData(root, line)
prefix = input("Enter the prefix of the word: ")
s = search(prefix, root)
var = False
if s is None:
    arr = permutation(prefix)
    for i in arr:
        s1 = search(i, root)
        if s1 is not None:
            autoComplete(s1, [], i)
            var = True
    if var == False:
        print("No such word exist")
else:
    autoComplete(s, [], prefix)
