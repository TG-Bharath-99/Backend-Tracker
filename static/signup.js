document.addEventListener("DOMContentLoaded", () => {
  const signupBtn = document.getElementById("signupBtn");

  signupBtn.addEventListener("click", async (e) => {
    e.preventDefault();

    const full_name = document.getElementById("full_name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!full_name || !email || !password) {
      alert("Fill all fields");
      return;
    }

    try {
      const res = await fetch(
        "https://backend-tracker-production.up.railway.app/routes_auth/signup",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            full_name: full_name,
            email: email,
            password: password
          })
        }
      );

      const data = await res.json();

      if (res.ok) {
        alert("Signup successful");
      } else {
        alert(data.detail || "Signup failed");
      }
    } catch (err) {
      alert("Server error");
      console.error(err);
    }
  });
});
