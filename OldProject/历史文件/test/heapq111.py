#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import heapq


portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
a = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# heapq.nsmallest(2, [1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
def heapsort(ilst):
    h = []
    for i in ilst:
        heapq.heappush(h, i)
        return [heapq.heappop(h) for x in range(len(h))]
# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
cheap = heapq.nsmallest(2, portfolio, key=lambda x:x['price'])
print(cheap)