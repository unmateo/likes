function search() {
    let form = document.getElementById("search-form");
    let query = form.query.value;
    window.location.href = `/search/${query}`;
}
