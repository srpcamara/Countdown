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

    list_time = list_time[::-1]
    
    for i, val in enumerate(list_time):
        seconds = seconds + int(list_time[i]) * int(multiplicadores[i])
    
    return(seconds)


def sec_to_time(seconds):

    hour = seconds // 3600
    min = (seconds - (3600 * hour)) // 60
    sec = seconds - (3600 * hour) - (60 * min)
    
    return f'{hour:02d}:{min:02d}:{sec:02d}'


def get_time():

    comando_saida = False    

    while not comando_saida:
        entrada_valida = True
        user_input = input('Digite o tempo (x-sair): ')

        if user_input == 'x':
            exit()  
    
        list_time = user_input.split(':')

        for i in list_time:
            if not i.isdigit():
                print(f'Valor inserido é inválido: "{user_input}". Utilize o formato "hh:mm:ss"')
                entrada_valida = False                    
        
        if entrada_valida:
            countdown(user_input)
      
get_time()