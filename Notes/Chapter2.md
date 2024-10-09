[toc]

# Chapter 2 Application Layer



## 2.1 Principles of Network Applications



### Network Application Architectures

* client-server architecture
* peer-to-peer (P2P) architecture

---

### Processes Communicating

> [!IMPORTANT]
>
> **Processes** on two different end systems communicate with each other by  **exchanging messages** across the computer network.

1. The **Interface** Between the Process and the Computer Network

A process sends messages into, and receives messages from, the network through a **software interface** called a **socket**.

![image-20241008190023050](https://gitee.com/OooAlex/study_note/raw/master/img/202410081900220.png)

2. Transport Services Available to Applications

**reliable data transfer, throughput, timing, and security**

3. Transport Services Provided by the Internet(TCP/IP networks)

* **TCP Services**

Connection-oriented Service(handshaking)

Reliable data transfer

congestion-control mechanism

> *TCP congestion control attempts to limit each TCP connection to its fair share of network bandwidth.*

* **UDP Services**

---

### Application-Layer Protocols

> [!IMPORTANT]
>
> An **application-layer protocol** defines **how an application’s processes**, running on different end systems,  **pass messages to each other**.

The Web’s application-layer protocol, **HTTP**, defines the **format and sequence of messages** exchanged between browser and Web server.



## 2.2 The Web and HTTP



