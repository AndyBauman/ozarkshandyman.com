# Ozarks Handyman

Static local SEO website for `ozarkshandyman.com`, targeting Springfield, Missouri and nearby Ozarks communities.

## Pages

- `/` homepage
- `/services/` plus seven service pages
- `/areas/` plus Springfield, Nixa, Ozark, Republic and Battlefield pages
- `/about/`, `/reviews/`, `/our-work/`, `/faq/`, `/contact/`, `/privacy/`

## Before Publishing

- Confirm the public contact email. The generated site currently uses `contact@ozarkshandyman.com`.
- Add real reviews only after customers provide permission.
- Replace project placeholders on `/our-work/` with real before-and-after work examples.

## GoDaddy DNS for Vercel

After deploying this folder to Vercel and adding `ozarkshandyman.com` plus `www.ozarkshandyman.com` as domains:

- Change the `A` record for `@` from `Parked` to `76.76.21.21`.
- Change the `CNAME` record for `www` to `cname.vercel-dns.com`.
- Keep GoDaddy nameservers unless you intentionally move DNS elsewhere.
- Remove conflicting parked/forwarding records if Vercel reports a conflict.

DNS can take a few minutes to 48 hours, but Vercel usually verifies quickly once the records are correct.
