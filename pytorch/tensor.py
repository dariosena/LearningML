import torch
import numpy as np

# Construct a 5 x 3 matrix, unitialized
a = torch.empty(5, 3)
print(a)

print('')

# Construct a randomly initialized matrix
a = torch.rand(5, 3)
print(a)

print('')

# Construct a matrix filled zeros and dtype long
a = torch.zeros(5, 3, dtype=torch.long)
print(a)

print('')

# Construct a tensor directly from data
a = torch.tensor([5.5, 3])
print(a)

print('')

# override type
a = a.new_ones(5, 3, dtype=torch.double)
print(a)

print('')

a = torch.randn_like(a, dtype=torch.float)
print(a)
print(a.size())

# Operations
x = torch.randn(3, 5)
y = torch.randn(3, 5)

print('')
print(x)
print('')
print(y)
print('')
print(x + y)
print('')
print(x.add(y))
print('')
print(x.add_(y))
print('')
print(torch.add(x, y))

testA = torch.tensor([[1, 1], [2, 2]])
testB = torch.tensor([[1, 1], [2, 2]])
print(torch.add(testA, testB))


result = torch.empty(2, 2, dtype=torch.long)
torch.add(testA, testB, out=result)
print(result)

a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print()
print(b)
