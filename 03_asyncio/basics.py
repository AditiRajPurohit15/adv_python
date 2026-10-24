"""
ASYNCIO IN PYTHON
-----------------
Asyncio supports concurrent I/O using coroutines.
A coroutine can pause at await, allowing the event loop
to run another ready coroutine.
"""

import asyncio
import time

async def fetch_data(task_id):
    """Simulate an asynchronous network request."""

    print(f"Task {task_id}: started")

    # Simulate waiting for I/O without blocking the event loop.
    # During this wait, other coroutines can run.
    await asyncio.sleep(2)

    print(f"Task {task_id}: completed")

    # Coroutines can return values just like regular functions.
    return f"Data from task {task_id}"

async def main():
    start_time = time.perf_counter()

    # Calling an async function creates a coroutine object.
    # create_task() schedules the coroutine to run concurrently.

    tasks=[
        asyncio.create_task(fetch_data(i))
        for i in range(1,4)
    ]

    # Wait for all scheduled tasks to finish and collect results.
    results=await asyncio.gather(*tasks)

    print("\nResults:")
    for result in results:
        print(result)

    end_time=time.perf_counter()
    print(f"Total time: {end_time-start_time:.2f}")

if __name__=="__main__":
    asyncio.run(main())