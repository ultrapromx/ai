# 3. Implement Alpha-Beta Tree search for any game search problem.

# Initial values of Alpha and Beta
MAX, MIN = 1000, -1000

def AlphaBeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = MIN
        for i in range(0, 2):

            val = AlphaBeta(depth+1, nodeIndex*2+i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = MAX
        for i in range(0, 2):
            val = AlphaBeta(depth+1, nodeIndex*2+i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


if __name__ == "__main__":
    values = [8, 7, 3, 6, 4, 2, -1, 0]
    print("The optimal value is :", AlphaBeta(0, 0, True, values, MIN, MAX))
