# Claude Chrome Prompts for GoDaddy DNS and Launch

Use these prompts when working in Chrome with GoDaddy, Vercel, Google Business Profile, or Search Console.

## 1. Connect GoDaddy DNS to Vercel

```text
You are helping me connect my GoDaddy domain ozarkshandyman.com to a Vercel static website.

Current GoDaddy DNS appears to have:
- A record: @ -> Parked
- NS records: ns49.domaincontrol.com and ns50.domaincontrol.com
- CNAME: email -> mailgun.org
- CNAME: www -> ozarkshandyman.com

Goal:
- Keep GoDaddy nameservers.
- Keep email-related records unless they conflict.
- Point the apex domain ozarkshandyman.com to Vercel.
- Point www.ozarkshandyman.com to Vercel.

Desired DNS records:
- A record: @ -> 76.76.21.21
- CNAME record: www -> cname.vercel-dns.com

Walk me step by step through the GoDaddy DNS screen. Tell me exactly what to click, what record to edit, what value to enter, and what not to delete.
Stop and ask before deleting any record.
```

## 2. Verify Vercel Domain Setup

```text
You are helping me verify domain setup in Vercel for ozarkshandyman.com.

Checklist:
- Confirm both ozarkshandyman.com and www.ozarkshandyman.com are added to the Vercel project.
- Confirm Vercel expects the apex A record to be 76.76.21.21.
- Confirm Vercel expects the www CNAME to be cname.vercel-dns.com.
- Identify any conflicting DNS records shown by Vercel.
- Do not change anything destructive without asking first.

Guide me through the Vercel Domains screen and tell me whether the domain is ready, pending DNS propagation, or blocked by a bad record.
```

## 3. Post-Launch SEO Setup

```text
You are helping launch local SEO for ozarkshandyman.com, a handyman service targeting Springfield, Missouri and nearby areas including Nixa, Ozark, Republic, Battlefield, Willard, Strafford, and Rogersville.

Tasks:
- Verify https://ozarkshandyman.com loads.
- Verify https://www.ozarkshandyman.com redirects or resolves correctly.
- Check that /sitemap.xml and /robots.txt load.
- Guide me through adding the domain property to Google Search Console.
- Submit https://ozarkshandyman.com/sitemap.xml.
- Check for obvious indexing, mobile, or canonical issues.

Give me clear click-by-click instructions in Chrome.
```

## 4. Google Business Profile Setup

```text
You are helping create or optimize a Google Business Profile for Ozarks Handyman.

Business:
- Name: Ozarks Handyman
- Website: https://ozarkshandyman.com
- Service area: Springfield, Missouri and nearby communities
- Services: drywall repair, door repair, fence repair, deck repair, punch-list handyman, rental property repairs, small home repairs

Important:
- Do not invent an address, license, years in business, reviews, or photos.
- Use a service-area business setup if there is no public storefront.
- Ask me for the official public contact email, business hours, service radius, and whether customers can visit a location.

Guide me through each Google Business Profile field and tell me what to enter, what to skip, and what needs owner confirmation.
```

## 5. Local Citation/NAP Consistency

```text
You are helping prepare local citation information for Ozarks Handyman.

Do not publish anything yet. First create a NAP checklist that needs owner confirmation:
- Exact business name
- Public contact email
- Public email
- Public website
- Whether there is a public address or service-area-only setup
- Service areas
- Business hours
- Primary category and secondary categories
- Short business description

Then recommend the first 10 local profiles/directories to update for Springfield, Missouri handyman SEO.
Avoid spammy directories and do not recommend fake reviews.
```
