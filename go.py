import time
import winsound
import sys

multiplicadores = [1, 60, 3600, 86400]
global seconds

def countdown(t):

    seg = time_to_sec(t)

    while seg > 0:
        if seg < 6:
           winsound.Beep(2500, 100)
        print(sec_to_time(seg), end = '\r')
        seg -= 1
        time.sleep(1)
       
    print("Tempo encerrado!")
    winsound.Beep(1000, 1000)


def time_to_sec(time):

    seconds = 0

    list_time = time.split(':')

    for i in list_time:
        if not i.isdigit():
            if i != 'x':
                print(f'Valor inserido é inválido: "{time}". Utilize o formato "hh:mm:ss"')
            exit()

    list_time = list_time[::-1]
    
    for i, val in enumerate(list_time):
        seconds = seconds + int(list_time[i]) * int(multiplicadores[i])
    
    return(seconds)


def sec_to_time(seconds):

    hour = seconds // 3600
    min = (seconds - (3600 * hour)) // 60
    sec = seconds - (3600 * hour) - (60 * min)
    
    return f'{hour:02d}:{min:02d}:{sec:02d}'

#countdown(input('Digite o tempo (hh:mm:ss): '))
#countdown(sys.argv[1])
#print(sys.argv[1])

entrada = '1'

while entrada != 'x':
     entrada = input('Digite o tempo: ')
     countdown(entrada)
