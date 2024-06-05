function some(el) {
    var btn = document.getElementById(el);
    var computedStyle = window.getComputedStyle(btn); // Obter o estilo computado

    if (computedStyle.display === 'none') {
        btn.style.display = 'flex';
    } else if (computedStyle.display === 'flex') {
        btn.style.display = 'none';
    }
}
