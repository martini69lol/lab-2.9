#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


if __name__ == '__main__':
    print(fib(5))
