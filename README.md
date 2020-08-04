# Fortigate Dump converter to Wireshark Hexdump

**Requires python >= 2.7**

## How to use

### Get some packets from Fortigate

#### In this case we're getting `1000` packets

```
printf "diagnose sniffer packet wan1 none 6 1000" | ssh USER@server.example.org | tee dump_firewall.txt
```
#### If you are using vdom

```
printf "config vdom\nedit root\ndiagnose sniffer packet wan1 none 6 1000" | ssh USER@server.example.org | tee dump_firewall.txt
```

### Converting packets from Fortigate Dump to Wireshark HexDump

1. Convert dump: `python3 fgt2wireshark.py dump_firewall.txt > dump_firewall-converted.txt`
2. Open Wireshark
3. Click **File**
4. Click **Import from Hex Dump...**
5. Click **Browse**
6. Choose the file `dump_firewall-converted.txt` and click **Open**
7. Click **Import**

