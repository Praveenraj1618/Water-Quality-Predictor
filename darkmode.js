function toggleDarkMode() {
    document.body.classList.toggle("dark");
    localStorage.setItem("dark-mode", document.body.classList.contains("dark") ? "on" : "off");
  }
  
  window.onload = function () {
    if (localStorage.getItem("dark-mode") === "on") {
      document.body.classList.add("dark");
      document.querySelector('.dark-toggle input').checked = true;
    }
  };
  
