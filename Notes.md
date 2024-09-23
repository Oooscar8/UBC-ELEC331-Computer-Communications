[toc]

# Notes

This file mainly consists of my Notes of UBC ELEC331 Computer Communications, my reading of the textbook *<u>COMPUTER NETWORKING A Top-Down Approach</u>* and its corresponding lectures.



# CHAPTER 1 Computer Networks and the Internet



## What is the Internet?



### A Nuts-and-Bolts Description



#### basic concepts

Devices connected to the Internet: **hosts** or **end system**

End systems are connected together by a network of **communication links** and **packet switches**. 

---

#### communication links

 Made up of different types of physical media

Different links have different **transmission rate**, measured in bits/seconds

When one end system has data to send to another end system, the sending end system segments(分段) the data and adds header bytes to each segment(段). The resulting packages of information, known as **packets**(分组), are then sent through the network to the destination end system, where they are reassembled into the original data

---

#### packet switch

Takes a packet arriving on one of its incoming communication links and forwards that packet on one of its outgoing communication links

* **routers**(路由器) 

> used in the network core

* **link-layer switches**(链路层交换机)

> used in access networks

The sequence of communication links and packet switches traversed by a packet from the sending end system to the receiving end system is known as a **route** or **path** through the network. 

---

#### Protocols

End systems, packet switches, and other pieces of the Internet run protocols that  control the sending and receiving of information within the Internet.

* TCP(Transmission Control Protocol)

* Internet Protocol (IP)

> specifies the format of packets

* TCP/IP



### A services Description



#### Definition

The Internet is an infrastructure that provides services to **distributed applications**.

---

#### socket interface

Socket interface is a set of rules that the sending program must follow so that the data can be delivered to destination program.



### What is a Protocol?



#### A Human Analogy

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409032148948.png" alt="image-20240903214826833" style="zoom: 33%;" />

---

#### Network Protocols

A protocol defines the **format** and the **order** of messages exchanged between two or more communicating entities, as well as the **actions** taken on the transmission and/or receipt of a message or other event.



## The Network Edge

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409041100101.png" alt="image-20240904110050027" style="zoom:50%;" />

hosts: 

* clients 

desktops, laptops, smartphones…

* servers

powerful machines that store and distribute Web pages, stream video, relay e-mail…

**in large data centers**



### Access Networks



#### Home Access

##### DSL Internet access

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409041120064.png" alt="image-20240904112018897" style="zoom:50%;" />

* DSL modem

Translate between digital data and high-frequency tones.

Data and telephone signals are encoded at different frequencies.

* DSLAM

On the telco side, DSLAM separates the data and phone signals and sends the data into the Internet.

* Splitter

On the customer side, a splitter separates the data and telephone signals arriving to the home and forwards the data signal to the DSL modem.

Asymmetric: downstream transmission rate is larger than upstream transmission rate

---

##### cable Internet access

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409041318239.png" style="zoom:50%;" />

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409041509538.png" alt="image-20240904150914348" style="zoom:50%;" />

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409041510599.png" alt="image-20240904151059445" style="zoom:50%;" />

Frequency division multiplexing(FDM): different channels transmitted in different frequency bands

Asymmetric: downstream transmission rate is larger than upstream transmission rate

CMTS‘s function is similar to DSLAM

---

##### fiber to the home (FTTH)

even faster!

provide an optical fiber path from the CO directly to the home

FTTH using the PON distribution architecture (passive optical networks):

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409041339786.png" alt="image-20240904133946720" style="zoom:50%;" />

packets sent from OLT are replicated at the splitter (similar to a cable head end)

---

##### 5G fixed wireless

without installing costly and failure-prone cabling



#### Access in the Enterprise (and the Home): Ethernet and WiFi

* Ethernet

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409041551016.png" alt="image-20240904155156845" style="zoom:50%;" />

---

* Home Network

  <img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409041558726.png" style="zoom:50%;" />



#### Wide-Area Wireless Access: 3G and LTE 4G and 5G

Employ the same wireless infrastructure used for cellular telephony to send/receive packets through a base station that is operated by the cellular network provider.



### Physical Media

guided media / unguided media.

* Twisted-Pair Copper Wire

Twisted pair is the dominant solution for high-speed LAN networking

* Coaxial Cable

Coaxial cable can be used as a guided shared medium

* Fiber Optics

* Terrestrial Radio Channels

Require no physical wire to be installed, can penetrate walls, provide connectivity to a mobile user, and can potentially carry a signal for long distances.

* Satellite Radio Channels



## The Network Core



### Packet Switching

R: transmission rate (bps)

L: length of a packet

**transmission delay**:

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409121311655.png" alt="image-20240912131136591" style="zoom:50%;" />

  

#### Store-and Forward Transmission

it takes 2L/R(time) for a packet to be sent from Source to Destination

it takes 4L/R(time) for all three packets to be sent from Source to Destination

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409121419327.png" alt="image-20240912141943199" style="zoom: 67%;" />

More general form: N links each of rate R

**end-to-end delay**:

![image-20240912142622318](https://gitee.com/OooAlex/study_note/raw/master/img/202409121426382.png)



#### Queuing Delays and Packet Loss

**output buffer** (**output queue**): the arriving packet **wait** here

result in output buffer **queuing delays**

if the output buffer is full, **packet loss** occurs

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409121445872.png" alt="image-20240912144530808" style="zoom:67%;" />



#### Forwarding Tables and Routing Protocols

> How do forwarding tables get set?

The Internet has a number of special **routing protocols** that are used to **automatically** set the forwarding tables



###  Circuit Switching

When two hosts want to communicate, the network establishes **a dedicated end-to-end connection.**

> Why is circuit switching less efficient than packet switching?

Circuit switching pre-allocates use of the transmission link  regardless of demand, with allocated but unneeded link time going unused

Packet  switching allocates link use on demand

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409221640398.png" alt="image-20240922164045198" style="zoom:50%;" />



### Internet is a "network of networks"!

Interconnection of ISPs:

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409221614053.png" alt="image-20240922161449805" style="zoom: 25%;" />



## Delay, Loss, and Throughput in Packet-Switched Networks

four delays:

* transmission delay: time to **push** the entire packet onto the link
* processing delay
* propagation delay
* queueing delay -> congestion and packet loss

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409221917593.png" alt="image-20240922191750407" style="zoom: 33%;" />



Throughput:

analogy to pipes

rate(bits/time unit) at which bits are being sent from sender to receiver

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409221937913.png" alt="image-20240922193702630" style="zoom:25%;" />



## Layering, encapsulation, service models

Layering and encapsulation:

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409222317594.png" alt="image-20240922231747247" style="zoom:40%;" />

The switches and routers only implement the lower layer of the protocol stack:

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409222320192.png" alt="image-20240922232032878" style="zoom:40%;" />
