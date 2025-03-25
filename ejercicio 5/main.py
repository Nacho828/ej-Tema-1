

from IPAddress import IPAddress
def main():
    ip_input = input("Enter an IP address: ")
    ip = IPAddress(ip_input)
    octets = ip.decompose()
    if isinstance(octets, list):
        for i, octet in enumerate(octets, start=1):
            print(f"Octet {i}: {octet}")
    else:
        print(f"Error: {octets}")

if __name__ == "__main__":
    main()