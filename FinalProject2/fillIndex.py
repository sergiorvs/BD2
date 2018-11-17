from AVL import *



if __name__ == '__main__':
    t = AVL()
    t.insert(5)
    t.insert(9)
    t.insert(13)
    t.insert(10)
    t.insert(18)
    t.preShow(t.root)
    afile = open(r'tree.pkl', 'wb')
    pickle.dump(t, afile)
    afile.close()
    print("\n")