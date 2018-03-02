import time
import multiprocessing

def area_sqr(length):
    for l in length:
        time.sleep(5)
        print('Area:', l * l)


def peri_sqr(length):
    for l in length:
        time.sleep(5)
        print('Perimeter:', 4 * l)

if __name__ == "__main__":
    length = [ 4, 5, 6 ]
    t = time.time()
    process1 = multiprocessing.Process(target=area_sqr, args=(length,))
    process2 = multiprocessing.Process(target=peri_sqr, args=(length,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

print("Finished in : ", time.time() - t)
