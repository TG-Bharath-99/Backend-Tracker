document.addEventListener("DOMContentLoaded", () => {
  console.log("✅ Script loaded successfully");
  console.log("📍 Current location:", window.location.href);
  loadCourses();
});

function loadCourses() {
  console.log("🔄 Fetching courses...");
  
  // Use relative URL - this is the key fix!
  fetch("/courses")
    .then(res => {
      console.log("📥 Response received:", res.status);
      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }
      return res.json();
    })
    .then(data => {
      console.log("✅ Data received:", data);
      const container = document.getElementById("courses");
      container.innerHTML = "";

      if (!data || data.length === 0) {
        container.innerHTML = "<p>No courses available</p>";
        return;
      }

      data.forEach(course => {
        const div = document.createElement("div");
        div.className = "course";
        div.innerText = course.course_name;
        div.onclick = () => selectCourse(course.id, course.course_name);
        container.appendChild(div);
      });
    })
    .catch(error => {
      console.error("❌ Error loading courses:", error);
      alert("Failed to load courses: " + error.message);
    });
}

function selectCourse(courseId, courseName) {
  console.log(`Selected course: ${courseName} (ID: ${courseId})`);
  alert(`You selected: ${courseName}`);
}