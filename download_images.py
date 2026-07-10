"""Download contextually relevant images for ozarkshandyman.com."""

from __future__ import annotations

import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "assets" / "images"
ROOT.mkdir(parents=True, exist_ok=True)

# Verified Unsplash URLs — Midwest/traditional homes and service-specific scenes.
DOWNLOADS = {
    # Regional / property style
    "ozarks-hills.jpg": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=1400&q=85&auto=format&fit=crop",
    "ozarks-forest.jpg": "https://images.unsplash.com/photo-1448375240586-882707db888b?w=1400&q=85&auto=format&fit=crop",
    "suburban-home.jpg": "https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=1400&q=85&auto=format&fit=crop",
    "craftsman-bungalow.jpg": "https://images.unsplash.com/photo-1583608205776-bfd35f0d9f83?w=1400&q=85&auto=format&fit=crop",
    "executive-home.jpg": "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=1400&q=85&auto=format&fit=crop",
    "traditional-estate.jpg": "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=1400&q=85&auto=format&fit=crop",
    "refined-interior.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1400&q=85&auto=format&fit=crop",
    # Service-specific
    "drywall-repair.jpg": "https://images.unsplash.com/photo-1581858726788-75bc0f6a952d?w=1400&q=85&auto=format&fit=crop",
    "door-repair.jpg": "https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=1400&q=85&auto=format&fit=crop",
    "fence-repair.jpg": "https://images.unsplash.com/photo-1592595896551-12b371d546d5?w=1400&q=85&auto=format&fit=crop",
    "deck-outdoor.jpg": "https://images.unsplash.com/photo-1600585152915-d208bec867a1?w=1400&q=85&auto=format&fit=crop",
    "trim-carpentry.jpg": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=1400&q=85&auto=format&fit=crop",
    "kitchen-cabinets.jpg": "https://images.unsplash.com/photo-1556911220-bff31c812dba?w=1400&q=85&auto=format&fit=crop",
    "tile-backsplash.jpg": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=1400&q=85&auto=format&fit=crop",
    "bath-caulk.jpg": "https://images.unsplash.com/photo-1620626011761-996317b8d101?w=1400&q=85&auto=format&fit=crop",
    "screen-porch.jpg": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1400&q=85&auto=format&fit=crop",
    "gutter-exterior.jpg": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1400&q=85&auto=format&fit=crop",
    "interior-paint.jpg": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=1400&q=85&auto=format&fit=crop",
    "closet-shelving.jpg": "https://images.unsplash.com/photo-1615529328331-f8917597711f?w=1400&q=85&auto=format&fit=crop",
    "tv-mounting.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=1400&q=85&auto=format&fit=crop",
    "handyman-detail.jpg": "https://images.unsplash.com/photo-1595846519845-68e298c2edd8?w=1400&q=85&auto=format&fit=crop",
    "rental-interior.jpg": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=1400&q=85&auto=format&fit=crop",
    "pre-sale-staging.jpg": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=1400&q=85&auto=format&fit=crop",
}

USER_AGENT = "Mozilla/5.0 (compatible; OzarksHandyman/1.0)"


def download(url: str, dest: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        dest.write_bytes(response.read())


def main() -> None:
    for name, url in DOWNLOADS.items():
        dest = ROOT / name
        print(f"Downloading {name}...")
        download(url, dest)
        print(f"  -> {dest.stat().st_size // 1024} KB")
    print("Done.")


if __name__ == "__main__":
    main()
