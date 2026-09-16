# Contributing to WebAtlas

Thank you for your interest in contributing! WebAtlas is a community-curated directory, and every high-quality resource helps the community.

## How to add a resource

1. **Find the appropriate category** — Browse the [resources/](resources/) directory to identify the right category file.
2. **Check for duplicates** — Search the category file and [`data/resources.json`](data/resources.json) to make sure the resource isn't already listed.
3. **Verify the official URL** — Confirm the resource's official website or GitHub repository. Prefer the canonical URL.
4. **Add a concise description** — Write a factual, one-to-two sentence description. No promotional language.
5. **Add appropriate tags** — Use relevant tags from [docs/taxonomy.md](docs/taxonomy.md) or introduce new ones sparingly.
6. **Submit a PR** — Open a pull request with your changes.

## Contribution guidelines

### Quality standards

- **No spam** — Do not submit resources designed primarily to drive traffic to your own site.
- **No duplicate entries** — Each resource should appear only once across all categories.
- **No misleading descriptions** — Descriptions must be factual and concise.
- **No affiliate links** — Only official URLs are accepted.
- **No URL shorteners** — Use the full, canonical URL.
- **No low-quality clones** — Resources must provide genuine value, not be derivative copies of existing entries.
- **No irrelevant entries** — Resources must be useful to website designers or frontend developers.

### Preferred resources

- Prefer **free** resources, but paid resources may be included when genuinely useful.
- Prefer **open-source** resources when available.
- Prefer **official websites** over third-party listings.

### Formatting

When adding to a Markdown category file, use this format:

```markdown
### Resource Name

> Brief, factual description.

**Tags:** Tag1 · Tag2 · Tag3

**Type:** Library

[Visit](https://example.com/)
```

When adding to `data/resources.json`, follow the schema defined in [docs/resource-schema.md](docs/resource-schema.md).

## How to suggest a resource

You can also suggest a resource without submitting a PR by opening a GitHub Discussion or an issue with the tag `resource-suggestion`. Include:

- Resource name and URL
- Category it belongs to
- A brief description
- Whether it's free or paid
- Whether it's open-source or proprietary

## Review process

Maintainers review submissions for:

- Accuracy of URLs and descriptions
- Proper categorization
- Absence of duplicates
- Adherence to quality guidelines

PRs are typically reviewed within a few days. Thanks for helping make WebAtlas better!
