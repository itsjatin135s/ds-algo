import time


def runtime_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record end time
        print(start_time, end_time)
        runtime = end_time - start_time  # Calculate the runtime
        print(f"Runtime of {func.__name__}: {runtime:.4f} seconds")
        return result
    return wrapper


# Example usage
@runtime_decorator
def example_function():
    time.sleep(2)  # Simulate a time-consuming operation


example_function()
