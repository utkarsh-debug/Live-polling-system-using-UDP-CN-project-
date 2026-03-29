# Design Document

## System Architecture

The system follows a **client-server model**:

* Clients send votes using UDP
* Server aggregates and processes votes
* Server provides real-time updates

---

## Design Decisions

### Why UDP?

* Low latency
* No connection overhead
* Suitable for real-time systems

### Reliability over UDP

Implemented using:

* Sequence numbers
* ACK mechanism
* Retransmission logic

### Duplicate Handling

Each client maintains a sequence number.
Server tracks received sequence numbers per client.

---

## Concurrency

* Server uses multithreading
* Handles multiple clients simultaneously

---

## Protocol

Custom protocol designed using structured messages:
TYPE|DATA

---

## Limitations

* No built-in encryption (UDP limitation)
* No authentication

##  Security Considerations: UDP, TLS, and DTLS

In traditional networked applications, secure communication is achieved using SSL/TLS, which provides encryption, authentication, and data integrity. However, TLS is designed to operate over reliable transport protocols such as TCP, which guarantee ordered delivery, retransmission of lost packets, and absence of duplication.

In contrast, this project is built using UDP, which is a connectionless and unreliable protocol. UDP does not guarantee packet delivery, ordering, or uniqueness. Because of these characteristics, TLS cannot be directly applied over UDP, as it relies on the underlying transport layer for reliability.

To address this limitation, a specialized protocol called DTLS (Datagram Transport Layer Security) is used in real-world systems. DTLS extends TLS to work over UDP by incorporating additional mechanisms such as:

* Sequence numbering for packets
* Retransmission of lost handshake messages
* Handling of out-of-order delivery
* Duplicate packet detection
* Anti-replay protection

These features effectively recreate reliability on top of UDP while still providing encryption and security. However, implementing DTLS is significantly more complex than standard TLS due to the need to manage both security and reliability simultaneously.

In the context of this project, implementing DTLS was not feasible due to:

* High implementation complexity
* Lack of direct support in Python’s standard libraries
* The requirement to manually handle low-level cryptographic and networking details

Instead, this project focuses on implementing application-layer reliability using techniques such as sequence numbers, acknowledgments (ACKs), and retransmission. These mechanisms simulate some of the reliability features required for secure communication.

DTLS is proposed as a future enhancement to enable full-fledged secure communication over UDP.


