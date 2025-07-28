# 🔐 Network Segmentation

**Network segmentation** is the practice of dividing a network into smaller, isolated sections (called segments or zones) to limit access and improve security.

---

## 🧱 Why Use Segmentation?

- Reduce attack surface
- Contain malware spread
- Enforce least privilege
- Protect legacy or vulnerable systems (especially in OT environments)
- Meet compliance standards (NIST, ISO, IEC 62443)

---

## 🧭 Common Segmentation Methods

| Method        | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| **VLANs**      | Logically divide network segments even on the same hardware                |
| **Firewalls**  | Enforce access rules between segments (e.g., allow/deny ports or IPs)      |
| **Subnets**    | IP-based segmentation, helps with routing and access control               |
| **Air gaps**   | Fully isolate critical systems (e.g., nuclear or SCADA environments)        |

---

## 🏢 Example: Corporate + OT Environment

| Zone                | Devices                                      | Security Purpose                                       |
|---------------------|----------------------------------------------|--------------------------------------------------------|
| **Level 4 - IT**     | Workstations, internet, printers             | Email & admin users — higher exposure                  |
| **Level 3 - DMZ**    | Firewalls, proxies, update servers           | Control point between IT & OT zones                    |
| **Level 2 - Control**| SCADA servers, HMI, engineering workstations | Interact with control devices                          |
| **Level 1 - Field**  | PLCs, RTUs, sensors                          | Real-time device control — should not connect to IT    |
| **Level 0 - Process**| Physical machinery                           | Core operations — absolutely no direct internet access |

---

## 🔒 Benefits of Segmentation

- Stops lateral movement in cyber attacks
- Easier incident detection and response
- Better performance and traffic management
- Stronger compliance with security frameworks

---

## 💬 In Job or Interview Terms:

> “I would use firewalls and VLANs to segment Level 3 IT from Level 1 PLCs, following Purdue Model best practices. That limits lateral movement and secures critical OT infrastructure.”

---

*Next: Add firewall rules, ACLs, and visual diagrams to enforce segmentation.*
