import itertools
import time

for char in itertools.cycle(r'\|/-'):
    # for i in range(4):
    # print(f'\r{char}正在加载...{i + 1}/4',end='')
    print(f'\r{char}正在加载...', end='')
    time.sleep(0.25)
    # break
