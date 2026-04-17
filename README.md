# 🚀 Packet Drop Simulator using SDN (POX + Mininet)

## 📌 Project Title

Packet Drop Simulator

---

## 🎯 Objective

Simulate packet loss using SDN flow rules by selectively dropping packets between specific hosts while allowing normal communication for others.

---

## 🛠️ Technologies Used

- Python
- Mininet
- POX Controller
- Open vSwitch (OVS)

---

## 📁 Project Structure

Packet-Drop-Simulator/
│── packet_drop.py (Controller logic)
│── topology.py (Network topology)
│── regression_test.py (Validation script)
│── README.md
│── Output/

---

## ⚙️ Setup and Execution Steps

### Step 1: Clean previous Mininet state

sudo mn -c
sudo pkill -f pox

---

### Step 2: Start POX Controller

cd ~/cn/pox
./pox.py packet_drop

---

### Step 3: Run Mininet Topology

sudo python3 topology.py

---

## 🧪 Testing Commands (Mininet CLI)

### ✅ Allowed Traffic

h1 ping h2

Expected:

- Replies received
- 0% packet loss

---

### ❌ Blocked Traffic

h1 ping h3

Expected:

- No replies
- 100% packet loss

---

### 📊 Network Summary

pingall

---

## 🔍 Flow Table Verification

Run in new terminal:
sudo ovs-ofctl dump-flows s1

Expected:

- Flow entries present
- Drop rule for traffic from 10.0.0.1 to 10.0.0.3

---

## 🧪 Validation (Regression Test)

sudo python3 regression_test.py

Expected:

- Drop rule exists
- Rule persists over time

---

## 📸 Output Screenshots

### Screenshot 1

![Screenshot 1](Output/output%201.jpeg)

### Screenshot 2

![Screenshot 2](Output/output%202.jpeg)

### Screenshot 3

![Screenshot 3](Output/output%203.jpeg)

### Screenshot 4

![Screenshot 4](Output/output%204.jpeg)

### Screenshot 5

![Screenshot 5](Output/output%205.jpeg)

### Screenshot 6

![Screenshot 6](Output/output%206.jpeg)

### Screenshot 7

![Screenshot 7](Output/output%207.jpeg)

---

## 🎯 Expected Results

| Test Case | Result  |
| --------- | ------- |
| h1 → h2   | Allowed |
| h1 → h3   | Dropped |
| h3 → h1   | Allowed |

---

## 🧠 Working Principle

- Switch sends packets to controller when no rule exists
- Controller inspects IPv4 source and destination
- If source = 10.0.0.1 and destination = 10.0.0.3:
  → Install DROP rule
- Otherwise:
  → Forward packet normally using learning switch logic

---

## 🎤 Viva Explanation

This project demonstrates SDN-based traffic control where the controller dynamically installs flow rules to block specific communication while allowing others.

---

## ✅ Conclusion

The project successfully:

- Implements SDN-based packet filtering
- Installs flow rules in the switch
- Demonstrates selective packet loss
- Verifies rule persistence using testing

---

## 👨‍💻 Author

Varun M L
