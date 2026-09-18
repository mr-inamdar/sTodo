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

export async function deleteAccaount() {
    const response = await fetch("/auth/deleteAcc", {
        method: "DELETE"
    });

    return response.json();
}

export async function logOutAccount() {
    const response = await fetch('/auth/logout', {
        method: 'PUT'
    })
}

export async function insertToso(data, uId) {
    const response = await fetch(`addTodo/${uId}`, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })

    return response.json();
}
export async function deleteToso(uId, todoId) {
    const response = await fetch(`deleteTodo/${uId}/${todoId}`, {
        method: 'DELETE'
    })

    return response.json();
}
export async function updateToso(data, uId, todoId) {
    const response = await fetch(`updateTodo/${uId}/${todoId}`, {
        method: 'PUT',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })

    return response.json();
}