import '/css/calculadora.css';

const calculator = document.querySelector(‘.calculator’)
const keys = calculator.querySelector(‘.calculator__keys’)

keys.addEventListener(‘click’, e => {
 if (e.target.matches(‘button’)) {
   // Fazer algo
 }
})
if (!action) {
    if (
      displayedNum === '0' ||
      previousKeyType === 'operator' ||
      previousKeyType === 'calculate'
    ) {
      display.textContent = keyContent
    } else {
      display.textContent = displayedNum + keyContent
    }
    calculator.dataset.previousKeyType = 'number'
  }
  
  if (action === 'decimal') {
    if (!displayedNum.includes('.')) {
      display.textContent = displayedNum + '.'
    } else if (
      previousKeyType === 'operator' ||
      previousKeyType === 'calculate'
    ) {
      display.textContent = '0.'
    }
    
  calculator.dataset.previousKeyType = 'decimal'
  }