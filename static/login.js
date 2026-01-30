console.log("login.js loaded");

async function handleLogin() {
  const email = document.getElementById("login_email").value;
  const password = document.getElementById("login_password").value;

  if (!email || !password) {
    alert("Fill all fields");
    return;
  }

  try {
    const res = await fetch(
      "https://backend-tracker-production.up.railway.app/auth/login",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
      }
    );

    const data = await res.json();
    console.log(data);

    if (res.ok) {
      alert("Login successful");
      window.location.href = "dashboard.html";
    } else {
      alert(data.detail || "Invalid credentials");
    }

  } catch (err) {
    console.error(err);
    alert("Server error");
  }
}
