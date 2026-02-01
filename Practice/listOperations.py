if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        operation, position, number = map(str,input().split())

    print(operation,position,number)
