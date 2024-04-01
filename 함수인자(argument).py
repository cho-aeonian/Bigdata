def login(msg, times=3, warn='wrong ID'):
    while True:
        id = input(msg)
        if id in ('user', 'User', 'USER'):
            return True
        times = times - 1
        if times < 0:
            print('time out')
            return False
        print(warn)