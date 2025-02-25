import os

# هدف فرضی (دامنه صرافی)
target = "example-exchange.com"

# جمع‌آوری اطلاعات دامنه با whois
print(f"Running WHOIS on {target}...")
os.system(f"whois {target} > whois_output.txt")

# اسکن پورت‌ها با nmap
print(f"Running Nmap scan on {target}...")
os.system(f"nmap -A {target} > nmap_output.txt")

print("Reconnaissance complete! Check whois_output.txt and nmap_output.txt.")
