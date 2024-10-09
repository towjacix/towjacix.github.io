import os

os.system("python initialize.py")
os.system("python jinja_render.py")
os.system("git add .")
os.system("git commit -m 'update index.html' ")
os.system("git push origin master")
# os.system("notify-run configure 'https://notify.run/c/H7yK2GMTFKfjdi4T9qDR'")
os.system("curl https://notify.run/H7yK2GMTFKfjdi4T9qDR -d 'message goes here' -a https://towjacix.github.io")
