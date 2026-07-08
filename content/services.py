from __future__ import annotations

from dataclasses import dataclass

from content.faqs import service_faqs
from content.images import IMAGES


@dataclass(frozen=True)
class Service:
    slug: str
    name: str
    title: str
    description: str
    intro: str
    long_copy: str
    fixes: tuple[str, ...]
    benefits: tuple[str, ...]
    projects: tuple[str, ...]
    image_key: str

    @property
    def faqs(self) -> tuple[tuple[str, str], ...]:
        return service_faqs(self.slug, self.name)


SERVICES: tuple[Service, ...] = (
    Service(
        "drywall-repair", "Drywall Repair",
        "Drywall Repair Springfield MO | Patches, Texture Matching and Ceiling Repair",
        "Refined drywall repair in Springfield, Nixa, Ozark and the Ozarks. Invisible patches, ceiling repair, texture blending and paint-ready prep for upscale homes.",
        "Damaged drywall undermines the finish of an otherwise beautiful room. We repair holes, cracks, nail pops and ceiling imperfections with careful prep, texture awareness and respect for your furnishings.",
        "Springfield-area homes—from historic neighborhoods to newer estates—often need drywall work that must disappear into the existing finish. We focus on patch quality, dust control and paint-ready results rather than quick cover-ups.",
        ("Doorknob impact holes and anchor damage", "Ceiling stains after resolved leaks", "Cracks at corners and seams", "Nail pops and loose tape", "Texture blending and skim touch-ups", "Rental turnover wall repairs", "Garage and mudroom drywall", "Stairwell and tall-wall patches", "Pre-listing cosmetic wall repairs", "Water-damage cosmetic prep after remediation", "Outlet and switch surround repairs", "Closet and pantry wall damage"),
        ("Invisible patch standards for refined interiors", "Floor and furniture protection as a default", "Honest guidance on texture match limits", "Ideal for estates, rentals and pre-sale prep"),
        ("Whole-wall patch blend in a Fremont Hills living room", "Ceiling stain repair before interior repainting", "Rental turnover hole repair package in south Springfield"),
        "luxury_interior",
    ),
    Service(
        "door-repair", "Door Repair",
        "Door Repair Springfield MO | Interior, Exterior and Hardware Alignment",
        "Premium door repair in Springfield MO. Sticking doors, latch alignment, hinge repair, weatherstripping and hardware upgrades for quality homes.",
        "A door that drags, rattles or fails to latch quietly degrades the feel of a home. We diagnose alignment, hardware and frame issues with a repair-first mindset.",
        "Ozarks humidity and seasonal movement affect doors throughout Springfield, from older Rountree bungalows to newer Nixa estates. We restore smooth operation and clean lines without pushing unnecessary replacements.",
        ("Sticking interior and exterior doors", "Loose hinges and stripped screws", "Latch and strike plate alignment", "Knob, lever and deadbolt replacement", "Weatherstripping and draft sealing", "Closet, pantry and bi-fold doors", "Door casing and trim touch-ups", "Patio door operation improvements", "Whole-house door tune-ups", "Pre-sale door adjustment lists", "Rental turnover hardware refreshes", "Seasonal humidity-related adjustments"),
        ("Repair-first recommendations", "Hardware expertise for common residential sets", "Quiet, precise operation as the goal", "Bundle multiple doors in one visit"),
        ("Whole-house hinge tune-up before listing in Southern Hills", "Front door weatherseal improvement in Ozark", "Interior latch alignment package in Rountree"),
        "springfield_home",
    ),
    Service(
        "fence-repair", "Fence Repair",
        "Fence Repair Springfield MO | Gates, Privacy Fencing and Storm Damage",
        "Fence repair for Springfield and Ozarks properties. Gate alignment, picket replacement, post bracing and storm-damage restoration with curb appeal in mind.",
        "A sagging gate or damaged privacy fence affects both security and the presentation of your property. We repair function first, then improve the finished appearance.",
        "Fence lines in the Ozarks take wind, moisture and ground movement. We handle practical repairs that preserve the look of established neighborhoods and larger suburban lots.",
        ("Sagging gate repair and bracing", "Picket and board replacement", "Loose rails and fasteners", "Latch and hinge replacement", "Storm-damage section repairs", "Leaning post stabilization", "Side-yard privacy fence touch-ups", "Pet-related fence damage", "Pre-sale fence presentation repairs", "Rental property fence resets", "Cap and trim board replacement", "Small-section rebuilds when practical"),
        ("Repair before replace whenever sensible", "Gate function restored for daily use", "Material matching when possible", "Clear advice when replacement is smarter"),
        ("Gate realignment on a Republic estate driveway", "Storm-damaged picket replacement in Nixa", "Privacy fence refresh before listing in Battlefield"),
        "estate_home",
    ),
    Service(
        "deck-repair", "Deck Repair",
        "Deck Repair Springfield MO | Railings, Boards, Stairs and Safety Prep",
        "Deck repair in Springfield MO for boards, railings, stairs and fasteners. Safety-minded repairs for outdoor living spaces in the Ozarks climate.",
        "Decks are central to Ozarks outdoor living, but sun, rain and freeze-thaw cycles wear them down. We address safety issues and visible defects with targeted repairs.",
        "From elevated backyard decks in Ozark to lower entertaining spaces in Springfield, we focus on usable, safe repairs that support inspections, hosting and resale.",
        ("Loose or damaged deck boards", "Soft boards and fastener pops", "Loose railings and handrails", "Stair tread and stringer repairs", "Deck screw and nail replacement", "Skirting and trim repairs", "Pre-inspection safety fixes", "Gate latch repairs on deck access", "Fascia board touch-ups", "Small structural carpentry within handyman scope", "Seasonal maintenance repairs", "Pre-sale deck presentation fixes"),
        ("Safety-first inspection mindset", "Targeted repairs without overselling rebuilds", "Clear boundaries on structural scope", "Great for inspections and move-in lists"),
        ("Railing tightening before a Springfield inspection", "Board replacement on an Ozark entertaining deck", "Stair repair package in Fremont Hills"),
        "deck_outdoor",
    ),
    Service(
        "punch-list", "Punch List Handyman",
        "Punch List Handyman Springfield MO | Pre-Sale, Move-In and Inspection Lists",
        "White-glove punch list handyman service in Springfield MO. Bundle pre-sale, move-in, inspection and estate maintenance repairs into one efficient visit.",
        "The best homes still accumulate a list of small items that never quite get scheduled. We turn that list into a clear, completed scope.",
        "Punch-list work is ideal for homeowners, buyers, sellers and property managers who want one trusted visit instead of five small appointments.",
        ("Pre-listing cosmetic repairs", "Move-in hardware and door adjustments", "Inspection response items", "Drywall and caulk touch-ups", "Fixture and accessory installs", "Fence and gate adjustments", "Deck and exterior safety items", "Closet and pantry adjustments", "Garage and utility room fixes", "Rental turnover punch lists", "Estate maintenance visits", "Photo-ready repairs before marketing"),
        ("One visit for multiple small items", "Priority guidance when the list is long", "Ideal for Realtors and remote owners", "Clear scope before work begins"),
        ("Pre-photo punch list in Phelps Grove", "Buyer move-in list in Republic", "Inspection response bundle in Springfield"),
        "craftsmanship",
    ),
    Service(
        "rental-property-repairs", "Rental Property Repairs",
        "Rental Property Repairs Springfield MO | Turnover and Portfolio Maintenance",
        "Rental property handyman repairs in Springfield MO. Fast turnover fixes, drywall, doors, hardware and maintenance lists for landlords and managers.",
        "Vacant days and deferred maintenance cost more than the repair itself. We help owners return units to rent-ready condition efficiently.",
        "Landlords across Springfield, Nixa and Ozark use handyman turnover work to protect asset quality without overpaying for oversized contractor scopes.",
        ("Move-out drywall and hole repair", "Door, hinge and lockset fixes", "Cabinet hardware and hinge adjustments", "Caulk and bath refresh items", "Fence and gate repairs", "Deck and stair safety fixes", "Shelving and accessory resets", "Light fixture and hardware swaps", "Paint-prep repairs", "Maintenance punch lists", "Duplex turnover bundles", "Remote-owner photo estimates"),
        ("Rent-ready prioritization", "Photo-friendly estimating", "Good for small portfolios", "Clear communication for managers"),
        ("Duplex turnover package in north Springfield", "Kitchen hardware refresh between tenants in Nixa", "Move-out repair sprint in Ozark"),
        "springfield_home",
    ),
    Service(
        "small-home-repairs", "Small Home Repairs",
        "Small Home Repairs Springfield MO | Estate Maintenance and Detail Work",
        "Small home repairs in Springfield MO for homeowners who expect careful work, clear communication and no drama on the detail list.",
        "Not every repair deserves a major contractor bid. We handle the refined, everyday fixes that keep a home feeling finished.",
        "This service is built for owners who value discretion, tidy work areas and practical solutions on the items that linger on the kitchen notepad.",
        ("Loose handles and hinges", "Drywall dents and patches", "Door and cabinet adjustments", "Caulk and grout touch-ups", "Shelving and mirror installs", "Fence gate fixes", "Deck board repairs", "Trim and baseboard touch-ups", "Fixture and hardware swaps", "Pet and family wear-and-tear fixes", "Senior safety hardware checks", "Seasonal maintenance items"),
        ("Small jobs taken seriously", "Bundle for better value", "Respectful in-home standards", "Straightforward estimates"),
        ("Whole-home detail visit in Brentwood", "Seasonal maintenance bundle in Willard", "Family home tune-up in Strafford"),
        "luxury_interior",
    ),
    Service(
        "trim-molding", "Trim and Molding Repair",
        "Trim and Molding Repair Springfield MO | Baseboards, Casing and Finish Carpentry",
        "Trim and molding repair in Springfield MO. Baseboards, door casing, crown touch-ups and finish carpentry for polished interiors.",
        "Trim is the frame of a room. Scuffs, gaps and loose pieces make even quality spaces feel tired. We restore crisp lines and tight joints.",
        "Older Springfield homes and updated estates both benefit from careful trim repair before painting or listing.",
        ("Baseboard repair and replacement sections", "Door and window casing fixes", "Crown molding touch-ups", "Shoe molding and sill trim", "Loose trim re-nailing", "Gap caulking before paint", "Corner joint repairs", "Stair skirt board fixes", "Built-in trim accents", "Scuff and impact damage repair", "Paint-prep trim smoothing", "Small custom trim patches"),
        ("Crisp finish lines matter", "Paint-prep friendly repairs", "Careful matching to existing profiles", "Pairs well with drywall and caulk work"),
        ("Baseboard replacement before interior repaint", "Casing repair around upgraded doors", "Stair trim touch-up in an older Springfield home"),
        "craftsmanship",
    ),
    Service(
        "cabinet-repair", "Cabinet Repair and Hardware",
        "Cabinet Repair Springfield MO | Hinges, Alignment and Hardware Upgrades",
        "Cabinet repair and hardware upgrades in Springfield MO. Hinge adjustment, door alignment, pull replacement and vanity fixes for kitchens and baths.",
        "Loose cabinet doors and dated hardware make kitchens and baths feel less refined than they should. We restore alignment and update details efficiently.",
        "From builder-grade rental kitchens to owner-occupied homes in Fremont Hills, cabinet tune-ups are one of the highest-impact handyman upgrades.",
        ("Hinge adjustment and replacement", "Cabinet door alignment", "Drawer front tightening", "Knob and pull upgrades", "Soft-close hinge installs", "Vanity door and hinge repair", "Pantry cabinet adjustments", "Bath hardware coordination", "Loose box tightening access repairs", "Rental kitchen refreshes", "Pre-sale cabinet tune-ups", "Laundry and mudroom cabinet fixes"),
        ("High visual impact for modest cost", "Rental-ready kitchen and bath refreshes", "Precise alignment and quiet close", "Coordinates with punch-list work"),
        ("Kitchen hardware refresh before listing", "Vanity hinge repair in a master bath", "Rental kitchen tune-up in Republic"),
        "luxury_interior",
    ),
    Service(
        "tile-backsplash", "Tile and Backsplash Repair",
        "Tile and Backsplash Repair Springfield MO | Kitchen and Bath Touch-Ups",
        "Tile and backsplash repair in Springfield MO. Cracked tile replacement, grout refresh, shower surround touch-ups and kitchen detail repairs.",
        "A cracked backsplash tile or failing grout line stands out in an otherwise refined kitchen or bath. We handle localized repairs with realistic finish expectations.",
        "Tile repair is detail work. We focus on practical improvements that restore appearance without unnecessary full-room retiling.",
        ("Cracked backsplash tile replacement", "Grout repair and refresh", "Loose tile stabilization", "Shower surround touch-ups", "Floor transition repairs", "Caulk and tile joint improvements", "Accent tile repairs", "Rental bath refresh items", "Pre-sale kitchen touch-ups", "Laundry room tile fixes", "Small backsplash installs", "Tile edge chip repairs"),
        ("Localized repair before full retile", "Pairs with caulk and hardware work", "Realistic finish expectations", "Great for rentals and refreshes"),
        ("Backsplash tile swap in a kitchen refresh", "Grout refresh before listing photos", "Bath surround touch-up in Ozark"),
        "luxury_interior",
    ),
    Service(
        "caulking-weather-sealing", "Caulking and Weather Sealing",
        "Caulking and Weather Sealing Springfield MO | Kitchen, Bath and Exterior Prep",
        "Caulking and weather sealing in Springfield MO. Fresh seals for kitchens, baths, windows, doors and exterior prep in the Ozarks climate.",
        "Old caulk makes fine homes look neglected and can allow moisture where it does not belong. We refresh seals with the right products for each area.",
        "Seasonal temperature swings in southwest Missouri make caulking maintenance one of the most cost-effective appearance upgrades available.",
        ("Tub, shower and sink recaulking", "Kitchen backsplash and counter joints", "Window and door seal improvements", "Exterior trim caulking", "Siding penetration sealing", "Paint-prep caulk lines", "Seasonal maintenance refresh", "Rental bath resealing", "Pre-sale cosmetic sealing", "Garage and utility area caulking", "Interior trim gap sealing", "Draft-reduction touch-ups"),
        ("Fast visual upgrade", "Right product for wet vs dry areas", "Pairs with paint and trim prep", "Seasonal maintenance friendly"),
        ("Master bath recaulk before guest season", "Exterior trim seal refresh in Willard", "Kitchen and bath rental turnover reseal"),
        "springfield_home",
    ),
    Service(
        "tv-mounting-fixtures", "TV Mounting and Fixture Installation",
        "TV Mounting Springfield MO | Fixtures, Shelves and Wall Accessories",
        "TV mounting and fixture installation in Springfield MO. TVs, mirrors, shelving, bath accessories and lighting swaps with clean placement.",
        "Poorly mounted TVs and crooked fixtures undermine an otherwise polished room. We install with proper anchoring and alignment.",
        "This service is popular in move-in punch lists, media room refreshes and rental upgrades where clean installation matters.",
        ("TV wall mounting", "Cable tidying where practical", "Mirror and art hanging", "Towel bars and bath accessories", "Light fixture change-outs within scope", "Floating shelf installs", "Closet rod and bracket installs", "Garage organizer mounting", "Entryway hook systems", "Kitchen accessory installs", "Patching old mount holes", "Bundled multi-room installs"),
        ("Proper anchoring for safety", "Clean alignment and spacing", "Patch old holes when needed", "Bundle multiple installs efficiently"),
        ("Media room TV mount and shelf install", "Master bath accessory package in Nixa", "Move-in mounting list in Springfield"),
        "luxury_interior",
    ),
    Service(
        "custom-shelving-carpentry", "Custom Shelving and Carpentry Accents",
        "Custom Shelving Springfield MO | Closets, Pantries and Built-In Details",
        "Custom shelving and carpentry accents in Springfield MO. Closet systems, pantry upgrades, mudroom details and practical built-in improvements.",
        "Thoughtful storage and carpentry details make daily life easier and homes feel more intentional. We build practical upgrades that fit the space.",
        "From pantry rebuilds in growing suburbs to mudroom upgrades in family homes, custom shelving is a high-value handyman category.",
        ("Closet shelving systems", "Pantry shelving upgrades", "Laundry room storage", "Mudroom bench and hook details", "Garage storage shelves", "Built-in repair and reinforcement", "Decorative accent carpentry", "Bookcase and niche shelving", "Entryway storage improvements", "Utility room organization", "Paint-prep carpentry", "Rental storage upgrades"),
        ("Custom fit without full remodel pricing", "Practical storage for daily use", "Pairs with trim and paint prep", "Strong move-in upgrade category"),
        ("Pantry shelving upgrade in Republic", "Mudroom detail package in Battlefield", "Closet system refresh in Fremont Hills"),
        "craftsmanship",
    ),
    Service(
        "pre-sale-home-prep", "Pre-Sale Home Prep",
        "Pre-Sale Home Prep Springfield MO | Listing Repairs and Inspection Response",
        "Pre-sale home prep in Springfield MO. Listing punch lists, inspection repairs and photo-ready improvements for discerning sellers.",
        "Buyers notice the details. We help sellers address the repairs that shape first impressions, showing feedback and inspection negotiations.",
        "Pre-sale prep is one of the highest-ROI handyman categories in the Springfield market, especially in competitive neighborhoods.",
        ("Pre-photo cosmetic repairs", "Inspection response items within scope", "Drywall, caulk and hardware fixes", "Door and trim adjustments", "Deck and fence presentation repairs", "Bath and kitchen touch-ups", "Fixture and accessory refreshes", "Curb-appeal exterior items", "Investor sale-ready bundles", "Agent-coordinated punch lists", "Priority sequencing by deadline", "Move-out sale prep for owners"),
        ("High-impact repair prioritization", "Agent-friendly coordination", "Photo and showing deadline awareness", "Pairs with all other service categories"),
        ("Listing prep in Southern Hills before photos", "Inspection response bundle in Rountree", "Investor sale-ready package in Ozark"),
        "estate_home",
    ),
    Service(
        "estate-maintenance", "Estate Maintenance",
        "Estate Maintenance Springfield MO | Executive Home Care and Seasonal Tune-Ups",
        "Estate maintenance in Springfield MO for executive homes, second residences and recurring repair lists across the Ozarks.",
        "Larger homes generate longer maintenance lists. We provide organized, discreet repair service with respect for your time, furnishings and finish standards.",
        "Properties in Fremont Hills, Del Lago, Southern Hills and surrounding Ozarks communities benefit from a trusted handyman partner for seasonal walkthroughs and recurring detail work.",
        ("Seasonal maintenance walkthroughs", "Recurring repair lists", "Hardware and trim tune-ups", "Drywall and caulk refresh", "Door and screen programs", "Deck and fence monitoring", "Fixture and accessory installs", "Guest house punch lists", "Second-home opening checklists", "Pre-entertaining repair visits", "Estate exterior presentation", "Whole-home detail tune-ups"),
        ("Discreet, respectful in-home standards", "Multi-item visit efficiency", "Clear written scope", "Ideal for executive and second homes"),
        ("Quarterly estate tune-up in Fremont Hills", "Seasonal exterior detail visit in Del Lago", "Guest house refresh before family arrival"),
        "estate_exterior",
    ),
    Service(
        "gutter-repair", "Gutter and Downspout Repair",
        "Gutter Repair Springfield MO | Leaks, Sagging Runs and Drainage Fixes",
        "Gutter and downspout repair in Springfield MO. Leak sealing, sagging correction, bracket replacement and drainage improvements.",
        "Proper drainage protects siding, foundations and landscaping. We repair gutters and downspouts with attention to water flow and curb presentation.",
        "Ozarks rainfall and seasonal debris make functional gutters essential on Springfield-area homes with mature tree cover.",
        ("Leak sealing at joints and seams", "Sagging gutter correction", "Bracket and hanger replacement", "Downspout reattachment", "Splash block alignment", "Corner and end cap repair", "Drainage path correction", "Fascia attachment review", "Pre-storm gutter tune-ups", "Pre-sale gutter polish", "Leaf-guard adjustment where present", "Whole-house gutter inspection visits"),
        ("Water-path focus", "Repair before full replacement", "Practical safety access", "Protects siding and foundation edges"),
        ("Gutter leak elimination on a Southern Hills home", "Downspout reroute in Republic", "Pre-storm gutter tune-up in Nixa"),
        "springfield_home",
    ),
    Service(
        "screen-repair", "Screen Repair",
        "Screen Repair Springfield MO | Windows, Doors and Porch Screens",
        "Screen repair in Springfield and the Ozarks. Window screens, door screens, porch panels and frame tune-ups for seasonal comfort.",
        "Torn screens invite pests and undermine curb appeal. We repair mesh, spline and frames for smooth seasonal operation.",
        "Spring and summer in the Ozarks make intact screens essential. We repair porch, window and door screens across Springfield metro homes and surrounding suburbs.",
        ("Window screen rescreening", "Sliding door screen replacement", "Porch screen panel repair", "Spline and frame tune-ups", "Screen door alignment", "Storm door screen inserts", "Pet-resistant screen upgrades", "Second-story screen access repairs", "Rental turnover screen resets", "Whole-home screen refresh visits", "Garage passage screens", "Seasonal screen storage prep"),
        ("Clean frame alignment", "Tight mesh finish", "Seasonal readiness", "Multi-opening bundles"),
        ("Porch screen restoration in Ozark", "Whole-home screen refresh in Springfield", "Rental turnover screen repair in Phelps Grove"),
        "estate_home",
    ),
    Service(
        "interior-paint-touchups", "Interior Paint Touch-Ups",
        "Interior Paint Touch-Ups Springfield MO | Walls, Trim and Ceiling Spots",
        "Interior paint touch-ups in Springfield MO. Wall spots, trim refresh, ceiling corrections and paint-ready repair finishing.",
        "Fresh paint touch-ups complete the repair story. We handle focused spots, trim refresh and ceiling corrections with careful masking in furnished rooms.",
        "After drywall or trim repairs, paint matching determines whether the work disappears. We handle practical touch-up scope suited to pre-sale, rental and estate maintenance needs.",
        ("Wall spot touch-ups after repairs", "Trim and casing refresh", "Ceiling stain blocking prep", "Door paint chip correction", "Closet and pantry spot painting", "Stair and hall scuff touch-ups", "Accent wall corrections", "Nail hole and patch paint blend", "Cabinet paint chip touch-ups", "Pre-sale paint polish", "Rental turnover spot painting", "Paint-prep after drywall repair"),
        ("Careful masking in lived-in spaces", "Sheen and blend realism", "Pairs with drywall and trim work", "Listing-ready finish focus"),
        ("Post-repair paint blend in Rountree living room", "Trim and wall refresh before listing photos", "Rental turnover paint spots in north Springfield"),
        "luxury_interior",
    ),
)

SERVICE_BY_SLUG = {service.slug: service for service in SERVICES}
