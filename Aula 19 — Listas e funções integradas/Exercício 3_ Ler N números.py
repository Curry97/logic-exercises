n = int(input("Quantos números? "))
nums = []
for i in range(n):
    nums.append(float(input("Número: ")))
print("Soma:", sum(nums))
print(f"Média: {sum(nums)/len(nums):.2f}")