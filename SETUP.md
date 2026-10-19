# Pixel Coast — setup and verification

## Design system
Midnight navy #102A56, coastal blue #164B78, ocean cyan #35B9DB, coral #F47C78, cloud pink #F2A0C0, gold #FFC978, cream #FFF0CE, twilight lavender #9D80C6.

Visual rule: crisp nearest-neighbor pixels, calm coastal scenes, restrained typography and two-column statistics. The artwork is intentionally rendered as a pixel-art GIF rather than smooth SVG gradients.

## Install
1. Back up your current `README.md` and `.github/workflows/` folder.
2. Upload the package's `README.md` and `assets/` folder into `jared-esquivel/jared-esquivel` on the `main` branch.
3. Add `.github/workflows/skyline.yml` without deleting your existing snake workflow.
4. Go to GitHub Actions and manually run `Generate 3D Contributions`.
5. Confirm the `output` branch contains `profile-3d-contrib/profile-night-rainbow.svg`. If the upstream generator produces a different filename, change the README path accordingly.
6. Confirm your existing snake workflow generates `github-snake.svg` on `output`. If it generates a different filename or branch, update the README image URL.
7. Refresh your GitHub profile and inspect on desktop, mobile, and both themes.

## Important limitations
- The pixel ocean hero GIF animates; the twilight footer and decorative dividers are static to avoid visual overload.
- Third-party statistics and activity endpoints have not been live-tested in GitHub and may be unavailable or rate-limited. They are themed to match, but may not be perfectly identical.
- GitHub's README renderer cannot run custom JavaScript, CSS, or interactive animations.
- The 3D workflow is supplied but has not been executed. Its external action version and output filename must be checked after first run.
- The public repositories could not be exhaustively audited. Project details are intentionally conservative. Verify repository paths before publishing.
- For best reliability, replace third-party stat images with scheduled locally generated assets once working endpoints are confirmed.

## Verification checklist
- [ ] All local PNG/GIF paths load
- [ ] Ocean hero animates on GitHub
- [ ] No broken external statistics images
- [ ] 3D workflow passes and generates expected file
- [ ] Snake image points to actual output filename
- [ ] Project links and descriptions are accurate
- [ ] Layout works on mobile
- [ ] Readable on light and dark GitHub themes
