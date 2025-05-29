import sys

def edit_distance(word1, word2):
    x = len(word1)
    y = len(word2)

    D = [[0 for _ in range(y + 1)] for _ in range(x + 1)]

    for i in range(x + 1):
        D[i][0] = i
    for j in range(y + 1):
        D[0][j] = j

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1

            D[i][j] = min(
                D[i - 1][j] + 1,
                D[i][j - 1] + 1,
                D[i - 1][j - 1] + cost
            )

    return D[x][y]

#----------------------------------------------------------------------------------

if len(sys.argv) != 3:
    print("Missing Inputs/Too Many Inputs")
    sys.exit(1)

word1 = sys.argv[1]
word2 = sys.argv[2]

print(edit_distance(word1, word2))
