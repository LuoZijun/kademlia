#!/usr/bin/env python3
#coding: utf8

import os, sys
import asyncio, logging

sys.path.insert(0, os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])


from kademlia.network import Server


logger = logging.getLogger('kademlia.examples.example')


def done(result):
    print("Key result:", result)

def setDone(result, server):
    server.get("a key").addCallback(done)

def bootstrapDone(found, server):
    server.set("a key", "a value").addCallback(setDone, server)


def main():
    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    server = Server()
    server.listen(8468)
    
    #server.bootstrap([("1.2.3.4", 8468)]).addCallback(bootstrapDone, server)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.close()


if __name__ == '__main__':
    logging.basicConfig(
        format  = '%(asctime)s %(levelname)-5s %(threadName)-10s %(name)-15s %(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S',
        level   = logging.DEBUG
    )
    
    logging.getLogger("asyncio").setLevel(logging.CRITICAL)
    
    main()