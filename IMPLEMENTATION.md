# Profile implementation notes

## Design

The hero is a generated animated GIF based on the supplied portfolio reference: dark navy atmosphere, long faint wave contours, left-aligned greeting, blue-to-green gradient name and underline. Its editable source is `scripts/generate_hero.py`. The decorative divider is editable SVG.

## Preview and publish

1. Create a public GitHub repository named exactly `jared-esquivel` under the `jared-esquivel` account, if it doesn't already exist.
2. Copy `README.md`, `assets/`, and `scripts/` into its root.
3. Preview `README.md` using GitHub's Preview tab. Check both light/dark appearance and mobile width.
4. Commit and push. The README should appear on the profile overview.

To regenerate the hero: `python3 -m pip install pillow` then `python3 scripts/generate_hero.py`.

## Claim review

- Digital NEST role, HITEC scholarship, and HackWatsonville founding: supplied by user; not independently verified in this deliverable.
- Lighthouse 95+: user-provided professional performance metric; no independent audit report reviewed. Wording avoids attributing it to a specific public repository.
- HackWatsonville 30+ attendees: user-provided event metric; not independently audited.
- Other metrics (80%, 100%, 35–45%) intentionally excluded pending supporting measurement details.
- Public GitHub profile was observed to contain 19 repositories; no individual repository was sufficiently audited to be promoted as flagship work.

## GitHub compatibility and limitations

The hero is a GIF, which GitHub can display as an image. No JavaScript or custom CSS is embedded in README. `<details>` provides a native expandable section. Technology icons are fetched from the Devicon CDN and may require an internet connection. The looping hero restarts its intro periodically; a static PNG alternative is provided for future use. The animation is not an exact source-code reproduction of the portfolio.

## Suggested commit

`feat(profile): redesign GitHub README with portfolio-inspired motion`

Extended description:

- Add wavelength-inspired animated hero and SVG divider
- Organize professional impact, technologies, and selected work
- Replace generic stats and badges with concise, evidence-aware copy
- Add source generator and implementation notes
