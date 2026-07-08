# Claude Chrome Prompts for GoDaddy Changes

Copy any prompt below into Claude in Chrome while you have GoDaddy open.

---

## 1. Point Domain to Vercel (DNS Records)

```text
You are helping me update GoDaddy DNS for ozarkshandyman.com so it points to my Vercel website.

Context:
- Domain: ozarkshandyman.com
- Website is already deployed on Vercel
- Vercel project name: ozarkshandyman.com
- Site contact email on the website: contact@ozarkshandyman.com
- We are NOT using a business phone number yet

Current GoDaddy DNS (from earlier screenshots):
- A record: Name @, Value Parked
- NS records: ns49.domaincontrol.com and ns50.domaincontrol.com
- CNAME: Name email, Value mailgun.org
- CNAME: Name www, Value ozarkshandyman.com

Goal:
- Keep GoDaddy nameservers (do NOT change nameservers unless absolutely necessary)
- Point ozarkshandyman.com to Vercel
- Point www.ozarkshandyman.com to Vercel
- Keep the email CNAME to mailgun.org unless it conflicts

Required DNS changes:
- Edit A record @ from Parked to 76.76.21.21
- For www, use whichever Vercel currently recommends in the Vercel Domains screen:
  - either A record www -> 76.76.21.21
  - or CNAME www -> cname.vercel-dns.com

Instructions I need from you:
1. Tell me exactly where to click in GoDaddy: My Products > Domain > DNS > DNS Records
2. Tell me which existing record to EDIT vs ADD NEW
3. Give me the exact values for Type, Name, Value, and TTL
4. Tell me what NOT to delete
5. Stop and ask before deleting any record
6. After changes, tell me how to verify in GoDaddy and in Vercel

Work one record at a time. Wait for my confirmation after each change.
```

---

## 2. Remove Parked Page / Domain Forwarding Conflicts

```text
You are helping me remove GoDaddy parking or forwarding that may block ozarkshandyman.com from showing my Vercel site.

Domain: ozarkshandyman.com
Problem: The domain may still be parked or forwarded in GoDaddy, even after DNS changes.

Check and guide me through:
1. GoDaddy domain Overview tab — look for parking, forwarding, or "Connect Domain" settings
2. GoDaddy DNS Records — confirm @ is NOT set to Parked
3. Any domain forwarding rules on @ or www
4. Any Website Builder or old hosting products attached to the domain
5. Whether "Use My Domain" or AIRO connect options would conflict with Vercel

Tell me exactly what to turn off, disable, or edit.
Do not delete email DNS records unless they are clearly conflicting.
Ask before any destructive change.
```

---

## 3. Create Domain Email (contact@ozarkshandyman.com)

```text
You are helping me set up contact@ozarkshandyman.com in GoDaddy for my website ozarkshandyman.com.

Context:
- The live website uses contact@ozarkshandyman.com as the only public contact method
- We are not using a business phone number yet
- There is an existing DNS record: CNAME email -> mailgun.org

I need one of these solutions:
A) Create a real mailbox: contact@ozarkshandyman.com
B) Forward contact@ozarkshandyman.com to my personal inbox
C) If Mailgun is the right tool, explain how to receive mail at contact@ozarkshandyman.com through Mailgun

Please:
1. Ask me whether I want a mailbox, forwarding, or Mailgun
2. Walk me click-by-click through the correct GoDaddy screen
3. Tell me any MX or DNS records that need to be added or changed
4. Warn me if the existing email CNAME to mailgun.org will conflict
5. Tell me how to send a test email and confirm it works

Do not assume I already have GoDaddy Email purchased. Show me the cheapest/simplest option first.
```

---

## 4. Set Up Email Forwarding Only (Fastest Option)

```text
You are helping me create a simple email forward in GoDaddy:

Forward: contact@ozarkshandyman.com
To: [ask me for the destination inbox]

Domain: ozarkshandyman.com

Walk me through GoDaddy step by step:
1. Where to find Email Forwarding or Forwarding settings
2. How to create the forward for contact@
3. Whether I need to buy anything
4. Whether DNS/MX records need to change
5. How to test that mail sent to contact@ozarkshandyman.com arrives

Keep instructions simple. I am not technical.
Ask me for my destination email before proceeding.
```

---

## 5. Verify DNS Propagation After GoDaddy Changes

```text
You are helping me verify that GoDaddy DNS changes for ozarkshandyman.com worked.

Expected result:
- https://ozarkshandyman.com loads my Ozarks Handyman website (not a GoDaddy parked page)
- https://www.ozarkshandyman.com loads or redirects correctly
- https://ozarkshandyman.com/sitemap.xml loads
- https://ozarkshandyman.com/contact/ shows contact@ozarkshandyman.com

Guide me to check:
1. GoDaddy DNS Records page — confirm final record values
2. Vercel project Domains page — confirm domain status
3. Open the live URLs in Chrome
4. Use an online DNS lookup if needed

Tell me what "success" looks like vs "still propagating" vs "misconfigured."
If something is wrong, tell me the most likely fix based on what you see on screen.
```

---

## 6. Full GoDaddy Launch Checklist (Do Everything in Order)

```text
You are my launch assistant for ozarkshandyman.com in GoDaddy and Vercel.

Business: Ozarks Handyman
Website: already deployed on Vercel
Contact email needed: contact@ozarkshandyman.com
No business phone number yet

Run this as a checklist in order:
1. Update DNS so @ and www point to Vercel
2. Remove parking/forwarding conflicts
3. Set up contact@ozarkshandyman.com (mailbox or forward)
4. Verify the live site loads on ozarkshandyman.com
5. Tell me what is done, what is still pending, and what I should do next

Rules:
- Click-by-click instructions only
- One step at a time
- Ask before deleting records
- Do not change nameservers unless DNS records fail
- Stop after each major step and wait for my confirmation
```

---

## 7. Troubleshooting: Domain Still Shows Parked Page

```text
I changed GoDaddy DNS for ozarkshandyman.com but the site still shows a parked page or wrong content.

Help me troubleshoot in Chrome.

Known setup:
- Vercel IP for apex: 76.76.21.21
- Website deployed at Vercel project ozarkshandyman.com
- Previous GoDaddy A record was @ -> Parked
- Existing CNAME email -> mailgun.org

Diagnose in this order:
1. What do the current GoDaddy DNS records show?
2. Is domain forwarding still enabled?
3. Is Vercel showing the domain as verified or invalid?
4. Is this a propagation delay or a wrong record?
5. What exact record should I change next?

Give me the single most likely fix first.
```
