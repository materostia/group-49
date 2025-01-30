# 1. გამოიყენეთ filter ფუნქცია რომ ამოწეროთ მხოლოდ ლუწი რიცხვები list'იდან: [1, 2, 3, 4, 5, 6, 7, 8].
list1 = {1, 2, 3, 4, 5, 6, 7, 8}
nums = list(filter(lambda x: x % 2 == 0, list1))
print(nums)