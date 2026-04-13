# Execution Guide – Live Polling System (UDP)

##  Overview

This guide provides step-by-step instructions to run the Live Polling System using UDP sockets. The system consists of a server and multiple clients communicating over the network.

---

##  Prerequisites

Make sure the following are installed:

* Python 3.x
* Terminal / Command Prompt / PowerShell

Check Python version:

```
python --version
```

---

##  Project Setup

1. Download or clone the repository:

```
git clone <your-repo-link>
cd live-polling-system
```

2. Ensure the following files are present:

* server.py
* client.py

---

##  Step 1: Start the Server

Open a terminal window and run:

```
python server.py
```

You should see:

```
UDP Server started...
```

 Keep this terminal open — this is your **server**

---

##  Step 2: Start Clients (IMPORTANT)

You must open **multiple terminal windows** to simulate multiple users.

###  Open a NEW terminal

Run:

```
python client.py
```

Enter a unique client ID:

```
Enter client ID: A
```

---

###  Open another terminal

Run again:

```
python client.py
```

Enter a different ID:

```
Enter client ID: B
```

---

###  Repeat for more clients

Each terminal = one client

Examples:

```
A, B, C, D...
```

---

## 🗳 Step 3: Cast Votes

Each client can vote by entering:

```
Python
C++
JavaScript
```

Example:

```
Enter vote: Python
```

---

##  How It Works

* Client sends vote to server
* Server acknowledges (ACK)
* If ACK is not received → client retransmits
* Server aggregates votes
* Results are displayed every 5 seconds

---

##  Step 4: View Live Results

Server terminal automatically displays:

* Total votes per option
* Vote percentages
* Packet statistics

---

##  Step 5: End Session

From any client terminal, type:

```
END
```

This will:

* Stop the session
* Display final report on server

---

##  Final Output Includes

* Total votes per language
* Votes per user
* Detailed breakdown (user vs language)

---

##  Important Notes

* Each client must use a **unique ID**
* If duplicate ID is entered → server will reject it
* Keep server running before starting clients
* Do NOT close server terminal during execution

---

##  Demo Tip (for Viva)

To demonstrate effectively:

1. Start server
2. Run 3–4 clients
3. Cast votes quickly
4. Show live updates
5. End session and display final report

---

##  Summary

* Server runs once
* Clients run in multiple terminals
* Communication is via UDP sockets
* System supports concurrent users

---
