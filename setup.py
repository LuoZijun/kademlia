#!/usr/bin/env python3

from setuptools import setup, find_packages

import kademlia

setup(
    name="kademlia",
    version=kademlia.__version__,
    description="Kademlia is a distributed hash table for decentralized peer-to-peer computer networks.",
    author="Brian Muller",
    author_email="bamuller@gmail.com",
    license="MIT",
    url="http://github.com/bmuller/kademlia",
    packages=find_packages(),
    install_requires=["u-msgpack-python>=1.5"]
)
