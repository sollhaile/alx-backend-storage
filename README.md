# 0x02. Redis Basic

This project is part of the ALX Backend Specialization. It introduces basic usage of **Redis** in Python, including storing and retrieving data, using UUIDs as keys, and optional data transformations.

## 🧠 Learning Objectives

- How to use Redis with Python
- How to store simple data in Redis
- How to store data with random keys
- How to retrieve data with optional formatting
- How to use type annotations
- How to apply Python coding best practices (PEP8)

## 📦 Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- `pip3` and `redis` Python package
- Redis server
- Code follows `pycodestyle` (PEP8) version 2.5

## 📁 Files

| Filename      | Description |
|---------------|-------------|
| `exercise.py` | Contains the `Cache` class for basic Redis operations (store, get, get_str, get_int). |
| `README.md`   | Project description and setup instructions. |

## 🔧 Setup Instructions

1. **Install Redis**
   ```bash
   sudo apt-get update
   sudo apt-get install redis-server -y
   sudo service redis-server start
# alx-backend-storage
