CREATE TABLE `chatdb`.`user` (
  `user_name` VARCHAR(20) NOT NULL,
  `user_psw` VARCHAR(45) NULL,
  `user_email` VARCHAR(45) NULL,
  `user_phn` VARCHAR(45) NULL,
  `user_gender` VARCHAR(45) NULL,
  `user_age` INT NULL,
  `status` VARCHAR(45) NULL,
  PRIMARY KEY (`user_name`),
  UNIQUE INDEX `user_phn_UNIQUE` (`user_phn` ASC),
  UNIQUE INDEX `user_email_UNIQUE` (`user_email` ASC));

