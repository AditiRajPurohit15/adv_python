from threading import Thread

def squared_numbers():
    for i in range():
        i*i

if __name__=="__main__":
    threads=[]
    num_threads=10

for i in range(num_threads):
    t=Thread(target=squared_numbers)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print('end main')