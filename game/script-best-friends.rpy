# Best Friends — a DDLC fan-mod script draft.
# This file assumes a DDLC/Ren'Py-style environment with the usual character
# definitions and sprites available. It intentionally avoids procedural details
# in the crisis scene while keeping the emotional consequences central.

label best_friends_start:
    scene bg residential_day
    with dissolve

    $ persistent.best_friends_seen = True

    "The week before the festival should have felt like a countdown to something bright."
    "Instead, every morning felt like watching clouds gather behind a blue sky."

    show sayori 1x at t11
    s "Heeeey!"
    mc "You're late again, Sayori."
    show sayori 2l
    s "Ahaha... sorry. My alarm and I are having creative differences."

    "She smiles the way she always does."
    "But lately, her smile arrives a second after her voice, like it has to run to catch up."

    mc "You okay?"
    show sayori 1k
    s "Of course. Festival stuff is just a lot, you know?"
    mc "You can tell me if it isn't just festival stuff."
    show sayori 4r
    s "Then who would be the sunshine?"

    "The joke lands softly and breaks apart at our feet."

    scene bg club_day
    with wipeleft_scene

    show monika 2b at t11
    m "Everyone, let's use today to finalize poems and decorations. We can still make this festival special."

    show monika at t21
    show natsuki 4c at t22
    n "We could, if certain people stopped spacing out with glue sticks in their hands."

    show natsuki at t31
    show yuri 2f at t32
    show sayori 1l at t33
    y "Natsuki..."
    n "What? I'm not wrong."

    show sayori 2h
    s "It's okay. I did kind of make the banner say 'Litature' for ten whole minutes."

    "Everyone laughs except Monika, whose eyes briefly flick to the classroom window."
    "The glass shows five reflections. For a blink, one of them is missing."

    show monika 1d
    m "...Sayori? If you need to take a break, you can."
    show sayori 1q
    s "President's orders?"
    show monika 1j
    m "Friend's orders."

    jump best_friends_confession

label best_friends_confession:
    scene bg sayori_bedroom
    with dissolve

    "That evening, Sayori tells me about the rainclouds."
    "Not all at once. Not neatly. The words come out crooked, ashamed, and tired."

    show sayori 1u at t11
    s "Sometimes I think everyone would be lighter if I wasn't making them worry."
    mc "Sayori... that isn't true."
    s "I know I'm supposed to believe that. I just... don't always know how."

    "I want to say the perfect thing."
    "I want to reach into the air between us and pull the rainclouds apart with my hands."
    "But there isn't a perfect thing. There is only my best friend sitting on her bed, looking smaller than I've ever seen her."

    mc "Then let me believe it with you until you can."
    show sayori 1v
    s "That's too heavy for you."
    mc "You carried me through half my childhood. Let me sit here for one bad evening."

    "Her laugh trembles."
    "When I leave, she promises she'll see me in the morning."
    "I believe her because I need to."

    jump best_friends_morning

label best_friends_morning:
    scene black
    with dissolve

    "Morning comes wrong."
    "No birds. No sunlight through my curtains. Just a pressure in my chest so sudden and cold that I sit up gasping."

    mc "Sayori."

    scene bg residential_day
    with hpunch

    "I run."
    "I don't stop for my bag. I don't stop for breath. I don't stop when my lungs start to burn."

    scene bg house
    with wipeleft

    "Her front door is unlocked."
    mc "Sayori!"

    scene bg sayori_bedroom
    with vpunch

    "What I find in her room turns the world into a thin, ringing line."
    "For one impossible second, my mind refuses to understand."
    "Then my body moves before thought can catch it."

    scene black
    with dissolve

    "I get her down."
    "I call for help."
    "I say her name until my throat hurts, and when I hear the smallest breath, I start crying so hard I can barely speak to the dispatcher."

    m "[glitchtext('This time, the door opened in time.')]"

    "Sirens arrive. Adults take over. I answer questions with shaking hands."
    "The festival does not happen that day."

    jump best_friends_hospital

label best_friends_hospital:
    scene bg hospital
    with dissolve

    "Hospitals do not feel like miracles."
    "They feel like plastic chairs, vending-machine coffee, white lights, and every minute stretching until it snaps."

    show monika 1g at t11
    m "She's alive."
    "Monika says it like a prayer and a warning at the same time."

    show monika at t31
    show yuri 3w at t32
    show natsuki 12b at t33
    y "I should have noticed. Her poems, her absences, the way she apologized for existing..."
    n "Stop it."
    y "But I—"
    n "I said stop it!"

    "Natsuki's fists are clenched so tightly her knuckles are pale."
    show natsuki 12f
    n "If everyone starts blaming themselves, then what? Does that help her? Does that make any of this less..."
    "Her voice cracks."
    n "...less scary?"

    mc "I keep seeing it. Every time I close my eyes."

    show monika 1p
    m "Then don't close them alone tonight. Call someone. Call me, or Yuri, or Natsuki. Call an adult. You don't have to be brave by yourself."

    "Monika looks down at her hands."
    m "None of us do. Not anymore."

    jump best_friends_recovery

label best_friends_recovery:
    scene bg sayori_bedroom
    with dissolve

    "Sayori comes home days later with a safety plan, follow-up appointments, and a tiredness that sleep doesn't fix."
    "Her parents speak carefully. The club visits carefully. I breathe carefully."

    show sayori 1u at t11
    s "Everyone keeps saying they're glad I'm here."
    mc "We are."
    s "But I hurt you. I hurt all of you."
    mc "You were hurting too."
    s "That doesn't erase it."
    mc "No. It doesn't."

    "The truth sits between us. Heavy, but not cruel."

    mc "I'm scared, Sayori. I think you should know that."
    show sayori 1v
    s "Of me?"
    mc "For you. And a little for me. I don't know how to stop seeing that morning."
    s "I'm sorry."
    mc "I know. But I don't want your apology more than I want you here."

    "She cries quietly. I sit beside her, not touching until she leans her shoulder against mine."

    scene bg club_day
    with wipeleft_scene

    "Recovery is not a straight line."
    "One Monday, Sayori laughs until Natsuki threatens to weaponize frosting."
    "One Thursday, she cannot get out of bed, and the club meeting becomes a group chat full of cat stickers and reminders to drink water."
    "Some days I hover too much, and Sayori snaps that she is not a glass ornament."
    "Some days she hides too well, and I have to ask the hard questions anyway."

    show monika 2q at t11
    m "I keep remembering a room where no one arrived."
    mc "What?"
    show monika 1p
    m "A nightmare, maybe. A previous draft. It doesn't matter."
    m "What matters is that this version keeps going."

    "The classroom lights flicker. For a moment, the poem notebook on the desk displays text I never wrote."
    window hide
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 0.25
    hide screen tear
    window show

    "STAY. STAY. STAY."

    jump best_friends_festival

label best_friends_festival:
    scene bg club_day
    with dissolve

    "Months later, the festival finally happens."
    "It is smaller than the one we planned. Quieter. More honest."
    "Paper clouds hang beside paper suns across the classroom windows. Nobody says the symbolism out loud. Nobody needs to."

    show natsuki 4z at t31
    show yuri 1b at t32
    show monika 1j at t33
    n "Cupcakes are on the left. Emotional devastation is apparently on the right."
    y "Natsuki, your cupcakes have little umbrellas on them."
    n "They're thematically appropriate, okay?"
    m "They're wonderful."

    show sayori 1d at t11
    "Sayori steps to the front with a folded poem in both hands."
    "Her fingers shake. She reads anyway."

    s "Tomorrow is a door I can't see through."
    s "Sometimes I hate it for being closed."
    s "Sometimes I am afraid of what waits with its hand on the knob."
    s "But today, my friends are sitting on this side with me."
    s "So I will put my hand on the handle."
    s "Not because I am fearless."
    s "Because I am not alone."

    "No one claps at first."
    "Then Yuri starts, crying openly. Natsuki follows, pretending not to. Monika's smile trembles like sunlight on water."

    mc "You did it."
    show sayori 1t
    s "We did it."

    "There will be bad days after this."
    "There will be appointments, awkward conversations, apologies, and mornings where hope feels like a language none of us remember how to speak."
    "But Sayori is here."
    "My best friend is here."
    "And when tomorrow comes, we will meet it together."

    return
