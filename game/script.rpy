## Best Friends - execution entry point.
## Ren'Py automatically calls `label splashscreen` before the main menu/start.
## This splash presents the Team Salvato fan-work disclaimer before the custom
## story can begin.

label splashscreen:
    scene black
    with dissolve

    centered "This is an unofficial fan work based on Doki Doki Literature Club."
    centered "Doki Doki Literature Club is owned by Team Salvato."
    centered "This mod is not affiliated with or endorsed by Team Salvato."
    centered "Please support the official game before playing fan works."
    pause 0.5

    return

label start:
    jump best_friends_start
