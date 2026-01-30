console.log("signup.js loaded");

const BASE_URL = "https://backend-tracker-production.up.railway.app";

async function handleSignup() {
  const full_name = document.getElementById("full_name").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (!full_name || !email || !password) {
    alert("All fields required");
    return;
  }

  try {
    const res = await fetch(`${BASE_URL}/auth/signup`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        full_name: full_name,
        email: email,
        password: password
      })
    });

    const data = await res.json();
    console.log("Signup response:", data);

    if (res.ok) {
      alert("Signup successful! Please login.");
      window.location.href = "/static/index.html";
    } else {
      alert(data.detail || "Signup failed");
    }

  } catch (err) {
    console.error(err);
    alert("Server error");
  }
}
