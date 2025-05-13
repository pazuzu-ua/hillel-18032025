-- Зазвичай назва таблиці йде в множині + з велокої літери
-- entity = сутність (!= істота)
-- constraint = обмеження
CREATE TABLE IF NOT EXISTS Users (
    -- завжди має бути якесь унікальне поле (зазвичай - це ID)
    -- id, user_id, userid, i_user
    -- НАЗВА ПОЛЯ        ТИП            НАЛАШТУВАННЯ
    i_user            INTEGER           PRIMARY KEY AUTOINCREMENT,
    -- PRIMARY KEY: це поле буде унікальним і заповнюватиметься автоматично
    -- AUTOINCREMENT: впевнюється, що кожне значення (нового запису) - більше попередніх
    email             TEXT               UNIQUE  NOT NULL,
    -- UNIQUE: значення має бути унікальним (NULL - не перевіряється)
    -- NOT NULL: забороняє значення NULL
    comment           TEXT,
    favourite_word    TEXT                DEFAULT 'bird'
    -- DEFAULT: значення за замовчуванням
);

DELETE FROM Users; -- видалить усі записи з таблиці Users
DELETE FROM Users WHERE email = 'a4@gmail.com'; -- видалить усі записи з таблиці Users, де email = 'a4@gmail.com'
DELETE FROM Users WHERE email != 'a4@gmail.com';
DELETE FROM Users WHERE email <> 'a4@gmail.com'; -- НЕ ДОРІВНЮЄ
DELETE FROM Users WHERE i_user > 10;  -- видалить усі записи з таблиці Users, де i_user > 10
DELETE FROM Users WHERE email = 'a4@gmail.com' AND i_user > 10;

DELETE FROM Users WHERE i_user BETWEEN 10 AND 20; -- з 10 по 20 видаляться
DELETE FROM Users WHERE i_user IN ( 1, 55, 22 );
