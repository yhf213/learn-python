def mul(x, y):
    return x * y

# 测试
# print('mul(5) =', mul(5))
# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))
# print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5,1) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
# elif mul(5, 6, 7) != 210:
#    print('mul(5, 6, 7)测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')
    mul(6,6)