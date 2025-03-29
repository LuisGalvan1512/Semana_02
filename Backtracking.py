def permutations(nums, length, path, used, count):
    if len(path) == length:
        print(path)
        count[0] += 1  
        return
    
    for i in range(len(nums)):
        if not used[i]:  
            used[i] = True  
            path.append(nums[i]) 
            permutations(nums, length, path, used, count)  
            path.pop()  
            used[i] = False  

n = int(input("Enter the number of elements: "))
nums = []
for _ in range(n):
    num = int(input("Enter a number: "))
    nums.append(num)
  

length = int(input("Enter the number of elements per permutation: "))
   

count = [0]  
used = [False] * len(nums)  

permutations(nums, length, [], used, count)

print(f"Total permutations: {count[0]}")