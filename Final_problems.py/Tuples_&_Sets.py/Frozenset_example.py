immutable_set = frozenset([1, 2, 3, 4, 5])
immutable_set.remove(2) # throughs error for frozenset, it has no attribute remove
print(f"Frozen Set : {immutable_set}")
print(type(immutable_set))