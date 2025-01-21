import time
from rich.progress import track
names = [
    "Mike",
    "Jay",
    "Taylor Swift"
]
for name in track(names, description="Metal;"):
    print(name)
    time.sleep(1)
