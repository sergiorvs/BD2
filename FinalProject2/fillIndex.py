from AVL import *



if __name__ == '__main__':
    t = AVL()
    # t.insert(5)
    # t.insert(9)
    # t.insert(13)
    # t.insert(10)
    # t.insert(18)
    # t.insert(28)
    # t.insert(95)
    # theList = []
    # theList.append(5)
    # theList.append(6)
    # t.insert(theList)
    t.insert('c')
    t.insert('x')
    t.insert('t')
    t.insert('u')
    t.insert('b')
    t.insert('w')
    t.insert('b')


    a = t.find('b')
    print(a.pointer)





    t.preShow(t.root)
    afile = open(r'tree.pkl', 'wb')
    pickle.dump(t, afile)
    afile.close()
    print("\n")