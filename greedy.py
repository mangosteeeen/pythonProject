# greedy 백준 문제 모음
# 2839

# num = int(input())
#
# count = 0
#
# while num >= 0:
#     if num % 5 == 0:
#         count += num//5
#         print(count)
#         break
#     num -= 3
#     count += 1
# else:
#     print(-1)

# greedy 백준 문제 모음
# 11399
# n = int(input())
#
# li = list(map(int,input().split()))
# li.sort()
# result = 0
# sum1 = 0
#
# for i in range(len(li)):
#     for j in range(i+1):
#         sum1 += li[j]
#     result += sum1
#     sum1 = 0
#
# print(result)

#11047
# n,money = map(int,input().split())
# li = []
# count = 0
# for i in range(n):
#     li.append(int(input()))
#
# li.sort(reverse=True)
#
# for i in  range(len(li)):
#     if (money // li[i] >= 1):
#         count += money // li[i]
#         money = money % li[i]
#
#
# print(count)

# n = int(input())
# li = []
# time = 0
#
# for i in range(n):
#     li.append(list(map(int,input().split())))
#
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         time = li[i][j]
#
# print(li)

# # 1541 읽어버린 괄호 최솟값 만들기
# s = ''
# start_flag = False
# count = 0
#
# input_s = list(input())
#
# while(True):
#     input_s[count].lstrip("0")
#     if(input_s[count] == '-' and not start_flag ):
#         input_s.insert(count+1,'(')
#         start_flag = True
#     elif(input_s[count] == '-' and start_flag):
#         input_s.insert(count+1,')')
#         start_flag = False
#     if (count == len(input_s)-1):
#         if(start_flag):
#             input_s.insert(count + 1, ')')
#             break
#         else:
#             break
#     count += 1
#
# result = ''.join(str(s) for s in input_s)
# s = eval(result)
# print(s)

# first_s = input().split('-')
# sum_li = []
#
#
# for i in first_s:
#     result = 0
#     for j in i.split('+'):
#         result += int(j)
#     sum_li.append(result)
# n = sum_li[0]
# for i in range(1,len(sum_li)):
#     n -= sum_li[i]
#
# print(n)

# inputindex = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# result = 0
#
# a.sort()
# b.sort(reverse=True)
#
# for i in range(len(a)):
#     result += a[i] * b[i]
#
#
# print(result)

# exchange = 1000 - int(input())
# money_in = [500,100,50,10,5,1]
# count = 0
#
# for i in range(len(money_in)):
#     if(exchange >= money_in[i]):
#         count += exchange//money_in[i]
#         exchange -= exchange//money_in[i] * money_in[i]
# print(count


# n = int(input())
# li = []
# maxli = []
# for i in range(n):
#     li.append(int(input()))
# li.sort(reverse=True)
#
# for i in range(n):
#     maxli.append((i+1)*li[i])
#
# print(max(maxli))































