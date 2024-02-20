import socket

def reverse_dns_lookup(ip_address):
    try:
        # Perform reverse DNS lookup
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return domain_name
    except socket.herror:
        # Handle DNS resolution error
        return "DNS resolution failed"
    except Exception as e:
        # Handle other exceptions
        return str(e)

# Example usage
if __name__ == "__main__":
    ip_address = "8.8.8.8"  # Example IP address
    domain_name = reverse_dns_lookup(ip_address)
    print("Domain name:", domain_name)
