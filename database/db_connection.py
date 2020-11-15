# result = []
# for i in range(4):
#     result.append((lambda x, i=i: i*x)(i))

# print(result)
# result = []
# for i in range(4):
#     result.append((lambda x: i*x)(1))
#
# print(result)



def multipliers():
    return [(lambda x: i * x)(2) for i in range(4)]


a = multipliers()
print(a)