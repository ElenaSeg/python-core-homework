from ex2 import fetcher
import time

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        # put your code here
        def return_func(*args, **kwargs):
            totalTime = 0

            for n in range(num):
                startTime = time.time()
                func(*args, **kwargs)
                endTime = time.time()
                totalTime += endTime - startTime
                print(endTime - startTime)

            print(totalTime / num)
        return return_func 

    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
