const articleTitles = document.querySelectorAll('.article-title');
articleTitles.forEach(title => {
    title.addEventListener('click', () => {
        const content = title.nextElementSibling;
        content.style.display = content.style.display === 'none' ? 'block' : 'none';
    });
});



// element.addEventListener('click', function () {
//     var x = document.getElementById(modifiedString);
//     if (x.style.display === "none") {
//         x.style.display = "block";
//     } else if (x.style.display === "block") {
//         x.style.display = "none";
//     }
// })
