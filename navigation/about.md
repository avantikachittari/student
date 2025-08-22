---
layout: post
title: About
permalink: /about/
comments: true
---

## As a conversation Starter

Here are some places I have lived.

<comment>
Flags are made using Wikipedia images
</comment>

<style>
   /* 🌸 Pastel Theme Styling */

   body {
       background: linear-gradient(to bottom, #F8C8DC, #CDB4DB, #A2D2FF);
       font-family: 'Arial', sans-serif;
       color: #444;
   }

   .grid-container {
       display: grid;
       grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); /* Dynamic columns */
       gap: 10px;
   }

   .grid-item {
       text-align: center;
       background: #FFF5B7;
       border-radius: 12px;
       padding: 10px;
       box-shadow: 0 2px 8px rgba(0,0,0,0.1);
       transition: transform 0.2s;
   }

   .grid-item:hover {
       transform: scale(1.05);
       background: #FFD6A5;
   }

   .grid-item img {
       width: 100%;
       height: 100px; /* Fixed height for uniformity */
       object-fit: contain;
   }

   .grid-item p {
       margin: 5px 0;
   }

   .image-gallery {
       display: flex;
       flex-wrap: nowrap;
       overflow-x: auto;
       gap: 10px;
   }

   .image-gallery img {
       max-height: 150px;
       object-fit: cover;
       border-radius: 10px;
   }
</style>

<!-- This grid_container class is used by CSS styling and the id is used by JavaScript connection -->
<div class="grid-container" id="grid_container">
   <!-- content will be added here by JavaScript -->
</div>

<script>
   // Connect to HTML container
   var container = document.getElementById("grid_container");

   // Flags + descriptions
   var http_source = "https://upload.wikimedia.org/wikipedia/commons/";
   var living_in_the_world = [
       {"flag": "0/01/Flag_of_California.svg", "greeting": "Hey", "description": "California - Lived here for the past 12 years"},
       {"flag": "b/b9/Flag_of_Oregon.svg", "greeting": "Hi", "description": "Oregon - 9 years"},
       {"flag": "b/be/Flag_of_England.svg", "greeting": "Alright mate", "description": "England - 2 years"},
       {"flag": "e/ef/Flag_of_Hawaii.svg", "greeting": "Aloha", "description": "Hawaii - 2 years"},
   ];

   // Build grid items
   for (const location of living_in_the_world) {
       var gridItem = document.createElement("div");
       gridItem.className = "grid-item";

       var img = document.createElement("img");
       img.src = http_source + location.flag;
       img.alt = location.flag + " Flag";

       var description = document.createElement("p");
       description.textContent = location.description;

       var greeting = document.createElement("p");
       greeting.textContent = location.greeting;

       gridItem.appendChild(img);
       gridItem.appendChild(description);
       gridItem.appendChild(greeting);

       container.appendChild(gridItem);
   }
</script>

---

### About Me

Hi, I'm Avantika!
