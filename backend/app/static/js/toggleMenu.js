function toggleMenu() {
    const menu = document.getElementById("menu");
    menu.style.width = menu.style.width === "250px" ? "0" : "250px";
}

function showCategory(category) {
    document.querySelectorAll(".category-content").forEach((content) => {
        content.style.display = "none";
    });
    document.getElementById(category).style.display = "grid";
}