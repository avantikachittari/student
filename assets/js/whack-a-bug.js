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
