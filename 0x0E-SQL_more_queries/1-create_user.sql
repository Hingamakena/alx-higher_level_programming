-- crate user_0d_1, password set to 'user_0d_1_pwd'
-- if user exits, script should not fail
CREATE USER IF NOT EXIST 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
