const menuBtn = document.querySelector('.menu-btn');
let menuOpen = false;
menuBtn.addEventListener('click', () => {
  if(!menuOpen) {
    menuBtn.classList.add('open');
    menuOpen = true;
    let openMenuBar= document.getElementById("popupMenuItems")
    openMenuBar.style.display="block"; // opens the menu
   
  } else {
    menuBtn.classList.remove('open');
    menuOpen = false;
    let openMenuBar= document.getElementById("popupMenuItems")
    openMenuBar.style.display="none"; //closes the menu
  }

});