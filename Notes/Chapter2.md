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

#### The **Interface** Between the Process and the Computer Network

A process sends messages into, and receives messages from, the network through a **software interface** called a **socket**.

![image-20241008190023050](https://gitee.com/OooAlex/study_note/raw/master/img/202410081900220.png)

#### Transport Services Available to Applications

reliable data transfer, throughput, timing, and security

#### Transport Services Provided by the Internet(TCP/IP networks)

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



### HTTP Message Format

#### HTTP Request Message

```http
GET /somedir/page.html HTTP/1.1
Host: www.someschool.edu
Connection: close
User-agent: Mozilla/5.0
Accept-language: fr
```

The first line of an HTTP request message is called the **request line**; the  subsequent lines are called the **header lines**.

**General format:**

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202410101654780.png" alt="image-20241010165440670" style="zoom: 67%;" />

If the value of the method field is POST, then the **entity body** contains what the user entered into the form fields.(e.g. when a  user provides search words to a search engine)

#### HTTP Response Message

```http
HTTP/1.1 200 OK
Connection: close
Date: Tue, 18 Aug 2015 15:44:04 GMT
Server: Apache/2.2.3 (CentOS)
Last-Modified: Tue, 18 Aug 2015 15:11:03 GMT
Content-Length: 6821
Content-Type: text/html
(data data data data data ...)
```

**General Format:**

![image-20241010171038904](https://gitee.com/OooAlex/study_note/raw/master/img/202410101710955.png)

---

### Cookies

Cookies allow sites to keep track of users.

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202410101743505.png" alt="image-20241010174352430"  />

---

### Web Caching

#### Web caching

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202410151249513.png" alt="image-20241015124919327" style="zoom: 80%;" />

#### Conditional GET

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202410151358041.png" alt="image-20241015135846944" style="zoom:67%;" />

---

### HTTP/2, HTTP/3





## 2.3 Email



![image-20241015154241336](https://gitee.com/OooAlex/study_note/raw/master/img/202410151542590.png)





## 2.4 The Domain Name System: DNS



**DNS is a distributed, hierarchical database.**

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202410151558437.png" alt="image-20241015155811336" style="zoom:150%;" />

  



## 2.7 Socket programming with UDP and TCP

 

UDP client:

```python
from socket import *
serverName = 'hostname'
serverPort = 12000
# create UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage.decode()
clientSocket.close()
```

UDP server:

```python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
# bind socket to local port number 12000
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
```

 

TCP client:

```python
from socket import *
serverName = 'hostname'
serverPort = 12000
# create TCP socket for server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print modifiedSentence.decode()
clientSocket.close()
```

TCP server:

```python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
# bind socket to local port number 12000
serverSocket.bind(('', serverPort))
serverSocket.listen(1);
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())

    connectionSocket.close()
```



