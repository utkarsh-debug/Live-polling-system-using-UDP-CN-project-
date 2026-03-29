# Live Polling System using UDP Socket Programming

##  Overview

This project implements a **real-time live polling system** using **UDP socket programming**. Multiple clients can connect to a server and cast votes, which are aggregated and displayed instantly.
The system demonstrates core networking concepts such as:

* UDP communication
* Custom protocol design
* Reliability over unreliable transport
* Concurrent client handling

----
##  Features

* Multi-client support (concurrent clients)
* Unique client ID registration
* Real-time vote updates
* Duplicate packet detection
* Reliable communication using:

  * Sequence numbers
  * Acknowledgements (ACK)
  * Retransmission
* Latency measurement
* Session termination with final report
* Per-user vote analytics

---

##  Architecture

Client → UDP → Server → Live Dashboard

---

##  Protocol Design

### Packet Types

* Registration:
  HELLO|client_id

* Server Response:
  WELCOME / REJECT

* Voting:
  DATA|client_id|sequence_number|vote

* Acknowledgment:
  ACK|sequence_number

* End Session:
  END

---

##  Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-link>
cd live-polling-system
```

### 2. Install Requirements

```
pip install -r requirements.txt
```

### 3. Run Server

```
python server.py
```

### 4. Run Clients (multiple terminals)

```
python client.py
```

---

##  How to Use

1. Start server
2. Start multiple clients
3. Enter unique client IDs
4. Cast votes:

   * Python
   * C++
   * JavaScript
5. Type `END` from any client to terminate session

---

##  Output

Server displays:

* Live vote count
* Vote percentages
* Packet statistics
* Final report (after END)

---

##  Security Note

* This system uses UDP, so standard TLS cannot be applied.
* Secure communication over UDP is typically implemented using **DTLS (Datagram TLS)**.
* Due to complexity, this project implements basic application-layer security and proposes DTLS as future work.

---

##  Performance Metrics

* Throughput (packets/sec)
* Duplicate packet rate
* Latency per vote

---

##  Future Enhancements

* DTLS-based secure communication
* GUI dashboard
* Database storage
* Authentication system
* One vote per user restriction

---

##  Author

GROUP PROJECT
B.TECH STUDENTS PES UNIVERSITY-560085
NAME        			SRN
UTKARSH KUMAR			PES1UG24AM310
SAMYUKTHA			PES1UG24AM312
BASAWARAJ PANCHAL		PES1UG24AM350

---
