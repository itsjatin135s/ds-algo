/* If you need to check for duplicates based on two columns before performing an insert or update operation in MySQL, 
    you can use a unique composite key. A composite key is a combination of two or more columns that uniquely identifies 
    a row in a table.

    Here’s how you can do it:

    Create or Alter the Table: Ensure the two columns have a unique composite key.
    Use INSERT ... ON DUPLICATE KEY UPDATE: Insert or update based on the composite key.
*/


ALTER TABLE users ADD UNIQUE KEY (email, username);


CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    UNIQUE KEY unique_email_username (email, username)
);


INSERT INTO users (username, email)
VALUES ('john_doe', 'john@example.com')
ON DUPLICATE KEY UPDATE
    username = VALUES(username);


/*
    Explanation

    - Create Composite Key: The table is created or altered to include a unique composite key on email and username. 
        ( Extra only if you want to compare with 2 unique columns )
    - Insert Attempt: The command tries to insert a new row with username = 'john_doe' and email = 'john@example.com'.
    - Duplicate Key Found: If a row with the combination of email = 'john@example.com' and username = 'john_doe' already exists, the ON DUPLICATE KEY UPDATE clause is triggered.
    - Update Action: The existing row's username column is updated with the new value.
*/