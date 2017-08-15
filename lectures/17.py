# python modules and packages
import module
import sys

print(module.sum(2, 4))
print(module.mul(2, 4))
print(module.safe_sum(2,"w"))
print(module.safe_sum(2,4))
print(module.safe_sum(10, 10.4)) # not operand type? lol

print(sys.path)
#sys.path.append("Where I want to search")
#sys.path.remove("Where I do not want to search")
