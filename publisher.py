import zmq
import time
from constPS import *

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(f"tcp://{HOST}:{PORT}")

print("=== CHAT PUBLISHER ===")
print("Envie mensagens no formato:")
print("[topico] mensagem")
print("Ex: grupo1 Olá pessoal!")
print("Tópicos sugeridos: grupo1, grupo2, avisos")

while True:
    msg = input("> ")
    if " " not in msg:
        print("⚠ Formato inválido! Use: [topico] mensagem")
        continue

    topic, text = msg.split(" ", 1)
    timestamp = time.strftime("%H:%M:%S")
    socket.send_string(f"{topic} [{timestamp}] {text}")
