
# a,b,c = map(int,input().split())
# i = 0
#
# while True:
#     i += 1
#     if i % a == 0 and i % b ==0 and i % c ==0:
#         print(i)
#         break

# a = int(input())
# b = list(map(int, input().split()))
# index = 0
#
# c = []
# for i in range(23):
#     c.append(0)
#
# for i in range(b.__len__()):
#     index = b[i]
#     c[index-1] += 1
#
# print(' '.join(map(str, c)))


# a = int(input())
# b = list(map(int, input().split()))
#
# b.reverse()
# print(' '.join(map(str,b)))

# a = int(input())
# b = list(map(int, input().split()))
# print(min(b))

# a = int(input())
#
# d = [[0 for j in range(19)] for i in range(19)]
#
# for i in range(a):
#     lix, liy = map(int,input().split())
#     d[lix-1][liy-1]=1
#
# for i in d:
#     for j in i:
#         print(j, end=' ')
#     print()
# li = []
#
# for i in range(19):
#     li.append(list(map(int,input().split())))
#
# n = int(input())
#
# for i in range(n):
#     x, y = map(int,input().split())
#     for k in range(19):
#         if (li[x-1][k] == 0):
#             li[x-1][k] = 1
#         elif(li[x-1][k] == 1):
#             li[x-1][k] = 0
#         if (li[k][y-1] == 0):
#             li[k][y-1] = 1
#         elif(li[k][y-1] == 1):
#             li[k][y-1] = 0
#
# for i in li:
#     for j in i:
#         print(j, end=' ')
#     print()

# x,y = map(int,input().split())
# li = [[0 for j in range(y)]for i in range(x)]
#
# n = int(input())
# for i in range(n):
#     l,d,x,y = map(int,input().split())
#     # l = length , d = 0 or 1 (가로 세로) , x,y(좌표)
#     if(d == 0):
#         for j in range(l):
#             li[x-1][y-1+j] = 1
#     else:
#         for k in range(l):
#             li[x-1+k][y-1] = 1
# for i in li:
#     for j in i:
#         print(j, end=' ')
#     print()

# li = []
# for i in range(10):
#     li.append(list(map(int,input().split())))
#
# x,y = 1,1
# while(True):
#     if(li[x][y] == 0):
#         li[x][y] = 9
#     elif(li[x][y] == 2):
#         li[x][y] = 9
#         break
#     if(li[x+1][y] == 1 and li[x][y+1] == 1):
#         break
#     if(li[x][y+1] != 1):
#         y += 1
#     elif(li[x+1][y] != 1):
#         x += 1
#
#
#
# for i in li:
#     for j in i:
#         print(j, end=' ')
#     print()

