# Scanny

A network discovery tool

Find other devices on the same local network using ARP requests.

Based on Zaid Sabih's tutorial in <https://www.udemy.com/course/learn-python-and-ethical-hacking-from-scratch>

## Table of Contents

[Requirements](##Requirements)  
[Installation](##Installation)  
[Configuration](##Configuration)  
[Execution](##Execution)  
[Contribution](##Contribution)  

## Requirements

- Python 3

- Pip and the `scapy` library

- a target network

## Installation

```bash
git clone https://github.com/abraidotti/Scanny
cd Scanny
```

## Configuration

None

## Execution

Make sure to specify an IP with a CIDR block. `/24` works best.

```bash
python3 scanny.py --target 192.168.0.1/24
```

## Contribution

If you'd like to contribute, file a pull request or github issue to discuss.

TODO:

- add some color
