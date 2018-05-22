"""
八皇后问题是一个以国际象棋为背景的问题：如何能够在8×8的国际象棋棋盘上放置八个皇后，
使得任何一个皇后都无法直接吃掉其他的皇后？为了达到此目的，
任两个皇后都不能处于同一条横行、纵行或斜线上。
八皇后问题可以推广为更一般的n皇后摆放问题：
这时棋盘的大小变为n×n，而皇后个数也变成n。当且仅当n = 1或n ≥ 4时问题有解[1]。
"""

import random
#冲突检查，在定义state时，采用state来标志每个皇后的位置，其中索引用来表示横坐标，基对应的值表示纵坐标，例如： state[0]=3，表示该皇后位于第1行的第4列上
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        #如果下一个皇后的位置与当前的皇后位置相邻（包括上下，左右）或在同一对角线上，则说明有冲突，需要重新摆放
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False

#采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置。
def queens(num, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            #产生当前皇后的位置信息
            if len(state) == num-1:
                yield (pos, )
            #否则，把当前皇后的位置信息，添加到状态列表里，并传递给下一皇后。
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos, ) + result


#为了直观表现棋盘，用X表示每个皇后的位置
def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. '*(length-pos-1)
    for pos in solution:
        print(line(pos))

if __name__ == "__main__":
    prettyprint(random.choice(list(queens(8))))