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

1. Open Wireshark
2. Click **File**
3. Click **Import from Hex Dump...**
4. Click **Browse**
5. Choose the file `dump_firewall.txt` and click **Open**
6. Click **Import**

