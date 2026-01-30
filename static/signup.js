console.log("signup.js loaded");

async function handleSignup() {
  console.log("signup button clicked");

  const full_name = document.getElementById("full_name").value;
  const email = document.getElementById("login_email").value;
  const password = document.getElementById("login_password").value;

  if (!full_name || !email || !password) {
    alert("Fill all fields");
    return;
  }

  try {
    const res = await fetch(
      "https://backend-tracker-production.up.railway.app/auth/signup",
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
  } catch (err) {
    console.error(err);
    alert("Server error");
  }
}
