const API = "";

document.addEventListener("DOMContentLoaded", () => {
  loadCourses();
});

function loadCourses() {
  fetch(`${API}/courses`)
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById("courses");
      container.innerHTML = "";

      data.forEach(course => {
        const div = document.createElement("div");
        div.className = "course";
        div.innerText = course.course_name;
        container.appendChild(div);
      });
    })
    .catch(() => {
      alert("API error");
    });
}
