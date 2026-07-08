from __future__ import annotations


def service_faqs(slug: str, name: str, city: str = "Springfield") -> tuple[tuple[str, str], ...]:
    specific = {
        "drywall-repair": [
            (f"How much does drywall repair cost in {city}?", f"Drywall repair pricing in {city} depends on hole size, ceiling vs wall work, texture matching and access. Small patches are often far less than full sheet replacement. Email photos for a clearer estimate."),
            ("Can you repair ceiling drywall?", "Yes. Ceiling patches, nail pops, tape separation and stain areas after resolved leaks are common requests."),
            ("Do you handle orange peel or knockdown texture?", "Many common residential textures can be matched or blended. We set expectations upfront when a perfect invisible match may not be realistic."),
            ("Should drywall be repaired before painting?", "Usually yes. Paint highlights uneven patches, so repair and primer prep should come first for a refined finish."),
            ("Can you repair drywall in rentals?", "Yes. Move-out holes, anchor damage and tenant wear are common turnover repairs."),
            ("How long does a drywall patch take?", "Small patches may be completed in one visit. Larger texture blending or ceiling work may need additional drying time."),
            ("Do you fix cracks that keep coming back?", "Recurring cracks may signal movement or loose tape. We repair the visible damage and explain when a structural or moisture issue should be addressed separately."),
            ("Can you patch around electrical boxes or vents?", "Yes, as part of a handyman scope when the surrounding drywall is the primary issue."),
        ],
        "door-repair": [
            (f"Why do doors stick in {city} homes?", "Humidity swings, seasonal expansion, settling foundations and loose hinges are common in the Ozarks climate."),
            ("Can you fix a door that will not latch?", "Often yes. Strike plate alignment, hinge adjustment and latch hardware are common fixes."),
            ("Do you replace interior door hardware?", "We can replace many knobs, levers, hinges and latch sets as part of a door repair visit."),
            ("Can you adjust patio or exterior doors?", "Many alignment and weatherseal issues can be improved. Full structural door replacement is reviewed case by case."),
            ("Do you repair bi-fold or closet doors?", "Yes. Track, pivot and alignment issues on closet and pantry doors are common handyman work."),
            ("Can you fix a dragging exterior door?", "We can often improve operation through hinge, threshold and weatherstrip adjustments."),
            ("Will you repair door trim at the same time?", "Minor casing and trim touch-ups can often be bundled with door repair work."),
            ("Can you help with a whole-house door tune-up?", "Yes. Multiple sticking doors are a strong fit for a bundled handyman visit."),
        ],
        "fence-repair": [
            (f"Can you repair wood privacy fences in {city}?", "Yes. Pickets, rails, posts and gate hardware are common fence repairs around Springfield-area homes."),
            ("Do you replace individual fence boards?", "Yes, when the surrounding structure is sound and a repair-first approach makes sense."),
            ("Can you fix a gate that will not close?", "Gate repairs are one of the most common fence requests and may include hinges, latches or bracing."),
            ("Do you repair storm-damaged fence sections?", "We handle smaller storm-related fence repairs when the structure is safe to work on."),
            ("Will new boards match old weathered wood?", "We match size and style when possible, but new wood can look different until it weathers or is stained."),
            ("Can you reinforce a leaning fence post?", "Some leaning sections can be improved with bracing or targeted post work. Severely rotted posts may need replacement."),
            ("Do you repair chain-link gates?", "Our focus is wood and mixed residential fence repairs. Chain-link scope is reviewed case by case."),
            ("Can fence repair be bundled with deck work?", "Yes. Exterior punch lists often combine fence gates, deck boards and small carpentry items."),
        ],
        "deck-repair": [
            (f"How do Ozarks weather cycles affect decks in {city}?", "Rain, sun, freeze-thaw cycles and heavy seasonal use wear boards, railings and fasteners over time."),
            ("Can you replace unsafe deck boards?", "Yes, when the underlying framing is serviceable and a targeted repair is the right approach."),
            ("Do you tighten loose deck railings?", "Loose railings and handrails are priority safety items we commonly address."),
            ("Can you repair deck stairs?", "Tread, stringer and railing repairs on stairs are common pre-sale and maintenance requests."),
            ("Do you rebuild entire decks?", "This service focuses on repair and punch-list work. Full deck construction is reviewed separately."),
            ("Can you help before a home inspection?", "Yes. Deck safety and visible defect repairs are common inspection-list items."),
            ("Do you replace popped deck screws or nails?", "Fastener replacement and board re-securing are routine deck maintenance tasks."),
            ("Can deck repairs be combined with exterior caulking?", "Often yes. Exterior maintenance lists frequently combine deck, caulk and trim touch-ups."),
        ],
        "punch-list": [
            (f"What belongs on a handyman punch list in {city}?", "Hardware, drywall touch-ups, door adjustments, caulk, trim, fixtures, fence gates and small exterior items are common."),
            ("Can you help with a pre-listing punch list?", "Yes. Sellers often bundle visible repairs that affect showing quality and inspection outcomes."),
            ("Do you handle buyer move-in lists?", "Yes. New homeowners often schedule one visit for multiple small fixes."),
            ("Can I prioritize items if the list is long?", "Yes. We help sequence work by impact and budget when the full list will not fit one visit."),
            ("Do you take photos for remote owners?", "Photo-based estimates are welcome for landlords and out-of-town owners."),
            ("Can punch-list work include multiple rooms?", "Yes. Whole-home punch lists are a core use case for handyman service."),
            ("Do you handle garage punch-list items?", "Often yes, including drywall, hardware, shelving and minor finish repairs."),
            ("Is there a minimum number of items?", "No. Small jobs are welcome, though bundling several items usually delivers better value."),
        ],
        "rental-property-repairs": [
            (f"Do you work with landlords in {city}?", "Yes. Turnover repairs and ongoing maintenance lists are a strong fit for rental properties."),
            ("Can you repair tenant-caused drywall damage?", "Move-out holes, anchor damage and worn areas are common turnover repairs."),
            ("Do you coordinate access without the owner present?", "Often yes, depending on access instructions and scope."),
            ("Can you turn a unit faster between tenants?", "Bundled turnover repairs help reduce vacancy time compared with scheduling multiple trades."),
            ("Do you work on duplexes and small portfolios?", "Yes. We support single homes, duplexes and smaller rental portfolios."),
            ("Can you provide photo updates after completion?", "Photo documentation can be arranged for remote owners and managers."),
            ("Do you handle lockset and door issues between tenants?", "Door hardware, latch problems and hinge repairs are common turnover items."),
            ("Can maintenance items be scheduled in batches?", "Yes. Ongoing landlord maintenance is often most efficient when grouped seasonally."),
        ],
        "small-home-repairs": [
            (f"What counts as a small home repair in {city}?", "Single-item fixes and short lists such as hardware, drywall dents, doors, caulk, trim and accessories."),
            ("Are tiny jobs really worth scheduling?", "Yes. Small jobs are welcome, especially when several are combined into one visit."),
            ("Can seniors schedule small safety-related fixes?", "Yes. Grab bar alignment checks, loose handrails and trip-hazard hardware fixes are common."),
            ("Do you help busy professionals who do not have time for DIY?", "Yes. That is one of the most common reasons homeowners hire a handyman."),
            ("Can I add items when you arrive?", "Minor additions may be possible if time and materials allow. Larger additions should be estimated first."),
            ("Do you work in condos and townhomes?", "Yes, subject to HOA rules, access and scope."),
            ("Can you hang shelves as part of a small repair visit?", "Yes. Shelving, mirrors and accessory installs are often bundled with other items."),
            ("What repairs do you refer out?", "Electrical panel work, major plumbing, HVAC, roofing and structural repairs are referred to licensed trades when needed."),
        ],
        "trim-molding": [
            (f"Do you repair baseboards and crown molding in {city}?", "Yes. Scuffed baseboards, loose trim, small gaps and minor carpentry touch-ups are common."),
            ("Can you replace a damaged section of trim?", "Often yes when matching profile stock or existing trim can be sourced."),
            ("Do you caulk trim gaps before painting?", "Caulk and prep work can be included as part of trim repair and finish prep."),
            ("Can you fix door casing that is pulling away?", "Loose casing and minor alignment issues are common trim repairs."),
            ("Do you install shoe molding?", "Smaller trim additions and replacements can often be handled in a handyman scope."),
            ("Can trim repair be bundled with drywall work?", "Yes. Pre-paint prep frequently combines drywall patches and trim touch-ups."),
            ("Will new trim match old stained wood?", "We source for the closest practical match and explain limits with aged or discontinued profiles."),
            ("Do you repair window stool and apron trim?", "Interior window trim touch-ups are common in older Springfield homes."),
        ],
        "cabinet-repair": [
            ("Can you fix loose cabinet hinges?", "Yes. Loose hinges, misaligned doors and worn hardware are common kitchen and bath repairs."),
            ("Do you adjust cabinet doors that do not close evenly?", "Hinge adjustment and strike alignment are routine cabinet fixes."),
            ("Can you replace cabinet handles and pulls?", "Yes. Hardware updates are a fast way to refresh kitchens, baths and built-ins."),
            ("Do you repair drawer fronts that are separating?", "Minor drawer and front repairs can often be handled without full cabinet replacement."),
            ("Can you fix a lazy susan or corner cabinet issue?", "Some accessibility and hardware issues can be improved depending on the cabinet type."),
            ("Do you install soft-close hinge upgrades?", "Many soft-close upgrades can be installed when compatible with existing cabinets."),
            ("Can you repair bathroom vanity cabinets?", "Yes. Vanity doors, hinges and hardware are common moisture-area repairs."),
            ("Do you build custom cabinet panels?", "Minor carpentry accents are possible. Full custom cabinetry is outside standard handyman scope."),
        ],
        "tile-backsplash": [
            ("Can you replace a cracked backsplash tile?", "Single-tile replacement and small backsplash repairs are common when spare tiles or close matches exist."),
            ("Do you repair loose shower or tub surround tiles?", "Small tile repairs may be possible. Widespread water damage should be evaluated carefully."),
            ("Can you re-grout a small kitchen area?", "Localized grout repair and refresh can often be handled as a handyman task."),
            ("Do you install a simple backsplash?", "Small backsplash installs may be possible depending on materials and substrate condition."),
            ("Can you fix chipped tile edges?", "Minor chip repairs or replacement of affected tiles are reviewed based on tile type and location."),
            ("Do you repair floor tile transitions?", "Small transition and threshold issues can sometimes be improved without full retiling."),
            ("Can tile work be bundled with caulk repair?", "Yes. Kitchen and bath refresh lists often combine grout, caulk and hardware fixes."),
            ("When do you refer tile work to a specialist?", "Large wet-area failures, mold concerns and full shower retiling are often referred out."),
        ],
        "caulking-weather-sealing": [
            (f"Why does caulk fail in {city} homes?", "Temperature swings, UV exposure, moisture and age cause caulk to shrink, crack or pull away."),
            ("Can you recaulk tubs, showers and sinks?", "Yes. Fresh caulk is one of the fastest ways to improve bath and kitchen appearance."),
            ("Do you seal window and door gaps?", "Exterior and interior seal improvements can reduce drafts and water intrusion at manageable points."),
            ("Can you fix dried-out exterior caulking?", "Localized exterior caulk refresh is common before paint or seasonal maintenance."),
            ("Do you caulk around trim before painting?", "Yes. Caulk prep is often paired with trim and drywall touch-ups."),
            ("Can you seal siding penetrations?", "Small exterior sealing around penetrations and trim joints can be part of weather-prep work."),
            ("What caulk do you use in wet areas?", "We use appropriate mold-resistant products for bath and kitchen wet zones."),
            ("Can weather sealing be part of a punch list?", "Yes. Seasonal maintenance lists often include caulk, hardware and small exterior items."),
        ],
        "tv-mounting-fixtures": [
            ("Can you mount a TV on drywall or studs?", "Yes. TV mounting with proper anchoring is a common handyman request."),
            ("Do you hide cables for a cleaner look?", "Basic cable management can often be improved depending on wall construction and layout."),
            ("Can you install light fixtures and ceiling fans?", "Simple fixture swaps may be possible. New wiring or complex electrical should be handled by a licensed electrician."),
            ("Do you hang heavy mirrors securely?", "Yes. Proper anchors and placement are important for heavy wall-mounted items."),
            ("Can you install towel bars and bath accessories?", "Yes. Coordinated bath hardware installs are common in refresh projects."),
            ("Do you mount shelving systems?", "Floating shelves and bracket shelving can often be installed as part of a handyman visit."),
            ("Can multiple installs be bundled?", "Yes. Mounting several TVs, mirrors or fixtures in one visit is efficient."),
            ("Do you patch holes from old mounts?", "Old anchor holes and patch prep can be combined with drywall repair."),
        ],
        "custom-shelving-carpentry": [
            ("Can you build custom closet shelving?", "Simple custom shelving and closet improvements are common handyman projects."),
            ("Do you install pantry shelving systems?", "Yes. Pantry, laundry and garage shelving are frequent requests."),
            ("Can you repair damaged built-in shelving?", "Loose, sagging or damaged shelves and supports can often be repaired."),
            ("Do you install decorative wall molding accents?", "Smaller accent carpentry can be handled depending on design and scope."),
            ("Can you add mudroom hooks and bench details?", "Entryway upgrades with hooks, trim and small carpentry details are popular."),
            ("Do you build garage storage solutions?", "Practical garage shelving and storage repairs are common in suburban Ozarks homes."),
            ("Can carpentry work be combined with paint prep?", "Yes. Shelving installs and trim repair are often part of pre-paint punch lists."),
            ("When is a project too large for handyman carpentry?", "Major structural changes, load-bearing work and full room builds are referred to a carpenter or contractor."),
        ],
        "pre-sale-home-prep": [
            (f"Why do sellers hire a handyman before listing in {city}?", "Visible repairs affect showing quality, buyer confidence and inspection negotiations."),
            ("Can you complete an inspection repair list?", "Many common inspection items fit handyman scope. Specialized trade work is flagged separately."),
            ("Do you help with cosmetic fixes before photos?", "Yes. Drywall, hardware, caulk, doors and small exterior items are common pre-listing work."),
            ("Can you work on a tight listing deadline?", "Timeline depends on scope. Photo-based estimates help us confirm what can be completed before photos or showings."),
            ("Do you coordinate with Realtors?", "Yes. We can work from agent punch lists when the homeowner authorizes the scope."),
            ("Can pre-sale work include curb-appeal repairs?", "Fence gates, porch details, exterior caulk and small carpentry touch-ups are common."),
            ("Will you prioritize high-impact repairs first?", "Yes. We focus first on what buyers and inspectors notice immediately."),
            ("Can rental owners use pre-sale prep before selling?", "Yes. Investor owners often bundle rent-ready and sale-ready repairs."),
        ],
        "estate-maintenance": [
            (f"What is estate maintenance in {city}?", "Recurring handyman visits for executive homes covering hardware, trim, drywall, caulk, doors, decks and seasonal detail work."),
            ("Do you offer seasonal walkthroughs?", "Yes. Seasonal tune-ups help catch small issues before they become visible or costly."),
            ("Can you maintain a second home in the Ozarks?", "Yes. Second-home opening and closing checklists are a common request."),
            ("Do you work discreetly in furnished executive homes?", "Yes. Floor protection, tidy work areas and respectful scheduling are standard."),
            ("Can estate maintenance include guest house repairs?", "Yes. Guest cottages and secondary structures are often part of estate lists."),
            ("How is estate maintenance different from a punch list?", "Estate maintenance is recurring and preventive. Punch lists are usually one-time event-driven scopes."),
            ("Can you coordinate with household managers or assistants?", "Yes. We can work from authorized contact lists and written scope documents."),
            ("Do you handle pre-entertaining repair visits?", "Yes. Quick detail repairs before hosting are a common estate request."),
        ],
        "gutter-repair": [
            (f"Why do gutters fail in {city}?", "Debris, age, freeze-thaw cycles and heavy Ozarks rainfall stress seams, hangers and downspouts."),
            ("Can you fix leaking gutter seams?", "Yes. Seams, corners and end caps are common leak points we address."),
            ("Do you repair sagging gutters?", "Sagging runs can often be corrected with hanger replacement and realignment."),
            ("Can you reattach downspouts?", "Loose or detached downspouts are common after storms and ladder bumps."),
            ("Do you replace gutter sections?", "Targeted section replacement is possible when repair is not practical."),
            ("Can gutter work be bundled with exterior caulk?", "Yes. Exterior maintenance lists often combine gutters, caulk and trim."),
            ("Do you clean gutters?", "Our focus is repair and tune-up. Full cleaning may be discussed as part of a broader maintenance visit."),
            ("When do you refer gutter replacement?", "When runs are severely deteriorated or improperly pitched beyond practical repair."),
        ],
        "screen-repair": [
            (f"When should screens be replaced in {city}?", "Torn mesh, bent frames and poor fit are common before spring and summer in the Ozarks."),
            ("Can you rescreen existing frames?", "Yes. Rescreening is often more practical than full frame replacement."),
            ("Do you repair porch screens?", "Porch and patio screen panels are common seasonal repair requests."),
            ("Can you fix sliding door screens?", "Yes. Sliding patio door screens are a frequent handyman repair."),
            ("Do you install pet-resistant screen?", "Pet-resistant mesh upgrades can be discussed during rescreening."),
            ("Can screens be done in a whole-home bundle?", "Yes. Multi-window screen refresh visits are efficient."),
            ("Do you repair screen doors?", "Screen door mesh, hinges and latches are common repairs."),
            ("Can screen repair be part of rental turnover?", "Yes. Torn screens are common move-out and move-in repair items."),
        ],
        "interior-paint-touchups": [
            (f"Can you touch up paint after drywall repair in {city}?", "Yes. Paint touch-ups often follow drywall patches for a finished result."),
            ("Do you match existing paint colors?", "Touch-ups work best with leftover owner paint. We discuss blend realism for older or sun-faded walls."),
            ("Can you paint trim scuffs?", "Small trim and casing touch-ups can be handled within practical handyman scope."),
            ("Do you paint ceilings?", "Ceiling spot blocking and touch-ups may be possible after stain remediation."),
            ("Can paint touch-ups be bundled with punch-list work?", "Yes. Pre-listing and move-in lists often include paint spots."),
            ("Do you handle full room repaints?", "Full repaints are generally outside handyman scope unless discussed as a larger project."),
            ("Will you mask furnishings and floors?", "Yes. Masking and protection are part of careful interior touch-up work."),
            ("Can rental owners use paint touch-ups between tenants?", "Yes. Spot painting is common in turnover work."),
        ],
    }

    common = [
        (f"Do you offer {name.lower()} in {city}, Missouri?", f"Yes. {name} is available in {city} and nearby Ozarks communities depending on schedule and project scope."),
        (f"How do I request a {name.lower()} estimate?", f"Email {city}-area project photos and details to request a clear estimate before work begins."),
        ("Do you take small jobs?", "Yes. Focused repairs and bundled small projects are a core part of our service."),
        ("Can I combine this service with other repairs?", "Yes. Bundling multiple repair types into one visit is often the most efficient approach."),
        ("Do you protect floors and furnishings during work?", "We take care to protect finished surfaces and clean up work areas before leaving."),
        ("How soon can work be scheduled?", "Timing depends on scope and current schedule. Email your project details for the next available options."),
        ("Do you provide materials?", "We can discuss whether materials are owner-supplied or included during the estimate."),
        ("What if the repair uncovers a bigger issue?", "We communicate clearly if the problem should be handled by a specialized licensed trade."),
        ("Do you serve nearby cities outside Springfield?", "Yes. Nixa, Ozark, Republic, Battlefield, Willard, Strafford, Rogersville and nearby communities are commonly served."),
        ("Can property managers request this service?", "Yes. Owners, landlords and managers can request estimates with photos and access instructions."),
        ("Is weekend or evening work available?", "Availability varies. Include your preferred timing in the estimate request."),
        ("Do you offer written scope before starting?", "Yes. Agreed scope and expectations are confirmed before work begins."),
    ]

    ozarks = [
        ("How does Missouri humidity affect home repairs?", "Seasonal humidity in the Ozarks can affect doors, trim gaps, caulk lines and exterior wood movement."),
        ("Do you work in older Springfield homes?", "Yes. Older homes often need trim, drywall, door and hardware repairs that fit handyman scope."),
        ("Can you help with storm-season exterior maintenance?", "Small fence, deck, caulk and exterior hardware repairs are common after seasonal weather."),
        ("Do you work in newer subdivisions?", "Yes. Move-in punch lists and builder-grade hardware upgrades are common in newer neighborhoods."),
    ]

    return tuple(specific.get(slug, []) + common + ozarks)


def area_faqs(
    slug: str,
    label: str,
    area_type: str,
    neighborhoods: tuple[str, ...],
    housing: str,
) -> tuple[tuple[str, str], ...]:
    place = label
    nearby_text = ", ".join(neighborhoods[:4]) if neighborhoods else "nearby communities"

    local = [
        (f"Do you provide handyman service in {place}?", f"Yes. We serve homeowners, landlords and property managers in {place} and surrounding areas."),
        (f"What repairs are most common in {place}?", f"Common requests in {place} include {housing.lower()}"),
        (f"Do you serve neighborhoods near {place}?", f"Yes. We commonly serve {nearby_text} and nearby streets depending on scheduling."),
        (f"Can I request an estimate for a home in {place}?", f"Email project photos and your {place} address details for a clear estimate."),
        (f"Do you work on rental properties in {place}?", "Yes. Turnover repairs and maintenance lists are available for rental owners and managers."),
        (f"Can you help with pre-sale repairs in {place}?", "Yes. Listing prep and inspection punch lists are common in this market."),
        (f"Do you handle small jobs in {place}?", "Yes. Small repairs are welcome, and bundling several items is often the best value."),
        (f"How quickly can you schedule work in {place}?", "Timing depends on scope and route schedule. Email details for the next available visit."),
    ]

    if area_type == "neighborhood":
        local.extend([
            (f"Is {place} part of your Springfield service area?", f"Yes. {place} is one of the Springfield neighborhoods we regularly serve."),
            (f"Do you understand the housing styles in {place}?", f"Yes. Homes in {place} often need repairs related to {housing.lower()}"),
            (f"Can you work near {nearby_text} on the same visit?", "Nearby jobs can sometimes be combined when scheduling allows."),
            (f"Do Realtors refer punch-list work in {place}?", "Agents often coordinate handyman punch lists before photos, showings and inspections."),
        ])
    else:
        local.extend([
            (f"Do you serve the full {place} city limits?", f"We serve {place} and nearby communities based on project scope and scheduling."),
            (f"Which {place} neighborhoods do you visit most?", f"Common routes include areas such as {nearby_text} and surrounding subdivisions."),
            (f"Can you help new residents moving into {place}?", "Move-in punch lists are one of the most common requests in growing Ozarks communities."),
            (f"Do you work outside {place} in nearby towns?", "Yes. We also serve surrounding Ozarks communities around the Springfield metro."),
        ])

    services = [
        ("What handyman services are available here?", "Drywall repair, door repair, fence repair, deck repair, trim and molding, cabinet hardware, tile touch-ups, caulking, mounting, shelving and punch-list work."),
        ("Can drywall and paint prep be done together?", "Yes. Drywall patches and trim/caulk prep are often combined before painting."),
        ("Do you repair decks and fences after storms?", "Smaller exterior repairs are common after seasonal Ozarks weather."),
        ("Can doors and hardware be fixed in one visit?", "Yes. Door alignment, hinges, knobs and related trim repairs are often bundled."),
        ("Do you install shelving and fixtures?", "TV mounting, shelving, mirrors and bath accessories are common add-ons to repair visits."),
        ("Can landlords bundle multiple unit repairs?", "Yes. Multi-item turnover lists are efficient for rental properties."),
        ("Do you handle cabinet hinge and hardware issues?", "Kitchen and bath cabinet adjustments are common handyman requests."),
        ("Can you help with caulk and weather sealing?", "Fresh caulk and sealing improvements are common kitchen, bath and exterior maintenance items."),
    ]

    process = [
        ("How do estimates work?", "Email photos, your location and a repair list. We confirm scope, timing and pricing before scheduling."),
        ("Can I send photos before scheduling?", "Yes. Photos are strongly recommended for faster and more accurate estimates."),
        ("What should I include in the request?", "Include your neighborhood, repair list, photos, urgency and whether the property is owner-occupied or rental."),
        ("Do you work with HOAs and condo associations?", "Yes, subject to association rules and access requirements."),
        ("What work do you refer to licensed trades?", "Major electrical, plumbing, HVAC, roofing and structural work are referred when needed."),
        ("Do you offer white-glove cleanup standards?", "We protect finished spaces and leave work areas tidy after repairs."),
        ("Can multiple repairs be prioritized by budget?", "Yes. We can sequence a larger list across one or more visits."),
        ("How do I contact you?", "Email contact@ozarkshandyman.com with your project details."),
    ]

    return tuple(local + services + process)
