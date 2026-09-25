# Risk Assessment: Cryptography & Network Security Exam

## 1. Assets, Vulnerabilities, and Possible Consequences
1. **Asset:** Student Records Database Server
   * **Vulnerability:** Guest network access to the records server and unencrypted file transfers (e.g., plain HTTP/FTP).
   * **Consequence:** Guest users or eavesdroppers can intercept or access sensitive student personal and academic data, violating privacy and data protection rules.

2. **Asset:** Staff User Accounts & Credentials
   * **Vulnerability:** Weak staff passwords.
   * **Consequence:** High risk of brute-force or dictionary attacks leading to unauthorized administrative access and privilege escalation.

3. **Asset:** Central Server System Infrastructure
   * **Vulnerability:** Outdated operating system and software packages.
   * **Consequence:** Exploitation of known security vulnerabilities by external attackers, potentially leading to unauthorized remote code execution (RCE) or complete system takeover.

---

## 2. Risk Ranking
1. **Risk 1: Guest Network Access to Records Server (Rank 1 - Highest)**
   * **Reason:** High Likelihood & High Impact. Any user connected to the guest Wi-Fi/network has direct line of sight to sensitive servers without perimeter filtering.
2. **Risk 2: Weak Staff Passwords (Rank 2 - Medium/High)**
   * **Reason:** High Likelihood & Medium Impact. Weak passwords are easy targets for automated cracking scripts, compromising system integrity.
3. **Risk 3: Unencrypted File Transfers (Rank 3 - Medium)**
   * **Reason:** Medium Likelihood & Medium Impact. Data in transit can be sniffed if attackers monitor internal traffic, compromising confidentiality.

---

## 3. Recommended Controls
1. **Control for Guest Network Access:** Network segmentation and firewall traffic filtering (dropping traffic from the Guest network subnet to the Server subnet).
2. **Control for Weak Passwords:** Enforce strict password complexity policies, regular rotation, and Multi-Factor Authentication (MFA).
3. **Control for Unencrypted Transfers:** Enforce secure, encrypted transport protocols (e.g., SFTP/SSH or HTTPS with TLS/SSL).