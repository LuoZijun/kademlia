#!/usr/bin/env python3
#coding: utf8

import hashlib

from functools import reduce, partial


def sha1(text):
    if type(text) == str:
        text = text.encode('utf8')
    elif type(text) == bytes:
        pass
    else:
        raise ValueError('Ooops..')

    m = hashlib.sha1()
    m.update(text)
    hex_str = m.hexdigest()

    return int(hex_str, 16)


def distance(w1, w2):
    n = sha1(w1) ^ sha1(w2)
    print(">> %d -> 计算 sha1(`%s`) ^ sha1(`%s`) " % (n, w1, w2) )
    return n


def gen(w):
    return list(map(lambda n: (w, w[0: len(w)-n*1]), list(range(len(w)))[1:] ))


def main():    
    samples = ("我们啦", "abcdefgh", "夏天的海滩和春天的阳光！")
    for x in map(gen, samples):
        print("@ Group: ", x[0][0])
        for y in x:
            distance(y[0], y[1])


if __name__ == '__main__':
    main()
