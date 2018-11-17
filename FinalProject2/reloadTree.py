from AVL import *


if __name__ == '__main__':
    afile = open(r'tree.pkl', 'rb')
    t = pickle.load(afile)
    afile.close()
    t.preShow(t.root)
    print("\n")
    t.preorder(t.root)
    print("\n")
    