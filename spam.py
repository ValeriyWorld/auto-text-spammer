import sys
import time as t

import pyautogui as pag

from config.config import counter, spam_box


# print string with delay after it
def ready_steady_go(str, delay=1):
    print('{0: >15}'.format(str))
    sys.stdout.flush()
    t.sleep(delay)

# separate your text word by word
list_spam_box = spam_box.split()

print('Text spam begins in 5 seconds. Choose your target for spamming ' + \
      'by clicking into the target\'s chat box.')
sys.stdout.flush()
t.sleep(1)
ready_steady_go('..3..')
ready_steady_go('..2..')
ready_steady_go('..1..')
ready_steady_go('Spam!')

while counter > 0:
    for spam in list_spam_box:
        pag.write(spam, interval = 0.01)
        pag.press('enter')
    counter -= 1
