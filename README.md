# Quiet Frames

A minimal photo and film portfolio by Amrit Nag.

**Live:** https://photo-gallery-three-sage.vercel.app

- 34 photographs across five series: Making of a Mother, Visitors, Strangers, After Dark and Match Day.
- 4 films edited for Photo Circle RAIT, which play as silent loops and open in a full-screen player.
- A single static page (`index.html`) with no build step and no framework.

## Structure

```
index.html          the whole site: layout, styles, and the photo / film lists
img/NN.jpg          source photos
img/NN-*.webp       640 / 1200 / 1800px versions the site serves (generated)
img/meta.js         photo sizes + blurred placeholders (generated)
video/*.mp4         full edits (1080p) and 6-second silent loops
video/*.webp        film covers
og-hero.jpg         link-preview image (LinkedIn, WhatsApp, X)
tools/make_sizes.py regenerates the webp files and meta.js
```

## Editing

- **Photos and series:** edit the `SERIES` list near the top of the script in `index.html`. Each photo is `[file number, title, [column start, column span]]` on a 12-column grid.
- **Films:** edit the `MOTION` list right below it.
- **Adding a photo:** save it as the next number in `img/` (for example `img/35.jpg`), run `python tools/make_sizes.py`, then add it to a series.

## Run locally

```
python -m http.server 5173
```

Then open http://localhost:5173.

## Deploy

The repo is connected to Vercel, so every push to `main` updates the live site automatically:

```
git add -A
git commit -m "describe the change"
git push
```

Other branches get their own preview link without touching the live site. You can still deploy by hand with `vercel deploy --prod`.

`.vercelignore` keeps the source JPGs and the tools folder out of the upload.
