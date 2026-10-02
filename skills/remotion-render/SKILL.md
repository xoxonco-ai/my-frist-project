---
name: remotion-render
description: Export a Remotion video
license: Remotion License (https://remotion.dev/license)
metadata:
  author: remotion-dev
  version: 4.0.532
  source: https://github.com/remotion-dev/skills
  upstream_folder: skills/remotion-render
  upstream_commit: 0b5db9d
---

## General rendering strategy

Render a video using:

```
npx remotion render
```

Full list of options: https://www.remotion.dev/docs/cli/render.md

Render a still using:

```
npx remotion still
```

Full list of options: https://www.remotion.dev/docs/cli/still.md

To render several frames as images in one call, use `render --frames`:

```
npx remotion render [composition-id] out/frames --frames=0,30,90 --image-format=png
```

See https://www.remotion.dev/docs/cli/render.md#--frames for more options.

## Transparent videos

See [Transparent videos](./transparent-videos.md) for rendering out a video with transparency.
