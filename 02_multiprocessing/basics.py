"""
MULTIPROCESSING IN PYTHON
-------------------------
Each process has its own Python interpreter and memory space.
Useful for CPU-bound work, such as calculations and
processing large amounts of data.
"""

from multiprocessing import Process, cpu_count
import time

def calculate_square(number):
    """Perform a CPU bound calcilation"""
    result=number*number
    print(f"Square of {number} = {result}")


if __name__=="__main__":
    # Important: the main guard prevents child processes from
    # repeatedly executing the process-creation code.
    start_time=time.perf_counter()

    numbers=[10,20,30,40,50]
    processes=[]

    print(f"Available logical CPUs: {cpu_count()}")

    # Create one process for each calculation.
    for number in numbers:
        process=Process(
            target=calculate_square,
            args=(number,)
        )

    #start each process
    for process in processes:
        process.start()

    #wait until all child processes finish
    for process in processes:
        process.join()

    end_time=time.perf_counter()

    print(f"All calculations completed in {end_time - start_time:.4f}s")
