var burgerMenu = document.getElementById('mcflurry');
var show = document.getElementById('menu');
  
burgerMenu.addEventListener('click', function(){
    this.classList.toggle("close");
    show.classList.toggle("show");
})