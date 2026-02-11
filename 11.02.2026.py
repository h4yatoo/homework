import asyncio
async def calculate(x, delay):
    await asyncio.sleep(delay)
    print(f"Квадрат {x} =",x**2)
async def main():
    task1 = asyncio.create_task(calculate(2, 1))
    task2 = asyncio.create_task(calculate(3, 2))
    task3 = asyncio.create_task(calculate(4, 1))
    await task1
    await task2
    await task3
asyncio.run(main())
