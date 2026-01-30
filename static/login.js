console.log("login.js loaded");

const BASE_URL = "https://backend-tracker-production.up.railway.app";

async function handleLogin() {
  const email = document.getElementById("login_email").value;
  const password = document.getElementById("login_password").value;

  if (!email || !password) {
    alert("Email & password required");
    return;
  }

  try {
    const res = await fetch(`${BASE_URL}/auth/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        email: email,
        password: password
      })
    });

    const data = await res.json();
    console.log("Login response:", data);

    if (res.ok) {
      alert("Login successful");
      window.location.href = "/static/dashboard.html";
    } else {
      alert(data.detail || "Wrong email or password");
    }

  } catch (err) {
    console.error(err);
    alert("Server error");
  }
}
