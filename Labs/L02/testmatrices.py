import numpy as np

# TEST MATRICES/LIN. SYSTEMS
A0 = np.random.rand(5, 5)
v = np.random.rand(5)

A1 = np.random.rand(4, 4)

A2 = np.random.rand(3, 4)

A3 = A1.copy()
A3[:, 2] = 0

A4 = A1.copy()
A4[:,0] = 0

A5 = np.hstack([A4, A1])
A5 = A5[:, :5]

A6 = A5.copy()
A6[:, 3] = 0

b0 = A0 @ np.ones((A0.shape[1], 1))
b1 = A1 @ np.ones((A1.shape[1], 1))
b2 = A2 @ np.ones((A2.shape[1], 1))
b3 = b1.copy()

Ab0 = np.hstack([A0, b0])
Ab1 = np.hstack([A1, b1])
Ab2 = np.hstack([A2, b2])
Ab3 = np.hstack([A3, b3])


def main():
    print('********** Matrix A0 **********')
    print(A0)
    print('')
    
    print('********** Matrix A1 **********')
    print(A1)
    print('')

    print('********** Matrix A2 **********')
    print(A2)
    print('')

    print('********** Matrix A3 **********')
    print(A3)
    print('')

    print('********** Matrix A4 **********')
    print(A4)
    print('')

    print('********** Matrix A5 **********')
    print(A5)
    print('')

    print('********** Matrix A6 **********')
    print(A6)
    print('')

    print('********** Vector v (random) **********')
    print(v)
    print('')
    
    print('********** Vector b0 **********')
    print(b0)
    print('N.B.: np.ones((A0.shape[1], 1)) is solution of the L.S.: A0x = b0')
    print('')
    
    print('********** Vector b1 **********')
    print(b1)
    print('N.B.: np.ones((A1.shape[1], 1)) is solution of the L.S.: A1x = b1')
    print('')

    print('********** Vector b2 **********')
    print(b2)
    print('N.B.: np.ones((A2.shape[1], 1)) is solution of the L.S.: A2x = b2')
    print('')

    print('********** Vector b3 **********')
    print(b3)
    print('')

    print('********** Augmented Matrix of L.S. A0x = b0 **********')
    print(Ab0)
    print('')
    
    print('********** Augmented Matrix of L.S. A1x = b1 **********')
    print(Ab1)
    print('')
    
    print('********** Augmented Matrix of L.S. A2x = b2 **********')
    print(Ab2)
    print('')
    
    print('********** Augmented Matrix of L.S. A3x = b3 **********')
    print(Ab3)
    print('')

if __name__ == '__main__':
    main()