document.addEventListener("DOMContentLoaded", () => {
  console.log("signup.js loaded");

  const signupBtn = document.getElementById("signupBtn");

  signupBtn.addEventListener("click", async () => {
    console.log("signup button clicked");

    const full_name = document.getElementById("full_name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!full_name || !email || !password) {
      alert("Fill all fields");
      return;
    }

    const res = await fetch(
      "https://backend-tracker-production.up.railway.app/signup",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          full_name,
          email,
          password
        })
      }
    );

    const data = await res.json();
    console.log(data);

    alert(res.ok ? "Signup successful" : "Signup failed");
  });
});
