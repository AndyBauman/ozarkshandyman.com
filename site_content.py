"""Rich SEO content, service/area definitions, and FAQ builders."""

from __future__ import annotations

from dataclasses import dataclass

EMAIL = "contact@ozarkshandyman.com"
PRIMARY_CITY = "Springfield"
REGION = "Missouri"
SHORT_REGION = "MO"

CITY_AREAS = [
    "Springfield", "Nixa", "Ozark", "Republic", "Battlefield",
    "Willard", "Strafford", "Rogersville", "Marshfield", "Clever",
]

NEIGHBORHOOD_AREAS = [
    "Rountree", "Phelps Grove", "Southern Hills", "Wilson's Creek",
    "Spring Creek", "Del Lago", "Highland Springs", "Walnut Street",
]

IMAGES = {
    "hero": "/assets/images/ozarks-hills.jpg",
    "forest": "/assets/images/ozarks-forest.jpg",
    "luxury": "/assets/images/luxury-home.jpg",
    "interior": "/assets/images/luxury-interior.jpg",
    "estate": "/assets/images/estate-exterior.jpg",
    "deck": "/assets/images/deck-outdoor.jpg",
    "craft": "/assets/images/craftsmanship.jpg",
    "springfield": "/assets/images/springfield-home.jpg",
}


@dataclass(frozen=True)
class Service:
    slug: str
    name: str
    title: str
    description: str
    intro: str
    detail: str
    fixes: tuple[str, ...]
    benefits: tuple[str, ...]
    projects: tuple[tuple[str, str], ...]
    image: str
    faqs: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class Area:
    slug: str
    display_name: str
    area_type: str
    parent_city: str | None
    title: str
    description: str
    intro: str
    neighborhoods: tuple[str, ...]
    housing_notes: str
    common_repairs: tuple[str, ...]
    nearby_slugs: tuple[str, ...]
    image: str
    faqs: tuple[tuple[str, str], ...]


def _service_faqs(name: str, slug: str, keyword: str) -> tuple[tuple[str, str], ...]:
    city = PRIMARY_CITY
    areas = ", ".join(CITY_AREAS[:6])
    return (
        (f"Do you offer {keyword} in {city}, Missouri?", f"Yes. {name} is one of our core services for homeowners, estate managers, and property owners across {city} and the surrounding Ozarks."),
        (f"What neighborhoods do you serve for {keyword}?", f"We regularly serve {city} neighborhoods including Rountree, Phelps Grove, Southern Hills, Wilson's Creek, Spring Creek, Del Lago, and nearby suburbs such as Nixa, Ozark, and Republic."),
        (f"How much does {keyword} cost in {city} MO?", f"Pricing depends on scope, access, materials, and finish expectations. Email {EMAIL} with photos for a clear estimate before work begins."),
        (f"Can you handle small {keyword} jobs?", f"Yes. Discerning homeowners often hire us for focused repairs that larger contractors decline. Small jobs are welcome when bundled thoughtfully."),
        (f"Do you provide written estimates for {name.lower()}?", f"Yes. We confirm scope, timing, and estimate details by email so expectations stay clear."),
        (f"How soon can you schedule {keyword} in the Ozarks?", f"Availability varies by season and project load. Share your timeline and we will reply with realistic scheduling options."),
        (f"Can I email photos before requesting {name.lower()}?", f"Yes. Photos are strongly encouraged. They help us understand finish level, access, and whether the work fits a handyman visit."),
        (f"Do you serve Nixa and Ozark for {keyword}?", f"Yes. We serve {areas} and nearby communities depending on schedule and project scope."),
        (f"What is included in your {name.lower()} service?", f"Included work is defined in the estimate. We focus on practical repairs, careful prep, and clean results appropriate to the home."),
        (f"What is outside the scope of {name.lower()}?", f"Specialized electrical, plumbing, HVAC, structural engineering, and full replacement projects may require a licensed trade or contractor."),
        (f"Do you work with rental properties on {keyword}?", f"Yes. Landlords and property managers use us for turnover repairs, inspection items, and ongoing maintenance lists."),
        (f"Can you help with pre-sale {keyword}?", f"Yes. Pre-listing repairs are common. We prioritize visible defects, buyer-confidence items, and inspection-ready details."),
        (f"Do you protect floors and furnishings during {name.lower()}?", f"Yes. Respect for the home is part of the service. We use appropriate protection in lived-in and furnished spaces."),
        (f"Can I bundle {keyword} with other handyman repairs?", f"Yes. Bundling drywall, doors, trim, hardware, and punch-list items into one visit is often the best use of time."),
        (f"Do you work in older Springfield homes for {keyword}?", f"Yes. Many Ozarks homes include older plaster, wood trim, settled frames, and mixed materials that require careful repair judgment."),
        (f"Do you work in newer subdivisions around {city}?", f"Yes. Newer homes in Nixa, Ozark, Republic, Willard, and Springfield suburbs often need punch-list and warranty-period adjustments."),
        (f"How long does typical {keyword} take?", f"Timing depends on the repair. A single focused item may take part of a visit, while bundled lists are scheduled with a clear priority order."),
        (f"Do you offer storm-related {keyword} in the Ozarks?", f"When weather causes minor damage, we can often help with practical repairs after safety concerns are addressed."),
        (f"Why choose Ozarks Handyman for {keyword}?", f"We focus on clear communication, refined workmanship, and repairs that respect the home. No pressure, no vague scope, no contractor runaround."),
        (f"How do I request {name.lower()} in {city}?", f"Email {EMAIL} with your city or neighborhood, photos, and a short description of the repair. We reply with next steps."),
        (f"Is {keyword} available in {REGION} winter weather?", f"Yes, for many interior and weather-protected repairs. Exterior work may be rescheduled around ice, heavy rain, or unsafe conditions."),
        (f"Do you serve estate and executive homes for {keyword}?", f"Yes. We are a strong fit for homeowners who expect careful work, discretion, and tidy results in higher-end properties."),
    )


def _area_faqs(display: str, slug: str, parent: str | None, area_type: str) -> tuple[tuple[str, str], ...]:
    label = f"{display}, {SHORT_REGION}" if area_type == "city" else f"{display} in {parent}"
    nearby = "Nixa, Ozark, Republic, Battlefield, and Willard"
    return (
        (f"Do you offer handyman service in {label}?", f"Yes. Ozarks Handyman serves {label} with practical repairs, punch lists, and estate-minded maintenance."),
        (f"What services are most common in {display}?", f"Common requests include drywall repair, door adjustment, trim and hardware work, deck and fence repairs, and pre-sale punch lists."),
        (f"Do you serve both homes and rentals in {display}?", f"Yes. We work with homeowners, landlords, property managers, and sellers depending on scope."),
        (f"How do estimates work in {display}?", f"Email {EMAIL} with photos, the property city or neighborhood, and your repair list. We confirm scope and timing before scheduling."),
        (f"Can you handle small jobs in {display}?", f"Yes. Focused repairs are welcome, especially when several items are grouped into one visit."),
        (f"Do you work in nearby neighborhoods around {display}?", f"Yes. We serve surrounding Ozarks communities including {nearby}, depending on schedule."),
        (f"Do you offer pre-sale repairs in {display}?", f"Yes. Listing prep, buyer-requested fixes, and inspection punch-list items are common."),
        (f"Can you help with storm wear and seasonal maintenance in {display}?", f"Ozarks weather can affect decks, fences, caulk lines, and exterior trim. We handle many practical weather-related repairs."),
        (f"Do you serve older homes in {display}?", f"Yes. Settled frames, plaster, wood trim, and mixed materials are common in the region and require careful repair judgment."),
        (f"Do you serve newer subdivisions in {display}?", f"Yes. New construction and recent builds often need warranty-period adjustments, hardware tuning, and punch-list help."),
        (f"What should I include in an estimate request for {display}?", f"Include neighborhood, photos, finish expectations, timing, and whether the property is occupied, vacant, or a rental turnover."),
        (f"Do you bundle multiple repairs in one visit in {display}?", f"Yes. Bundling is often the most efficient approach for busy homeowners and property managers."),
        (f"Are you a good fit for executive homes in {display}?", f"We are a strong fit when homeowners expect careful communication, tidy work areas, and refined finish standards."),
        (f"Do you work with property managers in {display}?", f"Yes. Turnover repairs, recurring maintenance, and photo-based estimates are common for rental workflows."),
        (f"How quickly can you respond to requests in {display}?", f"Response time varies by season and workload. Email is the fastest way to start with photos and scope details."),
        (f"What repairs are outside handyman scope in {display}?", f"Major electrical, plumbing, HVAC, roofing, and structural work should be handled by the appropriate licensed trade."),
        (f"Do you serve {display} on weekends?", f"Scheduling depends on availability. Share your preferred timing and we will confirm options."),
        (f"Can you help with inspection repair lists in {display}?", f"Often yes, for common handyman-scope items. Send the list and photos for review."),
        (f"Why choose a local handyman for {display} instead of a large contractor?", f"Large contractors may decline small or mixed lists. We specialize in practical, multi-item repair visits."),
        (f"Do you travel to {display} from Springfield?", f"Yes. {display} is part of our standard Ozarks service area when scheduling allows."),
        (f"How do I start service in {display}?", f"Email {EMAIL} with your repair list and photos. Mention {display} in the subject or message."),
        (f"Is {display} covered for emergency repairs?", f"Availability varies. Email urgent details and we will be transparent about timing and scope."),
    )


def _svc(
    slug: str, name: str, title: str, description: str, intro: str, detail: str,
    fixes: tuple[str, ...], benefits: tuple[str, ...],
    projects: tuple[tuple[str, str], ...], image: str, keyword: str,
) -> Service:
    return Service(slug, name, title, description, intro, detail, fixes, benefits, projects, image, _service_faqs(name, slug, keyword))


SERVICES: list[Service] = [
    _svc("drywall-repair", "Drywall Repair", "Drywall Repair Springfield MO | Invisible Patches and Texture Matching",
         "Premium drywall repair in Springfield, Nixa, Ozark and the Ozarks. Holes, cracks, texture matching, ceiling stains, and paint-ready finishing.",
         "Flawless walls signal a well-kept home. We repair drywall with careful prep, texture awareness, and finish standards suited to refined interiors.",
         "Springfield-area homes—from historic Rountree bungalows to newer Nixa estates—often need drywall repairs that must disappear into the existing surface. We patch with judgment, not bulk filler.",
         ("Invisible patch repairs", "Ceiling stain remediation", "Nail pops and seam cracks", "Anchor and doorknob holes", "Orange-peel and knockdown texture", "Plaster-over-drywall transitions", "Rental turnover wall repairs", "Stairwell and tall-wall patches", "Garage-to-living transitions", "Paint-ready skim prep"),
         ("Texture matching with realistic expectations", "Furniture and floor protection", "Repair-first guidance", "Listing-ready results"),
         (("Master suite patch and paint prep", "Invisible stairwell repair before listing", "Rental turnover wall restoration"), ("Three-room patch bundle", "Ceiling stain repair after resolved leak", "Historic-home crack stabilization")),
         IMAGES["interior"], "drywall repair"),
    _svc("door-repair", "Door Repair", "Door Repair Springfield MO | Interior, Exterior and Hardware",
         "Door repair and adjustment in Springfield MO. Sticking doors, hinges, latches, weatherstripping, and hardware upgrades for refined homes.",
         "A door that drags, rattles, or fails to latch undermines comfort and security. We diagnose alignment, hardware, and seasonal movement with precision.",
         "Ozarks humidity and seasonal settling affect doors throughout Springfield, Republic, and Ozark. We tune doors to close cleanly without unnecessary replacement.",
         ("Interior door alignment", "Exterior door adjustment", "Hinge and strike plate repair", "Latch and deadbolt tuning", "Weatherstripping replacement", "Pantry and closet doors", "French door hardware", "Door trim and casing touch-ups", "Sliding door catch issues", "Whole-house door tune-ups"),
         ("Diagnosis before replacement", "Hardware expertise", "Quiet, clean closing action", "Whole-home door programs"),
         (("Whole-house hinge and latch tune-up", "Front door weather seal restoration", "Historic-home sticky door correction"), ("Interior alignment package", "Hardware upgrade with alignment", "Pre-sale door performance fixes")),
         IMAGES["luxury"], "door repair"),
    _svc("fence-repair", "Fence Repair", "Fence Repair Springfield MO | Gates, Privacy Fencing and Storm Damage",
         "Fence repair across Springfield and the Ozarks. Gates, posts, pickets, privacy fencing, and storm-damage restoration.",
         "A leaning gate or damaged privacy fence diminishes curb appeal and security. We restore function with matched materials and careful alignment.",
         "Larger lots in Ozark, Nixa, and Springfield suburbs rely on fencing for privacy. Wind, pets, and soil movement create ongoing maintenance needs.",
         ("Sagging gate correction", "Latch and hinge replacement", "Picket and panel replacement", "Post stabilization", "Storm-damage sections", "Board-on-board repairs", "Side-yard privacy fixes", "Fence cap and trim", "Hardware upgrades", "Pre-sale fence touch-ups"),
         ("Repair-first philosophy", "Gate performance focus", "Material matching", "Honest replacement guidance"),
         (("Estate gate realignment", "Storm-damaged section rebuild", "Privacy fence refresh before listing"), ("Side-yard gate repair", "Picket replacement and stain prep", "Multi-section alignment")),
         IMAGES["estate"], "fence repair"),
    _svc("deck-repair", "Deck Repair", "Deck Repair Springfield MO | Railings, Boards and Outdoor Living",
         "Deck repair in Springfield MO. Loose boards, railings, stairs, fasteners, and safety corrections for Ozarks outdoor living spaces.",
         "Decks are central to Ozarks entertaining. We repair boards, rails, and stairs with safety and appearance in mind.",
         "Freeze-thaw cycles, sun, and moisture affect decks across Springfield and surrounding communities. We address problem areas before they become structural concerns.",
         ("Loose deck boards", "Soft board replacement", "Railing tightening", "Stair tread repair", "Fastener replacement", "Deck skirting fixes", "Post cap replacement", "Gate latch alignment", "Pre-inspection safety items", "Outdoor stair handrails"),
         ("Safety-first inspection", "Targeted board replacement", "Clear structural boundaries", "Entertaining-ready results"),
         (("Outdoor dining deck restoration", "Railing safety upgrade", "Pre-listing deck punch list"), ("Board replacement on aging deck", "Stair tread repair", "Fastener refresh")),
         IMAGES["deck"], "deck repair"),
    _svc("trim-carpentry", "Trim & Carpentry Repair", "Trim Carpentry Repair Springfield MO | Baseboards, Crown and Built-In Details",
         "Trim and carpentry repair in Springfield MO. Baseboards, crown, casings, shelving, and architectural detail restoration.",
         "Architectural trim defines the character of a refined home. We repair casings, baseboards, crown, and built-in details with sharp alignment.",
         "Older Springfield neighborhoods and executive homes in Southern Hills often feature wood trim that needs careful repair rather than rough replacement.",
         ("Baseboard replacement sections", "Crown molding repair", "Window and door casing", "Chair rail and wainscoting", "Loose trim re-nailing", "Corner bead and joint cracks", "Built-in shelf repairs", "Closet trim restoration", "Stair trim and skirt boards", "Paint-ready carpentry prep"),
         ("Sharp miter alignment", "Material match awareness", "Minimal disruption", "Refined finish prep"),
         (("Crown and casing refresh in formal living room", "Baseboard repair after flooring work", "Built-in bookshelf restoration"), ("Stair trim repair", "Window casing replacement section", "Whole-room trim tune-up")),
         IMAGES["craft"], "trim carpentry repair"),
    _svc("caulking-weather-sealing", "Caulking & Weather Sealing", "Caulking Springfield MO | Windows, Baths and Exterior Sealing",
         "Caulking and weather sealing in Springfield MO. Bathrooms, kitchens, windows, doors, and exterior gaps for energy comfort.",
         "Clean caulk lines are a subtle mark of a well-maintained home. We remove failing sealant and install crisp, durable lines.",
         "Ozarks temperature swings and humidity stress caulk around tubs, windows, and siding. Refreshing sealant prevents water intrusion and drafts.",
         ("Tub and shower recaulking", "Kitchen backsplash sealing", "Window and door perimeter seal", "Siding gap sealing", "Exterior trim joints", "Sink and countertop seams", "Vent and penetration sealing", "Garage transition sealing", "Painted caulk finish prep", "Pre-sale sealant refresh"),
         ("Neat, straight lines", "Proper surface prep", "Moisture-aware product choice", "Discreet visual improvement"),
         (("Master bath silicone refresh", "Window perimeter reseal package", "Exterior trim joint restoration"), ("Kitchen caulk update", "Guest bath maintenance seal", "Pre-listing sealant polish")),
         IMAGES["interior"], "caulking and weather sealing"),
    _svc("screen-repair", "Screen Repair", "Screen Repair Springfield MO | Windows, Doors and Porch Screens",
         "Screen repair in Springfield and the Ozarks. Window screens, door screens, porch panels, and frame tune-ups.",
         "Torn screens invite pests and detract from curb appeal. We repair mesh, spline, and frames for smooth operation.",
         "Spring and summer in the Ozarks make intact screens essential. We repair porch, window, and door screens across Springfield metro homes.",
         ("Window screen rescreening", "Sliding door screens", "Porch screen panels", "Spline replacement", "Frame corner repairs", "Pet-resistant screen upgrades", "Screen door alignment", "Storm door screen inserts", "Garage passage screens", "Bulk screen refresh visits"),
         ("Clean frame alignment", "Tight mesh finish", "Seasonal readiness", "Multi-opening bundles"),
         (("Porch screen restoration", "Whole-home window screen refresh", "Sliding door screen replacement"), ("Screen door tune-up", "Second-story window screens", "Rental turnover screen repair")),
         IMAGES["estate"], "screen repair"),
    _svc("cabinet-hardware", "Cabinet & Hardware", "Cabinet Hardware Springfield MO | Adjustments, Hinges and Pulls",
         "Cabinet repair and hardware upgrades in Springfield MO. Hinges, pulls, alignment, soft-close adjustments, and kitchen touch-ups.",
         "Kitchens and baths should feel deliberate and solid. We tune cabinet doors, replace hardware, and correct alignment issues.",
         "High-end kitchens in Springfield suburbs often need hinge tuning, soft-close adjustment, and hardware refreshes rather than full remodels.",
         ("Cabinet door alignment", "Hinge replacement", "Soft-close adjustment", "Drawer glide fixes", "Pull and knob upgrades", "Touch latch correction", "Bathroom vanity adjustments", "Pantry door tuning", "Lazy susan stabilization", "Hardware template installs"),
         ("Precise alignment", "Hardware style upgrades", "Quiet close performance", "Kitchen-ready cleanup"),
         (("Kitchen hardware refresh package", "Soft-close restoration", "Bath vanity hinge repair"), ("Pantry alignment visit", "Island cabinet tune-up", "Pre-sale kitchen polish")),
         IMAGES["luxury"], "cabinet hardware repair"),
    _svc("punch-list", "Punch List Handyman", "Punch List Handyman Springfield MO | Move-In, Pre-Sale and Inspection Lists",
         "Punch list handyman services in Springfield MO for move-in, pre-sale, inspection, and estate maintenance lists.",
         "When the list is precise but too varied for a single trade, we orchestrate the repairs with clear priorities.",
         "Executive homeowners and listing agents across the Ozarks rely on punch-list help to prepare homes for market or move-in.",
         ("Move-in repair lists", "Pre-sale polish items", "Inspection response repairs", "Builder warranty punch lists", "Rental turnover lists", "Condo walkthrough items", "Hardware and trim bundles", "Drywall and paint prep items", "Door and caulk tune-ups", "Final walkthrough fixes"),
         ("One coordinated visit", "Priority-based scheduling", "Listing-aware repairs", "Clear scope boundaries"),
         (("Pre-listing whole-home punch list", "Buyer walkthrough repair bundle", "Move-in weekend list"), ("Inspection response package", "Estate turnover list", "Condo resale polish")),
         IMAGES["springfield"], "punch list handyman"),
    _svc("pre-sale-home-prep", "Pre-Sale Home Prep", "Pre-Sale Home Prep Springfield MO | Listing Repairs and Buyer Confidence",
         "Pre-sale home prep in Springfield MO. Listing repairs, buyer-confidence fixes, and inspection-ready details.",
         "Buyers notice the details. We handle the repairs that shape first impressions and smoother inspections.",
         "Springfield's competitive listing market rewards homes that show crisp trim, working hardware, and flawless touch-up areas.",
         ("Visible drywall and paint prep", "Door and hardware tune-ups", "Caulk and trim polish", "Deck and fence touch-ups", "Fixture refreshes", "Loose handle corrections", "Closet and pantry fixes", "Garage detail repairs", "Exterior curb items", "Inspection-ready adjustments"),
         ("Listing-timeline awareness", "High-impact prioritization", "Discreet workmanship", "Agent-friendly communication"),
         (("Listing week polish package", "Inspection response repairs", "Buyer-requested touch-up visit"), ("Curb appeal repair bundle", "Interior detail refresh", "Vacant-home prep")),
         IMAGES["luxury"], "pre-sale home prep"),
    _svc("estate-maintenance", "Estate Maintenance", "Estate Maintenance Springfield MO | Executive Home Care and Repair Lists",
         "Estate maintenance and executive home care in Springfield MO. Ongoing repair lists, seasonal tune-ups, and discreet service.",
         "Larger homes generate longer maintenance lists. We provide calm, organized repair service with respect for your time and property.",
         "Executive properties in Southern Hills, Del Lago, and surrounding Ozarks communities benefit from a trusted handyman partner for recurring lists.",
         ("Seasonal maintenance walkthroughs", "Recurring repair lists", "Hardware and trim tune-ups", "Drywall and caulk refresh", "Door and screen programs", "Deck and fence monitoring", "Fixture and accessory installs", "Move-in/move-out support", "Guest house punch lists", "Second-home maintenance"),
         ("Discreet, respectful service", "Multi-item efficiency", "Clear written scope", "Long-term relationship fit"),
         (("Quarterly estate tune-up", "Seasonal exterior detail visit", "Guest house refresh"), ("Whole-home hardware program", "Second-home opening checklist", "Pre-entertaining repair visit")),
         IMAGES["estate"], "estate maintenance"),
    _svc("rental-property-repairs", "Rental Property Repairs", "Rental Property Repairs Springfield MO | Turnover and Management Support",
         "Rental property repairs in Springfield MO for landlords and managers. Turnover fixes, maintenance, and photo-based estimates.",
         "Vacant days have a cost. We help owners return units to rent-ready condition efficiently.",
         "Springfield, Ozark, and Nixa rental markets move quickly when turnovers are handled with organized repair lists.",
         ("Move-out wall repairs", "Door and lock hardware", "Cabinet and vanity fixes", "Caulk and trim refresh", "Screen and fence repairs", "Deck safety items", "Fixture replacements", "Photo-based scoping", "Recurring unit maintenance", "Inspection-ready repairs"),
         ("Rent-ready prioritization", "Remote owner communication", "Photo estimates", "Portfolio-friendly workflow"),
         (("Turnover repair bundle", "Multi-unit maintenance day", "Inspection response for rental"), ("Vacant-unit polish", "Annual maintenance refresh", "Tenant damage touch-up")),
         IMAGES["springfield"], "rental property repairs"),
    _svc("storm-damage-repair", "Storm Damage Repair", "Storm Damage Repair Springfield MO | Practical Exterior and Interior Fixes",
         "Storm damage repair in the Ozarks. Fence, deck, screen, siding touch-ups, and post-weather punch lists.",
         "After Ozarks storms, small damage can linger. We handle practical repairs once safety concerns are addressed.",
         "Wind and hail often affect fences, screens, and exterior trim across Greene and Christian County homes.",
         ("Fence and gate storm repairs", "Screen and window damage", "Loose siding and trim", "Deck board replacement", "Caulk and seal failures", "Gutter and downspout fixes", "Exterior hardware checks", "Tree-impact minor repairs", "Garage door trim", "Post-storm punch lists"),
         ("Practical triage mindset", "Safety-aware scoping", "Repair before replace", "Fast photo estimates"),
         (("Post-storm fence restoration", "Screen and trim storm bundle", "Deck and railing weather repair"), ("Exterior seal refresh after weather", "Gate and latch storm fixes", "Multi-item storm punch list")),
         IMAGES["forest"], "storm damage repair"),
    _svc("fixture-installation", "Fixture & Accessory Installation", "Fixture Installation Springfield MO | Lighting, Fans and Hardware",
         "Fixture and accessory installation in Springfield MO. Lighting, ceiling fans, mirrors, bath hardware, and designer accessories.",
         "The right fixture transforms a room. We install lighting, fans, mirrors, and bath hardware with clean alignment.",
         "Updated lighting and bath hardware are high-impact upgrades in Springfield kitchens, baths, and entry spaces.",
         ("Chandelier and pendant installs", "Ceiling fan installation", "Vanity light replacement", "Mirror hanging", "Towel bar and bath hardware", "Shelving and art hanging", "Entry hardware upgrades", "Closet rod and shelf installs", "Smart thermostat mounts", "Decorative hardware installs"),
         ("Level and centered installs", "Careful wall protection", "Existing wiring boundaries respected", "Designer finish awareness"),
         (("Master bath lighting upgrade", "Entry chandelier installation", "Whole-room fan replacement"), ("Mirror and hardware package", "Kitchen pendant install", "Closet system hardware")),
         IMAGES["interior"], "fixture installation"),
    _svc("gutter-repair", "Gutter & Downspout Repair", "Gutter Repair Springfield MO | Leaks, Sagging and Drainage Fixes",
         "Gutter and downspout repair in Springfield MO. Leaks, sagging runs, loose brackets, and drainage corrections.",
         "Proper drainage protects siding, foundations, and landscaping. We repair gutters and downspouts with attention to water flow.",
         "Ozarks rainfall makes functional gutters essential. We address leaks, separations, and loose sections on many Springfield homes.",
         ("Leak sealing and joint repair", "Sagging gutter correction", "Bracket and hanger replacement", "Downspout reattachment", "Splash block alignment", "Gutter seam maintenance", "Corner and end cap repair", "Fascia attachment review", "Drainage path correction", "Pre-sale gutter tune-up"),
         ("Water-path focus", "Practical safety access", "Repair-first guidance", "Curb and foundation protection"),
         (("Gutter leak elimination visit", "Downspout reroute and reattach", "Pre-storm gutter tune-up"), ("Sagging run correction", "Corner seal refresh", "Whole-house gutter inspection")),
         IMAGES["estate"], "gutter repair"),
    _svc("tile-grout-repair", "Tile & Grout Repair", "Tile and Grout Repair Springfield MO | Bath, Kitchen and Backsplash",
         "Tile and grout repair in Springfield MO. Cracked grout, loose caulk lines, small tile replacements, and bath refresh work.",
         "Bath and kitchen surfaces should feel pristine. We repair grout, silicone, and small tile issues with neat finish lines.",
         "Master baths in higher-end Springfield homes often need grout refresh and silicone renewal rather than full retiling.",
         ("Cracked grout repair", "Silicone renewal at tub and shower", "Loose backsplash tile", "Caulk line refresh", "Grout cleaning prep", "Small tile replacement", "Shower curb seal repair", "Kitchen backsplash touch-ups", "Floor tile chip repair", "Pre-sale bath polish"),
         ("Neat joint lines", "Moisture-aware materials", "Bath-ready cleanup", "Targeted not full remodel"),
         (("Master bath grout and silicone refresh", "Kitchen backsplash tile repair", "Guest bath pre-sale polish"), ("Shower curb reseal", "Loose tile correction", "Bath hardware plus grout bundle")),
         IMAGES["luxury"], "tile and grout repair"),
    _svc("interior-paint-touchups", "Interior Paint Touch-Ups", "Interior Paint Touch-Ups Springfield MO | Walls, Trim and Ceiling Spots",
         "Interior paint touch-ups in Springfield MO. Wall spots, trim refresh, ceiling stains, and paint-ready repair finishing.",
         "Fresh paint touch-ups complete the repair story. We handle focused spots, trim refresh, and ceiling corrections.",
         "After drywall or trim repairs, paint matching determines whether the work disappears. We handle practical touch-up scope.",
         ("Wall spot touch-ups", "Trim and casing refresh", "Ceiling stain blocking", "Door paint chips", "Closet and pantry spots", "Stair and hall scuffs", "Accent wall corrections", "Nail hole and patch paint", "Cabinet paint chips", "Pre-sale paint polish"),
         ("Careful masking", "Sheen awareness", "Spot blending realism", "Furnished-room caution"),
         (("Post-repair paint blend visit", "Trim and wall refresh package", "Listing paint polish"), ("Ceiling stain cover", "Hall and stair touch-up", "Rental turnover paint spots")),
         IMAGES["interior"], "interior paint touch-ups"),
    _svc("custom-shelving", "Custom Shelving & Built-Ins", "Custom Shelving Springfield MO | Closets, Pantries and Built-In Upgrades",
         "Custom shelving and built-in upgrades in Springfield MO. Closets, pantries, laundry rooms, and garage storage improvements.",
         "Thoughtful storage elevates daily life. We install shelving, rods, brackets, and built-in improvements with level precision.",
         "Executive homes around Springfield often need pantry, closet, and mudroom storage tuning rather than full renovation.",
         ("Closet shelf and rod installs", "Pantry shelving upgrades", "Laundry room storage", "Garage shelving", "Floating shelf installs", "Mudroom locker shelves", "Wine and display shelving", "Bracket and standard installs", "Custom cut-to-fit shelves", "Storage punch-list visits"),
         ("Level, solid mounting", "Custom spacing judgment", "Clean fastener finish", "Room-appropriate design"),
         (("Walk-in closet shelving upgrade", "Pantry storage optimization", "Mudroom built-in shelves"), ("Garage storage wall", "Floating shelf feature wall", "Laundry room rebuild")),
         IMAGES["craft"], "custom shelving"),
    _svc("small-home-repairs", "Small Home Repairs", "Small Home Repairs Springfield MO | Focused Repairs for Discerning Homeowners",
         "Small home repairs in Springfield MO. Hardware, drywall, doors, trim, and mixed repair lists for homeowners who value precision.",
         "Not every repair warrants a contractor crew. We handle the precise, varied list with calm efficiency.",
         "Busy homeowners across the Ozarks use us for the repairs that linger on the list—loose handles, sticky doors, wall dents, and more.",
         ("Loose handles and hinges", "Drywall dents and holes", "Door and cabinet adjustments", "Caulk and trim touch-ups", "Fence and gate fixes", "Deck board repairs", "Picture and mirror hanging", "Shelving installs", "Minor leak stain prep", "Mixed maintenance lists"),
         ("Small jobs taken seriously", "Bundled efficiency", "Clear estimates", "Respectful cleanup"),
         (("Weekend list clearance visit", "New homeowner tune-up", "Seasonal maintenance bundle"), ("Condo repair list", "Townhome punch list", "Retiree home safety tweaks")),
         IMAGES["springfield"], "small home repairs"),
]


def _area(
    slug: str, display: str, area_type: str, parent: str | None,
    description: str, intro: str, neighborhoods: tuple[str, ...],
    housing: str, repairs: tuple[str, ...], nearby: tuple[str, ...], image: str,
) -> Area:
    title = f"Handyman {display} MO | Estate Repairs and Home Maintenance" if area_type == "city" else f"Handyman {display} {parent} MO | Neighborhood Home Repairs"
    return Area(slug, display, area_type, parent, title, description, intro, neighborhoods, housing, repairs, nearby, image, _area_faqs(display, slug, parent, area_type))


AREAS: list[Area] = [
    _area("springfield", "Springfield", "city", None,
          "Premium handyman services in Springfield, Missouri for executive homes, rentals, and pre-sale repairs across the Ozarks metro.",
          "Springfield is the anchor of our service area. From historic neighborhoods near downtown to executive subdivisions in the south metro, homes here span Craftsman bungalows, mid-century ranches, and newer luxury builds—all with different repair rhythms.",
          ("Rountree", "Phelps Grove", "Southern Hills", "Wilson's Creek", "Spring Creek", "Del Lago", "Highland Springs", "Walnut Street", "Tom Watkins", "Seminole Hollow"),
          "Springfield housing mixes historic character homes, established mid-century neighborhoods, and newer executive subdivisions with larger outdoor living spaces.",
          ("Whole-house punch lists", "Pre-sale polish repairs", "Door and hardware tune-ups", "Drywall and trim restoration", "Deck and fence maintenance", "Rental turnover repairs", "Storm-related touch-ups", "Estate seasonal maintenance", "Cabinet and bath hardware", "Screen and caulk refresh"),
          ("nixa", "ozark", "republic", "battlefield", "rountree"), IMAGES["springfield"]),
    _area("nixa", "Nixa", "city", None,
          "Handyman services in Nixa, Missouri for family homes, executive subdivisions, and rental properties.",
          "Nixa has grown into one of the most active suburban markets around Springfield. Family homes, larger lots, and outdoor living spaces create steady demand for deck, fence, trim, and punch-list help.",
          ("North Nixa", "Fremont Hills", "Highlandville corridor"),
          "Nixa features newer subdivisions, family neighborhoods, and larger lots with decks, fences, and multi-area maintenance lists.",
          ("Move-in punch lists", "Deck and fence repairs", "Drywall and paint touch-ups", "Cabinet hardware tuning", "Garage and storage shelving", "Rental turnover repairs", "Storm damage touch-ups", "Screen replacement", "Caulk and weather sealing", "Pre-sale repairs"),
          ("springfield", "ozark", "republic", "battlefield"), IMAGES["luxury"]),
    _area("ozark", "Ozark", "city", None,
          "Handyman services in Ozark, Missouri for suburban homes, larger lots, and outdoor living repairs.",
          "Ozark homeowners often juggle fence, deck, screen, and interior punch-list needs across larger properties. We help prioritize what matters most for comfort, resale, and rental performance.",
          ("Downtown Ozark", "North Ozark", "Finley Creek area"),
          "Ozark combines suburban homes, acreage properties, and outdoor-focused living that wears on decks, fences, and exterior trim.",
          ("Deck and railing repairs", "Fence and gate fixes", "Screen porch repairs", "Interior punch lists", "Rental maintenance", "Storm damage repairs", "Shelving and storage installs", "Door and trim tuning", "Gutter repairs", "Pre-sale polish"),
          ("springfield", "nixa", "republic", "battlefield"), IMAGES["deck"]),
    _area("republic", "Republic", "city", None,
          "Handyman services in Republic, Missouri for growing subdivisions, rentals, and move-in repair lists.",
          "Republic's expansion brings steady demand for warranty-period adjustments, move-in lists, and pre-sale repairs. We serve homeowners who want precise work without contractor overhead.",
          ("Brookline", "Republic west subdivisions"),
          "Republic includes fast-growing subdivisions, family homes, and a strong base of move-in and pre-sale repair needs.",
          ("Move-in repairs", "Builder punch lists", "Drywall and trim fixes", "Hardware installs", "Fence and deck touch-ups", "Rental turnovers", "Caulk and seal refresh", "Fixture installs", "Closet shelving", "Inspection repairs"),
          ("springfield", "nixa", "ozark", "battlefield"), IMAGES["estate"]),
    _area("battlefield", "Battlefield", "city", None,
          "Handyman services in Battlefield, Missouri for suburban home repairs and maintenance lists.",
          "Battlefield homeowners often need practical help with doors, trim, drywall, and exterior wear—especially where family traffic meets Missouri weather.",
          ("Battlefield subdivisions", "Nearby Springfield south metro"),
          "Battlefield features suburban family housing with routine maintenance, punch-list, and pre-sale repair demand.",
          ("Door adjustments", "Drywall repairs", "Fence gate fixes", "Deck maintenance", "Interior hardware", "Caulk refresh", "Screen repairs", "Pre-sale polish", "Rental touch-ups", "Storm repairs"),
          ("springfield", "republic", "nixa", "ozark"), IMAGES["springfield"]),
    _area("willard", "Willard", "city", None,
          "Handyman services in Willard, Missouri for family homes, rentals, and rural-suburban repair lists.",
          "Willard combines suburban convenience with a slightly rural feel. Exterior wear, decks, fences, and seasonal maintenance are common requests.",
          ("Willard schools area", "North Willard"),
          "Willard includes family neighborhoods and rural-suburban properties with exterior maintenance needs.",
          ("Deck repairs", "Fence fixes", "Storm touch-ups", "Drywall and trim", "Rental repairs", "Shelving installs", "Door tune-ups", "Gutter repairs", "Screen replacement", "Punch lists"),
          ("springfield", "republic", "nixa", "ozark"), IMAGES["forest"]),
    _area("strafford", "Strafford", "city", None,
          "Handyman services in Strafford, Missouri for homes, rentals, and country-suburban maintenance.",
          "Strafford homeowners value dependable help with mixed repair lists that do not fit neatly into one trade.",
          ("Strafford area neighborhoods"),
          "Strafford features country-suburban homes with exterior and interior maintenance lists.",
          ("Fence repairs", "Deck boards", "Interior punch lists", "Rental turnovers", "Door repairs", "Drywall patches", "Fixture installs", "Storm repairs", "Caulk sealing", "Shelving"),
          ("springfield", "willard", "nixa", "ozark"), IMAGES["forest"]),
    _area("rogersville", "Rogersville", "city", None,
          "Handyman services in Rogersville, Missouri for suburban homes and maintenance-heavy repair lists.",
          "Rogersville's growth has increased demand for move-in, pre-sale, and family-home maintenance support.",
          ("Rogersville subdivisions"),
          "Rogersville includes newer suburban housing with punch-list and exterior maintenance needs.",
          ("Move-in lists", "Pre-sale repairs", "Deck and fence fixes", "Drywall touch-ups", "Hardware installs", "Rental repairs", "Storm damage", "Trim repairs", "Screen fixes", "Fixture installs"),
          ("springfield", "nixa", "ozark", "republic"), IMAGES["luxury"]),
    _area("marshfield", "Marshfield", "city", None,
          "Handyman services in Marshfield, Missouri for homes and properties west of the Springfield metro.",
          "Marshfield extends our reach for homeowners who want the same refined repair approach outside the immediate metro core.",
          ("Marshfield area"),
          "Marshfield includes established homes and rural-suburban properties with seasonal maintenance needs.",
          ("Exterior repairs", "Deck and fence work", "Interior punch lists", "Storm touch-ups", "Door repairs", "Drywall patches", "Shelving", "Fixture installs", "Rental repairs", "Gutter fixes"),
          ("springfield", "willard", "strafford", "nixa"), IMAGES["forest"]),
    _area("clever", "Clever", "city", None,
          "Handyman services in Clever, Missouri for suburban and rural-suburban home repair lists.",
          "Clever homeowners often need practical mixed repairs across interior and exterior spaces.",
          ("Clever area neighborhoods"),
          "Clever features smaller-community housing with exterior wear and family-home maintenance needs.",
          ("Fence and deck repairs", "Drywall and trim", "Door adjustments", "Storm repairs", "Shelving installs", "Rental touch-ups", "Fixture installs", "Screen repair", "Caulk refresh", "Punch lists"),
          ("nixa", "springfield", "ozark", "republic"), IMAGES["forest"]),
    _area("rountree", "Rountree", "neighborhood", "Springfield",
          "Handyman services in Rountree, Springfield MO for historic homes, rentals, and careful interior repairs.",
          "Rountree is one of Springfield's most character-rich neighborhoods. Craftsman details, plaster walls, wood trim, and older doors reward careful repair work instead of rough patches.",
          tuple(),
          "Historic Craftsman and bungalow homes with wood trim, plaster, older doors, and mature landscaping.",
          ("Plaster and drywall patches", "Door and trim repairs", "Historic hardware tuning", "Porch and screen fixes", "Rental turnover repairs", "Pre-sale polish", "Interior paint touch-ups", "Shelving and storage", "Fence gate repairs", "Inspection punch lists"),
          ("springfield", "phelps-grove", "southern-hills"), IMAGES["springfield"]),
    _area("phelps-grove", "Phelps Grove", "neighborhood", "Springfield",
          "Handyman services in Phelps Grove, Springfield MO for established homes near MSU and mature neighborhoods.",
          "Phelps Grove combines owner-occupied homes, rentals, and long-held properties that need practical maintenance with a tidy finish.",
          tuple(),
          "Established neighborhood housing with rentals, owner-occupied homes, and mature exterior features.",
          ("Rental turnover repairs", "Drywall and trim", "Door adjustments", "Screen repairs", "Deck maintenance", "Fixture installs", "Pre-sale polish", "Caulk refresh", "Hardware upgrades", "Punch lists"),
          ("springfield", "rountree", "southern-hills"), IMAGES["luxury"]),
    _area("southern-hills", "Southern Hills", "neighborhood", "Springfield",
          "Handyman services in Southern Hills, Springfield MO for executive homes and upscale maintenance lists.",
          "Southern Hills is known for larger homes and refined expectations. We handle detailed punch lists, hardware upgrades, and exterior maintenance with discretion.",
          tuple(),
          "Upscale mid-century and executive homes with larger interiors and higher finish expectations.",
          ("Estate maintenance lists", "Hardware and fixture upgrades", "Deck and fence care", "Drywall and paint touch-ups", "Cabinet tuning", "Pre-sale polish", "Storm repairs", "Custom shelving", "Screen and caulk refresh", "Whole-home tune-ups"),
          ("springfield", "del-lago", "wilson-creek"), IMAGES["estate"]),
    _area("wilson-creek", "Wilson's Creek", "neighborhood", "Springfield",
          "Handyman services in Wilson's Creek area, Springfield MO for suburban homes and mixed repair lists.",
          "The Wilson's Creek area includes family neighborhoods where decks, fences, and interior wear create steady handyman demand.",
          tuple(),
          "Suburban family housing with outdoor living spaces and routine maintenance needs.",
          ("Deck repairs", "Fence gates", "Interior punch lists", "Drywall patches", "Door tune-ups", "Storm repairs", "Fixture installs", "Rental touch-ups", "Gutter fixes", "Shelving"),
          ("springfield", "southern-hills", "republic"), IMAGES["deck"]),
    _area("spring-creek", "Spring Creek", "neighborhood", "Springfield",
          "Handyman services in Spring Creek, Springfield MO for newer homes and warranty-period adjustments.",
          "Spring Creek area homes often need builder punch-list help, hardware tuning, and move-in adjustments.",
          tuple(),
          "Newer subdivisions and family homes with punch-list and move-in repair needs.",
          ("Move-in punch lists", "Hardware installs", "Drywall touch-ups", "Cabinet adjustments", "Caulk and trim", "Shelving installs", "Fence and deck touch-ups", "Fixture installs", "Pre-sale polish", "Inspection items"),
          ("springfield", "republic", "nixa"), IMAGES["luxury"]),
    _area("del-lago", "Del Lago", "neighborhood", "Springfield",
          "Handyman services in Del Lago, Springfield MO for executive homes and refined repair standards.",
          "Del Lago homeowners often expect discretion, neat job sites, and careful finish work across mixed repair lists.",
          tuple(),
          "Executive subdivision homes with higher finish standards and larger maintenance lists.",
          ("Estate maintenance", "Fixture and hardware upgrades", "Deck and fence care", "Interior paint touch-ups", "Cabinet tuning", "Custom shelving", "Pre-sale polish", "Storm repairs", "Screen and caulk refresh", "Whole-home tune-ups"),
          ("springfield", "southern-hills", "wilson-creek"), IMAGES["estate"]),
    _area("highland-springs", "Highland Springs", "neighborhood", "Springfield",
          "Handyman services in Highland Springs, Springfield MO for family homes and suburban repair lists.",
          "Highland Springs area properties benefit from bundled repair visits that cover doors, drywall, trim, and exterior wear.",
          tuple(),
          "Family suburban housing with routine maintenance and move-in repair needs.",
          ("Move-in repairs", "Door adjustments", "Drywall patches", "Fence gate fixes", "Deck maintenance", "Fixture installs", "Rental touch-ups", "Shelving", "Caulk refresh", "Punch lists"),
          ("springfield", "nixa", "republic"), IMAGES["springfield"]),
    _area("walnut-street", "Walnut Street", "neighborhood", "Springfield",
          "Handyman services in the Walnut Street area, Springfield MO for historic and central-city homes.",
          "Central Springfield neighborhoods near Walnut Street often feature older homes where careful trim, door, and drywall work matters.",
          tuple(),
          "Older central-city homes with wood trim, varied materials, and rental and owner-occupied mix.",
          ("Historic trim repairs", "Plaster and drywall", "Door and hardware", "Rental turnovers", "Pre-sale polish", "Screen repairs", "Fixture installs", "Interior paint touch-ups", "Porch repairs", "Inspection lists"),
          ("springfield", "rountree", "phelps-grove"), IMAGES["springfield"]),
]

AREA_BY_SLUG = {a.slug: a for a in AREAS}
