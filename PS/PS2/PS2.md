# Problem Set 2



## **Problem 1**

> Question P5 on page 169 of the eText (Kurose and Ross, 8th edition).

> The text below shows the reply sent from the server in response to the HTTP GET message in the question above. Answer the following questions, indicating where in the message below you find the answer. 
>
> ```http
> HTTP/1.1 200 OK<cr><lf>
> Date: Tue, 07 Mar 2008 12:39:45GMT<cr><lf>
> Server: Apache/2.0.52 (Fedora)<cr><lf>
> Last-Modified: Sat, 10 Dec2005 18:27:46 GMT<cr><lf>
> ETag: ”526c3-f22-a88a4c80”<cr><lf>
> AcceptRanges: bytes<cr><lf>Content-Length: 3874<cr><lf>
> Keep-Alive: timeout=max=100<cr><lf>
> Connection:Keep-Alive<cr><lf>
> Content-Type: text/html;
> charset= ISO-8859-1<cr><lf>
> <cr><lf>
> <!doctype html public ”- 
> //w3c//dtd html 4.0transitional//en”><lf><html><lf>
> <head><lf> <meta http-equiv=”Content-Type” 
> content=”text/html; charset=iso-8859-1”><lf> <meta
> name=”GENERATOR” content=”Mozilla/4.79 [en] (Windows NT
> 5.0; U) Netscape]”><lf> <title>CMPSCI 453 / 591 / 
> NTU-ST550ASpring 2005 homepage</title><lf></head><lf>
> <much more document text following here (not shown)>
> ```

> a. Was the server able to successfully find the document or not? What time  was the document reply provided? 

The server was able to successfully find the document. This is indicated by the status code "200 OK" in the first line of the response.

The time the document reply was provided is: Tue, 07 Mar 2008 12:39:45 GMT, as shown in the "Date" field of the response header.

> b. When was the document last modified? 

The document was last modified on: Sat, 10 Dec 2005 18:27:46 GMT, as indicated by the "Last-Modified" field in the response header.

> c. How many bytes are there in the document being returned? 

The document being returned is 3874 bytes, as shown in the "Content-Length" field of the response header.

> d. What are the first 5 bytes of the document being returned? Did the server agree to a persistent connection?

The first 5 bytes of the document being returned are: <!doc

This can be seen at the beginning of the HTML content in the response.

Yes, the server agreed to a persistent connection. This is indicated by two things in the response header:

1. The "Connection: Keep-Alive" field
2. The "Keep-Alive: timeout=max=100" field, which specifies parameters for the persistent connection.



## **Problem 2**

> Questions P13 and P14 on page 171 of the eText (Kurose and Ross, 8th edition).

> P13. Consider sending over HTTP/2 a Web page that consists of one video clip,  and five images. Suppose that the video clip is transported as 2000 frames,  and each image has three frames.  

> a. If all the video frames are sent first without interleaving, how many  “frame times” are needed until all five images are sent? 

The total "frame times" needed until all five images are sent would be: 2000 + (3 * 5) = 2000 + 15 = 2015 frame times.

> b. If frames are interleaved, how many frame times are needed until all five images are sent.

The number of frame times needed until all five images are sent would be: 3 * 6 = 18 frame times.

> P14. Consider the Web page in problem 13. Now HTTP/2 prioritization is employed. Suppose all the images are given priority over the video clip, and that the first image is given priority over the second image, the second image over the third image, and so on. How many frame times will be needed until the second image is sent?

The total number of frame times needed until the second image is completely sent is:

3 (for the first image) + 3 (for the second image) = 6 frame times



## **Problem 3**

> In this assignment, you will develop a TCP server and a TCP client. 
>
> Specifically, your TCP client will (i) collects a string variable from the keyboard input; (ii) send the string variable to the TCP server; and (iii) receive the response from the TCP server over the TCP connection. 
>
> Your TCP server will (i) create a connect socket when contacted by the TCP client; (ii) receive the string variable sent by the TCP client; (iii) generate a reward based on the string variable sent by the TCP client. The rules for determining the reward are shown in Table 1; and (iv) inform the TCP client about the reward by sending a response over the TCP connection to the TCP client.
>
> Note that, when determining the reward based on Table 1, you need to differentiate between uppercase letters and lowercase letters. For example, the uppercase ’C’ should be assigned with a reward of 1 whereas the lowercase ’c’ should be assigned with a reward of *−*1.
>
> For this assignment, you may use TCPClient.py and TCPServer.py that are presented in Section 2.7.2 of the eText (Kurose and Ross, 8th edition) as the skeleton codes. You can also write your own codes.
>
> **What to Hand in**
>
> For this problem, you will hand in the codes for both your TCP client and TCP server. The reward received from the TCP server should be **displayed at your TCP client** (e.g., using Python print function). You need to provide the screenshots at the TCP client verifying that your codes works as required. There is no output requirement for your TCP server. The codes must include sufficient comment statements.
>
> <img src="https://gitee.com/OooAlex/study_note/raw/master/img/202410161438210.png" alt="image-20241016143804007" style="zoom: 80%;" />

I choose to implement a non-persistent TCP connection between the client and the server. That is to say, the client and the server close the sockets after each data transfer and create new sockets before new data transfer.

`TCPServer.py`:

```python
from socket import *

# calculate reward based on input string variable
def calculate_reward(string):    
    if string == 'A':
        return 3
    elif string == 'B':
        return 2
    elif string == 'C':
        return 1
    else:
        return -1

    serverPort = 15000

    # create a TCP socket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # bind socket to local port number 15000
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print("The server is ready to receive")

    while True:
        # wait for a client connection
        connectionSocket, addr = serverSocket.accept()

        # receive the string from the client and calculate the reward
        string = connectionSocket.recv(1024).decode().strip()
        reward = calculate_reward(string)
        # send back the reward
        connectionSocket.send(str(reward).encode())

        connectionSocket.close()
```

`TCPClient.py`:

```python
from socket import *

# set up server hostname and port number
serverName = 'localhost'
serverPort = 15000

# Run indefinitely to allow continuous client-server communication
while True:
    # create a TCP socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # connect to server at the specified hostname and port
    clientSocket.connect((serverName, serverPort))

    string = input('Input the string variable:')
    clientSocket.send(string.encode())

    # receive the reward from the server
    reward = clientSocket.recv(1024)
    print(reward.decode())
    clientSocket.close()
```

Reward received from the TCP server:

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202410161540178.png" alt="image-20241016154017959" style="zoom: 90%;" />



## **Problem 4**

> In this problem, you will learn the basics of socket programming for UDP in Python. You will learn how to send and receive datagram packets using UDP sockets and also, how to set a proper socket timeout. Throughout the problem, you will gain familiarity with a Ping application and its usefulness in computing statistics such as packet loss rate.
>
> You will first study a simple Internet ping server written in Python, and implement the corresponding client. The functionality provided by these programs is similar to the functionality provided by standard ping programs available in modern operating systems. However, these programs use a simpler protocol, UDP, rather than the standard Internet Control Message Protocol (ICMP) to communicate with each other. The ping protocol allows a client machine to send a data packet to a remote machine, and have the remote machine return the data back to the client unchanged (an action referred to as echoing). Among other uses, the ping protocol allows hosts to determine round-trip times to other machines.
>
> You are given the complete code for the Ping server below. Your task is to write the Ping client.
>
> **Server Code**
>
> The following code fully implements a ping server. You need to compile and run this code before running your client program. You do not need to modify this code.
>
> In this server code, some of the client’s packets are simulated to be lost. You should study this code carefully, as it will help you implement your Ping client.
>
> ![image-20241016162548995](https://gitee.com/OooAlex/study_note/raw/master/img/202410161625217.png)
>
> The server sits in an infinite loop listening for incoming UDP packets. When a packet comes in and if a randomized integer is greater than or equal to 18, the server simply capitalizes the encapsulated data and sends it back to the client.
>
> **Packet Loss**
>
> UDP provides applications with an unreliable transport service. Messages may get lost in the network due to router queue overflows, faulty hardware or some other reasons. The two processes normally run on two hosts on the Internet, but in this problem, you develop/debug them both running on one machine (using localhost or 127.0.0.1). Because packet loss is rare or even non-existent using localhost, the server in this problem injects artificial loss to simulate the effects of network packet loss. The server creates a variable randomized integer which determines whether a particular incoming packet is lost or not.
>
> **(a)** Calculate the packet loss based on the provided server code.

Probability of packet loss = Outcomes resulting in loss / Total possible outcomes = 18 / 50 = 0.36

Therefore, the packet loss rate based on this server code is 36%.

> **Client Code**
>
> **(b)** You need to implement the following client program.
>
> The client should send 20 pings to the server. Because UDP is an unreliable protocol, a packet sent from the client to the server may be lost in the network, or vice versa. For this reason, the client cannot wait indefinitely for a reply to a ping message. You should get the client wait up to two seconds for a reply; if no reply is received within two seconds, your client program should assume that the packet was lost during transmission across the network. You will need to look up the Python documentation to find out how to set the timeout value on a datagram socket.
>
> Specifically, your client program should
>
> • send the ping message using UDP (Note: Unlike TCP, you do not need to establish a connection first, since UDP is a connectionless protocol.)
>
> • print the response message from server, if any
>
> • calculate and print the round trip time (RTT), in seconds, of each packet, if server responses
>
> • otherwise, print “Request timed out”
>
> **Message Format**
>
> The ping messages in this problem are formatted in a simple way. The client message is one line, consisting of ASCII characters in the following format:
>
> Ping *sequence number time*
>
> where *sequence number* starts at 1 and progresses to 20 for each successive ping message sent by the client, and *time* is the time when the client sends the message.
>
> **What to Hand in**
>
> For part (b) of this problem, you will hand in the complete client code and screenshots at the client verifying that your ping program works as required, i.e., if the client receives a message from the server, it prints the received message and in the next line, it prints the RTT in seconds. Otherwise, it prints “Request time out”.
>
> The code must include sufficient comment statements.

`UDPPingerClient.py`:

```python
import time
from socket import *
from datetime import datetime

# Server address and port
server_addr = ('localhost', 12000)
# Number of pings to send
num_pings = 20
# Timeout in seconds
timeout = 2

# Create UDP client socket
client_socket = socket(AF_INET, SOCK_DGRAM)
# Set socket timeout
client_socket.settimeout(timeout)

for seq_num in range(1, num_pings + 1):
    # Get current time in a readable format
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create ping message
    message = f"Ping {seq_num} {current_time}"

    try:
        # Send ping and record time
        send_time = time.time()
        client_socket.sendto(message.encode(), server_addr)

        # Receive response
        responseMessage, server = client_socket.recvfrom(1024)
        recv_time = time.time()

        # Calculate and print RTT
        rtt = recv_time - send_time
        print(responseMessage.decode())
        print(f"RTT: {rtt:.6f} seconds")

    except TimeoutError:
        print("Request timed out")

        # Wait a bit before sending the next ping
        time.sleep(0.1)

        # Close the socket
        client_socket.close()
```

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202410162149987.png" alt="image-20241016214910906" style="zoom:80%;" />



## **Problem 5**

> Wireshark Lab: Domain Name System (DNS). Details can be found in the eText and book’s website, www.pearsonhighered.com/cs-resources. Please note that only DNS Wireshark lab of version 8.1 is acceptable. Also, when you hand in your assignment, provide the screenshots and annotate the output so that it is clear where in the output you are obtaining the information for your answer.

### 1. `nslookup`

> 1. Run `nslookup` to obtain the IP address of the web server for the Indian Institute of Technology in Bombay, India: www.iitb.ac.in.  What is the IP address of www.iitb.ac.in 

![image-20241016224158275](https://gitee.com/OooAlex/study_note/raw/master/img/202410162241351.png)

IPv4 Address: 103.21.124.133

IPv6 Address: 64:ff9b::6715:7c85

> 2. What is the IP address of the DNS server that provided the answer to your `nslookup` command in question 1 above?

10.255.255.254

> 3. Did the answer to your `nslookup` command in question 1 above come from an authoritative or non-authoritative server?

Non-authoritative server.

> 4. Use the `nslookup` command to determine the name of the authoritative name server for the iit.ac.in domain.  What is that name?  (If there are more than one authoritative servers, what is the name of the first authoritative server returned by `nslookup`)? If you had to find the IP address of that authoritative name server, how would you do so?

![image-20241016224945071](https://gitee.com/OooAlex/study_note/raw/master/img/202410162249177.png)

dns2.iitb.ac.in

> If you had to find the IP address of that authoritative name server, how would you do so?

```
nslookup dns2.iitb.ac.in
```

### 2. The DNS cache on your computer

clear DNS resolver cache:

![image-20241016230734005](https://gitee.com/OooAlex/study_note/raw/master/img/202410162307080.png)

### 3. Tracing DNS with Wireshark

![image-20241017011432802](https://gitee.com/OooAlex/study_note/raw/master/img/202410170114999.png)

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202410170114389.png" alt="image-20241017011404336" style="zoom:200%;" />

> 5. Locate the first DNS query message resolving the name gaia.cs.umass.edu. What is the packet number in the trace for the DNS query message?  Is this query message sent over UDP or TCP?  

The first DNS query message for gaia.cs.umass.edu:

- Packet number: 15
- Protocol: DNS (which runs over UDP)

> 6. Now locate the corresponding DNS response to the initial DNS query. What is the packet number in the trace for the DNS response message?  Is this response message received via UDP or TCP?  

The corresponding DNS response:

- Packet number: 17
- Protocol: DNS (which runs over UDP)

> 7. What is the destination port for the DNS query message? What is the source port of the DNS response message?

DNS query and response ports:

DNS query message:

![image-20241017004219496](https://gitee.com/OooAlex/study_note/raw/master/img/202410170042606.png)

DNS response message:

![image-20241017004319123](https://gitee.com/OooAlex/study_note/raw/master/img/202410170043194.png)

- Destination port for DNS query: 53
- Source port of DNS response: 53

> 8. To what IP address is the DNS query message sent? 

IP address the DNS query is sent to:

- 75.75.75.75 (as seen in the destination column for packet 15)

> 9. Examine the DNS query message. How many “questions” does this DNS message contain? How many “answers” answers does it contain?

Examining the DNS query message (packet 15):

![image-20241017010447086](https://gitee.com/OooAlex/study_note/raw/master/img/202410170104216.png)

- Questions: 1 (Standard query 0x3c29 A gaia.cs.umass.edu)
- Answers: 0 (queries don't contain answers)

> 10. Examine the DNS response message to the initial query message. How many “questions” does this DNS message contain? How many “answers” answers does it contain?

Examining the DNS response message (packet 17):

![](https://gitee.com/OooAlex/study_note/raw/master/img/202410170104159.png)

- Questions: 1 (the original question is typically repeated in the response)
- Answers: 1 (Standard query response 0x3c29 A gaia.cs.umass.edu A 128.119.245.12)

> 11. The web page for the base file http://gaia.cs.umass.edu/kurose_ross/ references the image object http://gaia.cs.umass.edu/kurose_ross/header_graphic_book_8E_2.jpg , which, like the base webpage, is on gaia.cs.umass.edu.  

> What is the packet number in the trace for the initial HTTP GET request for the base file http://gaia.cs.umass.edu/kurose_ross/?  

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202410170113740.png" alt="image-20241017011301589" style="zoom: 100%;" />

22

> What is the packet number in the trace of the DNS query made to resolve gaia.cs.umass.edu so that this initial HTTP request can be sent to the gaia.cs.umass.edu IP address?   

![image-20241017011625269](https://gitee.com/OooAlex/study_note/raw/master/img/202410170116425.png)

15

> What is the packet number in the trace of the received DNS response? 

17

> What is the packet number in the trace for the HTTP GET request for the image object http://gaia.cs.umass.edu/kurose_ross/header_graphic_book_8E2.jpg? 

![image-20241017011828574](https://gitee.com/OooAlex/study_note/raw/master/img/202410170118734.png)

205

> What is the packet number in the DNS query made to resolve gaia.cs.umass.edu so that this second HTTP request can be sent to the gaia.cs.umass.edu IP address? Discuss how DNS caching affects the answer to this last question.

There is no DNS query visible in this trace for the second HTTP request.

When the client first accessed gaia.cs.umass.edu for the base file, it would have made a DNS query to resolve the domain name to an IP address. After receiving the DNS response, the client's operating system or browser would have cached this DNS information, associating gaia.cs.umass.edu with its IP address. For the second HTTP request (the image file we see in packet 205), the client already knows the IP address for gaia.cs.umass.edu from its cache. Therefore, it doesn't need to perform another DNS query.

> Now let’s play with `nslookup`. 

![image-20241017014102470](https://gitee.com/OooAlex/study_note/raw/master/img/202410170141676.png)

> 12. What is the destination port for the DNS query message? What is the source port of the DNS response message?

destination port for the DNS query message: 53

source port of the DNS response message: 53

> 13. To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server?

75.75.75.75

Yes, it is the IP address of my default local DNS server.

> 14. Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?

Type A DNS query

![](https://gitee.com/OooAlex/study_note/raw/master/img/202410170143739.png)

No, the query message does not contain any "answers".

> 15. Examine the DNS response message to the query message. How many “questions” does this DNS response message contain? How many “answers”?

![image-20241017014418523](https://gitee.com/OooAlex/study_note/raw/master/img/202410170144689.png)

1 "question" and 1 "answer"

> Last, let’s use nslookup to issue a command that will return a type NS DNS record, Enter the following command:
>
> ```shell
> nslookup –type=NS umass.edu
> ```
>
> and then answer the following questions :

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202410170154642.png" alt="image-20241017015433418" style="zoom:200%;" />

> 16. To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server?

75.75.75.75

Yes, it is the IP address of my default local DNS server.

> 17. Examine the DNS query message. How many questions does the query have? Does the query message contain any “answers”?

![image-20241017020117183](https://gitee.com/OooAlex/study_note/raw/master/img/202410170201234.png)

The query has 1 question.

No, the query message does not contain any "answers".

> 18. Examine the DNS response message (in particular the DNS response message that has type “NS”).  How many answers does the response have?  What information is contained in the answers? How many additional resource records are returned? What additional information is included in these additional resource records (if additional information is returned)?

![image-20241017020213875](https://gitee.com/OooAlex/study_note/raw/master/img/202410170202039.png)

The response has 3 answers.

The answers contain the domain name of three name servers(authoritative DNS servers), which are responsible for resolving queries for the `umass.edu` domain.

3 additional resource records are returned.

The addition resource records include the corresponding IP addresses for the domain names above.

