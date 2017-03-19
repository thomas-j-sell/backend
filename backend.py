import dbPopulator
import feedGenerator
import feedServer

import time
import threading
import sys

def popAndGen():
    print('Populating DB')
    dbPopulator.populate()
    print('Building Feed')
    feed = feedGenerator.generate()
    target = open('rss.xml', 'w')
    target.truncate() # overwrite file
    target.write(feed)

print('Starting rss generator and server')
print('Press ctl + c to exit')
popAndGen()

# kick off a server in a seperate thread
serverThread = threading.Thread(target=feedServer.startServer)
serverThread.setDaemon(True) # allows program to exit with thread running
serverThread.start()

# update the database and feed once an hour
while True:
    try:
        print('Sleeping...')
        # time.sleep(3600)
        time.sleep(60)
        popAndGen()

    except KeyboardInterrupt:
        # serverThread.join()
        print('')
        sys.exit()
