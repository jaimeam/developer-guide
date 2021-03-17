# Python Guideline <!-- omit in toc -->

- [Time](#time)

## Time

Measure how much time a code section takes to run:
```python
import time

start = time.time()

'''
code that runs and takes time
'''

print('Duration: {} seconds'.format(time.time() - start))
```