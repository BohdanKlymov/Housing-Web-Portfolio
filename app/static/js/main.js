let currentLang = "de";

function setLanguage(lang) {
  currentLang = lang;
  document.querySelectorAll("[data-de]").forEach(el => {
    el.textContent = el.dataset[lang];
  });
}

function showSection(id) {
  const sections = document.querySelectorAll(".section");
  sections.forEach(s => {
    s.classList.remove("active");
    s.style.display = "none";
  });

  const target = document.getElementById(id);
  target.style.display = "block";
  requestAnimationFrame(() => target.classList.add("active"));
}

function toggleTheme() {
  const theme = document.body.dataset.theme === "dark" ? "" : "dark";
  document.body.dataset.theme = theme;
  localStorage.setItem("theme", theme);
}

document.addEventListener("DOMContentLoaded", () => {
  document.body.dataset.theme = localStorage.getItem("theme") || "";
  setLanguage("de");
  showSection("home");
});
