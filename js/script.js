function some(el) {
    var btn = document.getElementById(el);
    var border = document.getElementById("containerteste");
    var border1 = document.getElementById("containerteste1");
    var border2 = document.getElementById("containerteste2");
    var computedStyle = window.getComputedStyle(btn); // Obter o estilo computado

    if (computedStyle.display === 'none') {
        btn.style.display = 'block'; // Use block em vez de flex para elementos de bloco
        border.style.borderBottom = '0px';
        border1.style.borderBottom = '0px';
        border2.style.borderBottom = '0px';
    } else {
        btn.style.display = 'none';
        border.style.borderBottom = '2px solid #7c0109';
        border1.style.borderBottom = '2px solid #7c0109';
        border2.style.borderBottom = '2px solid #7c0109';
    }
}