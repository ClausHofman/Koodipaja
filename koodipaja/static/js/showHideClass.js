itemsAreHidden = true;
function renameElements() {
    if (itemsAreHidden)
        var visibilityElement = document.getElementById("VisibilityButton")
    else if (!itemsAreHidden)
        var visibilityElement = document.getElementById("HideButton")

    if (visibilityElement.id === "VisibilityButton") {
        itemsAreHidden = false;
        visibilityElement.setAttribute("id", "HideButton")
        visibilityElement.innerHTML = "Hide elements!"
        var elements = document.querySelectorAll('.hide')
        elements.forEach(function (element) {
            element.classList.replace('hide', 'show')
        })
    }
    else if (visibilityElement.id === "HideButton") {
        itemsAreHidden = true;
        var visibilityElement = document.getElementById("HideButton")
        visibilityElement.innerHTML = "Show elements!"
        var elements = document.querySelectorAll('.show')
        visibilityElement.setAttribute("id", "VisibilityButton")
        elements.forEach(function (element) {
            element.classList.replace('show', 'hide')
        });
    };
}