import socket
import threading

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
nickname = input('Choose a nickname: ')
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#receive data from server
def receive():
    while True:
        try:
            massage = client.recv(1024).decode('ascii')
            if massage == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(massage)
        except:
            print('An error occured!')
            client.close()
            break


def write():
    while True:
        massage = f'{nickname}: {input(">>> ")}'
        client.send(massage.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()