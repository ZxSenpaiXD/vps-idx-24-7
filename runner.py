import os
import time

REPO = "https://github.com/ZxSenpaiXD/vps-idx-24-7"
FOLDER = "app"

while True:
    try:
        # Clone if not exists
        if not os.path.exists(FOLDER):
            os.system(f"git clone {REPO} {FOLDER}")
        else:
            # Pull latest updates
            os.system(f"cd {FOLDER} && git pull")

        print("Starting app...")
        os.system(f"cd {FOLDER} && python3 app.py")

    except Exception as e:
        print("Error:", e)

    print("App crashed. Restarting in 5 seconds...")
    time.sleep(5)
