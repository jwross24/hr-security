if __name__ == '__main__':
    n = int(input())
    values = input().split()
    values = list(map(int, values))

for i in range(n):
    y = values.index(i+1)
    print(y+1)
