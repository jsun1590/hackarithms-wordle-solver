const NUMBER_OF_GUESSES = 6;
const NUMBER_OF_LETTERS = 5;

let currentGuess = 0;
let currentWord = "";

const initBoard = () => {
  let board = document.getElementById("board");

  for (let i = 0; i < NUMBER_OF_GUESSES; i++) {
    let row = document.createElement("div");
    row.className = "guess-row";

    for (let j = 0; j < NUMBER_OF_LETTERS; j++) {
      let cell = document.createElement("div");
      cell.className = "guess-cell";
      cell.setAttribute("bg", "0");
      cell.id = `${i}-${j}`;
      row.appendChild(cell);
    }
    board.appendChild(row);
  }
};

const changeBgColor = (e) => {
  if (currentGuess.toString() !== e.target.id.split("-")[0]) {
    return;
  }
  const colors = ["#6aaa64", "#c9b458", "#787c7e"];

  let index = parseInt(e.target.getAttribute("bg"));
  index = (index + 1) % colors.length;

  e.target.style.backgroundColor = colors[index];
  e.target.setAttribute("bg", index);
};

const activeGuess = () => {
  for (let i = 0; i < NUMBER_OF_GUESSES; i++) {
    for (let j = 0; j < NUMBER_OF_LETTERS; j++) {
      let cell = document.getElementById(`${i}-${j}`);
      if (currentGuess === i) {
        cell.style.border = "4px solid black";
        cell.style.cursor = "pointer";
      } else {
        cell.style.border = "2px solid gray";
        cell.style.cursor = "default";
      }
    }
  }
};
enterText = (e) => {
  e = e || window.event;

  if (/^[A-Za-z]$/.test(e.key)) {
    for (let i = 0; i < NUMBER_OF_LETTERS; i++) {
      if (document.getElementById(`${currentGuess}-${i}`).innerText === "") {
        document.getElementById(`${currentGuess}-${i}`).innerText = e.key;
        currentWord += e.key;
        break;
      }
    }
  } else if (e.key === "Backspace") {
    for (let i = NUMBER_OF_LETTERS - 1; i >= 0; i--) {
      if (document.getElementById(`${currentGuess}-${i}`).innerText !== "") {
        document.getElementById(`${currentGuess}-${i}`).innerText = "";
        currentWord = currentWord.slice(0, -1);
        break;
      }
    }
  } else if (e.key === "Enter") {
    if (currentWord.length !== NUMBER_OF_LETTERS) return;
    for (let i = 0; i < NUMBER_OF_LETTERS; i++) {
      if (
        document.getElementById(`${currentGuess}-${i}`).getAttribute("bg") ===
        "0"
      ) {
        return;
      }
      currentGuess++;
      currentWord = "";
      activeGuess();
    }
  }
};
initBoard();
activeGuess();
const cells = document.querySelectorAll(".guess-cell");
cells.forEach((el) => el.addEventListener("click", changeBgColor));
document.addEventListener("keydown", enterText, false);
