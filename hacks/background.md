---
layout: default 
title: Background with Object
description: Use JavaScript to have an in motion background.
sprite: images/platformer/sprites/Butterfly.png
background: images/platformer/backgrounds/sky.jpg
permalink: /Back
---

<!-- Canvas for the game -->
<canvas id="world"></canvas> 

<script>
  /* Load canvas + images */
  const canvas = document.getElementById("world"); 
  const ctx = canvas.getContext('2d');
  const backgroundImg = new Image(); 
  const spriteImg = new Image();  
  backgroundImg.src = '{{page.background}}';
  spriteImg.src = '{{page.sprite}}';
   
  /* Wait for both images to load */
  let imagesLoaded = 0; 
  backgroundImg.onload = function() {
    imagesLoaded++;
    startGameWorld();
  };
  spriteImg.onload = function() {
    imagesLoaded++;
    startGameWorld();
  };

  function startGameWorld() {
    if (imagesLoaded < 2) return;

    /* Base object class */
    class GameObject {
      constructor(image, width, height, x = 0, y = 0, speedRatio = 0) {
        this.image = image;
        this.width = width;
        this.height = height;
        this.x = x;
        this.y = y;
        this.speedRatio = speedRatio;
        this.speed = GameWorld.gameSpeed * this.speedRatio;
      }
      update() {}
      draw(ctx) {
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
      }
    }

    /* Scrolling background */
    class Background extends GameObject {
      constructor(image, gameWorld) {
        super(image, gameWorld.width, gameWorld.height, 0, 0, 0.1);
      }
      update() {
        this.x = (this.x - this.speed) % this.width;
      }
      draw(ctx) {
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
        ctx.drawImage(this.image, this.x + this.width, this.y, this.width, this.height);
      }
    }

    /* Player with sine movement */
    class Player extends GameObject {
      constructor(image, gameWorld) {
        const width = image.naturalWidth / 2;
        const height = image.naturalHeight / 2;
        const x = (gameWorld.width - width) / 2;
        const y = (gameWorld.height - height) / 2;
        super(image, width, height, x, y);
        this.baseY = y;
        this.frame = 0;
      }
      update() {
        this.y = this.baseY + Math.sin(this.frame * 0.05) * 20;
        this.frame++;
      }
    }

    /* Game manager + loop */
    class GameWorld {
      static gameSpeed = 5;
      constructor(backgroundImg, spriteImg) {
        this.canvas = document.getElementById("world");
        this.ctx = this.canvas.getContext('2d');
        this.width = window.innerWidth;
        this.height = window.innerHeight;
        this.canvas.width = this.width;
        this.canvas.height = this.height;
        this.canvas.style.width = `${this.width}px`;
        this.canvas.style.height = `${this.height}px`;
        this.canvas.style.position = 'absolute';
        this.canvas.style.left = `0px`;
        this.canvas.style.top = `${(window.innerHeight - this.height) / 2}px`;

        // Add background + player
        this.objects = [
          new Background(backgroundImg, this),
          new Player(spriteImg, this)
        ];
      }

      /* Main loop */
      gameLoop() {
        this.ctx.clearRect(0, 0, this.width, this.height);
        for (const obj of this.objects) {
          obj.update();
          obj.draw(this.ctx);
        }
        requestAnimationFrame(this.gameLoop.bind(this));
      }
      start() {
        this.gameLoop();
      }
    }
      
    /* Create + start game */
    const world = new GameWorld(backgroundImg, spriteImg);
    world.start();
  }
</script>
