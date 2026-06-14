# Best Friends — DDLC Mod Script

**Best Friends** is a Doki Doki Literature Club fan-mod story concept and Ren'Py script draft centered on Sayori surviving a suicide attempt and the Literature Club learning how to support each other through a long, imperfect recovery.

> Content warning: this mod discusses depression, suicidal ideation, a suicide attempt, hospitalization, trauma, and recovery. The rescue scene is intentionally written without procedural detail.

## What is included

- A DDLC/Ren'Py-style story script file in `game/script-best-friends.rpy`.
- `game/script.rpy`, which provides the execution entry point and Team Salvato fan-work disclaimer splash before the story starts.
- `game/options.rpy`, which manages package metadata, version numbering, and window settings.
- `game/definitions.rpy`, which declares fallback characters, transitions, positions, audio placeholders, and generic asset tags for clean Ren'Py test projects.
- A mod outline and implementation notes in `docs/story-outline.md`.

## Story premise

The story begins near the school festival, echoing the original setup as Sayori's depression becomes harder to miss. On the morning the protagonist is meant to meet her, a terrible feeling sends him running to her house. He finds her after an attempt, gets her down in time, and calls emergency services. Sayori survives, but the mod does not treat survival as a cure.

The remaining story follows Sayori, the protagonist, Natsuki, Yuri, and Monika through shock, guilt, therapy, fear, friendship, setbacks, and the slow rebuilding of trust. Subtle meta disturbances remain, especially around Monika, but they reinforce the value of a second chance rather than pushing the cast toward despair.

## Installation notes

This repository does not include DDLC assets or Ren'Py itself. To test as a DDLC mod, copy the `.rpy` files from `game/` into a legal DDLC mod project. `game/script.rpy` includes a `label start` entry point that immediately jumps into `label best_friends_start`, so it can run as the primary script in a simple DDLC mod workspace. If your mod template already defines `label start` or already provides richer DDLC definitions, merge these files carefully to avoid duplicate entry points or placeholder assets overriding your real assets.
