
from clockdeco import clock
import functools


"""
least recently used
lru_cache
实现，使用字典存储结果
"""
@functools.lru_cache()
@clock
def fibonacci(n):
	if n < 2:
		return n
	return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
	print(fibonacci(60))