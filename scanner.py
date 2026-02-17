# scanner.py

import socket
import threading

# List of common top 100 ports (you can expand later)
TOP_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 139, 143,
    443, 445, 3306, 3389, 8080
]

# Risk mapping dictionary
RISK_LEVELS = {
    21: "High",      # FTP
    22: "Medium",    # SSH
    23: "High",      # Telnet
    3389: "High",    # RDP
    445: "High",     # SMB
    80: "Low",
    443: "Low"
}

# Main scanning function
def scan_ports(target, start_port=None, end_port=None, mode="custom"):

    results = []   # Store scan results

    try:
        # Convert domain to IP
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        return {"error": "Invalid Host"}

    # Decide port range based on mode
    if mode == "top":
        ports = TOP_PORTS
    else:
        ports = range(start_port, end_port + 1)

    # Function to scan one port
    def scan(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)

            result = s.connect_ex((target_ip, port))

            if result == 0:

                # Try getting service name
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"

                # Get risk level
                risk = RISK_LEVELS.get(port, "Medium")

                # Append structured result
                results.append({
                    "port": port,
                    "service": service,
                    "risk": risk
                })

            s.close()

        except:
            pass

    threads = []

    # Create thread for each port
    for port in ports:
        t = threading.Thread(target=scan, args=(port,))
        threads.append(t)
        t.start()

    # Wait for all threads
    for t in threads:
        t.join()

    # Calculate overall risk score
    risk_score = 0
    for item in results:
        if item["risk"] == "High":
            risk_score += 3
        elif item["risk"] == "Medium":
            risk_score += 2
        else:
            risk_score += 1

    return {
        "results": results,
        "risk_score": risk_score
    }
