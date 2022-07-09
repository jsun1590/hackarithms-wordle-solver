const NUMBER_OF_GUESES = 5;
const NUMBER_OF_WORDS = 5;

const initBoard = () => {
  let board = document.getElementById("board");

  for (let i = 0; i < NUMBER_OF_GUESES; i++) {
    let row = document.createElement("div");
    row.className = "guess-row";

    for (let j = 0; j < NUMBER_OF_WORDS; j++) {
      let cell = document.createElement("div");
      cell.className = "guess-cell";
      row.appendChild(cell);
    }
    board.appendChild(row);
  }
};

initBoard();
