#!/usr/bin/env python3
'''
This script is used to generate a random number between 1 and 10.
'''
import asyncio
import random
from typing import AsyncGenerator
async def async_generator() -> AsyncGenerator[float, None, None]:
    '''This function generates a random number between 1 and 10.'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10