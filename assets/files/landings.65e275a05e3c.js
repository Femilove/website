let theme_switcher = document.querySelector(".theme-switcher");
let theme = localStorage.getItem("theme");
let icon = localStorage.getItem("icon");
setTheme(theme, icon);
theme_switcher.addEventListener("click", () => {
  if (theme_switcher.getAttribute("name") == "sunny-outline") {
    setTheme("dark", "moon-outline");
    theme_switcher.setAttribute("name", "moon-outline");
  } else {
    setTheme("light", "sunny-outline");
    theme_switcher.setAttribute("name", "sunny-outline");
  }
});

function setTheme(theme, icon) {
  document.documentElement.className = theme;
  theme_switcher.setAttribute("name", icon);
  localStorage.setItem("theme", theme);
  localStorage.setItem("icon", icon);
  if (
    (theme_switcher.getAttribute("name") == "" && theme == "") ||
    (theme == null && icon == null) ||
    (theme == "null" && icon == "null")
  ) {
    theme_switcher.setAttribute("name", "sunny-outline");
  }
}

let slideIndex = 0;
showSlides();

function showSlides() {
  const slides = document.getElementsByClassName("slide");
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none"; // Hide all slides
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1; // Reset to first slide
  }
  slides[slideIndex - 1].style.display = "block"; // Show the current slide
  setTimeout(showSlides, 3000); // Change slide every 3 seconds
}
