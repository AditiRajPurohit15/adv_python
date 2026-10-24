# AsyncIO in Python

## 1. What is AsyncIO?

AsyncIO is a Python library for writing concurrent programs using coroutines and an event loop. It is particularly useful for I/O-bound tasks, such as API requests, network communication, and database operations when the libraries support asynchronous I/O.

## 2. Important concepts

| Concept | Meaning |
|---|---|
| `async def` | Defines a coroutine function |
| `await` | Suspends a coroutine while an awaitable completes |
| Coroutine | An asynchronous unit of work |
| Event loop | Schedules and runs asynchronous tasks |
| `asyncio.run()` | Runs the top-level coroutine |
| `asyncio.create_task()` | Schedules a coroutine as a task |
| `asyncio.gather()` | Awaits multiple awaitables and collects results |
| `asyncio.sleep()` | Pauses a coroutine without blocking the event loop |

## 3. When should I use AsyncIO?

- Multiple network requests
- Concurrent API calls
- WebSocket connections
- Applications that handle many I/O operations

## 4. Common mistakes

1. Calling an async function and forgetting to await or schedule its coroutine.
2. Using `time.sleep()` instead of `await asyncio.sleep()` inside asynchronous code.
3. Assuming `asyncio` automatically makes CPU-heavy calculations faster.
4. Assuming `await` always means multiple tasks run concurrently. Concurrency requires opportunities for other tasks to run.

## 5. Interview questions

- What is the difference between concurrency and parallelism?
- What is an event loop?
- What happens when we call an async function?
- What is the difference between `await` and `asyncio.create_task()`?
- Why is `time.sleep()` problematic inside an async function?
- When would you choose multiprocessing over asyncio?

## 6. My own observations

- What I understood:
- What confused me:
- What happened when I changed the code:
- What I need to revise: