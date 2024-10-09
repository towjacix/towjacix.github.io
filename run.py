import os

os.system("python initialize.py")
os.system("python jinja_render.py")
os.system(("mv report.html html-output/"))
