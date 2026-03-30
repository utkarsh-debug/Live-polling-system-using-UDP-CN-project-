import socket
import time

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000
TIMEOUT = 2

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(TIMEOUT)

VALID_VOTES = {"Python", "C++", "JavaScript"}

def encrypt(msg):
    return msg[::-1]

def decrypt(msg):
    return msg[::-1]

# ==============================
# REGISTER CLIENT
# ==============================
while True:
    client_id = input("Enter client ID: ")

    sock.sendto(encrypt(f"HELLO|{client_id}").encode(), (SERVER_IP, SERVER_PORT))

    try:
        data, _ = sock.recvfrom(1024)
        response = decrypt(data.decode())

        if response == "WELCOME":
            print("Connected to server!")
            break
        else:
            print("Client ID already exists. Try another.")

    except socket.timeout:
        print("No response from server. Retrying...")

sequence_number = 1

# ==============================
# VOTING LOOP
# ==============================
while True:
    vote = input("Enter vote (Python/C++/JavaScript) or END to stop: ")

    if vote == "END":
        sock.sendto(encrypt(f"END|{client_id}").encode(), (SERVER_IP, SERVER_PORT))
        print("You ended your session.")
        break

    if vote not in VALID_VOTES:
        print("Invalid vote!")
        continue

    packet = f"DATA|{client_id}|{sequence_number}|{vote}"
    encrypted_packet = encrypt(packet)

    send_time = time.time()

    while True:
        try:
            sock.sendto(encrypted_packet.encode(), (SERVER_IP, SERVER_PORT))

            data, _ = sock.recvfrom(1024)
            ack = decrypt(data.decode())

            if ack == f"ACK|{sequence_number}":
                latency = (time.time() - send_time) * 1000
                print(f"Vote acknowledged! Latency: {latency:.2f} ms")
                break

        except socket.timeout:
            print("Timeout! Resending...")

    sequence_number += 1

sock.close()
