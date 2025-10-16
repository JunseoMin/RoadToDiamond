import sys

input = sys.stdin.readline

inStr = input().strip()
boom  = input().strip()

stack = []

for c in inStr:
    stack.append(c)
    if len(stack) >= len(boom):
        if "".join(stack[-len(boom):]) == boom:
            for _ in range(len(boom)):
                stack.pop()
if not stack:
    print("FRULA")
else:
    print("".join(stack))