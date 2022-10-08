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
