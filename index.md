---
layout: base
title: I'm Avantika
hide: true
---


<style>
/* Ocean background */
body {
   background: linear-gradient(to bottom, #74ebd5, #ACB6E5);
   background-attachment: fixed;
   color: #222;
   font-family: Arial, sans-serif;
}


/* Light pink buttons */
.button {
   background-color: #f8c8dc;
   border: none;
   padding: 8px 14px;
   border-radius: 8px;
   font-weight: bold;
   color: #4a4a4a !important;
   text-decoration: none;
   display: inline-block;
   transition: transform 0.2s ease, background-color 0.2s ease;
}
.button:hover {
   background-color: #f7b5d4;
   transform: scale(1.05);
}


/* Table header styling */
table th {
   background-color: #6ec6d9;
   color: white;
   padding: 8px;
}


/* Pretty links */
a {
   color: #3b7ca8;
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
   background-color: #3b7ca8;
   transform: scaleX(0);
   transition: transform 0.3s ease;
}
a:hover::after {
   transform: scaleX(1);
}
</style>


### Me and Team


Hi! My name is Avantika Chittari.


| Role         | Name     | Repo Location                       | Stream                | Repo Name |
|--------------|----------|-------------------------------------|-----------------------|-----------|
| Scrum Master | John     | github.com/jm1021/student           | upstream (OCS fork)   | student   |
| Scrummer     | Torin    | github.com/torin/student            | downstream (fork)     | student   |
| Scrummer     | Avantika | github.com/avantika/student         | downstream (fork)     | student   |
| Scrummer     | Aadit    | github.com/aaadit/student           | downstream (fork)     | student   |


## Links to Learning


### Development Environment


> Coding starts with tools, explore these tools and procedures with a click.


<a href="https://github.com/Open-Coding-Society/student" class="button">GitHub</a>
<a href="https://open-coding-society.github.io/student" class="button">GitHub Pages</a>
<a href="https://kasm.opencodingsociety.com/" class="button">KASM</a>
<a href="https://vscode.dev/" class="button">VSCODE</a>


<br><br>


### Class Progress


<a href="{{site.baseurl}}/snake" class="button">Snake Game</a>
<a href="{{site.baseurl}}/turtle" class="button">Turtle</a>


<br><br>


### Get in Touch


> Feel free to reach out if you'd like to collaborate or learn more about our work.


<p>Open Coding Society: <a href="https://opencodingsociety.com">Socials</a></p>


/* Flower buttons */
.button {
    background-color: #f8c8dc;
    border: none;
    padding: 20px;
    border-radius: 50%; /* makes them circular like a flower center */
    font-weight: bold;
    color: #4a4a4a !important;
    text-decoration: none;
    display: inline-block;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    margin: 20px;
}

/* Petals using pseudo-elements */
.button::before, .button::after {
    content: "";
    position: absolute;
    width: 100%;
    height: 100%;
    background: #f8c8dc;
    border-radius: 50%;
    z-index: -1;
    transition: transform 0.3s ease;
}

/* Petal positions */
.button::before {
    top: -50%;
    left: 0;
}
.button::after {
    left: 50%;
    top: 0;
}

/* Hover effect: bloom like a flower */
.button:hover {
    transform: scale(1.1);
    box-shadow: 0 0 15px #f7b5d4, 0 0 30px #f7b5d4;
}
.button:hover::before {
    transform: translateY(-10px) scale(1.1);
}
.button:hover::after {
    transform: translateX(10px) scale(1.1);
}
