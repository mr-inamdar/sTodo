Create Database studentApp;

use studentApp;

create Table student(
    sId INT AUTO_INCREMENT PRIMARY KEY,
    sName VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(250) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE todos (
    todoId INT AUTO_INCREMENT PRIMARY KEY,
    id INT NOT NULL,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    due_date DATE,
    completed BOOLEAN DEFAULT FALSE,

    FOREIGN KEY (id)
        REFERENCES student(sId)
        on DELETE CASCADE 
);
