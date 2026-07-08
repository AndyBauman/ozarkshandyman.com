from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SITE_URL = "https://ozarkshandyman.com"
BUSINESS_NAME = "Ozarks Handyman"
EMAIL = "contact@ozarkshandyman.com"
PRIMARY_CITY = "Springfield"
REGION = "Missouri"
SHORT_REGION = "MO"
TAGLINE = "Reliable handyman services for Springfield and the Ozarks"
AREAS = ["Springfield", "Nixa", "Ozark", "Republic", "Battlefield", "Willard", "Strafford", "Rogersville"]


@dataclass(frozen=True)
class Service:
    slug: str
    name: str
    title: str
    description: str
    intro: str
    fixes: tuple[str, ...]
    benefits: tuple[str, ...]
    faqs: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class Area:
    slug: str
    city: str
    description: str
    context: str


SERVICES = [
    Service(
        "drywall-repair",
        "Drywall Repair",
        "Drywall Repair Springfield MO | Patches, Cracks and Texture Matching",
        "Drywall repair in Springfield, Nixa, Ozark and nearby Missouri communities. Patches, cracks, nail pops, water-damage spots and texture matching.",
        "Drywall damage makes a room feel unfinished fast. We handle small wall and ceiling repairs, patch holes, clean up rough edges, and help get the surface ready for paint.",
        (
            "Small holes from doorknobs, anchors and accidents",
            "Cracks along seams and corners",
            "Ceiling stains after a resolved leak",
            "Nail pops and loose tape",
            "Texture touch-ups and paint-ready patching",
            "Rental turnover wall repairs",
            "Garage and utility room drywall damage",
        ),
        (
            "Clean patches that are made to disappear after paint",
            "Careful protection for floors and furniture",
            "Repair-first guidance before replacing large sections",
            "Fast help for move-out, listing and rental timelines",
        ),
        (
            ("Can you match existing texture?", "We can handle many common textures and will set expectations before work begins if the match may be visible."),
            ("Do I need to paint after drywall repair?", "Most drywall repairs need primer and paint after the patch dries. We can discuss paint-ready prep during the estimate."),
            ("Can you repair small holes?", "Yes. Small holes, dents, nail pops and anchor damage are exactly the kind of handyman repairs we handle."),
        ),
    ),
    Service(
        "door-repair",
        "Door Repair",
        "Door Repair Springfield MO | Interior, Exterior, Hardware and Alignment",
        "Door repair and adjustment in Springfield MO. Sticking doors, loose hinges, latches, knobs, weatherstripping and interior door fixes.",
        "A door that sticks, drags, will not latch or lets air in is more than annoying. We diagnose the cause and repair the door, hardware or frame when practical.",
        (
            "Interior doors that stick or rub",
            "Loose hinges and stripped screws",
            "Knobs, latches and strike plates",
            "Closet and pantry door adjustments",
            "Weatherstripping and draft issues",
            "Door trim and casing touch-ups",
            "Pre-hung door punch-list items",
        ),
        (
            "Practical diagnosis before replacing the door",
            "Clean hardware installation and alignment",
            "Help with both one-door fixes and whole-house lists",
            "Clear guidance when a larger carpentry repair is needed",
        ),
        (
            ("Why does my door suddenly stick?", "Seasonal humidity, settling, loose hinges or a shifted strike plate are common causes around Springfield homes."),
            ("Can you replace a doorknob or deadbolt?", "Yes. We can replace many common knobs, levers, hinges, latch sets and strike plates."),
            ("Do you install exterior doors?", "We can help with many door repairs and smaller installations. Larger structural door replacements are reviewed case by case."),
        ),
    ),
    Service(
        "fence-repair",
        "Fence Repair",
        "Fence Repair Springfield MO | Gates, Posts, Pickets and Storm Damage",
        "Fence repair in Springfield and surrounding Ozarks communities. Gates, posts, pickets, panels, hardware and storm-damage repairs.",
        "Wind, pets, wet ground and age can all wear down a fence. We focus on practical repairs that restore function, safety and curb appeal without overselling replacement.",
        (
            "Sagging gates and bad gate hardware",
            "Loose or missing pickets",
            "Leaning fence sections",
            "Damaged panels after storms",
            "Broken latches and hinges",
            "Fence board replacement",
            "Small privacy fence repairs",
        ),
        (
            "Repair-first approach when replacement is not needed",
            "Gate and latch repairs that improve daily use",
            "Matched materials when practical",
            "Clear recommendations for posts or sections past repair",
        ),
        (
            ("Can you fix a sagging gate?", "Yes. Gate repairs are common and may include hinges, latch alignment, bracing or hardware replacement."),
            ("Do you repair storm damage?", "We handle small storm-related fence repairs when the structure is safe to work on."),
            ("Will the new boards match?", "We try to match size and style, but weathered wood and new wood can look different until it ages or is stained."),
        ),
    ),
    Service(
        "deck-repair",
        "Deck Repair",
        "Deck Repair Springfield MO | Boards, Railings, Steps and Safety Fixes",
        "Deck repair in Springfield MO. Loose boards, steps, railings, fasteners, small carpentry repairs and safety punch-list items.",
        "Decks in the Ozarks deal with rain, sun, freeze-thaw cycles and heavy use. We repair common problem spots and flag safety concerns before they become bigger issues.",
        (
            "Loose deck boards",
            "Soft or damaged boards",
            "Loose railings and handrails",
            "Step and stair tread repairs",
            "Fastener replacement",
            "Small trim and skirting fixes",
            "Pre-sale deck punch-list items",
        ),
        (
            "Safety-minded inspection of visible problem areas",
            "Targeted repairs for boards, rails and steps",
            "Honest guidance when structural work is outside handyman scope",
            "Good fit for listing, move-in and maintenance lists",
        ),
        (
            ("Can you replace damaged deck boards?", "Yes. We can replace many damaged or unsafe boards when the framing is in usable condition."),
            ("Do you build new decks?", "This site is focused on handyman repairs. Full deck builds or structural rebuilds are reviewed separately."),
            ("Can you help before selling a house?", "Yes. Deck punch-list repairs are common before listing, inspections and appraisals."),
        ),
    ),
    Service(
        "punch-list",
        "Punch List Handyman",
        "Punch List Handyman Springfield MO | Move-In, Pre-Sale and Inspection Lists",
        "Punch list handyman services in Springfield MO for pre-sale repairs, move-in fixes, inspection items and small home repair lists.",
        "When the list is too small for a contractor and too long for your weekend, we can bundle repairs into one practical handyman visit.",
        (
            "Loose handles, hinges and hardware",
            "Drywall touch-ups and small wall repairs",
            "Caulk, trim and minor finish repairs",
            "Door and latch adjustments",
            "Fence, gate and deck touch-ups",
            "Small fixture and accessory installs",
            "Inspection repair lists",
        ),
        (
            "One request for several small repairs",
            "Clear priorities if the list is bigger than one visit",
            "Good fit for sellers, buyers, landlords and busy homeowners",
            "Straightforward scheduling and estimate process",
        ),
        (
            ("Can I send photos of my list?", "Yes. Photos help us understand the scope and decide whether the work fits a handyman visit."),
            ("Do you handle inspection repairs?", "We can handle many common inspection punch-list items, depending on scope and trade requirements."),
            ("Is there a minimum job size?", "Small jobs are welcome, and bundling several repairs into one visit is usually the best value."),
        ),
    ),
    Service(
        "rental-property-repairs",
        "Rental Property Repairs",
        "Rental Property Repairs Springfield MO | Turnover and Maintenance Handyman",
        "Rental property repair help in Springfield MO for landlords and property managers. Turnover fixes, drywall, doors, hardware and small maintenance lists.",
        "Vacant days cost money. We help landlords and property managers knock out practical repairs between tenants and keep small maintenance items from piling up.",
        (
            "Move-out drywall damage",
            "Door, hinge and lockset issues",
            "Loose fixtures and hardware",
            "Fence and gate repairs",
            "Deck and stair safety items",
            "Small paint-ready repairs",
            "Maintenance punch lists",
        ),
        (
            "Photo-friendly estimate process",
            "Repair lists prioritized by rent-ready impact",
            "Clear communication for owners and managers",
            "Good fit for single homes, duplexes and small portfolios",
        ),
        (
            ("Do you work with landlords?", "Yes. Rental turnover and small maintenance lists are a natural fit for handyman service."),
            ("Can you coordinate without me onsite?", "Often yes, depending on access and the work. We can discuss details before scheduling."),
            ("Do you handle urgent requests?", "Availability varies. Email us with details and we will be clear about timing."),
        ),
    ),
    Service(
        "small-home-repairs",
        "Small Home Repairs",
        "Small Home Repairs Springfield MO | No-Drama Fixes Around the House",
        "Small home repair handyman service in Springfield MO. Help with nagging repairs, maintenance lists, hardware, drywall, doors, decks and fences.",
        "Most homes have a few repairs that never make it to the top of the list. We make those small jobs easier to schedule, easier to understand and easier to finish.",
        (
            "Loose hardware and fixtures",
            "Drywall dents and holes",
            "Door and cabinet adjustments",
            "Caulk and trim touch-ups",
            "Fence and gate fixes",
            "Deck board and railing repairs",
            "General maintenance lists",
        ),
        (
            "Small jobs are taken seriously",
            "Multiple repairs can be bundled in one visit",
            "Plain-language estimates",
            "Respectful cleanup after the work",
        ),
        (
            ("What kinds of small repairs do you do?", "Common work includes drywall, doors, hardware, trim, fence gates, deck boards and general punch lists."),
            ("Can I bundle several small jobs?", "Yes. Bundling is often the best way to get more value from a handyman visit."),
            ("What if my repair needs a licensed trade?", "We will say so clearly if the work should be handled by a specialized licensed trade."),
        ),
    ),
]

AREA_DATA = [
    Area("springfield", "Springfield", "Handyman services for homeowners, landlords and property managers across Springfield, Missouri.", "Springfield homes range from older central neighborhoods to newer subdivisions, so repair needs can vary from trim and door adjustments to fence, deck and rental turnover work."),
    Area("nixa", "Nixa", "Handyman help for Nixa homeowners who need small repairs, punch lists and practical maintenance.", "Nixa's growing neighborhoods often need move-in fixes, family-home wear and tear repairs, fence gate adjustments and deck maintenance."),
    Area("ozark", "Ozark", "Home repair and handyman service for Ozark, Missouri and nearby communities.", "Ozark properties often combine suburban homes, larger lots and outdoor living spaces, making deck, fence, door and general repair lists common."),
    Area("republic", "Republic", "Reliable handyman services for Republic homeowners, sellers, buyers and rental properties.", "Republic's growth creates steady demand for move-in punch lists, pre-sale fixes, drywall repairs and routine maintenance."),
    Area("battlefield", "Battlefield", "Small home repairs and handyman punch-list help in Battlefield, Missouri.", "Battlefield homeowners often call for practical fixes around doors, decks, fences, drywall and small maintenance items."),
]


def path_for(url_path: str) -> Path:
    if url_path == "/":
        return ROOT / "index.html"
    return ROOT / url_path.strip("/") / "index.html"


def url_for(url_path: str) -> str:
    return f"{SITE_URL}{url_path if url_path == '/' else url_path.rstrip('/') + '/'}"


def nav(current: str) -> str:
    links = [
        ("/", "Home"),
        ("/services/", "Services"),
        ("/areas/", "Areas"),
        ("/our-work/", "Our Work"),
        ("/faq/", "FAQ"),
        ("/contact/", "Contact"),
    ]
    return "".join(
        f'<a href="{href}" {"aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in links
    )


def layout(
    *,
    title: str,
    description: str,
    path: str,
    h1: str,
    eyebrow: str = "Springfield MO Handyman",
    body: str,
    schema: list[dict] | None = None,
) -> str:
    canonical = url_for(path)
    schema = schema or []
    schema_json = ""
    if schema:
        import json

        schema_json = '<script type="application/ld+json">' + json.dumps(schema, indent=2) + "</script>"

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="{BUSINESS_NAME}">
  <link rel="stylesheet" href="/assets/styles.css">
  {schema_json}
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="container nav-wrap">
      <a class="brand" href="/" aria-label="{BUSINESS_NAME} home">
        <span class="brand-mark">OH</span>
        <span><strong>{BUSINESS_NAME}</strong><small>{TAGLINE}</small></span>
      </a>
      <button class="menu-button" data-menu-button aria-expanded="false" aria-controls="site-nav">Menu</button>
      <nav id="site-nav" class="site-nav" data-site-nav>{nav(path)}</nav>
      <a class="header-call" href="mailto:{EMAIL}">Email Us</a>
    </div>
  </header>

  <main id="main">
    <section class="hero">
      <div class="container hero-grid">
        <div>
          <p class="eyebrow">{escape(eyebrow)}</p>
          <h1>{escape(h1)}</h1>
          <p class="hero-copy">{escape(description)}</p>
          <div class="button-row">
            <a class="button primary" href="/contact/">Request an Estimate</a>
            <a class="button secondary" href="mailto:{EMAIL}">Email {EMAIL}</a>
          </div>
          <p class="reassurance">Free estimates. Small jobs welcome. Same-week scheduling when available.</p>
        </div>
        <aside class="hero-card" aria-label="Service promise">
          <strong>One request for the repair list.</strong>
          <p>Drywall, doors, fences, decks, punch lists, rental turnovers and small home repairs in Springfield and nearby Ozarks communities.</p>
          <ul>
            <li>Clear scope before work starts</li>
            <li>Repair-first recommendations</li>
            <li>Clean, respectful work</li>
          </ul>
        </aside>
      </div>
    </section>

    {body}
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <strong>{BUSINESS_NAME}</strong>
        <p>{TAGLINE}. Serving {", ".join(AREAS[:6])} and nearby communities.</p>
      </div>
      <div>
        <strong>Contact</strong>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div>
        <strong>Popular Services</strong>
        <p><a href="/services/drywall-repair/">Drywall Repair</a><br><a href="/services/door-repair/">Door Repair</a><br><a href="/services/punch-list/">Punch Lists</a></p>
      </div>
    </div>
    <div class="container footer-bottom">
      <span>&copy; {date.today().year} {BUSINESS_NAME}. All rights reserved.</span>
      <a href="/privacy/">Privacy</a>
    </div>
  </footer>
  <script src="/assets/site.js" defer></script>
</body>
</html>
"""


def local_business_schema(path: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": f"{SITE_URL}/#localbusiness",
        "name": BUSINESS_NAME,
        "url": SITE_URL,
        "email": EMAIL,
        "areaServed": [{"@type": "City", "name": area, "addressRegion": SHORT_REGION} for area in AREAS],
        "priceRange": "$$",
        "description": TAGLINE,
        "sameAs": [],
    }


def breadcrumb_schema(items: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": index + 1, "name": name, "item": url_for(path)}
            for index, (name, path) in enumerate(items)
        ],
    }


def faq_schema(faqs: tuple[tuple[str, str], ...]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }


def cards(items: list[str]) -> str:
    return "".join(f"<li>{escape(item)}</li>" for item in items)


def service_cards() -> str:
    return "".join(
        f"""<article class="card">
          <h3><a href="/services/{service.slug}/">{service.name}</a></h3>
          <p>{service.description}</p>
        </article>"""
        for service in SERVICES
    )


def area_links() -> str:
    return "".join(f'<a class="pill" href="/areas/{area.slug}/">{area.city}</a>' for area in AREA_DATA)


def write(path: str, html: str) -> None:
    target = path_for(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")


def home() -> None:
    body = f"""
    <section class="section">
      <div class="container trust-bar">
        <span>Small jobs welcome</span>
        <span>Free estimates</span>
        <span>Repair-first guidance</span>
        <span>Springfield service area</span>
        <span>Clean workmanship</span>
      </div>
    </section>

    <section class="section split">
      <div class="container two-col">
        <div>
          <p class="eyebrow">Why homeowners reach out</p>
          <h2>Small repairs do not stay small forever.</h2>
          <p>Loose handrails, cracked drywall, sticking doors, storm-damaged fence gates and unfinished punch lists all make a home harder to enjoy, rent or sell. {BUSINESS_NAME} helps Springfield-area homeowners knock out practical repairs before they turn into bigger problems.</p>
        </div>
        <div class="panel">
          <h3>A better handyman visit</h3>
          <ul class="check-list">
            <li>Send photos or email the repair list.</li>
            <li>Get a clear scope and straightforward estimate.</li>
            <li>Bundle several small repairs into one visit when practical.</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container section-heading">
        <p class="eyebrow">Services</p>
        <h2>Handyman services built around the real repair list.</h2>
        <p>Start with the common work homeowners, sellers, buyers, landlords and property managers need most often.</p>
      </div>
      <div class="container card-grid">{service_cards()}</div>
    </section>

    <section class="section accent">
      <div class="container two-col">
        <div>
          <p class="eyebrow">Service Area</p>
          <h2>Springfield, Missouri and surrounding Ozarks communities.</h2>
          <p>We serve Springfield first, with nearby handyman availability in Nixa, Ozark, Republic, Battlefield, Willard, Strafford, Rogersville and nearby communities depending on schedule and job scope.</p>
          <div class="pill-row">{area_links()}</div>
        </div>
        <div class="panel">
          <h3>Good-fit projects</h3>
          <ul class="check-list">
            <li>One-room or whole-house repair lists</li>
            <li>Pre-sale and move-in punch lists</li>
            <li>Rental turnover repairs</li>
            <li>Small exterior repairs after weather</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container three-steps">
        <div>
          <p class="eyebrow">How It Works</p>
          <h2>Simple from the first message.</h2>
        </div>
        <article><span>1</span><h3>Send the list</h3><p>Tell us what needs attention. Photos are helpful for drywall, doors, decks, fences and punch lists.</p></article>
        <article><span>2</span><h3>Get a clear estimate</h3><p>We confirm what fits a handyman visit and flag anything that needs a specialized trade.</p></article>
        <article><span>3</span><h3>Get it handled</h3><p>We show up with the agreed scope, work cleanly and leave you with a shorter repair list.</p></article>
      </div>
    </section>

    <section class="section cta">
      <div class="container">
        <h2>Ready to stop looking at the same repair list?</h2>
        <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> or request an estimate for handyman service in Springfield and nearby Missouri communities.</p>
        <div class="button-row centered">
          <a class="button primary" href="/contact/">Request an Estimate</a>
          <a class="button secondary light" href="mailto:{EMAIL}">Email Us</a>
        </div>
      </div>
    </section>
    """
    write(
        "/",
        layout(
            title=f"{BUSINESS_NAME} | Handyman Services in Springfield MO",
            description="Reliable handyman services in Springfield, Nixa, Ozark, Republic and nearby Missouri communities. Drywall, doors, fences, decks, punch lists and small repairs.",
            path="/",
            h1="Stop Letting Small Repairs Turn Into Big Problems",
            body=body,
            schema=[local_business_schema("/")],
        ),
    )


def services_hub() -> None:
    body = f"""
    <section class="section">
      <div class="container section-heading">
        <p class="eyebrow">Services Hub</p>
        <h2>Choose the repair category that best matches your project.</h2>
        <p>Every service page is written for practical Springfield-area repair needs, not generic contractor filler.</p>
      </div>
      <div class="container card-grid">{service_cards()}</div>
    </section>
    """
    write(
        "/services/",
        layout(
            title=f"Handyman Services Springfield MO | {BUSINESS_NAME}",
            description="Explore Springfield MO handyman services for drywall repair, door repair, fence repair, deck repair, punch lists, rental property repairs and small home repairs.",
            path="/services/",
            h1="Handyman Services in Springfield, MO",
            body=body,
            schema=[local_business_schema("/services/"), breadcrumb_schema([("Home", "/"), ("Services", "/services/")])],
        ),
    )


def service_page(service: Service) -> None:
    faq_html = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in service.faqs)
    related = "".join(
        f'<a class="pill" href="/services/{other.slug}/">{other.name}</a>'
        for other in SERVICES
        if other.slug != service.slug
    )
    body = f"""
    <section class="section">
      <div class="container two-col">
        <div>
          <p class="eyebrow">Local Repair Help</p>
          <h2>{service.name} that fits real Springfield homes.</h2>
          <p>{service.intro}</p>
        </div>
        <div class="panel">
          <h3>Common {service.name.lower()} work</h3>
          <ul class="check-list">{cards(list(service.fixes))}</ul>
        </div>
      </div>
    </section>

    <section class="section accent">
      <div class="container section-heading">
        <p class="eyebrow">Why Choose Us</p>
        <h2>Practical repairs, clear expectations.</h2>
      </div>
      <div class="container card-grid compact">{''.join(f'<article class="card"><h3>{escape(item)}</h3></article>' for item in service.benefits)}</div>
    </section>

    <section class="section">
      <div class="container two-col">
        <div>
          <p class="eyebrow">Process</p>
          <h2>How the repair visit works.</h2>
          <ol class="number-list">
            <li>Email or send photos of the issue.</li>
            <li>We confirm the likely scope and estimate range.</li>
            <li>We schedule the repair and complete the agreed work.</li>
          </ol>
        </div>
        <div class="faq-list">
          <h3>{service.name} FAQ</h3>
          {faq_html}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container section-heading">
        <p class="eyebrow">Related Services</p>
        <h2>Other handyman services people often bundle.</h2>
        <div class="pill-row centered">{related}</div>
      </div>
    </section>
    """
    path = f"/services/{service.slug}/"
    write(
        path,
        layout(
            title=service.title,
            description=service.description,
            path=path,
            h1=f"{service.name} in Springfield, MO",
            body=body,
            schema=[
                local_business_schema(path),
                {
                    "@context": "https://schema.org",
                    "@type": "Service",
                    "name": service.name,
                    "provider": {"@id": f"{SITE_URL}/#localbusiness"},
                    "areaServed": AREAS,
                    "description": service.description,
                },
                breadcrumb_schema([("Home", "/"), ("Services", "/services/"), (service.name, path)]),
                faq_schema(service.faqs),
            ],
        ),
    )


def areas_hub() -> None:
    area_cards_html = "".join(
        f"""<article class="card">
          <h3><a href="/areas/{area.slug}/">{area.city}, MO</a></h3>
          <p>{area.description}</p>
        </article>"""
        for area in AREA_DATA
    )
    body = f"""
    <section class="section">
      <div class="container section-heading">
        <p class="eyebrow">Service Areas</p>
        <h2>Local handyman help around Springfield and the Ozarks.</h2>
        <p>Location pages are focused on real local context and practical repair needs to avoid thin city-swap pages.</p>
      </div>
      <div class="container card-grid">{area_cards_html}</div>
    </section>
    """
    write(
        "/areas/",
        layout(
            title=f"Service Areas | Springfield MO Handyman | {BUSINESS_NAME}",
            description="Handyman service areas for Ozarks Handyman, including Springfield, Nixa, Ozark, Republic and Battlefield, Missouri.",
            path="/areas/",
            h1="Handyman Service Areas Near Springfield, MO",
            body=body,
            schema=[local_business_schema("/areas/"), breadcrumb_schema([("Home", "/"), ("Areas", "/areas/")])],
        ),
    )


def area_page(area: Area) -> None:
    service_pills = "".join(f'<a class="pill" href="/services/{service.slug}/">{service.name}</a>' for service in SERVICES[:6])
    body = f"""
    <section class="section">
      <div class="container two-col">
        <div>
          <p class="eyebrow">Local Service Area</p>
          <h2>Handyman service for {area.city} homes and rental properties.</h2>
          <p>{area.context}</p>
          <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> when you need help with a repair list that is too small for a general contractor and too important to ignore.</p>
        </div>
        <div class="panel">
          <h3>Popular services in {area.city}</h3>
          <div class="pill-row">{service_pills}</div>
        </div>
      </div>
    </section>
    """
    path = f"/areas/{area.slug}/"
    write(
        path,
        layout(
            title=f"Handyman {area.city} MO | Small Repairs and Punch Lists",
            description=area.description,
            path=path,
            h1=f"Handyman Services in {area.city}, MO",
            body=body,
            schema=[local_business_schema(path), breadcrumb_schema([("Home", "/"), ("Areas", "/areas/"), (area.city, path)])],
        ),
    )


def simple_page(path: str, title: str, description: str, h1: str, body: str) -> None:
    write(
        path,
        layout(
            title=title,
            description=description,
            path=path,
            h1=h1,
            body=body,
            schema=[local_business_schema(path), breadcrumb_schema([("Home", "/"), (h1, path)])],
        ),
    )


def supporting_pages() -> None:
    simple_page(
        "/about/",
        f"About {BUSINESS_NAME} | Springfield MO Handyman",
        "Learn about Ozarks Handyman, a practical handyman service for Springfield Missouri homeowners, landlords and property managers.",
        f"About {BUSINESS_NAME}",
        """
        <section class="section">
          <div class="container two-col">
            <div>
              <p class="eyebrow">Local, Practical, Repair-Focused</p>
              <h2>Built for the jobs homeowners actually need done.</h2>
              <p>Ozarks Handyman exists for the repair list that keeps getting pushed to next weekend: drywall dents, door issues, loose hardware, fence gates, deck boards, rental turnover items and inspection punch lists.</p>
              <p>The promise is simple: clear scope, practical recommendations and respectful work in Springfield and nearby Missouri communities.</p>
            </div>
            <div class="panel">
              <h3>What to expect</h3>
              <ul class="check-list">
                <li>Plain-language communication</li>
                <li>Small jobs and bundled repair lists</li>
                <li>Honest scope boundaries</li>
                <li>No fake urgency or pressure</li>
              </ul>
            </div>
          </div>
        </section>
        """,
    )
    simple_page(
        "/reviews/",
        f"Reviews | {BUSINESS_NAME}",
        "Review information for Ozarks Handyman in Springfield MO. Customer review collection page for local handyman service.",
        "Customer Reviews",
        """
        <section class="section">
          <div class="container narrow">
            <p class="eyebrow">No Fake Reviews</p>
            <h2>Real customer feedback belongs here.</h2>
            <p>This page is prepared for real reviews as they come in. Do not publish invented testimonials. Add customer feedback only when it is accurate, permissioned and tied to real work.</p>
            <div class="panel">
              <h3>Helpful review topics</h3>
              <ul class="check-list">
                <li>Was communication clear?</li>
                <li>Did the repair solve the problem?</li>
                <li>Was the work area cleaned up?</li>
                <li>Would the customer call again?</li>
              </ul>
            </div>
          </div>
        </section>
        """,
    )
    simple_page(
        "/our-work/",
        f"Our Work | Springfield MO Handyman Project Examples",
        "Examples of handyman repair work to document for Ozarks Handyman, including drywall, doors, fences, decks, rental turnovers and punch lists.",
        "Our Work",
        """
        <section class="section">
          <div class="container section-heading">
            <p class="eyebrow">Project Examples</p>
            <h2>Use this page to document real repairs.</h2>
            <p>Before-and-after examples are one of the strongest trust assets for local service businesses. Add photos and short notes after each completed project.</p>
          </div>
          <div class="container card-grid">
            <article class="card"><h3>Drywall patch and paint-ready prep</h3><p>Document hole size, room type, texture notes and final result.</p></article>
            <article class="card"><h3>Door alignment and latch repair</h3><p>Document the symptom, diagnosis and hardware adjustment.</p></article>
            <article class="card"><h3>Fence gate repair</h3><p>Document hinge, latch, bracing and usability improvements.</p></article>
          </div>
        </section>
        """,
    )
    faqs = (
        ("What handyman services do you offer?", "Common services include drywall repair, door repair, fence repair, deck repair, punch lists, rental property repairs and small home repairs."),
        ("Do you serve areas outside Springfield?", "Yes. Nearby availability includes Nixa, Ozark, Republic, Battlefield, Willard, Strafford, Rogersville and nearby communities depending on schedule and scope."),
        ("Do you take small jobs?", "Yes. Small jobs are welcome, and bundling several repairs into one visit is often the best value."),
        ("Can I send photos before scheduling?", "Yes. Photos help clarify scope and make the estimate process easier."),
        ("What work is outside handyman scope?", "Specialized electrical, plumbing, HVAC, roofing and structural work may require a licensed trade. We will flag that clearly when needed."),
        ("How do estimates work?", "Email or submit the contact form with details and photos. We confirm the scope, timing and estimate before work begins."),
    )
    faq_html = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in faqs)
    write(
        "/faq/",
        layout(
            title=f"Handyman FAQ Springfield MO | {BUSINESS_NAME}",
            description="Answers to common questions about handyman services in Springfield MO, including service areas, small jobs, estimates, photos and repair scope.",
            path="/faq/",
            h1="Handyman FAQ",
            body=f'<section class="section"><div class="container narrow faq-list">{faq_html}</div></section>',
            schema=[local_business_schema("/faq/"), breadcrumb_schema([("Home", "/"), ("FAQ", "/faq/")]), faq_schema(faqs)],
        ),
    )
    simple_page(
        "/contact/",
        f"Contact {BUSINESS_NAME} | Handyman Estimate Springfield MO",
        "Contact Ozarks Handyman for a Springfield MO handyman estimate. Email or send details about drywall, doors, fences, decks, punch lists and small repairs.",
        "Request a Handyman Estimate",
        f"""
        <section class="section">
          <div class="container two-col">
            <div>
              <p class="eyebrow">Start Here</p>
              <h2>Tell us what needs fixing.</h2>
              <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> or use the form below. Include your city, repair list, photos if available and how soon you need the work completed.</p>
              <div class="panel">
                <h3>What to include</h3>
                <ul class="check-list">
                  <li>Service address city or neighborhood</li>
                  <li>Photos of the repair area</li>
                  <li>Whether this is urgent, pre-sale, move-in or routine maintenance</li>
                  <li>Best time to reply</li>
                </ul>
              </div>
            </div>
            <form class="contact-form" action="mailto:{EMAIL}" method="post" enctype="text/plain">
              <label>Name <input name="name" autocomplete="name" required></label>
              <label>Email <input name="email" type="email" autocomplete="email" required></label>
              <label>City <input name="city" autocomplete="address-level2"></label>
              <label>Repair list <textarea name="message" rows="6" required></textarea></label>
              <button class="button primary" type="submit">Send Estimate Request</button>
            </form>
          </div>
        </section>
        """,
    )
    simple_page(
        "/privacy/",
        f"Privacy Policy | {BUSINESS_NAME}",
        "Privacy policy for Ozarks Handyman.",
        "Privacy Policy",
        f"""
        <section class="section">
          <div class="container narrow">
            <p>We collect the information you choose to send when requesting an estimate, such as your name, email, city and repair details. We use that information to respond to your request and provide handyman service communication.</p>
            <p>We do not sell personal information. If analytics or advertising tools are added later, this policy should be updated before launch.</p>
            <p>Contact: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
          </div>
        </section>
        """,
    )


def assets() -> None:
    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets" / "styles.css").write_text(
        """:root{--ink:#17211b;--muted:#5d6b62;--bg:#fbfaf5;--panel:#fff;--brand:#2e6b4f;--brand-2:#d88a34;--line:#e5e0d5;--soft:#eef5ef;--shadow:0 20px 45px rgba(23,33,27,.08)}*{box-sizing:border-box}body{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:var(--ink);background:var(--bg);line-height:1.6}a{color:inherit}img{max-width:100%}.container{width:min(1120px,calc(100% - 40px));margin-inline:auto}.skip-link{position:absolute;left:-999px;top:12px;background:#fff;padding:10px;z-index:20}.skip-link:focus{left:12px}.site-header{position:sticky;top:0;z-index:10;background:rgba(251,250,245,.94);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}.nav-wrap{display:flex;align-items:center;gap:22px;padding:14px 0}.brand{display:flex;align-items:center;gap:10px;text-decoration:none;min-width:240px}.brand-mark{display:grid;place-items:center;width:42px;height:42px;border-radius:12px;background:var(--brand);color:#fff;font-weight:800}.brand small{display:block;color:var(--muted);font-size:.78rem}.site-nav{display:flex;gap:18px;margin-left:auto}.site-nav a{text-decoration:none;color:var(--muted);font-weight:700;font-size:.94rem}.site-nav a[aria-current=page],.site-nav a:hover{color:var(--brand)}.header-call{background:var(--ink);color:#fff;text-decoration:none;padding:10px 14px;border-radius:999px;font-weight:800;white-space:nowrap}.menu-button{display:none}.hero{padding:78px 0 54px;background:linear-gradient(135deg,#f8f3e8 0%,#eef6ef 100%)}.hero-grid{display:grid;grid-template-columns:1.25fr .75fr;gap:42px;align-items:center}.eyebrow{text-transform:uppercase;letter-spacing:.12em;color:var(--brand);font-weight:900;font-size:.78rem;margin:0 0 10px}h1,h2,h3{line-height:1.1;margin:0 0 14px}h1{font-size:clamp(2.4rem,6vw,5rem);letter-spacing:-.06em;max-width:820px}h2{font-size:clamp(1.9rem,4vw,3.2rem);letter-spacing:-.04em}h3{font-size:1.2rem}.hero-copy{font-size:1.18rem;color:var(--muted);max-width:720px}.button-row{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}.button{display:inline-flex;align-items:center;justify-content:center;padding:13px 18px;border-radius:999px;font-weight:900;text-decoration:none;border:2px solid transparent;cursor:pointer;font:inherit}.primary{background:var(--brand);color:#fff}.secondary{border-color:var(--brand);color:var(--brand);background:#fff}.secondary.light{border-color:#fff;color:#fff;background:transparent}.reassurance{color:var(--muted);font-weight:700}.hero-card,.panel,.card,.contact-form{background:var(--panel);border:1px solid var(--line);border-radius:24px;padding:26px;box-shadow:var(--shadow)}.hero-card strong{font-size:1.35rem}.hero-card ul,.check-list{padding-left:0;list-style:none}.hero-card li,.check-list li{position:relative;padding-left:28px;margin:10px 0}.hero-card li:before,.check-list li:before{content:"";position:absolute;left:0;top:.45em;width:15px;height:15px;border-radius:50%;background:var(--brand-2)}.section{padding:64px 0}.section.accent{background:var(--soft)}.trust-bar{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}.trust-bar span{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px;text-align:center;font-weight:800;color:var(--brand)}.two-col{display:grid;grid-template-columns:1fr 1fr;gap:34px;align-items:start}.section-heading{max-width:760px;text-align:center}.section-heading p{color:var(--muted)}.card-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.card h3 a{text-decoration:none}.card p{color:var(--muted)}.compact .card{min-height:120px}.pill-row{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}.pill{display:inline-flex;border:1px solid var(--line);background:#fff;border-radius:999px;padding:9px 13px;text-decoration:none;font-weight:800;color:var(--brand)}.centered{justify-content:center}.three-steps{display:grid;grid-template-columns:1.1fr repeat(3,1fr);gap:18px}.three-steps article{background:#fff;border:1px solid var(--line);border-radius:20px;padding:22px}.three-steps span{display:grid;place-items:center;width:38px;height:38px;background:var(--brand);color:#fff;border-radius:50%;font-weight:900;margin-bottom:12px}.cta{background:var(--brand);color:#fff;text-align:center}.cta p{color:#e8f3eb}.number-list li{margin:12px 0}.faq-list details{background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:12px 0}.faq-list summary{cursor:pointer;font-weight:900}.narrow{max-width:820px}.contact-form{display:grid;gap:14px}.contact-form label{display:grid;gap:6px;font-weight:800}.contact-form input,.contact-form textarea{width:100%;border:1px solid var(--line);border-radius:12px;padding:12px;font:inherit;background:#fff}.site-footer{background:#111b15;color:#fff;padding:42px 0 20px}.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr;gap:28px}.footer-grid p,.footer-grid a{color:#d7ded9}.footer-bottom{border-top:1px solid rgba(255,255,255,.15);margin-top:28px;padding-top:18px;display:flex;justify-content:space-between;color:#d7ded9}@media (max-width:850px){.menu-button{display:inline-flex;margin-left:auto}.site-nav{display:none;position:absolute;left:20px;right:20px;top:72px;background:#fff;border:1px solid var(--line);border-radius:18px;padding:18px;box-shadow:var(--shadow);flex-direction:column}.site-nav.open{display:flex}.header-call{display:none}.hero-grid,.two-col,.three-steps,.footer-grid{grid-template-columns:1fr}.trust-bar,.card-grid{grid-template-columns:1fr}.nav-wrap{position:relative}.brand{min-width:0}h1{font-size:2.5rem}.section{padding:46px 0}}""",
        encoding="utf-8",
    )
    (ROOT / "assets" / "site.js").write_text(
        """const button=document.querySelector("[data-menu-button]");const nav=document.querySelector("[data-site-nav]");if(button&&nav){button.addEventListener("click",()=>{const open=nav.classList.toggle("open");button.setAttribute("aria-expanded",String(open));});}""",
        encoding="utf-8",
    )


def technical_files() -> None:
    urls = ["/", "/services/"] + [f"/services/{s.slug}/" for s in SERVICES] + ["/areas/"] + [f"/areas/{a.slug}/" for a in AREA_DATA] + ["/about/", "/reviews/", "/our-work/", "/faq/", "/contact/", "/privacy/"]
    today = date.today().isoformat()
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in urls:
        priority = "1.0" if path == "/" else "0.8"
        sitemap.append(f"  <url><loc>{url_for(path)}</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq><priority>{priority}</priority></url>")
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    (ROOT / "vercel.json").write_text('{"cleanUrls": true, "trailingSlash": true}\n', encoding="utf-8")
    (ROOT / "README.md").write_text(
        f"""# {BUSINESS_NAME}

Static local SEO website for `ozarkshandyman.com`, targeting Springfield, Missouri and nearby Ozarks communities.

## Pages

- `/` homepage
- `/services/` plus seven service pages
- `/areas/` plus Springfield, Nixa, Ozark, Republic and Battlefield pages
- `/about/`, `/reviews/`, `/our-work/`, `/faq/`, `/contact/`, `/privacy/`

## Before Publishing

- Confirm the public contact email. The generated site currently uses `{EMAIL}`.
- Add real reviews only after customers provide permission.
- Replace project placeholders on `/our-work/` with real before-and-after work examples.

## GoDaddy DNS for Vercel

After deploying this folder to Vercel and adding `ozarkshandyman.com` plus `www.ozarkshandyman.com` as domains:

- Change the `A` record for `@` from `Parked` to `76.76.21.21`.
- Change the `CNAME` record for `www` to `cname.vercel-dns.com`.
- Keep GoDaddy nameservers unless you intentionally move DNS elsewhere.
- Remove conflicting parked/forwarding records if Vercel reports a conflict.

DNS can take a few minutes to 48 hours, but Vercel usually verifies quickly once the records are correct.
""",
        encoding="utf-8",
    )


def main() -> None:
    home()
    services_hub()
    for service in SERVICES:
        service_page(service)
    areas_hub()
    for area in AREA_DATA:
        area_page(area)
    supporting_pages()
    assets()
    technical_files()


if __name__ == "__main__":
    main()
