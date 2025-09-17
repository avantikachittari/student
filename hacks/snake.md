---
layout: base
title: Snake Game
permalink: /snake/
---
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Epic Snake Game</title>
<style>
    body {
        margin: 0;
        background: #111;
        color: #eee;
        font-family: Arial, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        flex-direction: column;
    }
    canvas {
        border: 5px solid cyan;
        background: black;
        display: none;
        box-shadow: 0 0 20px cyan;
    }
    #menu, #settings, #gameover {
        text-align: center;
        padding: 20px;
        background: #222;
        border-radius: 15px;
        box-shadow: 0 0 20px #0ff;
    }
    h1 {
        color: #39FF14;
        text-shadow: 0 0 15px #39FF14;
    }
    button {
        margin: 10px;
        padding: 10px 20px;
        font-size: 18px;
        border: none;
        border-radius: 10px;
        background: #ff1493;
        color: #fff;
        cursor: pointer;
        box-shadow: 0 0 10px #ff1493;
        transition: 0.2s;
    }
    button:hover {
        background: #39FF14;
        box-shadow: 0 0 20px #39FF14;
    }
</style>
</head>
<body>

<div id="menu">
    <h1>Snake Game</h1>
    <button onclick="startGame()">Play</button>
    <button onclick="showSettings()">Settings</button>
</div>

<div id="settings" style="display:none;">
    <h1>Settings</h1>
    <label>Snake Speed:
        <select id="speed">
            <option value="150">Slow</option>
            <option value="100" selected>Normal</option>
            <option value="70">Fast</option>
        </select>
    </label><br><br>
    <label>Snake Growth:
        <input type="number" id="growth" value="3" min="1" max="10">
    </label><br><br>
    <button onclick="backToMenu()">Back</button>
</div>

<div id="gameover" style="display:none;">
    <h1>Game Over</h1>
    <p id="scoreDisplay"></p>
    <button onclick="startGame()">Restart</button>
    <button onclick="backToMenu()">Menu</button>
</div>

<canvas id="gameCanvas" width="600" height="400"></canvas>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let snake, foods, obstacles, dx, dy, speed, growth, score, lives, interval;

// --- UI ---
function showSettings() {
    document.getElementById("menu").style.display = "none";
    document.getElementById("settings").style.display = "block";
}
function backToMenu() {
    document.getElementById("settings").style.display = "none";
    document.getElementById("gameover").style.display = "none";
    document.getElementById("menu").style.display = "block";
}

// --- Game Setup ---
function startGame() {
    document.getElementById("menu").style.display = "none";
    document.getElementById("settings").style.display = "none";
    document.getElementById("gameover").style.display = "none";
    canvas.style.display = "block";

    speed = parseInt(document.getElementById("speed").value);
    growth = parseInt(document.getElementById("growth").value);
    score = 0;
    lives = 3;

    snake = [{x: 10, y: 10}];
    dx = 1; dy = 0;

    foods = [];
    spawnFood();
    spawnFood(); // multiple foods
    obstacles = [];
    spawnObstacles();

    if (interval) clearInterval(interval);
    interval = setInterval(update, speed);
}

// --- Spawn Functions ---
function spawnFood() {
    let f = {
        x: Math.floor(Math.random() * 30),
        y: Math.floor(Math.random() * 20),
        color: ["#FF1493","#FFD700","#1E90FF"][Math.floor(Math.random()*3)]
    };
    foods.push(f);
}
function spawnObstacles() {
    for (let i=0;i<5;i++) {
        obstacles.push({
            x: Math.floor(Math.random()*30),
            y: Math.floor(Math.random()*20)
        });
    }
}

// --- Draw ---
function draw() {
    ctx.fillStyle = "#000";
    ctx.fillRect(0,0,canvas.width,canvas.height);

    // Snake
    snake.forEach((s,i)=>{
        ctx.fillStyle = i===0 ? "#39FF14" : "#7FFF00";
        ctx.shadowBlur = i===0 ? 15 : 0;
        ctx.shadowColor = "#39FF14";
        ctx.fillRect(s.x*20,s.y*20,20,20);
    });
    ctx.shadowBlur = 0;

    // Food
    foods.forEach(f=>{
        ctx.fillStyle = f.color;
        ctx.shadowBlur = 15;
        ctx.shadowColor = f.color;
        ctx.beginPath();
        ctx.arc(f.x*20+10,f.y*20+10,10,0,Math.PI*2);
        ctx.fill();
    });
    ctx.shadowBlur = 0;

    // Obstacles
    ctx.fillStyle = "#888";
    obstacles.forEach(o=>{
        ctx.fillRect(o.x*20,o.y*20,20,20);
    });

    // Score + Lives
    ctx.fillStyle="#fff";
    ctx.font="18px Arial";
    ctx.fillText("Score: "+score,10,20);
    ctx.fillText("Lives: "+lives,500,20);
}

// --- Update ---
function update() {
    let head = {x: snake[0].x+dx, y: snake[0].y+dy};

    // Wall wrap
    if (head.x<0) head.x=29;
    if (head.x>29) head.x=0;
    if (head.y<0) head.y=19;
    if (head.y>19) head.y=0;

    // Collision with self
    if (snake.some(s=>s.x===head.x && s.y===head.y)) return loseLife();

    // Collision with obstacles
    if (obstacles.some(o=>o.x===head.x && o.y===head.y)) return loseLife();

    snake.unshift(head);

    // Eating food
    let ate=false;
    foods.forEach((f,i)=>{
        if (head.x===f.x && head.y===f.y) {
            ate=true;
            score+=10;
            foods.splice(i,1);
            spawnFood();

            // grow snake
            for (let j=0;j<growth;j++) {
                snake.push({...snake[snake.length-1]});
            }
        }
    });

    if (!ate) {
        snake.pop(); // normal movement
    }

    draw();
}

function loseLife() {
    lives--;
    if (lives<=0) {
        clearInterval(interval);
        canvas.style.display="none";
        document.getElementById("gameover").style.display="block";
        document.getElementById("scoreDisplay").innerText="Final Score: "+score;
    } else {
        snake=[{x:10,y:10}];
        dx=1;dy=0;
    }
}

// --- Controls (Arrows + WASD) ---
document.addEventListener("keydown",e=>{
    if ((e.key==="ArrowUp"||e.key==="w") && dy!==1){dx=0;dy=-1;}
    else if ((e.key==="ArrowDown"||e.key==="s") && dy!==-1){dx=0;dy=1;}
    else if ((e.key==="ArrowLeft"||e.key==="a") && dx!==1){dx=-1;dy=0;}
    else if ((e.key==="ArrowRight"||e.key==="d") && dx!==-1){dx=1;dy=0;}
});
</script>

</body>
</html>
