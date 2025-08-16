"""
Solution for Async Await Introduction
Problem ID: F088
"""

import asyncio
import time

async def async_task(task_id, delay=1):
    """
    Simple async task with delay.
    Args:
        task_id (int): task identifier
        delay (float): delay in seconds
    Returns:
        dict: task result
    """
    print(f"Task {task_id} starting...")
    await asyncio.sleep(delay)
    print(f"Task {task_id} completed!")
    
    return {
        "task_id": task_id,
        "delay": delay,
        "status": "completed"
    }

async def fetch_data(url):
    """
    Mock async data fetching function.
    Args:
        url (str): URL to fetch (mock)
    Returns:
        dict: mock response data
    """
    # Simulate network delay
    await asyncio.sleep(0.1)
    
    return {
        "url": url,
        "status": 200,
        "data": f"Mock data from {url}",
        "timestamp": time.time()
    }

async def process_urls(urls):
    """
    Process multiple URLs concurrently.
    Args:
        urls (list): list of URLs to process
    Returns:
        list: list of responses
    """
    tasks = [fetch_data(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    return responses

async def producer(queue, num_items=5):
    """
    Producer coroutine that adds items to queue.
    Args:
        queue (asyncio.Queue): queue to add items to
        num_items (int): number of items to produce
    """
    for i in range(num_items):
        item = f"item_{i}"
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.1)
    
    # Signal completion
    await queue.put(None)

async def consumer(queue):
    """
    Consumer coroutine that processes items from queue.
    Args:
        queue (asyncio.Queue): queue to consume items from
    Returns:
        list: list of processed items
    """
    processed_items = []
    
    while True:
        item = await queue.get()
        
        if item is None:
            # End signal received
            break
        
        # Process item
        processed_item = f"processed_{item}"
        processed_items.append(processed_item)
        print(f"Consumed: {processed_item}")
        
        # Mark task as done
        queue.task_done()
        await asyncio.sleep(0.05)
    
    return processed_items

async def producer_consumer_example():
    """
    Demonstrate producer-consumer pattern with asyncio.
    Returns:
        dict: results of producer-consumer example
    """
    queue = asyncio.Queue(maxsize=10)
    
    # Start producer and consumer
    producer_task = asyncio.create_task(producer(queue, 3))
    consumer_task = asyncio.create_task(consumer(queue))
    
    # Wait for producer to finish
    await producer_task
    
    # Wait for consumer to process all items
    processed_items = await consumer_task
    
    return {
        "items_processed": len(processed_items),
        "processed_items": processed_items
    }

async def async_context_manager_example():
    """
    Demonstrate async context manager usage.
    Returns:
        dict: context manager results
    """
    class AsyncContextManager:
        async def __aenter__(self):
            print("Entering async context")
            await asyncio.sleep(0.01)
            return "context_data"
        
        async def __aexit__(self, exc_type, exc_val, exc_tb):
            print("Exiting async context")
            await asyncio.sleep(0.01)
    
    async with AsyncContextManager() as data:
        await asyncio.sleep(0.01)
        result = f"Used {data} in context"
    
    return {"result": result, "context_used": True}

def run_async_examples():
    """
    Run async examples using asyncio.run()
    Returns:
        dict: results of all async examples
    """
    async def main_async():
        results = {}
        
        # Test basic async task
        task_result = await async_task(1, 0.1)
        results["basic_task"] = task_result
        
        # Test concurrent URL processing
        urls = ["http://example.com", "http://test.com", "http://demo.com"]
        url_results = await process_urls(urls)
        results["url_processing"] = len(url_results)
        
        # Test producer-consumer
        pc_result = await producer_consumer_example()
        results["producer_consumer"] = pc_result
        
        # Test async context manager
        cm_result = await async_context_manager_example()
        results["context_manager"] = cm_result
        
        return results
    
    return asyncio.run(main_async())

def main():
    """
    Función principal para 088_async_await_introduction
    """
    print("Async Await Introduction Examples:")
    
    # Run all async examples
    results = run_async_examples()
    
    print(f"\nAsync examples completed:")
    print(f"- Basic task: {results['basic_task']['status']}")
    print(f"- URLs processed: {results['url_processing']}")
    print(f"- Producer-consumer items: {results['producer_consumer']['items_processed']}")
    print(f"- Context manager used: {results['context_manager']['context_used']}")
    
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")
