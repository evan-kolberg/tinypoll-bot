import subprocess

bots = int(input('How many bots would you like?:  '))

def run(abots):
    for i in range(abots):
        subprocess.call(' python bot.py 1', shell=True)


if __name__ == '__main__':
    run(bots)