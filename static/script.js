function toggleMode(){
 let body = document.body;

 if(body.classList.contains("dark")){
   body.classList.remove("dark");
   body.classList.add("light");
 } else {
   body.classList.remove("light");
   body.classList.add("dark");
 }
}

function flipCard(btn){
 let card = btn.closest(".card");
 card.classList.toggle("flipped");
}