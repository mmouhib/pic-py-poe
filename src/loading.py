import time


def loading():
    bar = '██'
    progress = 7
    print('loading...')
    for i in range(progress):
        bar += '██'
        print(bar, end='')
        if i < 3:
            time.sleep(0.2)
        elif i in (3, 6):
            time.sleep(0.1)
        else:
            time.sleep(0.05)
