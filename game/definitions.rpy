## Best Friends — fallback definitions for a lightweight DDLC/Ren'Py mod.
## A full DDLC mod template may already define some of these names. If so, keep
## the template's richer assets and remove matching fallback definitions here.

default player = "MC"

## Characters.
define mc = Character("[player]", color="#ffffff")
define s = Character("Sayori", color="#22a6ff")
define m = Character("Monika", color="#1fb36b")
define n = Character("Natsuki", color="#ff6fae")
define y = Character("Yuri", color="#b07cff")

## Music and sound variable placeholders. Replace with real DDLC/mod audio paths
## in a full release.
define audio.t_best_friends = None
define audio.t_recovery = None
define audio.t_festival_return = None

## Transitions used by the script. These are intentionally conservative so they
## work even outside a complete DDLC template.
define wipeleft = Dissolve(0.35)
define wipeleft_scene = Dissolve(0.5)

## Positions roughly matching common DDLC staging helpers.
transform t11:
    xalign 0.5
    yalign 1.0

transform t21:
    xalign 0.33
    yalign 1.0

transform t22:
    xalign 0.67
    yalign 1.0

transform t31:
    xalign 0.25
    yalign 1.0

transform t32:
    xalign 0.5
    yalign 1.0

transform t33:
    xalign 0.75
    yalign 1.0

## Minimal background fallbacks so the script can launch in a clean Ren'Py test
## project without crashing on missing images. Replace these with DDLC assets in
## an actual mod package.
image bg residential_day = Solid("#87bfe8")
image bg club_day = Solid("#d7c7a1")
image bg sayori_bedroom = Solid("#f5c7d1")
image bg house = Solid("#9bcf9b")

## Minimal sprite fallbacks. They display as text placeholders in clean Ren'Py;
## DDLC mod templates should replace them with the real character art.
image sayori 1x = Text("Sayori", color="#22a6ff", size=48)
image sayori 2l = Text("Sayori", color="#22a6ff", size=48)
image sayori 1k = Text("Sayori", color="#22a6ff", size=48)
image sayori 4r = Text("Sayori", color="#22a6ff", size=48)
image sayori 1l = Text("Sayori", color="#22a6ff", size=48)
image sayori 2h = Text("Sayori", color="#22a6ff", size=48)
image sayori 1q = Text("Sayori", color="#22a6ff", size=48)
image sayori 1u = Text("Sayori", color="#22a6ff", size=48)
image sayori 1v = Text("Sayori", color="#22a6ff", size=48)
image sayori 1d = Text("Sayori", color="#22a6ff", size=48)
image sayori 1t = Text("Sayori", color="#22a6ff", size=48)

image monika 2b = Text("Monika", color="#1fb36b", size=48)
image monika 1d = Text("Monika", color="#1fb36b", size=48)
image monika 1j = Text("Monika", color="#1fb36b", size=48)
image monika 1g = Text("Monika", color="#1fb36b", size=48)
image monika 1p = Text("Monika", color="#1fb36b", size=48)
image monika 2q = Text("Monika", color="#1fb36b", size=48)

image natsuki 4c = Text("Natsuki", color="#ff6fae", size=48)
image natsuki 12b = Text("Natsuki", color="#ff6fae", size=48)
image natsuki 12f = Text("Natsuki", color="#ff6fae", size=48)
image natsuki 4z = Text("Natsuki", color="#ff6fae", size=48)

image yuri 2f = Text("Yuri", color="#b07cff", size=48)
image yuri 3w = Text("Yuri", color="#b07cff", size=48)
image yuri 1b = Text("Yuri", color="#b07cff", size=48)
