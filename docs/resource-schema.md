# Resource Schema

Every resource in WebAtlas follows this schema. The schema is used for the structured JSON data in [`data/resources.json`](../data/resources.json) and enables future search, filtering, and display features.

## Schema

```json
{
  "name": "",
  "url": "",
  "category": "",
  "subcategory": "",
  "tags": [],
  "description": "",
  "type": "Library",
  "open_source": true,
  "free": true,
  "technology": [],
  "github": "",
  "license": ""
}
```

## Field Definitions

### Required Fields

| Field | Type | Description |
|---|---|---|
| `name` | string | The name of the resource. Must be unique across the entire dataset. |
| `url` | string | The canonical URL of the resource (official website or GitHub repo). Must be a valid URL. |
| `category` | string | The primary category. Must match a category in [taxonomy.md](taxonomy.md). |
| `tags` | array | Array of tag strings. Must match tags defined in taxonomy or be a new, meaningful tag. |
| `description` | string | A concise, factual description (1-2 sentences). |

### Optional Fields

| Field | Type | Default | Description |
|---|---|---|---|
| `subcategory` | string | `null` | A subcategory within the primary category. Must match a subcategory in taxonomy. |
| `type` | string | `"Library"` | The type of resource. See Resource Types in taxonomy.md. |
| `open_source` | boolean | `null` | Whether the resource is open source. Only include when verifiable. |
| `free` | boolean | `null` | Whether the resource is free to use. Only include when verifiable. |
| `technology` | array | `[]` | Technologies used (e.g., `["React", "Tailwind", "Motion"]`). |
| `github` | string | `null` | URL to the official GitHub repository, if one exists. |
| `license` | string | `null` | Open source license identifier (e.g., `"MIT"`, `"Apache-2.0"`). Only include when verifiable. |

## Field Guidelines

### URL
- Use the **official URL** as the canonical URL.
- Do not use URL shorteners.
- Prefer `https://` URLs.
- If the resource is primarily a GitHub project, the URL may point to the GitHub repo.

### Tags
- Use tags from taxonomy when applicable.
- New tags may be introduced but should be meaningful and reusable.
- Tags should be concise (1-3 words).
- Do not duplicate tags already captured in `technology` or `subcategory`.

### open_source / free
- Only set these fields when you can **reliably verify** the status.
- `null` means the status is unknown or not applicable.
- `true` means confirmed open source / free.
- `false` means confirmed proprietary / paid.

### type
- `Library` — Reusable code library (default)
- `Tool` — Utility or application
- `Gallery` — Curated browsing collection
- `Template` — Pre-built project starting point
- `Guide` — Educational resource
- `Asset` — Static resource bundle

### GitHub
- Only include the **official** GitHub repository URL.
- Do not include individual contributor forks unless that IS the canonical repo.

### description
- 1-2 sentences maximum.
- Factual, not promotional.
- Describe what it is, not why you like it.
