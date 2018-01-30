num = 0
while True:
    print(num)
    num += 1
    if num >= 4:
        break

for x in range(5):
    if x % 2 == 0:
        continue
    print(x)
