// Javascript section to ensure that the search input stays in the search bar when clicking on pagination buttons -->

// Get search form and page link
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

// Ensure search form exists
if(searchForm){
    for(let i=0; pageLinks.length >i; i++){
        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault() // On click stop whatever the default action would be
            
            // Get the data attribute
            let page = this.dataset.page
            //console.log('PAGE:', page)

            // Add hidden search input to form
            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

            // Submit form
            searchForm.submit()
        })
    }
}