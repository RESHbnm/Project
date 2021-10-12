x, y, z = len(input()), len(input()), len(input())
x1 = min(x, y, z)
x2 = max(x, y, z)
x3 = (x + y + z) / 3
if x2 - x3 == x3 - x1:
    print("YES")
else:
    print("NO")
