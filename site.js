// Mobile menu, current year, and pre-select the service from ?service= on the contact page.
const btn = document.querySelector(".menu-btn");
const nav = document.getElementById("nav");
btn?.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  btn.setAttribute("aria-expanded", String(open));
});
const yr = document.getElementById("yr");
if (yr) yr.textContent = new Date().getFullYear();
const want = new URLSearchParams(location.search).get("service");
const sel = document.getElementById("service");
if (want && sel) for (const o of sel.options) if (o.text === want) o.selected = true;
