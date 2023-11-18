def extract_domains(emails):
    domains = set()
    email_count = {}
    
    for email in emails:
        # جدا کردن دامنه از ایمیل
        domain = email.split('@')[-1]
        
        # اگر این دامنه قبلاً در خروجی ظاهر نشده باشد، اضافه کن
        if domain not in email_count:
            domains.add(domain)

        # افزایش تعداد ایمیل‌های این دامنه
        email_count[domain] = email_count.get(domain, 0) + 1

    return sorted(domains,reverse=True)

def main():
    # خواندن تعداد ایمیل‌ها
    n = int(input())

    # خواندن ایمیل‌ها
    emails = []
    for _ in range(n):
        email = input()
        emails.append(email)

    # استخراج دامنه‌ها با ترتیب
    domains = extract_domains(emails)

    # چاپ دامنه‌ها
    for domain in reversed(domains):
        print(domain)

if __name__ == "__main__":
    main()
