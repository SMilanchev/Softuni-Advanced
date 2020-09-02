def my_sum(x, *args):
    print(args)
    return sum(args) + x


print(my_sum(1, 2))
print(my_sum(1, 2, 3))
print(my_sum(0))