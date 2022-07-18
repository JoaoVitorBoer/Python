import logging
import random
from logging import FileHandler, Filter

class Filter(Filter):
    def filter(self, record):
        if 'Random' in record.msg:
            return False
        return True 

file_handler = FileHandler("./Logs/logs.log")
file_handler.setLevel(logging.DEBUG)
file_handler.addFilter(Filter())

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s :: %(levelname)s :: %(filename)s :: %(lineno)d :: %(message)s",
    handlers = [file_handler]
)

'''
    logging.basicConfig(
        level=logging.DEBUG,
        filename="./Logs/logs.log",
        format="%(asctime)s :: %(levelname)s :: %(filename)s :: %(lineno)d :: %(message)s",
        
)

'''

input_ini = input('Digite um numero teto: ')

if input_ini.isdigit():
    input_ini = int(input_ini)

else: 
    print("Erro: valor não numérico")
    logging.critical("Erro Critico, valor não numérico")
    quit()

random = random.randint(0, input_ini)
logging.info("Random Numero Gerado")
attempts = 0

while True:
    user = input("Advinhe o Numero: ")
    if user.isdigit():
        user = int(user)
    else: 
        print("Erro: valor não numérico...")
        logging.error("Usuario informou valor não numérico")
        continue

    attempts += 1
    if user == random:
        print("Acertou!")
        logging.info(f"Usuario advinhou o numero após {attempts} tentativas")
        break
    else:
        print("Tente Novamente")