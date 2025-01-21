import time
from tqdm import tqdm as tq

for i in tq(range(100), desc="Training", unit="bit"):        # desc ="Training" 描述信息;unit="bit" 单位
    time.sleep(0.1)

