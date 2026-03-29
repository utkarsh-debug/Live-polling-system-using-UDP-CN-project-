import socket
import threading
import time
from collections import defaultdict

SERVER_IP = "0.0.0.0"
SERVER_PORT = 5000
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print("UDP Server started...")

votes = defaultdict(int)
received_sequences = defaultdict(set)
registered_clients = set()

user_votes = defaultdict(int)
user_vote_breakdown = defaultdict(lambda: defaultdict(int))

total_packets = 0
duplicate_packets = 0
start_time = time.time()

VALID_VOTES = {"Python", "C++", "JavaScript"}

lock = threading.Lock()
session_active = True


def encrypt(msg):
    return msg[::-1]


def decrypt(msg):
    return msg[::-1]


# ==============================
# DASHBOARD
# ==============================
def print_dashboard():
    print("\n----- LIVE RESULTS -----")

    total_votes = sum(votes.values())

    for option in VALID_VOTES:
        count = votes[option]
        percent = (count / total_votes) * 100 if total_votes > 0 else 0
        print(f"{option}: {count} votes ({percent:.2f}%)")

    elapsed_time = time.time() - start_time
    throughput = total_packets / elapsed_time if elapsed_time > 0 else 0
    duplicate_rate = (duplicate_packets / total_packets) * 100 if total_packets > 0 else 0

    print("\nStatistics:")
    print(f"Total packets: {total_packets}")
    print(f"Duplicate packets: {duplicate_packets}")
    print(f"Duplicate rate: {duplicate_rate:.2f}%")
    print(f"Throughput: {throughput:.2f} packets/sec")
    print("-------------------------\n")


# ==============================
# FINAL REPORT
# ==============================
def print_final_report():
    print("\n========== FINAL REPORT ==========")

    print("\nTotal Votes Per Language:")
    for option in VALID_VOTES:
        print(f"{option}: {votes[option]}")

    print("\nVotes Per User:")
    for user in user_votes:
        print(f"{user}: {user_votes[user]} votes")

    print("\nDetailed Breakdown:")
    for user in user_vote_breakdown:
        print(f"\n{user}:")
        for option in VALID_VOTES:
            print(f"  {option}: {user_vote_breakdown[user][option]}")

    print("=================================\n")


# ==============================
# PERIODIC DASHBOARD (5 sec)
# ==============================
def periodic_dashboard():
    while session_active:
        time.sleep(5)
        with lock:
            print_dashboard()


# ==============================
# RECEIVE LOGIC
# ==============================
def receive_votes():
    global total_packets, duplicate_packets, session_active

    while session_active:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        message = decrypt(data.decode())

        try:
            parts = message.split("|")

            # END SESSION
            if parts[0] == "END":
                print("\nSession ending...")
                with lock:
                    print_final_report()
                session_active = False
                break

            # CLIENT REGISTRATION
            if parts[0] == "HELLO":
                client_id = parts[1]

                if client_id in registered_clients:
                    sock.sendto(encrypt("REJECT").encode(), addr)
                else:
                    registered_clients.add(client_id)
                    sock.sendto(encrypt("WELCOME").encode(), addr)

                continue

            total_packets += 1

            if parts[0] != "DATA":
                continue

            _, client_id, seq_no, vote = parts
            seq_no = int(seq_no)

            # SEND ACK
            sock.sendto(encrypt(f"ACK|{seq_no}").encode(), addr)

            # DUPLICATE CHECK
            if seq_no in received_sequences[client_id]:
                duplicate_packets += 1
                continue

            received_sequences[client_id].add(seq_no)

            # VALIDATION
            if vote not in VALID_VOTES:
                continue

            # UPDATE COUNTS
            votes[vote] += 1
            user_votes[client_id] += 1
            user_vote_breakdown[client_id][vote] += 1

        except:
            continue


# ==============================
# THREADS
# ==============================
threading.Thread(target=receive_votes, daemon=True).start()
threading.Thread(target=periodic_dashboard, daemon=True).start()

while session_active:
    time.sleep(1)

sock.close()
print("Server shut down.")