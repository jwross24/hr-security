if __name__ == '__main__':
    n = int(input())
    values = input().split()
    values = list(map(int, values))

count = 0
for i in range(n):
    if i+1 in values:
        count += 1

if count == n:
    print('YES')
else:
    print('NO')
