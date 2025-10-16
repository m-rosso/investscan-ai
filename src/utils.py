import time
from functools import wraps

def time_it(func):
    """
    Decorator que mede o tempo de execução.
    Se a função decorada receber 'verbose=True' como argumento,
    imprime o tempo de execução.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time

        # captura verbose se existir nos kwargs, default False
        verbose = kwargs.get("verbose", False)
        if verbose:
            print(f"Tempo de execução: {elapsed_time:.2f} s")
        return result
    return wrapper
