import re
def extract_domain(email):
    # Match any characters after the last dot in the domain
    pattern = r"@([A-Za-z0-9.-]+)\.([A-Za-z0-9.-]+)"
    match = re.findall(pattern, email)
    return '.'.join(match[0])



n = int(input())
domains = set()
for i in range(n):
    email = input()
    domain = extract_domain(email)
    domains.add(domain)

jeff =sorted(domains, reverse=True)
for domain in reversed(jeff):
    print(domain)

