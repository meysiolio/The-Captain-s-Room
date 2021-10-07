k = int(input())

roomNumbers = list(map(int, input().split()))

rooms = set(roomNumbers)

print((sum(rooms)*k - sum(roomNumbers))//(k-1))