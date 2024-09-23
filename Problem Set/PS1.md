# Problem Set 1



## Problem 1

> Go to [IETF’s website](https://www.ietf.org/) to see what they are doing. Select a project you are interested in and write a half-page summary on the problem and the proposed solution.

### Decentralization of the Internet Research Group (DINRG)

The Decentralization of the Internet Research Group (DINRG) is working on a big issue: the growing centralization of the Internet. Over recent years, we've seen a few big players dominate Internet applications, services, and infrastructure. This centralization can lead to various problems, such as reduced competition, less innovation, and potential threats to privacy and freedom of expression.

DINRG's main goal is to understand why this centralization is happening and what its impacts are. They are looking into several factors, including how the market economy, architecture and protocol designs, and government regulations contribute to this trend. They also want to measure how centralized the Internet has become and what societal impacts this has.

To address these issues, DINRG is working on developing a common language and understanding of what decentralization means. They are engaging with the broader research community to explore new ideas and technical solutions for creating decentralized systems and applications. They aim to document their findings in research papers and RFCs to contribute to the wider conversation about Internet centralization.

DINRG is open to different technology solutions and wants to foster a better understanding of the pros and cons of specific technologies related to Internet decentralization. They plan to meet regularly, at least once a year at IETF meetings, and may hold additional meetings at other events. They also want to collaborate with other research groups and reach out to non-networking communities, like regulatory bodies and economics researchers, to organize panels and workshops on Internet decentralization.

In summary, DINRG is focused on understanding and addressing the centralization of the Internet by investigating its causes, measuring its impacts, and exploring solutions to promote a more decentralized Internet.



## Problem 2

> Suppose a 1 Gbps point-to-point link is being set up between the Earth and a new lunar colony. The distance from the moon to the Earth is approximately 385,000 km, and data travels over the link at the speed of light – 3 × 10^8 m/s.
>

>(a) Calculate the minimum round trip time (RTT) for the link.  

$RTT = (2* s * v) / v = \frac{385000*10^3*2}{3*10^8} = 2.567s$

> (b) Using the RTT as the delay, calculate the bandwidth × delay product for the link. 

$bandwidth * delay = 10^9(bits/second) * 2.567(seconds) = 2.567 * 10^9(bits) = 3.209*10^8(B) = 320.875(MB)$

> (c) What is the significance of the bandwidth × delay product computed in (b)?  

The product represents the amount of data that can be in transit on the link between the Earth and the lunar colony at any given time.

> (d) A camera on the lunar base takes pictures of the Earth and saves them in digital format to disk. Suppose Mission Control on Earth wishes to download the most current image, which is 25 megabytes (MB). What is the minimum amount of time that will elapse between when the request for the data goes out and the transfer is finished?

$t_{min} = RTT + L / R = 2.567 + 25 * 8 * 10^6/10^9(s) = 2.767(s)$​  



## Problem 3

> Assume you wish to transfer an F bytes (B) file along a path composed of the source, destination, 6 point-to-point links, and 5 switches. Suppose each link has a propagation delay of 2 milliseconds (`ms`) and a bandwidth of 4 megabits per second (Mb/s). Each switch supports both circuit switching and packet switching.
>
> For packet switching, the file is divided into packets. Each packet has 24 bytes of packet header information and 1 kilobyte (kB) of payload. The store-and-forward packet processing at each switch incurs a 1 `ms` delay after the packet has been completely received. Packets can be sent continuously without waiting for acknowledgements. The file size is assumed to be a multiple of 1000 bytes.
>
> For circuit switching, a circuit first needs to be set up through the switches. The file is then sent as one contiguous bitstream. For circuit setup, the source first needs to send a 1024-byte “connection request” message. If all the intermediate switches accept the request, then the destination will send a 1024-byte “connection reply” message to the source. Each switch incurs a 1 `ms` processing delay after either the “connection request” or “connection reply” message has been completely received. Assume switches introduce no delay to data traversing a circuit.

> (a) For what file size F (in bytes) is the total number of bytes sent across the network by using circuit switching to be smaller than the number of bytes sent across the network by using packet switching?  

Assume file size F = N(bytes)

$ 1024 * 2 + N < N/1000 * 1024$

Therefore, file size F should be at least 43kB(kilobytes).

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409230146444.jpg" alt="de31089cb8d71a4727deaf00b3215c3" style="zoom:50%;" />

> (b) For what file size F (in bytes) is the total delay incurred before the entire file arrives at the destination by using circuit switching to be lower than the total delay incurred by using packet switching?

As shown below, file size F should be at least 139KB.

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409230208176.jpg" alt="9f2318c1c713602e404061eb2ada90a" style="zoom:50%;" />



## Problem 4

> Question P18 from the `eText` (Kurose and Ross, 8th edition), p. 72.

> P18. Perform a Traceroute between source and destination on the same continent  at three different hours of the day. 

```
root@LAPTOP-D6H0EK35:/mnt/c/Users/s1590# traceroute google.com
traceroute to google.com (142.250.217.110), 30 hops max, 60 byte packets
 1  LAPTOP-D6H0EK35.mshome.net (172.21.0.1)  0.324 ms  0.301 ms  0.336 ms
 2  172.20.10.1 (172.20.10.1)  5.492 ms  2.821 ms  5.480 ms
 3  * * *
 4  * * *
...
root@LAPTOP-D6H0EK35:/mnt/c/Users/s1590# traceroute google.com
traceroute to google.com (142.250.217.110), 30 hops max, 60 byte packets
 1  LAPTOP-D6H0EK35.mshome.net (172.21.0.1)  0.307 ms  0.254 ms  0.247 ms
 2  172.20.10.1 (172.20.10.1)  2.848 ms  4.357 ms  3.032 ms
 3  * * *
 4  * * *
...
root@LAPTOP-D6H0EK35:/mnt/c/Users/s1590# traceroute google.com
traceroute to google.com (142.251.33.110), 30 hops max, 60 byte packets
 1  LAPTOP-D6H0EK35.mshome.net (172.21.0.1)  0.267 ms  0.274 ms  0.318 ms
 2  172.20.10.1 (172.20.10.1)  5.737 ms  4.140 ms  2.676 ms
 3  * * *
 4  * * *
 ...
```

> a. Find the average and standard deviation of the round-trip delays at each of  the three hours. 

Hop1:

| Run  | Average (ms) | Standard Deviation (ms) |
| ---- | ------------ | ----------------------- |
| 1    | 0.320        | 0.017                   |
| 2    | 0.269        | 0.030                   |
| 3    | 0.286        | 0.026                   |

Hop2:

| Run  | Average (ms) | Standard Deviation (ms) |
| ---- | ------------ | ----------------------- |
| 1    | 4.264        | 1.379                   |
| 2    | 3.412        | 0.751                   |
| 3    | 4.184        | 1.411                   |

> b. Find the number of routers in the path at each of the three hours. Did the paths change during any of the hours? 

| Run  | Number of Routers | Path Description        |
| ---- | ----------------- | ----------------------- |
| 1    | 2                 | 172.21.0.1, 172.20.10.1 |
| 2    | 2                 | 172.21.0.1, 172.20.10.1 |
| 3    | 2                 | 172.21.0.1, 172.20.10.1 |

The paths remained the same across all three runs. Each run had the same two routers successfully responding.

> c. Try to identify the number of ISP networks that the Traceroute packets pass through from source to destination. Routers with similar names and/or similar IP addresses should be considered as part of the same ISP. In your experiments, do the largest delays occur at the peering interfaces between adjacent ISPs? 

2 ISP networks

Yes, the largest delays occur at the peering interfaces between adjacent ISPs.

> d. Repeat the above for a source and destination on different continents.  Compare the intra-continent and inter-continent results

inter-continent results:

```
root@LAPTOP-D6H0EK35:/mnt/c/Users/s1590# traceroute 4Web.ca
traceroute to 4Web.ca (199.96.31.141), 30 hops max, 60 byte packets
 1  LAPTOP-D6H0EK35.mshome.net (172.21.0.1)  0.679 ms  0.541 ms  0.410 ms
 2  * 172.20.10.1 (172.20.10.1)  2.445 ms *
 3  * * *
 4  * * *
...
root@LAPTOP-D6H0EK35:/mnt/c/Users/s1590# traceroute 4Web.ca
traceroute to 4Web.ca (199.96.31.141), 30 hops max, 60 byte packets
 1  LAPTOP-D6H0EK35.mshome.net (172.21.0.1)  0.443 ms  0.427 ms  0.423 ms
 2  172.20.10.1 (172.20.10.1)  4.876 ms  3.871 ms  4.867 ms
 3  * * *
 4  * * *
...
root@LAPTOP-D6H0EK35:/mnt/c/Users/s1590# traceroute 4Web.ca
traceroute to 4Web.ca (199.96.31.141), 30 hops max, 60 byte packets
 1  LAPTOP-D6H0EK35.mshome.net (172.21.0.1)  0.312 ms  0.295 ms  0.252 ms
 2  172.20.10.1 (172.20.10.1)  5.095 ms  5.089 ms  5.555 ms
 3  * * *
 4  * * *
...
```

Route Delay Results Table:

| Hop Number | Average RTT (ms)  | Standard Deviation (ms) |
| ---------- | ----------------- | ----------------------- |
| Hop 1      | 0.41967           | 0.12345                 |
| Hop 2      | 4.23467           | 0.56789                 |
| Hop 3      | Request Timed Out | -                       |



## Problem 5

> Question P22 from the `eText` (Kurose and Ross, 8th edition), p. 73.

> P22. Consider Figure 1.19(b). Suppose that each link between the server and the  client has a packet loss probability p, and the packet loss probabilities for these links are independent. What is the probability that a packet (sent by the server) is successfully received by the receiver? If a packet is lost in the path from the server to the client, then the server will re-transmit the packet. On average, how many times will the server re-transmit the packet in order for the client to successfully receive the packet?
>
> <img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409221515222.png" style="zoom: 67%;" />

1. What is the probability that a packet (sent by the server) is successfully received by the receiver? 

    $(1-p)^N$

2. On average, how many times will the server re-transmit the packet in order for the client to successfully receive the packet?

   $\frac{1}{(1-p)^N}$

