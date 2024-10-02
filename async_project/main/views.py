from django.shortcuts import render
import asyncio
from django.http import JsonResponse

async def async_counter(request):
    data = []
    for i in range(1, 6):
        await asyncio.sleep(1)  # Aguarda 1 segundo
        data.append(f"Contagem: {i}")
    return JsonResponse({'contador': data})
