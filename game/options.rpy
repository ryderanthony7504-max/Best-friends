## Best Friends — Ren'Py/DDLC package options.
## These settings keep the mod self-contained for a lightweight Ren'Py workspace.

init -1 python:
    config.name = "Best Friends"
    config.version = "0.2.0"
    config.window_title = "Best Friends — A DDLC Fan Mod"

    ## DDLC-style window behavior.
    config.window = "auto"
    config.window_show_transition = Dissolve(0.2)
    config.window_hide_transition = Dissolve(0.2)

    ## Basic package metadata for builds.
    build.name = "BestFriendsDDLCMod"
    build.directory_name = "BestFriendsDDLCMod-0.2.0"
