# auto-text-spammer

For PyAutoGUI install:
- **pip install pyautogui**

To change text for spamming and number of text itterations:
- go to **/config/config.py**
- constant `counter` contains the number of text repetitions
- constant `spam_box` contains your text for spam

To run program:
- open console and type **python spam.py**
- **don't run the program until reading the ATTENTION! below**

***ATTENTION!***
1. After starting the program click in chat, text editor etc. because the program will try to type a text 'executing symbols' otherwise it can cause keyboard hotkeys and problems.
2. Text spamming stops ONLY if program completed the task (you can choose the number of iterations of your text) OR if you activate console and press `Ctrl + C` - it will cause      KeyboardInterrupt and program abort.
