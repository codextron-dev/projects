const jokeText = document.getElementById("joke");
const deliveryText = document.getElementById("delivery");
const statusText = document.getElementById("status");
const button = document.getElementById("newJoke");

const API_URL =
  "https://v2.jokeapi.dev/joke/Any?safe-mode&type=single,twopart";

async function getJoke() {
  button.disabled = true;
  statusText.textContent = "Loading...";
  deliveryText.textContent = "";

  try {
    const response = await fetch(API_URL);

    if (!response.ok) {
      throw new Error("Could not get a joke.");
    }

    const joke = await response.json();

    if (joke.error || !joke.joke && !joke.setup) {
      throw new Error("No joke found.");
    }

    if (joke.type === "single") {
      jokeText.textContent = joke.joke;
      deliveryText.textContent = "";
    } else {
      jokeText.textContent = joke.setup;
      deliveryText.textContent = joke.delivery;
    }

    statusText.textContent = "";
  } catch (error) {
    jokeText.textContent = "Sorry, something went wrong.";
    deliveryText.textContent = "";
    statusText.textContent = "Try again";
  } finally {
    button.disabled = false;
  }
}

button.addEventListener("click", getJoke);

getJoke();