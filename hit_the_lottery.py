n=input()
result = 0
n = int(n)
result = (n // 100)
n %= 100
result = result + (n//50)
n %= 50
result = result +  (n // 20)
n %= 20
result = result + (n//10)
n %= 10
result = result + (n // 5)
n %= 5
result = result + (n//1)
print(result)