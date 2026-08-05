import time
import random

def retry(max_retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):

            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)

                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")

                    if attempt == max_retries:
                        raise

                    time.sleep(delay)

        return wrapper
    return decorator


@retry(max_retries=3, delay=1)
def fetch_data():

    if random.randint(1, 3) != 3:
        raise Exception("Network Error")

    return "API Response Received"


print(fetch_data())