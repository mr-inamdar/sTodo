import { singUp } from "./api.js";

const registerForm = document.getElementById("registerForm");

const registerBtn = document.getElementById("registerBtn");

const authMessage = document.getElementById("authMessage");


registerForm.addEventListener("submit", async function(event) {

    event.preventDefault();


    const password = document.getElementById("password").value;

    const confirmPassword = document.getElementById("confirmPassword").value;


    if (password !== confirmPassword) {

        authMessage.className = "auth-message error show";

        authMessage.textContent = "Passwords do not match.";

        return;

    }


    registerBtn.disabled = true;
    registerBtn.textContent = "Creating...";

    authMessage.className = "auth-message";
    authMessage.textContent = "";


    const data = {

        name: document.getElementById("name").value.trim(),

        email: document.getElementById("email").value.trim(),

        password: password

    };


    try {


        const result = await singUp(data);


        if (result.success !== false) {

            authMessage.className = "auth-message success show";

            authMessage.textContent = result.message || "Account created successfully.";


            setTimeout(function() {

                window.location.href = "/login";

            }, 700);


            return;

        }


        authMessage.className = "auth-message error show";

        authMessage.textContent = result.message || "Unable to create account.";


    } catch (error) {

        authMessage.className = "auth-message error show";

        authMessage.textContent = "Server error. Please try again.";

    }


    registerBtn.disabled = false;
    registerBtn.textContent = "Create Account";

});
