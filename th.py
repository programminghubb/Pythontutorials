import time


def area_sqr(length):
    for l in length:
        time.sleep(0.1)
        print('Area:', l * l)


def peri_sqr(length):
    for l in length:
        time.sleep(0.1)
        print('Perimeter:', 4 * l)


length = [ 4, 5, 6, 7 ]
t = time.time()

print(area_sqr(length))
print(peri_sqr(length))

print("Finished in : ", time.time() - t)
