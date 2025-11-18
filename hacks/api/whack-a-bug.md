---
layout: base
title: Whack-a-Bug
permalink: /whack-a-bug
---

<style>
#grid {
  width: 330px;
  margin: 20px auto;
  display: grid;
  grid-template-columns: repeat(3, 100px);
  gap: 10px;
}

.square {
  width: 100px;
  height: 100px;
  background: #fff;
  border: 3px solid #9b59b6;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 50px;
  cursor: pointer;
  transition: background 0.2s;
}

.bug {
  font-size: 50px;
}

#score, #timer {
  font-size: 20px;
  margin: 10px;
}

#startBtn {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 18px;
  background: #9b59b6;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}
</style>

<div id="gameContainer">
  <h1>Whack-a-Bug</h1>
  <div id="score">Score: 0</div>
  <div id="timer">Time: 30</div>
  <button id="startBtn">Start Game</button>
  <div id="grid"></div>
</div>

<script>
const grid = document.getElementById("grid");
const scoreDisplay = document.getElementById("score");
const timerDisplay = document.getElementById("timer");
const startBtn = document.getElementById("startBtn");

let score = 0;
let timeLeft = 30;
let gameInterval;
let bugTimeout;
let currentBug = null;

// Create 9 squares
for (let i = 0; i < 9; i++) {
  const square = document.createElement("div");
  square.classList.add("square");
  square.dataset.id = i;
  grid.appendChild(square);

  square.addEventListener("click", () => {
    if (square.classList.contains("bug")) {
      score++;
      scoreDisplay.textContent = "Score: " + score;
      removeBug();
    }
  });
}

function startGame() {
  score = 0;
  timeLeft = 30;
  scoreDisplay.textContent = "Score: 0";
  timerDisplay.textContent = "Time: 30";

  startBtn.disabled = true;

  gameInterval = setInterval(() => {
    timeLeft--;
    timerDisplay.textContent = "Time: " + timeLeft;

    if (timeLeft <= 0) {
      endGame();
    }
  }, 1000);

  spawnBug();
}

function spawnBug() {
  removeBug();

  const squares = document.querySelectorAll(".square");
  const randomSquare = squares[Math.floor(Math.random() * squares.length)];

  randomSquare.classList.add("bug");
  randomSquare.textContent = "🐞";
  currentBug = randomSquare;

  bugTimeout = setTimeout(spawnBug, 2000 + Math.random() * 1000);
}

function removeBug() {
  if (currentBug) {
    currentBug.classList.remove("bug");
    currentBug.textContent = "";
    currentBug = null;
  }
  clearTimeout(bugTimeout);
}

function endGame() {
  clearInterval(gameInterval);
  removeBug();
  startBtn.disabled = false;
  alert("Time's up! Your score: " + score);
}

startBtn.addEventListener("click", startGame);
</script>
