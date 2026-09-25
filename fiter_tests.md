# Section 3: Network Traffic Filtering Documentation

## Firewall Setup
Commands executed on the server firewall (`iptables`):

```bash
# 1. Clear existing rules
sudo iptables -F

# 2. Keep existing established connections active
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# 3. Block Guest Network (192.168.20.0/24) from reaching the records server
sudo iptables -A INPUT -s 192.168.20.0/24 -j DROP

# 4. Permit Authorised Staff Network (192.168.10.0/24) access to SSH (Port 22)
sudo iptables -A INPUT -s 192.168.10.0/24 -p tcp --dport 22 -j ACCEPT

# 5. Block all other inbound access to SSH (Port 22)
sudo iptables -A INPUT -p tcp --dport 22 -j DROP