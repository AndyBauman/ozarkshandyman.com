from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Project:
    slug: str
    title: str
    location: str
    service: str
    summary: str
    details: str
    image_key: str


PROJECTS: tuple[Project, ...] = (
    Project("fremont-hills-listing-prep", "Fremont Hills Listing Prep Package", "Fremont Hills, Springfield", "Pre-Sale Home Prep",
            "A pre-photo punch list covering drywall, trim, hardware and exterior presentation details.",
            "The homeowner needed a polished presentation before photography and showings. Work included drywall patch blending, baseboard scuff repair, cabinet hardware alignment, exterior caulk touch-ups and gate adjustment.",
            "estate_home"),
    Project("rountree-door-trim", "Rountree Door and Trim Tune-Up", "Rountree, Springfield", "Door Repair",
            "Whole-home door alignment and trim touch-ups in an older Springfield bungalow.",
            "Seasonal humidity had caused multiple doors to stick and trim joints to open slightly. We adjusted hinges, aligned latches and recaulked select trim joints before interior painting.",
            "craftsmanship"),
    Project("nixa-move-in-bundle", "Nixa Move-In Upgrade Bundle", "Nixa, MO", "Punch List Handyman",
            "Move-in punch list with shelving, mounting and hardware upgrades in a newer suburban home.",
            "The buyers wanted one visit to handle pantry shelving, TV mounting, towel bar installs, door hardware swaps and drywall anchor-hole repair left from previous décor.",
            "luxury_interior"),
    Project("ozark-deck-fence", "Ozark Deck and Fence Refresh", "Ozark, MO", "Deck Repair",
            "Deck board replacement, railing tightening and fence gate realignment after seasonal wear.",
            "Outdoor entertaining space needed safety-minded repairs before hosting season. We replaced damaged boards, secured railings and restored smooth gate operation.",
            "deck_outdoor"),
    Project("republic-rental-turnover", "Republic Rental Turnover Sprint", "Republic, MO", "Rental Property Repairs",
            "Fast turnover repairs for a duplex between tenants.",
            "Work included drywall hole patching, bath recaulking, cabinet hinge adjustment, interior door latch repair and fixture replacements to return the unit to rent-ready condition.",
            "springfield_home"),
    Project("phelps-grove-interior-refresh", "Phelps Grove Interior Refresh", "Phelps Grove, Springfield", "Small Home Repairs",
            "Interior detail bundle for an updated bungalow near the central corridor.",
            "Project scope included drywall patches, shelf installation, mirror hanging, cabinet pull upgrades and kitchen caulk refresh for a cleaner finished look.",
            "luxury_interior"),
    Project("southern-hills-exterior", "Southern Hills Exterior Maintenance", "Southern Hills, Springfield", "Caulking and Weather Sealing",
            "Seasonal exterior caulk and hardware maintenance for a family home with mature landscaping.",
            "We refreshed failing caulk lines, tightened loose exterior hardware and addressed minor fence gate drag before summer weather exposure.",
            "springfield_home"),
    Project("battlefield-kitchen-cabinets", "Battlefield Kitchen Cabinet Tune-Up", "Battlefield, MO", "Cabinet Repair and Hardware",
            "Kitchen cabinet alignment and soft-close hinge upgrade before listing.",
            "Several cabinet doors were misaligned and noisy. We adjusted hinges, replaced worn hardware and installed soft-close upgrades for a more refined kitchen presentation.",
            "luxury_interior"),
    Project("willard-garage-storage", "Willard Garage Storage Upgrade", "Willard, MO", "Custom Shelving and Carpentry Accents",
            "Custom garage shelving and storage wall for a rural-suburban property.",
            "The owner needed practical storage for tools and seasonal equipment. We built a custom shelving layout and reinforced existing brackets for heavier loads.",
            "craftsmanship"),
    Project("walnut-street-condo-punch", "Walnut Street Condo Punch List", "Walnut Street District, Springfield", "Punch List Handyman",
            "Compact punch list for a downtown-adjacent condo before move-in.",
            "Work included TV mounting, drywall anchor repair, interior door adjustment, fixture installs and bath caulk refresh in a tighter urban-adjacent space.",
            "luxury_interior"),
    Project("springfield-backsplash-repair", "Springfield Backsplash Tile Repair", "Springfield, MO", "Tile and Backsplash Repair",
            "Cracked kitchen backsplash tile replacement and grout refresh.",
            "A single damaged tile and stained grout line were undermining an otherwise updated kitchen. We replaced the tile, refreshed surrounding grout and sealed the repair area.",
            "luxury_interior"),
    Project("strafford-inspection-response", "Strafford Inspection Response Bundle", "Strafford, MO", "Pre-Sale Home Prep",
            "Inspection-response handyman bundle for a family home sale.",
            "The seller needed help addressing visible inspection items including deck railing tightening, exterior caulk, door hardware and drywall patch work before closing negotiations concluded.",
            "estate_home"),
    Project("marshfield-seasonal-maintenance", "Marshfield Seasonal Maintenance Visit", "Marshfield, MO", "Estate Maintenance",
            "Seasonal exterior and interior maintenance bundle for a rural-suburban property.",
            "Scope included gutter tune-up, exterior caulk refresh, screen repair, door hardware adjustment and a short interior punch list before winter weather arrived.",
            "ozarks_forest"),
    Project("clever-fence-gate", "Clever Fence and Gate Restoration", "Clever, MO", "Fence Repair",
            "Privacy fence gate realignment and picket replacement on a family property.",
            "A dragging gate and several storm-damaged pickets were affecting security and curb appeal. We realigned hardware, replaced damaged boards and improved latch performance.",
            "estate_home"),
    Project("del-lago-estate-tuneup", "Del Lago Estate Tune-Up", "Del Lago, Springfield", "Estate Maintenance",
            "Quarterly estate maintenance visit for an executive home.",
            "Work included cabinet hardware tuning, bath caulk refresh, drywall touch-ups, deck board tightening and fixture alignment across multiple living areas.",
            "estate_exterior"),
    Project("highland-springs-move-in", "Highland Springs Move-In List", "Highland Springs, Springfield", "Punch List Handyman",
            "Move-in punch list for a family home in southwest Springfield.",
            "New owners requested help with shelving, TV mounting, door adjustments, drywall anchor repair and kitchen hardware alignment in one coordinated visit.",
            "luxury_interior"),
    Project("gutter-downspout-repair", "Gutter and Downspout Repair Package", "Springfield, MO", "Gutter and Downspout Repair",
            "Leak sealing and downspout reattachment on a mature-tree property.",
            "Seams were leaking and a downspout had pulled away from the fascia. We sealed joints, replaced hangers and restored proper drainage away from the foundation.",
            "springfield_home"),
)
