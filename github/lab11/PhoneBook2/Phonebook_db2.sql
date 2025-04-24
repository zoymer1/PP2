CREATE DATABASE IF NOT EXISTS Phonebook_db2;
USE Phonebook_db2;

CREATE TABLE IF NOT EXISTS phonebook (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
);

DROP FUNCTION IF EXISTS get_users_by_pattern;
DELIMITER //
CREATE FUNCTION get_users_by_pattern(pattern VARCHAR(100))
RETURNS TEXT
DETERMINISTIC
BEGIN
    DECLARE result TEXT DEFAULT '';
    DECLARE done INT DEFAULT 0;
    DECLARE n VARCHAR(100);
    DECLARE p VARCHAR(20);
    DECLARE cur CURSOR FOR SELECT name, phone FROM phonebook WHERE name LIKE CONCAT('%', pattern, '%') OR phone LIKE CONCAT('%', pattern, '%');
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO n, p;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SET result = CONCAT(result, n, ':', p, '; ');
    END LOOP;
    CLOSE cur;
    RETURN result;
END;
//
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_or_update_user;
DELIMITER //
CREATE PROCEDURE insert_or_update_user(IN uname VARCHAR(100), IN uphone VARCHAR(20))
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = uname) THEN
        UPDATE phonebook SET phone = uphone WHERE name = uname;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES(uname, uphone);
    END IF;
END;
//
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_multiple_users;
DELIMITER //
CREATE PROCEDURE insert_multiple_users()
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE total INT;
    DECLARE uname VARCHAR(100);
    DECLARE uphone VARCHAR(20);
    CREATE TEMPORARY TABLE temp_users(name VARCHAR(100), phone VARCHAR(20));
    INSERT INTO temp_users(name, phone) VALUES('John', '87001234567'), ('Kate', '777'), ('Tom', '87009876543');
    SELECT COUNT(*) INTO total FROM temp_users;

    WHILE i < total DO
        SELECT name, phone INTO uname, uphone FROM temp_users LIMIT i,1;
        IF CHAR_LENGTH(uphone) < 10 THEN
            SELECT CONCAT('Invalid: ', uname, ', ', uphone);
        ELSE
            CALL insert_or_update_user(uname, uphone);
        END IF;
        SET i = i + 1;
    END WHILE;
    DROP TEMPORARY TABLE temp_users;
END;
//
DELIMITER ;

DROP FUNCTION IF EXISTS paginate_users;
DELIMITER //
CREATE FUNCTION paginate_users(offset_val INT, limit_val INT)
RETURNS TEXT
DETERMINISTIC
BEGIN
    DECLARE result TEXT DEFAULT '';
    DECLARE done INT DEFAULT 0;
    DECLARE n VARCHAR(100);
    DECLARE p VARCHAR(20);
    DECLARE cur CURSOR FOR SELECT name, phone FROM phonebook LIMIT offset_val, limit_val;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO n, p;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SET result = CONCAT(result, n, ':', p, '; ');
    END LOOP;
    CLOSE cur;
    RETURN result;
END;
//
DELIMITER ;

DROP PROCEDURE IF EXISTS delete_user_by_name_or_phone;
DELIMITER //
CREATE PROCEDURE delete_user_by_name_or_phone(IN uname VARCHAR(100), IN uphone VARCHAR(20))
BEGIN
    DELETE FROM phonebook WHERE name = uname OR phone = uphone;
END;
//
DELIMITER ;