const paletteDiv = document.getElementById("palette");

const generateRandomColor = () => "#" + Math.floor(Math.random() * 0xffffff).toString(16).padStart(6, "0");

function generatePalette(){
    paletteDiv.innerHTML="";
    for(let i = 0; i < 5; i++){
        const color = generateRandomColor();
        paletteDiv.innerHTML += `<span class="color-box" style="background:${color}">${color.toUpperCase()}</span>`;
    }
}
generatePalette();
