[toc]

# Lecture Notes

This file mainly consists of my Lecture Notes of UBC ELEC331 Computer Communications and my reading of the textbook *<u>COMPUTER NETWORKING A Top-Down Approach</u>*



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

---



### A services Description



#### Definition

The Internet is an infrastructure that provides services to **distributed applications**.

---

#### socket interface

Socket interface is a set of rules that the sending program must follow so that the data can be delivered to destination program.

---



### What is a Protocol?



#### A Human Analogy

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409032148948.png" alt="image-20240903214826833" style="zoom: 33%;" />

---

#### Network Protocols

A protocol defines the **format** and the **order** of messages exchanged between two or more communicating entities, as well as the **actions** taken on the transmission and/or receipt of a message or other event.

---



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

On the  telco side, DSLAM separates the data and phone signals and sends the data into the Internet.

* Splitter

On the customer side, a splitter separates the data and telephone signals arriving to the home and forwards the data signal to the DSL modem.

---

##### cable Internet access

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409041318239.png" style="zoom:50%;" />

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409041509538.png" alt="image-20240904150914348" style="zoom:50%;" />

<img src="https://gitee.com/OooAlex/study_note/raw/master/img/202409041510599.png" alt="image-20240904151059445" style="zoom:50%;" />

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

Require no physical wire to be installed, can penetrate  walls, provide connectivity to a mobile user, and can potentially carry a signal for long distances.

* Satellite Radio Channels



## The Network Core



