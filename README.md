# Approximate Floating Point Counter (Csuros Counter)

# Introduction

Counting events is an important subject to study because when analysing complex systems, the same event might happen multiple times to an extent, which can create memory issues. As an example when counting a type of packet passing a router or how many times a molecule interacts with another molecule on a large simulation. This problem has a lot of solutions such as only counting a fraction of times the event happens (approximate counter with fixed probability) which is better than just count every event, however this is still linearly increasing. Other techniques such as Csuros Counter (approximate counter with decreasing probability) are far better because even when highly frequent events happen the counter will not be linear but logarithmic.

# How to run

## Setup environment

Create virtual environment
```bash
python3 -m venv venv
```

Enter the virtual envionment
```bash
source venv/bin/activate
```

Install requirements (matplotlib)
```bash
pip3 install -r requirements.txt
```

## Run the script to get the results

```bash
python3 src/results.py
```

Note: for the file in example (``datasets/history_of_portugal.txt``) it takes a few minutes to compute. The charts only appear when all everything is done however the statistics are provided as the algorithm runs.
