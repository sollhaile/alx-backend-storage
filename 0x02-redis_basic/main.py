#!/usr/bin/env python3
"""
Main file
"""
from exercise import Cache

cache = Cache()
key = cache.store(b"123")
print(cache.get(key, int))  # Output: 123

key2 = cache.store("hello")
print(cache.get(key2, lambda x: x.decode("utf-8")))  # Output: hello
