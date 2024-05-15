document.getElementById("login-btn").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent default form submission
  
    // Client-side email validation (optional)
    const email = document.getElementById("form2Example17").value;
    const emailRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()-_+=]).{8,}$/;
    if (!emailRegex.test(email)) {
      alert("Invalid email format. Please enter a valid email address.");
      return;
    }
  
    // Simulate form submission (replace with actual logic if needed)
    const form = document.getElementById("login-form");
    form.submit(); // Submit the form after validation
  
    // Show a loading indicator (optional)
    document.getElementById("login-btn").innerHTML = "Logging in...";
  });
  