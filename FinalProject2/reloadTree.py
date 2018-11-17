from AVL import *


if __name__ == '__main__':
    afile = open('idx_edad.pkl', 'rb')
    t = pickle.load(afile)
    afile.close()
    t.preShow(t.root)
    print("\n")
    t.preorder(t.root)
    print("\n")
    

    a = t.find(17)
    # a = t.find(28)
    print("after find: ", a.label, " ", a.pointer)