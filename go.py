import time
import winsound
import sys
import configparser

multiplieries = [1, 60, 3600, 86400]
global seconds
global utilizar_motivo

def load_config(arquivo):    

    config = configparser.ConfigParser()
    config.read(arquivo)

    return config.get('GERAL', 'utilizar_motivo')


def countdown(timer, motivo):

    seg = time_to_sec(timer)

    if motivo == '':
        motivo = 'Motivo não informado'

    while seg > 0:
        if seg < 4:
           winsound.Beep(2500, 100)
        print(sec_to_time(seg), end = '\r')
        seg -= 1
        time.sleep(1)
       
    print(f"Tempo encerrado: {motivo}")
    winsound.Beep(1000, 1000)


def time_to_sec(time):

    seconds = 0

    list_time = time.split(':')

    list_time = list_time[::-1]
    
    for i, val in enumerate(list_time):
        seconds = seconds + int(list_time[i]) * int(multiplieries[i])
    
    return(seconds)


def sec_to_time(seconds):

    hour = seconds // 3600
    min = (seconds - (3600 * hour)) // 60
    sec = seconds - (3600 * hour) - (60 * min)
    
    return f'{hour:02d}:{min:02d}:{sec:02d}'


def get_time():

    comando_saida = False    

    while not comando_saida:
        valid_input = True
        user_input = input('Digite o tempo (x-sair): ')

        if user_input == 'x':
            exit()  
    
        list_time = user_input.split(':')

        for i in list_time:
            if not i.isdigit():
                print(f'Valor inserido é inválido: "{user_input}". Utilize o formato "hh:mm:ss"')
                valid_input = False                    
        
        utilizar_motivo = bool(int(load_config('app.conf')))
        
        if utilizar_motivo:
            user_input_motivo = input('Digite o motivo: ')
        else:
            user_input_motivo = ''

        if valid_input:
            countdown(user_input, user_input_motivo)

get_time()