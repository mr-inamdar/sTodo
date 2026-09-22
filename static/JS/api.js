const url = 'http://127.0.0.1:8000'

export async function login(data) {
    const response = await fetch("/auth/login", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(data)

    });

    const result = await response.json();

    console.log("STATUS:", response.status);
    console.log("RESPONSE:", result);

    return result;

}

export async function singUp(data) {
    const response = await fetch(`${url}/auth/register`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(data)

    });

    return response.json();
}

export async function deleteAccaount(id) {
    const response = await fetch(`/auth/deleteAcc/${id}`, {
        method: "DELETE"
    });

    return response.json();
}

export async function logOutAccount() {
    const response = await fetch('/auth/logout', {
        method: 'PUT'
    })
}

export async function getAllTodos(id) {
    await fetch(`/${id}`, {
        method: "GET"
    });
}

export async function insertToso(data, uId) {
    const response = await fetch(`addTask/${uId}`, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })

    return response.json();
}
export async function deleteTodo(uId, todoId) {
    const response = await fetch(`deleteTask/${uId}/${todoId}`, {
        method: 'DELETE'
    })

    return response.json();
}
export async function updateTodo(data, uId, todoId) {
    const response = await fetch(`updateTask/${uId}/${todoId}`, {
        method: 'PUT',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })

    return response.json();
}

export async function syncSession() {
    try {
        const res = await fetch('/auth/sessionStatus');

        const data = await res.json();

        if (!data.loggedIn) {
            localStorage.removeItem('user');
            window.location.href = "/login";
        }

    } catch (error) {
        console.error("Session check failed:", error);
    }
}