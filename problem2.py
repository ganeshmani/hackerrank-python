
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     first = second = 0
#     for i in arr:   
#         if i > first:
#             second = first
#             first = i
#         elif i > second and i != first:
#             second = i

#     print(second)


arr = [-2,-1,0,0,0]
first = second = -2147483648
for i in arr:   
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i

print(second)

       