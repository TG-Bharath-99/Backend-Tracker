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

        // 🔥 CHANGE: load topics instead of alert
        div.onclick = () => loadTopics(course.id, course.course_name);

        container.appendChild(div);
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
      topicsContainer.innerHTML = `<h3>${courseName} Topics</h3>`;

      if (!data || data.length === 0) {
        topicsContainer.innerHTML += "<p>No topics found</p>";
        return;
      }

      data.forEach(topic => {
        const div = document.createElement("div");
        div.className = "topic";

        div.innerHTML = `
          <h4>${topic.topic_name}</h4>
          <p>${topic.subtopic_name}</p>
          <a href="${topic.resource_link}" target="_blank">
            Open Resource
          </a>
        `;

        topicsContainer.appendChild(div);
      });
    })
    .catch(error => {
      console.error("❌ Error loading topics:", error);
      alert("Failed to load topics: " + error.message);
    });
}
