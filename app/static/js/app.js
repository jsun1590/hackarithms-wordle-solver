/*
bg code
0 = gray
1 = yellow
2 = green
*/

const NUMBER_OF_GUESSES = 6;
const NUMBER_OF_LETTERS = 5;

let currentGuess = 0;
let validWord = false;

const initBoard = () => {
    let board = document.getElementById("board");

    for (let i = 0; i < NUMBER_OF_GUESSES; i++) {
        let row = document.createElement("div");
        row.className = "guess-row";

        for (let j = 0; j < NUMBER_OF_LETTERS; j++) {
            let cell = document.createElement("div");
            cell.className = "guess-cell";
            cell.setAttribute("bg", "-1");
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
    const colors = ["#787c7e", "#c9b458", "#6aaa64"];

    e.target.style.color = "white";

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

const displayWord = (data) => {
    let suggestedWord = document.getElementById("suggested-word");
    console.log(data);
    suggestedWord.innerText = data;
};

// const checkWord = async () => {
//     let payload2 = [];
//     for (let i = 0; i < currentGuess + 1; i++) {
//         let word = {};
//         for (let j = 0; j < NUMBER_OF_LETTERS; j++) {
//             word[j] = [
//                 document.getElementById(`${i}-${j}`).innerText,
//                 document.getElementById(`${i}-${j}`).getAttribute("bg"),
//             ];
//         }
//         payload2.push(word);
//     }

//     payload2 = JSON.stringify(payload2);
//     console.log(payload2);

//     let res = await fetch("api/validate_word", {
//         method: "POST",
//         headers: {
//             Accept: "application/json, text/plain, */*",
//             "Content-Type": "application/json",
//         },
//         body: payload2,
//     });

//     let data = await res.json();
//     console.log("data", await data);
//     validWord = (await data) === "true";
//     return validWord;
// };

const sendData = () => {
    let payload = [];
    for (let i = 0; i < currentGuess; i++) {
        let word = {};
        for (let j = 0; j < NUMBER_OF_LETTERS; j++) {
            word[j] = [
                document.getElementById(`${i}-${j}`).innerText,
                document.getElementById(`${i}-${j}`).getAttribute("bg"),
            ];
        }
        payload.push(word);
    }

    payload = JSON.stringify(payload);
    console.log(payload);

    fetch("api/process_words", {
        method: "POST",
        headers: {
            Accept: "application/json, text/plain, */*",
            "Content-Type": "application/json",
        },
        body: payload,
    })
        .then((res) => {
            return res.json();
        })
        .then((data) => {
            displayWord(data);
        })
        .catch((err) => {
            console.log(err);
        });
};

enterText = (e) => {
    e = e || window.event;

    // test if char is a letter
    if (/^[A-Za-z]$/.test(e.key)) {
        for (let i = 0; i < NUMBER_OF_LETTERS; i++) {
            if (
                document.getElementById(`${currentGuess}-${i}`).innerText === ""
            ) {
                document.getElementById(`${currentGuess}-${i}`).innerText =
                    e.key.toUpperCase();
                break;
            }
        }
    } else if (e.key === "Backspace") {
        for (let i = NUMBER_OF_LETTERS - 1; i >= 0; i--) {
            if (
                document.getElementById(`${currentGuess}-${i}`).innerText !== ""
            ) {
                document.getElementById(`${currentGuess}-${i}`).innerText = "";
                break;
            }
        }
    } else if (e.key === "Enter") {
        if (currentGuess >= NUMBER_OF_GUESSES - 1) return;
        let currentWord = 0;
        for (let i = 0; i < NUMBER_OF_LETTERS; i++) {
            if (
                document.getElementById(`${currentGuess}-${i}`).innerText !== ""
            ) {
                currentWord += 1;
            }

            if (
                document
                    .getElementById(`${currentGuess}-${i}`)
                    .getAttribute("bg") === "-1"
            ) {
                return;
            }
        }
        if (currentWord !== NUMBER_OF_LETTERS) return;
        // if (!checkWord()) {
        //     console.log("not a valid word");
        //     console.log("check word", validWord);
        //     return;
        // }
        currentGuess++;
        sendData();

        activeGuess();
        console.log("check word", validWord);
    }
};
initBoard();
activeGuess();
const cells = document.querySelectorAll(".guess-cell");
cells.forEach((el) => el.addEventListener("click", changeBgColor));
document.addEventListener("keydown", enterText, false);
