#!/usr/bin/env python3
"""This module defines a Cache class that stores and retrieves data using Redis."""

import redis
from uuid import uuid4
from typing import Union, Callable, Optional


class Cache:
    """Cache class to interact with Redis and handle data storage and retrieval."""

    def __init__(self):
        """Initialize Redis connection and flush database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis using a random key.

        Args:
            data: The data to be stored.

        Returns:
            The key under which the data is stored.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis by key, optionally applying a conversion function.

        Args:
            key: The key to look up in Redis.
            fn: Optional callable to convert the data.

        Returns:
            The retrieved data, optionally converted, or None if not found.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve data as a UTF-8 string."""
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve data as an integer."""
        return self.get(key, lambda d: int(d))
