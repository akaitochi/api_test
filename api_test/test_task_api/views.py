import aiohttp
import asyncio
import json
import random
import requests
import time

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def someitems(url):
    delay = random.randint(1, 100) / 1000
    time.sleep(delay)

    if random.random() < 0.15:
        raise Exception('Internal Server Error')
    else:
        return url


def send_request(url):
    try:
        response = requests.get(url)
        return response.elapsed.total_seconds() * 1000
    except requests.exceptions.ConnectionError:
        return -1


async def send_request_async(session, url):
    try:
        async with session.get(url) as response:
            start_time = time.time()
            await response.read()  # чтение всего ответа
            elapsed_time = time.time() - start_time
            return elapsed_time * 1000
    except aiohttp.ClientConnectionError:
        return -1


def sequential_request(requests_count, url):
    fails = 0
    responses = []
    total_time = []

    for _ in range(requests_count):
        start_time = time.time()
        result = send_request(url)
        if result != -1:
            responses.append(result)
        else:
            fails += 1
        elapsed_time = (time.time() - start_time) * 1000
        total_time.append(elapsed_time)

    return fails, total_time


async def parallel_request(requests_count, url):
    results = []
    total_time = []
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        tasks = []
        for _ in range(requests_count):
            task = asyncio.ensure_future(send_request_async(session, url))
            tasks.append(task)
            elapsed_time = (time.time() - start_time) * 1000
            total_time.append(elapsed_time)
        results = await asyncio.gather(*tasks)

        fail_result = [r for r in results if r > -1]
        fails = requests_count - len(fail_result)

        return fails, total_time


@csrf_exempt
def ping(request):
    request_data = json.loads(request.body.decode('utf-8'))
    requests_count = request_data.get('requests', 0)
    mode = request_data.get('mode', '')
    url = someitems('http://127.0.0.1:8000/api/v1/someitems')

    if mode == 'parallel':
        async def parallel():
            fails, total_time = await parallel_request(requests_count, url)
            response = {
                'requests': requests_count,
                'fails': fails,
                'min': round(min(total_time), 5),
                'avg': round(sum(total_time) / len(total_time), 5),
                'max': round(max(total_time), 5),
            }

            return JsonResponse(response)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(parallel())
        loop.close()
        return result

    elif mode == 'sequence':
        fails, total_time = sequential_request(requests_count, url)
        response = {
            'requests': requests_count,
            'fails': fails,
            'min': round(min(total_time), 3),
            'avg': round(sum(total_time) / len(total_time), 3),
            'max': round(max(total_time), 3),
        }

        return JsonResponse(response)
