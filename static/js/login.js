const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", function(event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    
    // Sample hardcoded credentials (in a real scenario, these should be stored securely)
    const validUsername = "admin";
    const validPassword = "secretpassword";
    
    if (username === validUsername && password === validPassword) {
        // Redirect to the user dashboard upon successful login
        // window.location.href = "dashboard.html";
        loginForm.submit()
    } else {
        alert("Invalid credentials. Please try again.");
    }
});
