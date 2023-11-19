import re
def extract_domain(email):
    # Match any characters after the last dot in the domain
    pattern = r"@([A-Za-z0-9.-]+)\.([A-Za-z0-9.-]+)"
    match = re.findall(pattern, email)
    domain_parts = email.split('@')[-1].split('.')
        
        # Check if there are more than one part after splitting by dot
    if len(domain_parts) > 1:
            # Take the last two parts to consider the TLD and the last subdomain
            domain = '.'.join(domain_parts[:2])
            return domain

    return '.'.join(match[0])



n = int(input())
domains = set()
for i in range(n):
    email = input() 
    if '@' in email:
        domain = extract_domain(email)
        domains.add(domain)
 

jeff =sorted(domains, reverse=True)
for domain in reversed(jeff):
    print(domain)

