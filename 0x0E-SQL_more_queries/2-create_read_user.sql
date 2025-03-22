-- create database hbtn_0d_2 and user_0d_2script should not fail
-- user to have only select privilege, password is user_0_2_pwd
CREATE DATABASE hbtn_0d_2 IF NOT EXIST;
CREATE USER IF NOT EXIST 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
