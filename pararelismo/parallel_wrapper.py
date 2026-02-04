from concurrent.futures import ThreadPoolExecutor, as_completed
import asyncio

def parallel_run(func, items, max_workers=4):
    """
    func = função que será executada em paralelo
    items = lista de argumentos (cada item gera uma chamada da função)
    max_workers = quantidade máxima de tarefas simultâneas
    """
    
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(func, item) for item in items]

        for future in as_completed(futures):
            results.append(future.result())

    return results

import asyncio

async def parallel_run_async(func, items, max_concurrent=4):
    """
    func = função assíncrona que será executada em paralelo
    items = lista de argumentos (cada item gera uma chamada da função)
    max_workers = quantidade máxima de tarefas simultâneas
    """
    
    semaphore = asyncio.Semaphore(max_concurrent)

    async def sem_task(item):
        async with semaphore:
            return await func(item)

    tasks = [asyncio.create_task(sem_task(item)) for item in items]

    results = []
    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results
