import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            all_data.append(line.strip())

if __name__ == '__main__':
    file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', "file 4.txt"]

    # Линейный подход
    start_time = time.time()
    for name in file_names:
        read_info(name)
    linear_duration = time.time() - start_time
    print(f"Время выполнения линейного подхода: {linear_duration:.2f} секунд")

    # Многопроцессный подход
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, file_names)
    multiprocessing_duration = time.time() - start_time
    print(f"Время выполнения многопроцессного подхода: {multiprocessing_duration:.2f} секунд")