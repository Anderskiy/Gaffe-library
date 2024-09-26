function showImage(element) {
    var listItem = element.closest('.film-li'); // Найти текущий <li>
    listItem.classList.add('show'); // Добавить класс для показа изображения
}

function hideImage(element) {
    var listItem = element.closest('.film-li'); // Найти текущий <li>
    listItem.classList.remove('show'); // Убрать класс для скрытия изображения
}