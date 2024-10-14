 #!/usr/bin/env python3
'''
This script is used to generate a random number between 1 and 100.
'''
import asyncio
import random
async def wait_random(max_delay=10):
    """Wait for a random amount of time between 0 and max_delay seconds."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay