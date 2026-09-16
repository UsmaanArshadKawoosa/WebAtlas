#!/usr/bin/env python3
"""Validate WebAtlas resources.json."""

import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / "data" / "resources.json"

VALID_CATEGORIES = {
    "Design Inspiration",
    "UI Components",
    "Animation & Interaction",
    "3D & WebGL",
    "Colors",
    "Typography",
    "Assets",
    "Icons",
    "Developer Tools",
    "AI",
    "Design Systems",
    "Accessibility",
    "Learning",
}

VALID_TYPES = {
    "Library",
    "Tool",
    "Gallery",
    "Template",
    "Guide",
    "Asset",
}

VALID_TAGS = {
    "React", "JavaScript", "Vue", "Tailwind", "shadcn", "Animation", "Motion",
    "Open Source", "Free", "Components", "Blocks", "Templates", "WebGL", "3D",
    "Color", "Typography", "Tool", "Gallery", "Library", "Data Visualization",
    "Particles", "Interactive", "Icons", "Design Systems", "Accessibility",
    "Design Galleries", "Landing Page Inspiration", "SaaS Inspiration",
    "Portfolio Inspiration", "Experimental Websites", "Product Design Inspiration",
    "Motion Inspiration", "React Animation", "Animation Libraries",
    "Scroll Animations", "Cursor Effects", "Micro-interactions",
    "Particle Effects", "Transition Libraries", "3D Tools",
    "Three.js Ecosystem", "WebGL", "3D Asset Resources",
    "Color Palette Generators", "Theme Generators", "Contrast Checkers",
    "Gradient Generators", "Color Tools", "Font Libraries", "Font Pairing",
    "Type Scales", "Typography Tools", "Variable Fonts", "Images",
    "Illustrations", "SVGs", "Textures", "Backgrounds", "Forms", "Navigation",
    "Dashboards", "CSS Generators", "Shadow Generators", "SVG Tools",
    "Responsive Tools", "Browser Tools", "Code Generators",
}

REQUIRED_FIELDS = ["name", "url", "category", "tags", "description"]


def validate_resources():
    errors = []

    # Load JSON
    if not DATA_FILE.exists():
        print(f"ERROR: {DATA_FILE} not found")
        return 1

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            resources = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON — {e}")
        return 1

    if not isinstance(resources, list):
        print("ERROR: resources.json must contain an array")
        return 1

    if len(resources) == 0:
        print("WARNING: resources.json is empty")

    seen_urls = set()
    seen_names = set()

    for i, r in enumerate(resources):
        prefix = f"[{i}] {r.get('name', 'unknown')}"

        # Required fields
        for field in REQUIRED_FIELDS:
            if field not in r or not r[field]:
                errors.append(f"{prefix}: missing required field '{field}'")

        # URL validation
        url = r.get("url", "")
        if url:
            if not isinstance(url, str) or not url.startswith("http://") and not url.startswith("https://"):
                errors.append(f"{prefix}: invalid URL '{url}'")
            if url in seen_urls:
                errors.append(f"{prefix}: duplicate URL '{url}'")
            seen_urls.add(url)

        # Name uniqueness
        name = r.get("name", "")
        if name:
            if name in seen_names:
                errors.append(f"{prefix}: duplicate name '{name}'")
            seen_names.add(name)

        # Category validation
        category = r.get("category", "")
        if category and category not in VALID_CATEGORIES:
            errors.append(f"{prefix}: invalid category '{category}'")

        # Type validation
        rtype = r.get("type", "")
        if rtype and rtype not in VALID_TYPES:
            errors.append(f"{prefix}: invalid type '{rtype}'")

        # Tags validation
        tags = r.get("tags", [])
        if not isinstance(tags, list):
            errors.append(f"{prefix}: 'tags' must be an array")
        else:
            for tag in tags:
                if not isinstance(tag, str) or not tag.strip():
                    errors.append(f"{prefix}: invalid tag '{tag}'")

        # Description length
        desc = r.get("description", "")
        if desc and len(desc) > 300:
            errors.append(f"{prefix}: description too long ({len(desc)} chars, max 300)")

        # URL reachability (optional — warn only)
        if url and (isinstance(url, str) and url.startswith("https://")):
            try:
                req = urllib.request.Request(url, method="HEAD")
                req.add_header("User-Agent", "WebAtlas-Validator/1.0")
                resp = urllib.request.urlopen(req, timeout=5)
                if resp.status >= 400:
                    errors.append(f"{prefix}: URL returned status {resp.status}")
            except urllib.error.URLError:
                pass  # Skip reachability check on network errors
            except Exception:
                pass

    # Print results
    if errors:
        print(f"\nValidation failed with {len(errors)} error(s):")
        for e in errors:
            print(f"  {e}")
        return 1

    print(f"Validation passed - {len(resources)} resources checked")
    return 0


if __name__ == "__main__":
    sys.exit(validate_resources())
