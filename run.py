import os
from notify_run import Notify

os.system("python initialize.py")
os.system("python jinja_render.py")
os.system("git add .")
os.system("git commit -m 'update index.html' ")
os.system("git push origin master")
notify = Notify()
notify.send("Si so", "towjacix.github.io")
