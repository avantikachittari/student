---
layout: base
title: I'm Avantika
hide: true
---

<style>
/* Rainbow gradient variables */
:root {
    --rainbow: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
}

/* Rainbow text */
.rainbow-text {
    background: var(--rainbow);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Rainbow buttons */
.button {
    background: var(--rainbow);
    border: none;
    padding: 8px 14px;
    border-radius: 6px;
    font-weight: bold;
    color: white !important;
    text-decoration: none;
    display: inline-block;
}
.button:hover {
    opacity: 0.85;
}

/* Table header rainbow */
table th {
    background: var(--rainbow);
    color: white;
    padding: 8px;
}

/* Link hover rainbow underline */
a {
    color: inherit;
    text-decoration: none;
    position: relative;
}
a::after {
    content: "";
    position: absolute;
    width: 100%;
    height: 2px;
    left: 0;
    bottom: -2px;
    background: var(--rainbow);
    transform: scaleX(0);
    transition: transform 0.3s ease;
}
a:hover::after {
    transform: scaleX(1);
}
</style>

### <span class="rainbow-text">Me and Team</span>

Hi! My name is Avantika Chittari.

| Role         | Name     | Repo Location                                                                 | Stream                | Repo Name |
|--------------|----------|-------------------------------------------------------------------------------|-----------------------|-----------|
| Scrum Master | John     | [github.com/jm1021/student](https://github.com/jm1021/student)                | upstream (OCS fork)   | student   |
| Scrummer     | Torin    | [github.com/torin/student](https://github.com/torin/student)                   | downstream (fork)     | student   |
| Scrummer     | Avantika | [github.com/avantika/student](https://github.com/avantika/student)             | downstream (fork)     | student   |
| Scrummer     | Aadit    | [github.com/aaadit/student](https://github.com/aaadit/student)                 | downstream (fork)     | student   |


## <span class="rainbow-text">Links to Learning</span>

### <span class="rainbow-text">Development Environment</span>

> Coding starts with tools, explore these tools and procedures with a click.

<a href="https://github.com/Open-Coding-Society/student" class="button">GitHub</a>
<a href="https://open-coding-society.github.io/student" class="button">GitHub Pages</a>
<a href="https://kasm.opencodingsociety.com/" class="button">KASM</a>
<a href="https://vscode.dev/" class="button">VSCODE</a>

<br><br>

### <span class="rainbow-text">Class Progress</span>

<a href="{{site.baseurl}}/snake" class="button">Snake Game</a>
<a href="{{site.baseurl}}/turtle" class="button">Turtle</a>

<br><br>

### <span class="rainbow-text">Get in Touch</span>

> Feel free to reach out if you'd like to collaborate or learn more about our work.

<p>Open Coding Society: <a href="https://opencodingsociety.com">Socials</a></p>
