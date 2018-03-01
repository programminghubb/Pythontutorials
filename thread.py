import time
import threading


def area_sqr(length):
    for l in length:
        time.sleep(0.1)
        print('Area:', l * l)


def peri_sqr(length):
    for l in length:
        time.sleep(0.1)
        print('Perimeter:', 4 * l)


length = [ 4, 5, 6 ]

t = time.time()

thread1 = threading.Thread(target=area_sqr, args=(length,))
thread2 = threading.Thread(target=peri_sqr, args=(length,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Finished in : ", time.time() - t)
