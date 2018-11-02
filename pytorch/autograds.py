'''
AUTOGRAD: AUTOMATIC DIFFERENTIATION
'''

import torch

# Tensor


def add_requires_grad():
    '''Function requires grad.'''
    tensor_x = torch.ones(2, 2, requires_grad=True)
    print(tensor_x)
    return tensor_x


Y = add_requires_grad() + 2
print(Y)
print(Y.grad_fn)

Z = Y * Y * 3
OUT = Z.mean()

print(Z, OUT)

A = torch.randn(2, 2)
A = ((A*3) / (A-1))
print(A.requires_grad)
A.requires_grad_(True)
print(A.requires_grad)
B = (A*A).sum()
print(B.grad_fn)

# Gradients
