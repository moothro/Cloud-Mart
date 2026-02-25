// Mobile nav toggle
const navToggle = document.getElementById("navToggle");
const navMenu = document.getElementById("navMenu");

if (navToggle && navMenu) {
  navToggle.addEventListener("click", () => {
    const isOpen = navMenu.classList.toggle("show");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });
}

// FAQ accordion
document.querySelectorAll(".faq-q").forEach((btn) => {
  btn.addEventListener("click", () => {
    const expanded = btn.getAttribute("aria-expanded") === "true";
    btn.setAttribute("aria-expanded", String(!expanded));
  });
});

// Footer year
document.getElementById("year").textContent = new Date().getFullYear();

// Demo toast
const toastBtn = document.getElementById("demoToast");
const toast = document.getElementById("toast");

if (toastBtn && toast) {
  toastBtn.addEventListener("click", () => {
    toast.classList.add("show");
    window.setTimeout(() => toast.classList.remove("show"), 2200);
  });
}
