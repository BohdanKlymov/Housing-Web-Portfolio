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

document.addEventListener("DOMContentLoaded", () => {
  setLanguage("de");
  showSection("home");
});
