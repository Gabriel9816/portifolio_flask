window.onload = function() {
    let content512 = document.getElementsByClassName('content512')[0];

    for (let x = 1; x < 513; x++) {
        let row = document.createElement('div');
        row.className = 'row';
        row.id = 'row' + x;
        for (let i = 1; i < 513; i++) {
            row.appendChild(div1pixel(i))
        }
        content512.appendChild(row);
    }
}


function div1pixel(n) {
    let div1pixel = document.createElement('div');
    div1pixel.className = 'divs1pixel';
    div1pixel.id = 'div1pixel' + n;
    return div1pixel;
}