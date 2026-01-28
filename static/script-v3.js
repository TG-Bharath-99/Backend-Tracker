const BASE_URL = "https://backend-tracker-production.up.railway.app";

const loginForm = document.getElementById("loginForm");
const signupForm = document.getElementById("signupForm");
const message = document.getElementById("message");
const tabs = document.querySelectorAll(".tab");

function showLogin() {
  loginForm.classList.remove("hidden");
  signupForm.classList.add("hidden");
  tabs[0].classList.add("active");
  tabs[1].classList.remove("active");
  message.innerText = "";
}

function showSignup() {
  signupForm.classList.remove("hidden");
  loginForm.classList.add("hidden");
  tabs[1].classList.add("active");
  tabs[0].classList.remove("active");
  message.innerText = "";
}

loginForm.addEventListener("submit", e => {
  e.preventDefault();

  const email = document.getElementById("loginEmail").value;
  const password = document.getElementById("loginPassword").value;

  fetch(`${BASE_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  })
  .then(res => res.json())
  .then(data => {
    if (data.access_token) {
      localStorage.setItem("token", data.access_token);
      message.style.color = "green";
      message.innerText = "Login successful ✅";
      // redirect later
      // window.location.href = "dashboard.html";
    } else {
      message.style.color = "red";
      message.innerText = data.detail || "Login failed ❌";
    }
  })
  .catch(() => {
    message.style.color = "red";
    message.innerText = "Server error";
  });
});

signupForm.addEventListener("submit", e => {
  e.preventDefault();

  const name = document.getElementById("signupName").value;
  const email = document.getElementById("signupEmail").value;
  const password = document.getElementById("signupPassword").value;

  fetch(`${BASE_URL}/auth/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, email, password })
  })
  .then(res => res.json())
  .then(data => {
    message.style.color = "green";
    message.innerText = "Account created 🎉 Please login";
    showLogin();
  })
  .catch(() => {
    message.style.color = "red";
    message.innerText = "Signup failed ❌";
  });
});
