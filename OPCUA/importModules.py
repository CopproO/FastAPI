import OPCUA
import asyncio 
import time 

# https://superfastpython.com/asyncio-return-value/

url = "opc.tcp://192.168.16.200:4840"
session  = OPCUA.client(url)

def run(instance):
    st = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(instance)

    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

run(session.connect())


#time.sleep(10)
#run(session.disconnect())



