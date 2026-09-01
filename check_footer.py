import urllib.request

res = urllib.request.urlopen('https://topschoolsrankings.com/').read().decode('utf-8', errors='ignore')

print("Privacy link:", 'privacy-policy' in res)
print("Terms link:", 'terms-and-conditions' in res)
print("Contact link:", 'contact-us' in res)
print("About link:", 'about-us' in res)
