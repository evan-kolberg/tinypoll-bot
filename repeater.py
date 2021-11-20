import subprocess

cmd = 'python bot.py'
bots = int(input('How many bots would you like?:  '))

def run(bots):
    for i in range(bots):
        subprocess.call(' python bot.py 1', shell=True)


if __name__ == '__main__':
    run(bots)