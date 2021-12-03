DROP DATABASE IF EXISTS trivia;
DROP DATABASE IF EXISTS trivia_test;
DROP USER IF EXISTS caryn;
CREATE DATABASE trivia;
CREATE DATABASE trivia_test;
CREATE USER caryn WITH ENCRYPTED PASSWORD 'mypass';
GRANT ALL PRIVILEGES ON DATABASE trivia TO caryn;
GRANT ALL PRIVILEGES ON DATABASE trivia_test TO caryn;
ALTER USER caryn CREATEDB;
ALTER USER caryn WITH SUPERUSER;