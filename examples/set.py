#!/usr/bin/env python3
#coding: utf8

import os, sys
import logging, asyncio

sys.path.insert(0, os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])


from kademlia.network import Server


logger = logging.getLogger('kademlia.examples.set')


def main():
    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    server = Server()
    server.listen(8469)
    loop.run_until_complete(server.bootstrap([("127.0.0.1", 8468)]))
    loop.run_until_complete(server.set(sys.argv[1], sys.argv[2]))
    server.stop()
    loop.close()


if __name__ == '__main__':
    logging.basicConfig(
        format  = '%(asctime)s %(levelname)-5s %(threadName)-10s %(name)-15s %(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S',
        level   = logging.DEBUG
    )
    if len(sys.argv) != 3:
        logger.error('Usage: python set.py <key> <value>')
        sys.exit(1)

    main()