"""Image registry — each key maps to a service- or context-specific photo."""

IMAGES = {
    # Ozarks / regional
    "ozarks_hills": ("/assets/images/ozarks-hills.jpg", "Rolling Ozarks hills near Springfield, Missouri"),
    "ozarks_forest": ("/assets/images/ozarks-forest.jpg", "Ozarks woodland landscape in southwest Missouri"),
    # Property styles (Midwest / Ozarks — traditional, not coastal-modern)
    "suburban_home": ("/assets/images/suburban-home.jpg", "Well-maintained suburban home in the Springfield Ozarks area"),
    "craftsman_bungalow": ("/assets/images/craftsman-bungalow.jpg", "Craftsman-style home in a Springfield neighborhood"),
    "executive_home": ("/assets/images/executive-home.jpg", "Traditional executive home on a wooded Ozarks lot"),
    "traditional_estate": ("/assets/images/traditional-estate.jpg", "Classic American estate home with lawn and mature trees"),
    "refined_interior": ("/assets/images/refined-interior.jpg", "Refined living room with quality finishes"),
    # Service-specific
    "drywall_repair": ("/assets/images/drywall-repair.jpg", "Drywall patch and interior wall repair work"),
    "door_repair": ("/assets/images/door-repair.jpg", "Interior door and hardware detail"),
    "fence_repair": ("/assets/images/fence-repair.jpg", "Wood privacy fence and gate on a residential property"),
    "deck_outdoor": ("/assets/images/deck-outdoor.jpg", "Backyard deck and outdoor living space"),
    "trim_carpentry": ("/assets/images/trim-carpentry.jpg", "Finish carpentry and trim detail work"),
    "kitchen_cabinets": ("/assets/images/kitchen-cabinets.jpg", "Kitchen cabinetry and hardware"),
    "tile_backsplash": ("/assets/images/tile-backsplash.jpg", "Kitchen tile backsplash detail"),
    "bath_caulk": ("/assets/images/bath-caulk.jpg", "Bathroom tile and caulk finish detail"),
    "screen_porch": ("/assets/images/screen-porch.jpg", "Screened porch and window area on a home"),
    "gutter_exterior": ("/assets/images/gutter-exterior.jpg", "House exterior with roofline and gutters"),
    "interior_paint": ("/assets/images/interior-paint.jpg", "Interior paint touch-up and wall finishing"),
    "closet_shelving": ("/assets/images/closet-shelving.jpg", "Custom closet shelving and storage"),
    "tv_mounting": ("/assets/images/tv-mounting.jpg", "Wall-mounted television in a living room"),
    "handyman_detail": ("/assets/images/handyman-detail.jpg", "Residential handyman repair work inside a home"),
    "rental_interior": ("/assets/images/rental-interior.jpg", "Clean rental property interior ready for turnover"),
    "pre_sale_staging": ("/assets/images/pre-sale-staging.jpg", "Well-staged home interior prepared for listing"),
}

# Default hero images by page type
HERO_HOME = "ozarks_hills"
HERO_SERVICES = "handyman_detail"
HERO_AREAS = "ozarks_hills"
