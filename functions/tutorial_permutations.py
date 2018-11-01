if __name__ == '__main__':
    n = int(input())
    values = input().split()
    values = list(map(int, values))

result = [values[i-1] for i in values]
[print(item) for item in result]
