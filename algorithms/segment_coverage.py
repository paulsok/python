import sys


input = sys.stdin
n = int(input.readline())

S = []

for i in range(1, n + 1):
  x, y = map(int, input.readline().split())
  S.append([x, y])

S.sort(key=lambda x: x[1])

list_dots = set()

while S:
    list_dots.add(S[0][1])
    S = list(filter(lambda x: not(x[0] <= S[0][1] <= x[1]), S))

print(len(list_dots))
print(*list_dots)
