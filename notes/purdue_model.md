# 🏗️ Purdue Model for Industrial Control Systems (ICS)

The **Purdue Model** is a framework used to design and segment Industrial Control Systems (ICS) into distinct levels. It helps organizations apply security controls to each layer effectively.

---

## 🧱 Purdue Model Levels

- **Level 5 – Enterprise Network**
  - Business systems (email, HR, finance)
  - External internet access
  - Least access to control systems

- **Level 4 – Site Business Planning & Logistics**
  - Plant-level operations
  - Production scheduling, inventory systems
  - Interfaces with Level 3

- **Level 3 – Operations / DMZ**
  - Supervisory control systems (like SCADA)
  - Firewalls to restrict access to lower levels

- **Level 2 – Control Systems**
  - PLCs (Programmable Logic Controllers)
  - HMI (Human Machine Interface)

- **Level 1 – Basic Control**
  - Sensors, actuators
  - Direct interaction with machinery

- **Level 0 – Physical Process**
  - Actual physical operations (valves, conveyors, motors)

---

## 🔐 Why It's Important

- Supports **network segmentation**
- Enhances **zero-trust design** in OT environments
- Helps with **compliance** (e.g., IEC 62443, NIST)

---

🛠️ **Use Cases:**
- OT network assessments
- Designing secure ICS systems
- Interview talking point for cybersecurity & ICS roles
