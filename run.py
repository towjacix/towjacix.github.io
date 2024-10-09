import os
from notify_run import Notify

os.system("python initialize.py")
os.system("python jinja_render.py")
os.system("git add .")
os.system("git commit -m 'update index.html' ")
os.system("git push origin master")
notify = Notify(endpoint="https://notify.run/c/H7yK2GMTFKfjdi4T9gDR")
notify.register()
notify.send('Si so', 'https://towjacix.github.io')
