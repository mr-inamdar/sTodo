import { deleteAccaount, deleteTodo, getAllTodos, insertToso, logOutAccount, syncSession, updateTodo } from "./api.js"

const submitForm = document.getElementById('submitForm');
const deleteAccountBtn = document.getElementById('deleteAccount');
const logotAccount = document.getElementById('logotAccount');
const singupAccount = document.getElementById('singupAccount');
const loginAccount = document.getElementById('loginAccount');
const addBtns = document.querySelectorAll('.addBtns');
const todoEditBtn = document.querySelectorAll('.todoEditBtn');
const todoDeleteBtn = document.querySelectorAll('.todoDeleteBtn');
const typ1 = document.querySelectorAll('.typ1');
const typ2 = document.querySelectorAll('.typ2');

document.addEventListener('DOMContentLoaded', async () => {

    await syncSession();

    const user = JSON.parse(localStorage.getItem('user'));

    console.log("USER:", user);

    if (user) {
        await getAllTodos(user.id);
    }

    if (user && addBtns.length > 0) {

        addBtns.forEach((btn) => {
            btn.setAttribute('data-bs-toggle', 'modal');
            btn.setAttribute('data-bs-target', '#exampleModal');
        });

    }
    if (user && typ1.length > 0 && typ2.length > 0) {
        typ1.forEach((btn)=>{
            btn.style.display = 'none';
        });
        typ2.forEach((btn)=>{
            btn.style.display = 'initial';
        })
    }
});
function openAddModal() {
    document.getElementById("exampleModalLabel").innerText = "Add Todo";

    document.getElementById("title").value = "";
    document.getElementById("desc").value = "";

    document.getElementById("submitForm").innerText = "Save";

    document.getElementById("submitForm").dataset.mode = "add";
}
if (addBtns.length > 0) {
    addBtns.forEach((btn) => {
        btn.addEventListener('click', openAddModal)
    })
}
function openUpdateModal(todoId, title, description) {

    document.getElementById("exampleModalLabel").innerText = "Update Todo";

    document.getElementById("title").value = title;
    document.getElementById("desc").value = description;

    document.getElementById("submitForm").innerText = "Update";

    document.getElementById("submitForm").dataset.mode = "update";
    document.getElementById("submitForm").dataset.todoId = todoId;
}

if (submitForm){
    submitForm.addEventListener('click', async (e)=>{
        e.preventDefault();

        const title = document.getElementById('title');
        const desc = document.getElementById('desc');
        
        const data = {
            title: title?.value,
            desc: desc?.value
        }
        const user = JSON.parse(localStorage.getItem('user'))

        if (submitForm.dataset.mode == 'add') {

            if (user) {

                const res = await insertToso(data, user.id);
                

                if(res.success){
                    alert(res.message)
                }
                else{
                    if (res.status === 401) {
                        localStorage.removeItem("user");
                        window.location.href = "/login";
                        return;
                    }
                    alert(res.message)
                }
            }
        }
        else if (submitForm.dataset.mode == "update") {

            if (user) {

                const todoId = Number(submitForm.dataset.todoId);

                const res = await updateTodo(data, user.id, todoId)

                if(res.success){
                    alert(res.message)
                }
                else{
                    if (res.status === 401) {
                        localStorage.removeItem("user");
                        window.location.href = "/login";
                        return;
                    }
                    alert(res.message)
                }
            }
        }
        document.getElementById('closeForm').click();
    })
}

if (deleteAccountBtn){
    deleteAccountBtn.addEventListener('click', async (e)=>{
        e.preventDefault();

        const user = JSON.parse(localStorage.getItem("user"));

        if (user) {
            confirmBtn.dataset.mode = 'account';
            confirmBtn.dataset.id = user.id;
        }
        // if (localStorage.getItem('user')) {
        //     const res = await deleteAccaount();
        
        // }
    })
}

if (logotAccount){
    logotAccount.addEventListener('click', async (e)=>{
        e.preventDefault();
        
        if (localStorage.getItem('user')) {
            const res = await logOutAccount();

            if(res.success){
                alert(res.message)
            }
            else{
                if (res.status === 401) {
                    localStorage.removeItem("user");
                    window.location.href = "/login";
                    return;
                }
                alert(res.message)
            }
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

if (todoEditBtn.length > 0){
    todoEditBtn.forEach((btn)=>{
        btn.addEventListener('click', async (e)=>{
            e.preventDefault();

            const todoId = btn.dataset.todoId;
            const title = btn.dataset.title;
            const description = btn.dataset.description;

            openUpdateModal(todoId, title, description);
        })
    })
}
if (todoDeleteBtn.length > 0){

    todoDeleteBtn.forEach((button) => {

        button.addEventListener("click", (e) => {

            e.preventDefault();

            const todoId = Number(button.dataset.todoId);

            console.log("Todo ID:", todoId);

            const uId = JSON.parse(localStorage.getItem('user')).id;

            confirmBtn.dataset.todoId = todoId;
            confirmBtn.dataset.uId = uId;
            confirmBtn.dataset.mode = 'todo';
        });
    });
}

const confirmBtn = document.getElementById('confirmBtn');
const cancelBtn = document.getElementById('cancelBtn');

if (confirmBtn) {
    confirmBtn.addEventListener('click', async () => {

        if (confirmBtn.dataset.mode == 'account') {

            const id = confirmBtn.dataset.id;
            
            const res = await deleteAccaount(id);

            if(res.success){
                cancelBtn.click();
                alert(res.message)

            }
            else{
                if (res.status === 401) {
                    localStorage.removeItem("user");
                    window.location.href = "/login";
                    return;
                }
                alert(res.message)
            }

        }
        else if (confirmBtn.dataset.mode == 'todo') {
            const todoId = confirmBtn.dataset.todoId;
            const uId = confirmBtn.dataset.uId;

            const res = await deleteTodo(uId, todoId);

            if(res.success){
                cancelBtn.click();
                alert(res.message)
                
            }
            else{
                if (res.status === 401) {
                    localStorage.removeItem("user");
                    window.location.href = "/login";
                    return;
                }
                alert(res.message)
            }
        }
    })
}

// localStorage.clear()