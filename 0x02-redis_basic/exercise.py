#!/usr/bin/env python3
"""This module defines a Cache class to store and retrieve data using Redis."""

import redis
from uuid import uuid4
from typing import Union, Callable, Optional


class Cache:
    """Cache class for storing and retrieving data using Redis."""

    def __init__(self):
        """Initialize Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a randomly generated key.

        Args:
            data: The data to store (str, bytes, int, or float).

        Returns:
            The key under which the data was stored.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis using the given key. Optionally apply a transformation.

        Args:
            key: The Redis key.
            fn: Optional callable to transform the data before returning.

        Returns:
            The data, transformed if fn is provided. None if the key doesn’t exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data
