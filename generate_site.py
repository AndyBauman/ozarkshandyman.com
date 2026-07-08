from __future__ import annotations

from datetime import date
from html import escape
from pathlib import Path

from content.areas import AREAS, AREA_BY_SLUG, CITY_AREAS, NEIGHBORHOOD_AREAS
from content.images import IMAGES
from content.projects import PROJECTS
from content.services import SERVICES

ROOT = Path(__file__).resolve().parent
SITE_URL = "https://ozarkshandyman.com"
BUSINESS_NAME = "Ozarks Handyman"
EMAIL = "contact@ozarkshandyman.com"
TAGLINE = "Refined handyman care for distinguished Ozarks homes"


def path_for(url_path: str) -> Path:
    if url_path == "/":
        return ROOT / "index.html"
    return ROOT / url_path.strip("/") / "index.html"


def url_for(url_path: str) -> str:
    return f"{SITE_URL}{url_path if url_path == '/' else url_path.rstrip('/') + '/'}"


def image_src(key: str) -> str:
    return IMAGES[key][0]


def image_alt(key: str) -> str:
    return IMAGES[key][1]


def nav(current: str) -> str:
    links = [
        ("/", "Home"),
        ("/services/", "Services"),
        ("/areas/", "Areas"),
        ("/our-work/", "Projects"),
        ("/faq/", "FAQ"),
        ("/contact/", "Contact"),
    ]
    return "".join(
        f'<a href="{href}" {"aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in links
    )


def img_block(image_key: str, caption: str = "") -> str:
    src, alt = IMAGES[image_key]
    cap = f"<figcaption>{escape(caption)}</figcaption>" if caption else ""
    return f'<figure class="media-block"><img src="{src}" alt="{escape(alt)}" loading="lazy" width="1200" height="800">{cap}</figure>'


def faq_html(faqs: tuple[tuple[str, str], ...]) -> str:
    return "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in faqs)


def layout(
    *,
    title: str,
    description: str,
    path: str,
    h1: str,
    eyebrow: str = "Springfield Missouri Handyman",
    body: str,
    hero_image_key: str = "ozarks_hills",
    schema: list[dict] | None = None,
) -> str:
    canonical = url_for(path)
    hero_src = image_src(hero_image_key)
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
  <meta property="og:image" content="{SITE_URL}{hero_src}">
  <meta property="og:site_name" content="{BUSINESS_NAME}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
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
      <a class="header-cta" href="/contact/">Request Estimate</a>
    </div>
  </header>

  <main id="main">
    <section class="hero hero-image" style="--hero-image: url('{hero_src}')">
      <div class="hero-overlay"></div>
      <div class="container hero-grid">
        <div class="hero-copy-block">
          <p class="eyebrow">{escape(eyebrow)}</p>
          <h1>{escape(h1)}</h1>
          <p class="hero-copy">{escape(description)}</p>
          <div class="button-row">
            <a class="button primary" href="/contact/">Request an Estimate</a>
            <a class="button secondary light" href="mailto:{EMAIL}">{EMAIL}</a>
          </div>
          <p class="reassurance">Serving Springfield, Missouri and surrounding Ozarks communities.</p>
        </div>
      </div>
    </section>

    {body}
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <strong>{BUSINESS_NAME}</strong>
        <p>{TAGLINE}. Serving {", ".join(a.label for a in CITY_AREAS[:6])} and select Springfield neighborhoods.</p>
      </div>
      <div>
        <strong>Contact</strong>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div>
        <strong>Signature Services</strong>
        <p><a href="/services/estate-maintenance/">Estate Maintenance</a><br><a href="/services/pre-sale-home-prep/">Pre-Sale Prep</a><br><a href="/services/trim-molding/">Trim &amp; Carpentry</a></p>
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


def local_business_schema() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": f"{SITE_URL}/#localbusiness",
        "name": BUSINESS_NAME,
        "url": SITE_URL,
        "email": EMAIL,
        "areaServed": [{"@type": "City", "name": area.label, "addressRegion": "MO"} for area in AREAS if area.area_type == "city"],
        "priceRange": "$$$",
        "description": TAGLINE,
        "image": f"{SITE_URL}{image_src('ozarks_hills')}",
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


def write(path: str, html: str) -> None:
    target = path_for(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")


def service_cards(limit: int | None = None) -> str:
    items = SERVICES if limit is None else SERVICES[:limit]
    return "".join(
        f"""<article class="card service-card">
          <div class="card-image" style="background-image:url('{image_src(s.image_key)}')"></div>
          <div class="card-body">
            <h3><a href="/services/{s.slug}/">{s.name}</a></h3>
            <p>{s.description}</p>
          </div>
        </article>"""
        for s in items
    )


def area_cards(areas: list) -> str:
    return "".join(
        f"""<article class="card area-card">
          <div class="card-image" style="background-image:url('{image_src(a.image_key)}')"></div>
          <div class="card-body">
            <h3><a href="/areas/{a.slug}/">{a.label}{", MO" if a.area_type == "city" else ", Springfield"}</a></h3>
            <p>{a.description}</p>
          </div>
        </article>"""
        for a in areas
    )


def home() -> None:
    cities = [a for a in AREAS if a.area_type == "city"][:8]
    neighborhoods = [a for a in AREAS if a.area_type == "neighborhood"][:8]
    body = f"""
    <section class="section">
      <div class="container trust-bar">
        <span>Refined workmanship</span>
        <span>Estate-minded service</span>
        <span>Springfield &amp; Ozarks</span>
        <span>Written estimates</span>
        <span>Discreet, tidy work</span>
      </div>
    </section>

    <section class="section split media-section">
      <div class="container two-col">
        <div>
          <p class="eyebrow">For discerning homeowners</p>
          <h2>Your home deserves repairs that respect the finish.</h2>
          <p>{BUSINESS_NAME} serves Springfield, Missouri and surrounding Ozarks communities with handyman care tailored to executive homes, pre-sale preparation, estate maintenance, and refined interior and exterior repairs.</p>
          <p>From Rountree character homes to Fremont Hills estates and growing suburbs in Nixa, Ozark, and Republic, we handle the repair list with calm precision—not contractor chaos.</p>
        </div>
        {img_block("luxury_home", "Executive homes across the Ozarks deserve careful repair work.")}
      </div>
    </section>

    <section class="section">
      <div class="container section-heading">
        <p class="eyebrow">Signature Services</p>
        <h2>Handyman services designed for higher standards.</h2>
        <p>Explore {len(SERVICES)} service pages with detailed scope, project examples, and 20+ FAQs for Springfield-area homeowners.</p>
      </div>
      <div class="container card-grid">{service_cards(9)}</div>
      <div class="container centered-action"><a class="button secondary" href="/services/">View All Services</a></div>
    </section>

    <section class="section accent media-section">
      <div class="container two-col">
        {img_block("ozarks_forest", "The Ozarks region shapes how homes age, settle, and weather over time.")}
        <div>
          <p class="eyebrow">Rooted in the Ozarks</p>
          <h2>Local knowledge for Springfield, neighborhoods, and surrounding cities.</h2>
          <p>We serve Springfield first—plus Nixa, Ozark, Republic, Battlefield, Willard, Strafford, Rogersville, Marshfield, Clever, and select neighborhoods including Rountree, Phelps Grove, Fremont Hills, Southern Hills, Del Lago, and more.</p>
          <div class="pill-row">{''.join(f'<a class="pill" href="/areas/{a.slug}/">{a.label}</a>' for a in cities[:6])}</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container section-heading">
        <p class="eyebrow">Neighborhoods</p>
        <h2>Springfield neighborhood handyman pages.</h2>
      </div>
      <div class="container card-grid compact">{area_cards(neighborhoods)}</div>
      <div class="container centered-action"><a class="button secondary" href="/areas/">Explore All Areas</a></div>
    </section>

    <section class="section cta">
      <div class="container">
        <h2>Ready for a shorter repair list?</h2>
        <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> with photos and your property location in Springfield or the surrounding Ozarks.</p>
        <div class="button-row centered">
          <a class="button primary" href="/contact/">Request an Estimate</a>
          <a class="button secondary light" href="mailto:{EMAIL}">Email Us</a>
        </div>
      </div>
    </section>
    """
    write("/", layout(title=f"{BUSINESS_NAME} | Premium Handyman Services Springfield MO", description="Premium handyman services in Springfield, Missouri and the Ozarks. Estate maintenance, pre-sale prep, drywall, trim, decks, fences, and refined home repairs.", path="/", h1="Refined Handyman Care for Distinguished Ozarks Homes", body=body, schema=[local_business_schema()]))


def services_hub() -> None:
    body = f"""
    <section class="section">
      <div class="container section-heading">
        <p class="eyebrow">Services</p>
        <h2>Comprehensive handyman services for Springfield and the Ozarks.</h2>
        <p>Each of our {len(SERVICES)} service pages includes detailed scope, project examples, local context, and 20+ FAQs.</p>
      </div>
      <div class="container card-grid">{service_cards()}</div>
    </section>
    <section class="section accent media-section"><div class="container">{img_block("craftsmanship", "Precision matters in refined Ozarks homes.")}</div></section>
    """
    write("/services/", layout(title=f"Handyman Services Springfield MO | {BUSINESS_NAME}", description="Explore premium handyman services in Springfield MO including estate maintenance, pre-sale prep, drywall, trim, decks, fences, fixtures, and more.", path="/services/", h1="Handyman Services in Springfield, Missouri", body=body, hero_image_key="craftsmanship", schema=[local_business_schema(), breadcrumb_schema([("Home", "/"), ("Services", "/services/")])]))


def service_page(service) -> None:
    projects = "".join(
        f"<article class='project-card'><h3>{escape(title)}</h3><p>{escape(service.name)} project example in the Springfield Ozarks market.</p></article>"
        for title in service.projects
    )
    related = "".join(f'<a class="pill" href="/services/{s.slug}/">{s.name}</a>' for s in SERVICES if s.slug != service.slug)
    area_pills = "".join(f'<a class="pill" href="/areas/{a.slug}/">{a.label}</a>' for a in AREAS if a.area_type == "city")
    body = f"""
    <section class="section">
      <div class="container two-col">
        <div>
          <p class="eyebrow">Service Overview</p>
          <h2>{service.name} for Springfield-area homes.</h2>
          <p>{service.intro}</p>
          <p>{service.long_copy}</p>
        </div>
        {img_block(service.image_key, f"Premium {service.name.lower()} across the Ozarks.")}
      </div>
    </section>

    <section class="section accent">
      <div class="container two-col">
        <div class="panel">
          <h3>What we repair</h3>
          <ul class="check-list">{''.join(f'<li>{escape(x)}</li>' for x in service.fixes)}</ul>
        </div>
        <div class="panel">
          <h3>Why homeowners choose us</h3>
          <ul class="check-list">{''.join(f'<li>{escape(x)}</li>' for x in service.benefits)}</ul>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container section-heading">
        <p class="eyebrow">Project Examples</p>
        <h2>Representative {service.name.lower()} projects.</h2>
      </div>
      <div class="container card-grid compact">{projects}</div>
    </section>

    <section class="section media-section">
      <div class="container two-col">
        {img_block("ozarks_forest", "Local climate and housing character inform every repair decision.")}
        <div>
          <p class="eyebrow">Local Context</p>
          <h2>{service.name} across Springfield, Nixa, Ozark, and nearby communities.</h2>
          <p>We serve homeowners in {", ".join(a.label for a in CITY_AREAS[:6])} and select Springfield neighborhoods. Email {EMAIL} with photos and your city or neighborhood for a clear estimate.</p>
          <div class="pill-row">{area_pills}</div>
        </div>
      </div>
    </section>

    <section class="section accent">
      <div class="container section-heading">
        <p class="eyebrow">FAQ</p>
        <h2>{service.name} FAQ — {len(service.faqs)} questions.</h2>
        <p>Detailed answers for homeowners researching {service.name.lower()} in Springfield, Missouri.</p>
      </div>
      <div class="container faq-grid">{faq_html(service.faqs)}</div>
    </section>

    <section class="section">
      <div class="container section-heading">
        <p class="eyebrow">Related Services</p>
        <h2>Often bundled with {service.name.lower()}.</h2>
        <div class="pill-row centered">{related}</div>
      </div>
    </section>
    """
    path = f"/services/{service.slug}/"
    write(path, layout(title=service.title, description=service.description, path=path, h1=f"{service.name} in Springfield, Missouri", body=body, hero_image_key=service.image_key, schema=[local_business_schema(), {"@context": "https://schema.org", "@type": "Service", "name": service.name, "provider": {"@id": f"{SITE_URL}/#localbusiness"}, "areaServed": [a.label for a in CITY_AREAS], "description": service.description, "image": f"{SITE_URL}{image_src(service.image_key)}"}, breadcrumb_schema([("Home", "/"), ("Services", "/services/"), (service.name, path)]), faq_schema(service.faqs)]))


def areas_hub() -> None:
    cities = [a for a in AREAS if a.area_type == "city"]
    neighborhoods = [a for a in AREAS if a.area_type == "neighborhood"]
    body = f"""
    <section class="section">
      <div class="container section-heading">
        <p class="eyebrow">Cities &amp; Communities</p>
        <h2>Handyman service areas across Springfield and the Ozarks.</h2>
        <p>{len(cities)} city pages and {len(neighborhoods)} Springfield neighborhood pages, each with local context and 20+ FAQs.</p>
      </div>
      <div class="container card-grid">{area_cards(cities)}</div>
    </section>
    <section class="section accent">
      <div class="container section-heading">
        <p class="eyebrow">Springfield Neighborhoods</p>
        <h2>Neighborhood-specific handyman pages.</h2>
      </div>
      <div class="container card-grid">{area_cards(neighborhoods)}</div>
    </section>
    <section class="section media-section"><div class="container">{img_block("ozarks_hills", "Springfield sits in the heart of the Ozarks.")}</div></section>
    """
    write("/areas/", layout(title=f"Service Areas | Springfield MO Handyman | {BUSINESS_NAME}", description="Handyman service areas including Springfield, Nixa, Ozark, Republic, Battlefield, Willard, Marshfield, Clever, and neighborhoods like Rountree, Fremont Hills, and Del Lago.", path="/areas/", h1="Handyman Service Areas in the Ozarks", body=body, hero_image_key="ozarks_hills", schema=[local_business_schema(), breadcrumb_schema([("Home", "/"), ("Areas", "/areas/")])]))


def area_page(area) -> None:
    label = f"{area.label}, MO" if area.area_type == "city" else f"{area.label}, Springfield"
    neighborhoods = "".join(f"<li>{escape(n)}</li>" for n in area.neighborhoods) if area.neighborhoods else "<li>Nearby Springfield metro neighborhoods and suburbs</li>"
    nearby = "".join(f'<a class="pill" href="/areas/{slug}/">{AREA_BY_SLUG[slug].label}</a>' for slug in area.nearby_slugs if slug in AREA_BY_SLUG)
    services = "".join(f'<a class="pill" href="/services/{s.slug}/">{s.name}</a>' for s in SERVICES[:12])
    body = f"""
    <section class="section">
      <div class="container two-col">
        <div>
          <p class="eyebrow">Local Service Area</p>
          <h2>Handyman services in {label}.</h2>
          <p>{area.intro}</p>
          <p>Homes in {area.label} often reflect {area.housing}. That shapes the repairs we see most often and the finish standards homeowners expect.</p>
        </div>
        {img_block(area.image_key, f"Handyman services in {label}.")}
      </div>
    </section>

    <section class="section accent">
      <div class="container two-col">
        <div class="panel">
          <h3>Common repairs in {area.label}</h3>
          <ul class="check-list">{''.join(f'<li>{escape(r)}</li>' for r in area.common_repairs)}</ul>
        </div>
        <div class="panel">
          <h3>Neighborhoods &amp; nearby context</h3>
          <ul class="check-list">{neighborhoods}</ul>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container section-heading">
        <p class="eyebrow">Services Available</p>
        <h2>Popular handyman services in {area.label}.</h2>
        <div class="pill-row centered">{services}</div>
      </div>
    </section>

    <section class="section media-section">
      <div class="container two-col">
        {img_block("ozarks_forest", "The Ozarks region influences the repair needs of local homes.")}
        <div>
          <p class="eyebrow">Nearby Areas</p>
          <h2>Also serving communities near {area.label}.</h2>
          <div class="pill-row">{nearby}</div>
          <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> with photos and mention {area.label} for a clear estimate.</p>
        </div>
      </div>
    </section>

    <section class="section accent">
      <div class="container section-heading">
        <p class="eyebrow">FAQ</p>
        <h2>{area.label} handyman FAQ — {len(area.faqs)} questions.</h2>
        <p>Local answers for homeowners researching handyman service in {area.label}.</p>
      </div>
      <div class="container faq-grid">{faq_html(area.faqs)}</div>
    </section>
    """
    path = f"/areas/{area.slug}/"
    write(path, layout(title=area.title, description=area.description, path=path, h1=f"Handyman Services in {label}", body=body, hero_image_key=area.image_key, schema=[local_business_schema(), breadcrumb_schema([("Home", "/"), ("Areas", "/areas/"), (area.label, path)]), faq_schema(area.faqs)]))


def supporting_pages() -> None:
    project_cards = "".join(
        f"""<article class="card project-showcase">
          <div class="card-image" style="background-image:url('{image_src(p.image_key)}')"></div>
          <div class="card-body">
            <p class="eyebrow">{escape(p.location)} · {escape(p.service)}</p>
            <h3>{escape(p.title)}</h3>
            <p>{escape(p.summary)}</p>
            <p>{escape(p.details)}</p>
          </div>
        </article>"""
        for p in PROJECTS
    )
    global_faqs = (
        ("What areas does Ozarks Handyman serve?", f"We serve {', '.join(a.label for a in CITY_AREAS)} and Springfield neighborhoods including {', '.join(a.label for a in NEIGHBORHOOD_AREAS[:8])}."),
        ("What makes Ozarks Handyman different?", "We focus on refined workmanship, clear written scope, and repairs suited to executive homes and discerning homeowners."),
        ("How do I request an estimate?", f"Email {EMAIL} with photos, your city or neighborhood, and a repair list."),
        ("Do you offer estate maintenance?", "Yes. Estate maintenance is a signature service for recurring repair lists and seasonal tune-ups."),
        ("Do you help with pre-sale repairs?", "Yes. Pre-sale home prep is a core service for listings across Springfield and the Ozarks."),
    )
    from content.faqs import area_faqs

    extra = area_faqs("springfield", "Springfield", "city", AREAS[0].neighborhoods, AREAS[0].housing)[:18]
    all_faqs = global_faqs + extra

    write("/about/", layout(title=f"About {BUSINESS_NAME} | Springfield MO Handyman", description="About Ozarks Handyman — refined handyman services for Springfield Missouri executive homes, estates, and discerning homeowners.", path="/about/", h1=f"About {BUSINESS_NAME}", hero_image_key="luxury_home", body=f"""
    <section class="section split"><div class="container two-col"><div><p class="eyebrow">Our Approach</p><h2>Calm, capable, and respectful of your home.</h2><p>Ozarks Handyman exists for homeowners who expect more than a rushed repair. We serve Springfield and the surrounding Ozarks with practical craftsmanship, written scope, and tidy job sites.</p><p>From Fremont Hills estates to Rountree bungalows and growing suburbs in Nixa and Ozark, our work is built around finish quality and clear communication.</p></div>{img_block("luxury_interior", "Details matter in executive homes.")}</div></section>
    <section class="section accent media-section"><div class="container two-col">{img_block("estate_exterior", "Ozarks estate properties deserve ongoing maintenance.")}<div><p class="eyebrow">The Ozarks</p><h2>Local homes. Local weather. Local judgment.</h2><p>Humidity, storms, seasonal temperature swings and varied housing stock across Springfield and nearby communities all influence the right repair approach.</p></div></div></section>
    """, schema=[local_business_schema(), breadcrumb_schema([("Home", "/"), ("About", "/about/")])]))

    write("/our-work/", layout(title=f"Projects | {BUSINESS_NAME}", description="Handyman project examples across Springfield MO services including estate maintenance, pre-sale prep, trim, drywall, decks, and more.", path="/our-work/", h1="Project Examples Across Our Services", hero_image_key="craftsmanship", body=f"""
    <section class="section"><div class="container section-heading"><p class="eyebrow">Projects</p><h2>{len(PROJECTS)} representative projects across our service lines.</h2><p>Real project documentation should replace or expand these examples over time.</p></div><div class="container card-grid">{project_cards}</div></section>
    <section class="section media-section"><div class="container">{img_block("deck_outdoor", "Outdoor living is central to Ozarks home life.")}</div></section>
    """, schema=[local_business_schema(), breadcrumb_schema([("Home", "/"), ("Projects", "/our-work/")])]))

    write("/faq/", layout(title=f"Handyman FAQ Springfield MO | {BUSINESS_NAME}", description="Comprehensive handyman FAQ for Springfield Missouri and the Ozarks.", path="/faq/", h1="Handyman FAQ", hero_image_key="ozarks_hills", body=f'<section class="section"><div class="container section-heading"><p class="eyebrow">FAQ</p><h2>{len(all_faqs)}+ questions</h2></div><div class="container faq-grid">{faq_html(all_faqs)}</div></section>', schema=[local_business_schema(), breadcrumb_schema([("Home", "/"), ("FAQ", "/faq/")]), faq_schema(all_faqs)]))

    write("/contact/", layout(title=f"Contact {BUSINESS_NAME}", description="Contact Ozarks Handyman for premium handyman estimates in Springfield MO. Email contact@ozarkshandyman.com with photos and your repair list.", path="/contact/", h1="Request a Handyman Estimate", hero_image_key="estate_exterior", body=f"""
    <section class="section"><div class="container two-col"><div><p class="eyebrow">Start Here</p><h2>Tell us about your home and repair list.</h2><p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> with your neighborhood, photos, and timeline.</p><ul class="check-list"><li>City or Springfield neighborhood</li><li>Photos of each repair area</li><li>Whether this is pre-sale, move-in, rental or routine maintenance</li><li>Your preferred timing</li></ul></div><form class="contact-form panel" action="mailto:{EMAIL}" method="post" enctype="text/plain"><label>Name <input name="name" required></label><label>Email <input type="email" name="email" required></label><label>City / Neighborhood <input name="city"></label><label>Repair List <textarea name="message" rows="7" required></textarea></label><button class="button primary" type="submit">Send Request</button></form></div></section>
    """, schema=[local_business_schema(), breadcrumb_schema([("Home", "/"), ("Contact", "/contact/")])]))

    write("/reviews/", layout(title=f"Reviews | {BUSINESS_NAME}", description="Customer reviews for Ozarks Handyman in Springfield MO.", path="/reviews/", h1="Customer Reviews", body='<section class="section"><div class="container narrow"><h2>Real reviews only</h2><p>Add verified customer feedback here as it becomes available. We do not publish invented testimonials.</p></div></section>', schema=[local_business_schema()]))
    write("/privacy/", layout(title="Privacy Policy", description="Privacy policy for Ozarks Handyman.", path="/privacy/", h1="Privacy Policy", body=f'<section class="section"><div class="container narrow"><p>We collect estimate request information you submit, including name, email, city, and repair details. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a></p></div></section>', schema=[local_business_schema()]))


def assets() -> None:
    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets" / "styles.css").write_text("""
:root{--ink:#101418;--muted:#5d646c;--bg:#f6f2eb;--panel:#fffdf9;--brand:#1c4a38;--gold:#b08d57;--gold-soft:#e8d4b2;--line:#e4ddd1;--soft:#eceee8;--shadow:0 28px 70px rgba(16,20,24,.11)}
*{box-sizing:border-box}body{margin:0;font-family:Manrope,ui-sans-serif,system-ui,sans-serif;color:var(--ink);background:var(--bg);line-height:1.7}
h1,h2,h3{font-family:"Cormorant Garamond",Georgia,serif;font-weight:600;letter-spacing:-.02em;line-height:1.06}
a{color:inherit}.container{width:min(1200px,calc(100% - 40px));margin-inline:auto}
.skip-link{position:absolute;left:-999px;top:12px;background:#fff;padding:10px;z-index:30}.skip-link:focus{left:12px}
.site-header{position:sticky;top:0;z-index:20;background:rgba(246,242,235,.94);backdrop-filter:blur(16px);border-bottom:1px solid var(--line)}
.nav-wrap{display:flex;align-items:center;gap:20px;padding:18px 0}.brand{display:flex;gap:12px;text-decoration:none;align-items:center}
.brand-mark{display:grid;place-items:center;width:48px;height:48px;border-radius:14px;background:linear-gradient(135deg,var(--brand),#123126);color:#fff;font-weight:800;box-shadow:var(--shadow)}
.brand small{display:block;color:var(--muted);font-size:.76rem;max-width:280px}.site-nav{display:flex;gap:18px;margin-left:auto}
.site-nav a{text-decoration:none;color:var(--muted);font-weight:700;font-size:.92rem}.site-nav a[aria-current=page],.site-nav a:hover{color:var(--brand)}
.header-cta{background:var(--ink);color:#fff;text-decoration:none;padding:12px 18px;border-radius:999px;font-weight:800;white-space:nowrap}
.menu-button{display:none}
.hero-image{position:relative;padding:132px 0 96px;background:var(--ink) center/cover no-repeat;background-image:linear-gradient(120deg,rgba(16,20,24,.82),rgba(16,20,24,.48)),var(--hero-image)}
.hero-overlay{position:absolute;inset:0;background:linear-gradient(180deg,transparent,rgba(16,20,24,.28))}
.hero-grid{position:relative;z-index:1}.hero-copy-block{max-width:780px;color:#fff}
.eyebrow{text-transform:uppercase;letter-spacing:.18em;color:var(--gold);font-weight:800;font-size:.72rem;margin:0 0 12px}
.hero-copy-block .eyebrow{color:var(--gold-soft)}.hero-copy-block h1{font-size:clamp(2.9rem,6vw,5.6rem);margin:0 0 16px}
.hero-copy{font-size:1.14rem;color:#e8e3da;max-width:700px}.reassurance{color:#d8d2c8;font-weight:600}
.button-row{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}.button{display:inline-flex;align-items:center;justify-content:center;padding:14px 22px;border-radius:999px;font-weight:800;text-decoration:none;border:2px solid transparent;cursor:pointer;font:inherit;transition:.2s ease}
.primary{background:var(--gold);color:var(--ink)}.primary:hover{filter:brightness(1.05)}.secondary{border-color:#fff;color:#fff;background:transparent}.secondary.light{border-color:#fff;color:#fff}
.section{padding:78px 0}.section.accent{background:var(--soft)}.section-heading{max-width:860px;margin:0 auto 30px;text-align:center}.section-heading p{color:var(--muted)}
.trust-bar{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}.trust-bar span{background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:18px;text-align:center;font-weight:800;color:var(--brand);box-shadow:var(--shadow)}
.two-col{display:grid;grid-template-columns:1.05fr .95fr;gap:38px;align-items:center}.panel,.card,.contact-form,.project-card,.project-showcase{background:var(--panel);border:1px solid var(--line);border-radius:26px;box-shadow:var(--shadow)}
.panel,.contact-form,.project-card{padding:28px}.card,.project-showcase{overflow:hidden}.card-body{padding:24px}.card-image{height:190px;background:center/cover no-repeat}
.service-card h3,.area-card h3,.project-showcase h3{font-size:1.55rem}.card p,.project-showcase p{color:var(--muted)}.card-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}.compact .card-image{height:150px}
.check-list{list-style:none;padding:0}.check-list li{position:relative;padding-left:28px;margin:10px 0}.check-list li:before{content:"";position:absolute;left:0;top:.55em;width:14px;height:14px;border-radius:50%;background:var(--gold)}
.media-block{margin:0;border-radius:26px;overflow:hidden;box-shadow:var(--shadow)}.media-block img{display:block;width:100%;height:auto}.media-block figcaption{padding:14px 18px;background:var(--panel);color:var(--muted);font-size:.92rem}
.pill-row{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px}.pill{display:inline-flex;border:1px solid var(--line);background:#fff;border-radius:999px;padding:10px 15px;text-decoration:none;font-weight:800;color:var(--brand)}
.centered-action{text-align:center;margin-top:26px}.centered{justify-content:center}.faq-grid details{background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:18px 20px;margin:10px 0}
.faq-grid summary{cursor:pointer;font-weight:800}.contact-form{display:grid;gap:14px}.contact-form label{display:grid;gap:6px;font-weight:700}
.contact-form input,.contact-form textarea{width:100%;border:1px solid var(--line);border-radius:12px;padding:12px;font:inherit;background:#fff}
.cta{background:linear-gradient(135deg,var(--brand),#123126);color:#fff;text-align:center}.cta p{color:#e7ece8}.narrow{max-width:820px}
.site-footer{background:var(--ink);color:#fff;padding:52px 0 24px}.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr;gap:28px}.footer-grid p,.footer-grid a{color:#d5d9de}
.footer-bottom{border-top:1px solid rgba(255,255,255,.12);margin-top:28px;padding-top:18px;display:flex;justify-content:space-between;color:#d5d9de}
@media (max-width:900px){.menu-button{display:inline-flex;margin-left:auto}.site-nav{display:none;position:absolute;left:20px;right:20px;top:76px;background:#fff;border:1px solid var(--line);border-radius:18px;padding:18px;flex-direction:column}.site-nav.open{display:flex}.header-cta{display:none}.two-col,.footer-grid,.trust-bar,.card-grid{grid-template-columns:1fr}.hero-copy-block h1{font-size:2.6rem}.section{padding:56px 0}}
""", encoding="utf-8")
    (ROOT / "assets" / "site.js").write_text("const button=document.querySelector('[data-menu-button]');const nav=document.querySelector('[data-site-nav]');if(button&&nav){button.addEventListener('click',()=>{const open=nav.classList.toggle('open');button.setAttribute('aria-expanded',String(open));});}", encoding="utf-8")


def technical_files() -> None:
    urls = ["/", "/services/"] + [f"/services/{s.slug}/" for s in SERVICES] + ["/areas/"] + [f"/areas/{a.slug}/" for a in AREAS] + ["/about/", "/reviews/", "/our-work/", "/faq/", "/contact/", "/privacy/"]
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

Premium local SEO website for `ozarkshandyman.com`, targeting Springfield, Missouri and the Ozarks.

## Scale

- {len(SERVICES)} service pages, each with 20+ FAQs and project examples
- {len([a for a in AREAS if a.area_type == "city"])} city area pages
- {len([a for a in AREAS if a.area_type == "neighborhood"])} Springfield neighborhood pages
- {len(PROJECTS)} project examples on `/our-work/`

## Regenerate

```bash
python generate_site.py
```

## Contact

Public email: `{EMAIL}`
""",
        encoding="utf-8",
    )


def main() -> None:
    home()
    services_hub()
    for service in SERVICES:
        service_page(service)
    areas_hub()
    for area in AREAS:
        area_page(area)
    supporting_pages()
    assets()
    technical_files()


if __name__ == "__main__":
    main()
