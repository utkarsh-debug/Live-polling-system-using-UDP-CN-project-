# Tech Stack

This project is implemented using **Python 3**, leveraging its standard library for low-level network programming and concurrency. The core communication is handled using the built-in `socket` library, which provides direct access to UDP sockets for sending and receiving data over the network. This allows the system to implement custom communication protocols without relying on high-level abstractions. Additionally, the `threading` module is used on the server side to enable concurrent handling of incoming client requests and periodic result broadcasting, ensuring smooth real-time performance.

The project also utilizes modules such as `time` for latency measurement and periodic scheduling, and `collections` (specifically `defaultdict`) for efficient data storage and aggregation of votes, client states, and statistics. No external dependencies or third-party frameworks are used, making the system lightweight, portable, and easy to set up. The entire application runs in a terminal-based environment, emphasizing core networking concepts, protocol design, and system-level programming.

Although standard SSL/TLS cannot be directly applied over UDP, the project incorporates a simplified **application-layer encryption mechanism** to replicate basic secure communication behavior. This is achieved using lightweight encoding/decoding (message transformation) techniques along with reliability features such as acknowledgments, retransmission, and duplicate detection. While this does not provide full cryptographic security like TLS, it conceptually demonstrates secure data handling and forms a foundation for future integration of DTLS (Datagram TLS).

---

## 🔧 Technologies Used

* **Python 3** – Core programming language
* **socket (standard library)** – UDP communication and network handling
* **threading (standard library)** – Concurrent server operations
* **time (standard library)** – Latency measurement and periodic execution
* **collections.defaultdict** – Efficient data storage and counting
* **UDP Protocol** – Connectionless, low-latency communication
* **Custom Application Protocol** – Structured packet format (DATA, ACK, HELLO, END)
* **Basic Encryption (Application Layer)** – Simulated secure communication (encoding/decoding)
* **SSL/TLS (Conceptual / Referenced)** – Security model inspiration; DTLS proposed for UDP
* **Terminal/CLI Interface** – User interaction and output display
* **Git & GitHub** – Version control and project hosting
