# bobux-gen-jokes

Bobux Gen Jokes

Written In Python Language

# How It Works?

importing some modules and forces installing it -> print some text -> verification required -> redirect to a website -> exit

# Codes

```python
import webbrowser
import subprocess
import sys

def install(webbrowser):
    subprocess.check_call([sys.executable, "-m", "pip", "install", webbrowser])
    
print('Loading....')
print('Connecting To API Services..')
print('Please Insert Ur Roblox Username...')
uname = input()
print('Welcome', uname)
print('Please Insert Ur Wanted Bobux...')
bx = input()
print('Sending',bx,' to ',uname)
print('Human Verification Needed!')
print('Redirect U To Verification Site...')
webbrowser.open('https://www.youtube.com/watch?v=a3Z7zEc7AXQ')
exit
```
Freely To Fork / Pull Request :)

Created On Saturday, 08 October 2022 at 03.00 PM
