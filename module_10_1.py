import time
from time import sleep
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

start_time = time.time()

# Вызовы функции напрямую
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
print(f"Время выполнения функций: {end_time - start_time} секунд")


def thread_function(word_count, file_name):
    write_words(word_count, file_name)


threads = []
start_time_threads = time.time()

for args in [(10, 'example5.txt'), (30, 'example6.txt'),
             (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = Thread(target=thread_function, args=args)
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

end_time_threads = time.time()
print(f"Время выполнения потоков: {end_time_threads - start_time_threads} секунд")