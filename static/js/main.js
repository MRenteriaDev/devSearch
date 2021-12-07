// GET SEARCH FORM AND PAGE LINKS
let searchForm = document.getElementById("searchForm");
let pageLinks = document.getElementsByClassName("page-link");

//ENSURE SEARCH FORM TEXTS
if (searchForm) {
  for (let i = 0; pageLinks.length > i; i++) {
    pageLinks[i].addEventListener("click", function (e) {
      e.preventDefault();
      // Get a data attribute
      let page = this.dataset.page;
      console.log("page :", page);

      // Add an hidden search input to form
      searchForm.innerHTML += `<input value=${page} name="page" hidden />`;

      // Submit form
      searchForm.submit();
    });
  }
}
