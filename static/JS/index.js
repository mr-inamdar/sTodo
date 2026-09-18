import { deleteAccaount, insertToso, logOutAccount } from "./api.js"

const submitForm = document.getElementById('submitForm')
const deleteAccount = document.getElementById('deleteAccount')
const logotAccount = document.getElementById('logotAccount')
const singupAccount = document.getElementById('singupAccount')
const loginAccount = document.getElementById('loginAccount')
const title = document.getElementById('title')
const desc = document.getElementById('desc')
const addBtns = document.querySelectorAll('addBtns')

if (submitForm){
    submitForm.addEventListener('click', async (e)=>{
        e.preventDefault();
        
        const data = {
            title: title.value(),
            desc: desc.value()
        }

        let userId;

        if (localStorage.getItem('user')) {
            userId = localStorage.getItem('user').id || null;
        }

        const res = await insertToso(data, userId)

        if(res.success){
            alert(res.message)
        }
        else{
            alert(res.message)
        }

        document.getElementById('closeForm').click();
    })
}

if (deleteAccount){
    deleteAccount.addEventListener('click', async (e)=>{
        e.preventDefault();

        if (localStorage.getItem('user')) {
            const res = await deleteAccaount();
        
        }
    })
}

if (logotAccount){
    logotAccount.addEventListener('click', async (e)=>{
        e.preventDefault();
        
        if (localStorage.getItem('user')) {
            const res = await logOutAccount()
        }

    })
}

if (singupAccount){
    singupAccount.addEventListener('click', (e)=>{
        e.preventDefault();

        window.location.href = '/register'
    })
}

if (loginAccount){
    loginAccount.addEventListener('click', (e)=>{
        e.preventDefault();

        window.location.href = '/login'

    })
}

if (addBtns.length > 0){
    for(let i = 0; i < 2; i++){           
        if(localStorage.getItem('user')){
            addBtns[i].setAttribute('data-bs-toggle', 'modal');
            addBtns[i].setAttribute('data-bs-target', '#exampleModal')
        }
    }
}


const deleteModal = document.getElementById("deleteModal");

const deleteBtn = document.getElementById("deleteAccountBtn");

const closeDeleteModal = document.getElementById("closeDeleteModal");

const cancelDelete = document.getElementById("cancelDelete");

const confirmDelete = document.getElementById("confirmDelete");



function openDeleteModal() {

    deleteModal.classList.add("show");

    deleteModal.setAttribute(
        "aria-hidden",
        "false"
    );

}


function closeModal() {

    deleteModal.classList.remove("show");

    deleteModal.setAttribute(
        "aria-hidden",
        "true"
    );

}


deleteBtn?.addEventListener(
    "click",
    openDeleteModal
);


closeDeleteModal?.addEventListener(
    "click",
    closeModal
);


cancelDelete?.addEventListener(
    "click",
    closeModal
);


deleteModal?.addEventListener(
    "click",
    function(event) {

        if (event.target === deleteModal) {

            closeModal();

        }

    }
);


document.addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Escape") {

            closeModal();

        }

    }
);


confirmDelete?.addEventListener(
    "click",
    async function() {

        confirmDelete.disabled = true;

        confirmDelete.textContent =
            "Deleting...";


        try {

            const response =
                await fetch(
                    "/auth/deleteAccount",
                    {
                        method: "DELETE"
                    }
                );


            const data =
                await response.json();


            if (
                response.ok &&
                data.success !== false
            ) {

                window.location.href =
                    data.redirect ||
                    "/auth/login";

                return;

            }


            alert(
                data.message ||
                "Unable to delete account."
            );


        } catch (error) {

            alert(
                "Server error. Please try again."
            );

        }


        confirmDelete.disabled = false;

        confirmDelete.textContent =
            "Yes, Delete Account";

    }
);