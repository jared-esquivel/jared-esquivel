# Installation

1. Download and extract this package.
2. Open `https://github.com/jared-esquivel/jared-esquivel`.
3. Upload `README.md`, the `assets/` directory, and `.github/workflows/skyline.yml` preserving paths. Do not delete the existing `.github/workflows/snake.yml`.
4. Commit changes to `main`.
5. Go to Actions > 3D Contribution Skyline > Run workflow. The skyline will be missing until the first successful run. If the action version is unavailable, check the upstream repository for a current supported release.
6. Confirm the generated `profile-3d-contrib/profile-night-rainbow.svg` exists on the default branch. If the action produces a different filename, update the README accordingly.
7. Verify the existing snake Action is successful and the `output` branch contains the SVG files.
8. Check all external statistics services. They are optional third-party services and may occasionally rate-limit or fail.
9. Preview on GitHub in both light and dark themes and on mobile.

## Notes
- `assets/` uses locally hosted, self-contained animated SVG files with no JavaScript.
- GitHub renders SVG animation differently across clients; users with reduced-motion settings may see less motion.
- 3D skyline is a generated static graphic, not a continuously animated chart.
- Public GitHub languages represent repository contents, not necessarily proficiency.
- Some professional outcomes are self-reported, not independently verified by public code.
- No live changes were made to your GitHub repository.
