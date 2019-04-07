# coding: utf-8
"""
手中一幅扑克牌，假设顺序为ABCDEF，把第一张放到桌面上，第二张挪到最后，第三张放到桌面，第四张挪到最后，一直到所有牌都在桌面

BCDEF　　 A
CDEFB
DEFB　　　AC
EFBD
…

把最后在桌面上的这副牌给你，求出原始牌的顺序
"""

# input: [D, F, B, E, C, A]
# output:[A, B, C, D, E, F]
import numpy as np
global count
count = 0

def create_stack(input = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']):
    output = []
    add = True
    while(len(input) != 0):
        if add is True:
            output.insert(0, input[0])
            input.pop(0)
            add = False
        else:
            card = input[0]
            input.pop(0)
            input.append(card)
            add = True
    print('create stack: ', output) # ['D', 'F', 'B', 'E', 'C', 'A']
    return output # ['H', 'D', 'F', 'B', 'G', 'E', 'C', 'A']


def make_stack(input):
    global count
    stacks = []
    start = len(input)
    end = None
    while start != 1:
        stack = []
        end = int(np.ceil(start / 2))
        for i in range(start - 1, end - 1, -1):
            stack.append(input[i])
            count += 1
        stacks.append(stack)
        start = end
        print(stacks)
    stacks.append([input[0]])
    return stacks

def insert(A, B):
    # len(A) < len(B)
    """
    将 A 插入 B:
    e.g., A = ['B', 'F'], B = ['D']
    => C = ['B', 'D', 'F']
    :param A:
    :param B:
    :return: C
    """
    global count
    try:
        assert len(A) >= len(B)
    except AssertionError:
        print('A 的长度应该比 B 大.')
        raise AssertionError
    C = []
    for i in range(len(B)):
        C.append(A[i])
        C.append(B[i])
        count += 1
    if len(A) != len(B):
        print(B[-1])
        C.append(B[-1])
    return C

def insert_all(stack):
    C = stack[-1]
    for i in range(len(stack) - 2, -1, -1):
        C = insert(stack[i], C)
        print(C)

def sol():
    """
    啊，就是把原本的过程倒着来一下哇！！
    :return:
    """
    # 把列表的最后一个元素放到第一位
    global count
    count = 0
    def end_to_start(list=[]):
        global count
        if len(list) <= 1:
            count += 1
            pass
        else:
            list.insert(0, list[-1])
            list.pop()
            count += 1
        return list

    aim_list = ['D', 'F', 'B', 'E', 'C', 'A']  # 排序牌面
    result = []  # 起始牌面

    for i in range(len(aim_list), 0, -1):
        end_to_start(result)
        # 将排序牌面最后一个拍放到起始牌面第一位
        result.insert(0, aim_list[i - 1])

    print('sol: ', result, count)

if __name__ == '__main__':
    input = ['D', 'F', 'B', 'E', 'C', 'A']
    input = ['H', 'D', 'F', 'B', 'G', 'E', 'C', 'A']

    stacks = make_stack(input)
    print(stacks)
    insert_all(stacks)
    print(count)

    sol()
    create_stack(['A', 'B', 'C', 'D', 'E', 'F'])