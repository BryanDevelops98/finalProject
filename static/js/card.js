function flipCard(){
    this.classList.toggle('is-flipped');

}

document.getElementById("cardBryan").addEventListener("click", flipCard);
document.getElementById("cardCaleb").addEventListener("click", flipCard);
document.getElementById("cardDriverOne").addEventListener("click", flipCard);
document.getElementById("cardDriverTwo").addEventListener("click", flipCard);
document.getElementById("cardDriverThree").addEventListener("click", flipCard);


