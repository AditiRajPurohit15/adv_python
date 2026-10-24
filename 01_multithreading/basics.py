"""
MULTITHREADING IN PYTHON
------------------------
Threads share the same process memory.
Useful for I/O-bound tasks, where work often waits
for a network response, file, or other external resource.
"""

import threading
import time

def download_file(file_name):
    """Simulate downloading a file (an I/O-bound task)."""
    print(f"Starting download: {file_name}")

    # Simulate waiting for a network response.
    # time.sleep() pauses this thread, allowing another
    # thread to make progress.

    time.sleep(2)
    print(f"Finished download: {file_name}")

if __name__=="__main__":
    start_time=time.perf_counter()
    # Create thread objects.
    # target is the function to execute.
    # args passes arguments to that function as a tuple.
    threads=[]

for i in range(5):
    thread=threading.Thread(
        target=download_file,
        args=(f"file_{i+1}.pdf",)
    )
    threads.append(thread)

# Start all threads before waiting for any one of them.
# This allows the downloads to overlap.

for thread in threads:
    thread.start()

# Wait for every thread to finish before proceeding.
# Without join(), the main thread could continue too early.
for thread in threads:
    thread.join()

end_time=time.perf_counter()

print(f"All downloads completed in {end_time-start_time:.2f}s")