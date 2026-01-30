async function handleLogin() {
  const email = document.getElementById("login_email").value;
  const password = document.getElementById("login_password").value;

  if (!email || !password) {
    alert("Fill all fields");
    return;
  }

  const formData = new URLSearchParams();
  formData.append("username", email);
  formData.append("password", password);

  try {
    const res = await fetch(
      "https://backend-tracker-production.up.railway.app/auth/login",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        body: formData.toString()
      }
    );

    const data = await res.json();

    if (!res.ok) {
      alert("❌ Invalid credentials");
      return;
    }

    console.log("✅ Login success:", data);

    localStorage.setItem("token", data.access_token);

    window.location.href = "dashboard.html";

  } catch (err) {
    console.error(err);
    alert("Server error");
  }
}
