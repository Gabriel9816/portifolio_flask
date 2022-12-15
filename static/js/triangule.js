const ladoA = document.getElementById('ladoA');
const ladoB = document.getElementById('ladoB');
const ladoC = document.getElementById('ladoC');

const trianguloParaCima = document.getElementById('triangulo-para-cima');

trianguloParaCima.style.borderLeftWidth = `${ladoA.value}px` 
trianguloParaCima.style.borderRightWidth = `${ladoB.value}px`
trianguloParaCima.style.borderBottomWidth = `${ladoC.value}px`
