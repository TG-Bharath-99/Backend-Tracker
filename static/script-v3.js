document.addEventListener("DOMContentLoaded", () => {
  console.log("✅ Script loaded successfully");
  console.log("📍 Current location:", window.location.href);
  loadCourses();
});

const BASE_URL = "https://backend-tracker-production.up.railway.app";

function loadCourses() {
  console.log("🔄 Fetching courses...");

  fetch(`${BASE_URL}/courses`)
    .then(res => {
      console.log("📥 Courses response:", res.status);
      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }
      return res.json();
    })
    .then(data => {
      console.log("✅ Courses received:", data);

      const coursesContainer = document.getElementById("courses");
      coursesContainer.innerHTML = "";

      if (!data || data.length === 0) {
        coursesContainer.innerHTML = "<p>No courses available</p>";
        return;
      }

      data.forEach(course => {
        const div = document.createElement("div");
        div.className = "course";
        div.textContent = course.course_name;

        
        div.onclick = () => loadTopics(course.id, course.course_name);

        coursesContainer.appendChild(div);
      });
    })
    .catch(error => {
      console.error("❌ Error loading courses:", error);
      alert("Failed to load courses: " + error.message);
    });
}


function loadTopics(courseId, courseName) {
  console.log(`📚 Loading topics for ${courseName} (ID: ${courseId})`);

  fetch(`${BASE_URL}/topics?course_id=${courseId}`)
    .then(res => {
      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }
      return res.json();
    })
    .then(data => {
      console.log("✅ Topics received:", data);

      const topicsContainer = document.getElementById("topics");
      topicsContainer.innerHTML = `
        <h3>${courseName} Topics</h3>
        <hr />
      `;

      if (!data || data.length === 0) {
        topicsContainer.innerHTML += "<p>No topics found</p>";
        return;
      }

      data.forEach(topic => {
        const div = document.createElement("div");
        div.className = "topic";

        div.innerHTML = `
          <h4>${topic.topic_name}</h4>
          <a href="${topic.youtube_url}" target="_blank">
            ▶ Watch Video
          </a>
        `;

        topicsContainer.appendChild(div);
      });
    })
    .catch(error => {
      alert("Failed to load topics: " + error.message);
    });
}

function showMotivation() {
  fetch("/motivation/random")
    .then(res => res.json())
    .then(data => {
      document.getElementById("motivation").innerText = data.message;
    });
}
