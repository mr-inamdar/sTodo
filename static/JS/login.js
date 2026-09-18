import { login } from "./api.js";

const loginForm = document.getElementById("loginForm");
const loginBtn = document.getElementById("loginBtn");
const authMessage = document.getElementById("authMessage");


loginForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    loginBtn.disabled = true;
    loginBtn.textContent = "Signing in...";

    authMessage.className = "auth-message";
    authMessage.textContent = "";


    const data = {

        email: document.getElementById("email").value.trim(),
        password: document.getElementById("password").value

    };


    try {

        

        const result = await login(data);


        if (result.success !== false) {

            window.location.href = result.redirect || "/";

            localStorage.setItem('user', result.user)

            return;

        }


        authMessage.className = "auth-message error show";

        authMessage.textContent = result.message || "Invalid email or password.";


    } catch (error) {

        authMessage.className = "auth-message error show";

        authMessage.textContent = "Server error. Please try again.";

    }


    loginBtn.disabled = false;
    loginBtn.textContent = "Sign In";

});