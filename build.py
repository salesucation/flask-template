from app import app, pages
import os
import shutil

client = app.test_client();

def load(path):
    res = client.get(path)
    if path.endswith("index"):
        path = path.replace("/index", "")
    try:
        os.makedirs(f"{os.getcwd()}/build/{path}")
    except:
        pass
    f = open(f"{os.getcwd()}/build/{path}/index.html", "wb")
    f.write(res.data)  
    f.close()

if os.path.exists(f"{os.getcwd()}/build"):
    shutil.rmtree(f"{os.getcwd()}/build")
shutil.copytree(f"{os.getcwd()}/static", f"{os.getcwd()}/build/static")
for page in pages:
    load(page.path)
