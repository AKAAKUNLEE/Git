import time
for i in range(10):
    part_1 = "-" * i
    part_2 = " " * (9 - i)
    print(
        f'\r正在加载... [{part_1}{part_2}] {i+1}/10',
        end=''
    )
    time.sleep(0.4)
