function showImage(element) {
    var listItem = element.closest('.film-li');
    listItem.classList.add('show');
}

function hideImage(element) {
    var listItem = element.closest('.film-li');

    setTimeout(function() {
        listItem.classList.remove('show');
    }, 1000);

}