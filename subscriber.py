import zmq
from constPS import *

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://{HOST}:{PORT}")

print("=== CHAT SUBSCRIBER ===")
print("Digite o(s) grupo(s) que deseja assinar separados por vírgula")
print("Ex: grupo1,avisos")

topics = input("Assinar: ").split(",")

for t in topics:
    socket.setsockopt_string(zmq.SUBSCRIBE, t.strip())
    print(f"✅ Assinado no tópico: {t.strip()}")

print("\nAguardando mensagens...\n")

while True:
    msg = socket.recv_string()
    print(f"📩 {msg}")
