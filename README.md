## Comparison of Python Multi Trading, Multi Processing,anc Concurrency

This mocks download 4 url pages and write them into files.
- http://python.org
- https://docs.python.org/3/library/asyncio.html
- https://docs.aiohttp.org/en/stable/
- https://github.com/mosquito/aiofile

### Test Results

| Method                                                             | Time Spent  |
|--------------------------------------------------------------------|-------------|
| [Multi Threading](test_multithreading.py)                          | 3.06s       |
| [Multi Processing Thread Pool](test_multiprocessing_ThreadPool.py) | 1.78s       |
| [Multi Processing Pool](test_multiprocessing_Pool.py)              | 2.02s       |
| [Asyncio](test_asyncio.py)                                         | 1.70s       |


### Multi Processing Pool Methods Differences

|                   | Multi-args   | Concurrence    | Blocking     | Ordered-results  |
| ----------------- | ------------ | -------------- | ------------ |------------------|
| Pool.map          | no           | yes            | yes          | yes              |
| Pool.map_async    | no           | yes            | no           | yes              |
| Pool.apply        | yes          | no             | yes          | no               |
| Pool.apply_async  | yes          | yes            | no           | no               |
| Pool.starmap      | yes          | yes            | yes          | yes              |
| Pool.starmap_async| yes          | yes            | no           | no               |
