fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

nums = list(map(int, input().split()))
k = input()
# print(str(nums[0]) + k)
fout.write(str(nums[0]) + k)
