
-- 创建数据库 spark
CREATE DATABASE spark DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE spark;

-- 用户表 s_user
CREATE TABLE IF NOT EXISTS s_user(
    user_id INT AUTO_INCREMENT,
    user_name VARCHAR(50) NOT NULL,
    user_username VARCHAR(50) NOT NULL,
    user_password VARCHAR(50) NOT NULL,
    user_pic_addr VARCHAR(50),
    -- user_sex VARCHAR(50),
    -- user_desc VARCHAR(200),
    reserve_1 VARCHAR(50),
    reserve_2 VARCHAR(50),
    PRIMARY KEY(user_id)
);

-- 管理员表 s_admin
CREATE TABLE IF NOT EXISTS s_admin(
    admin_id INT AUTO_INCREMENT,
    admin_name VARCHAR(50) NOT NULL,
    admin_username VARCHAR(50) NOT NULL,
    admin_password VARCHAR(50) NOT NULL,
    reserve_1 VARCHAR(50),
    reserve_2 VARCHAR(50),
    PRIMARY KEY(admin_id)
);

-- 壁纸分类表 s_category
CREATE TABLE IF NOT EXISTS s_category(
    category_id INT AUTO_INCREMENT,
    category_pid INT,
    category_name VARCHAR(50),
    reserve_1 VARCHAR(50),
    reserve_2 VARCHAR(50),
    PRIMARY KEY(category_id)
);

-- 壁纸表 s_img
CREATE TABLE IF NOT EXISTS s_img(
    img_id INT AUTO_INCREMENT,
    img_addr VARCHAR(50) NOT NULL,
    img_addr_small VARCHAR(50),
    img_size VARCHAR(50),
    -- img_desc VARCHAR(200),
    img_author_id INT,
    img_category_id INT,
    img_pv_count INT,
    img_md5 VARCHAR(200),
    reserve_1 VARCHAR(50),
    reserve_2 VARCHAR(50),
    PRIMARY KEY(img_id),
    FOREIGN KEY(img_author_id) REFERENCES s_user(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(img_category_id) REFERENCES s_category(category_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 评论表 s_discuss
CREATE TABLE IF NOT EXISTS s_discuss(
    discuss_id INT AUTO_INCREMENT,
    img_id INT,
    user_id INT,
    user_name VARCHAR(50),
    discuss_content VARCHAR(200),
    discuss_date DATETIME,
    discuss_reply_id INT,  -- 当reply为空或者0时，意味着无回复对象
    reserve_1 VARCHAR(50),
    reserve_2 VARCHAR(50),
    PRIMARY KEY(discuss_id),
    FOREIGN KEY(img_id) REFERENCES s_img(img_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(user_id) REFERENCES s_user(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 评论点赞表 s_discuss_praise
CREATE TABLE IF NOT EXISTS s_discuss_praise(
    discuss_id INT,
    user_id INT,
    FOREIGN KEY(user_id) REFERENCES s_user(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(discuss_id) REFERENCES s_discuss(discuss_id) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE(discuss_id,user_id)
);

-- 壁纸点赞表 s_img_praise
CREATE TABLE IF NOT EXISTS s_img_praise(
    img_id INT,
    user_id INT,
    FOREIGN KEY(user_id) REFERENCES s_user(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(img_id) REFERENCES s_img(img_id) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE(img_id,user_id)
);

-- 壁纸feed流 s_img_feed
CREATE TABLE IF NOT EXISTS s_img_feed(
    feed_id INT,
    feed_type VARCHAR(50),
    img_id INT,
    reserve_1 VARCHAR(50),
    reserve_2 VARCHAR(50),
    FOREIGN KEY(img_id) REFERENCES s_img(img_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 用户收藏壁纸表 s_img_collet
CREATE TABLE IF NOT EXISTS s_img_collet(
    user_id INT,
    img_id INT,
    collet_type INT,
    collet_name VARCHAR(50),
    reserve_1 VARCHAR(50),
    reserve_2 VARCHAR(50),
    FOREIGN KEY(img_id) REFERENCES s_img(img_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(user_id) REFERENCES s_user(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 用户关注用户表 s_user_follow
CREATE TABLE IF NOT EXISTS s_user_follow(
    user_id_a INT,
    user_id_b INT,
    FOREIGN KEY(user_id_a) REFERENCES s_user(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(user_id_b) REFERENCES s_user(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE(user_id_a,user_id_b)
);

-- 用户关注类别表 s_user_follow
CREATE TABLE IF NOT EXISTS s_category_follow(
    user_id_a INT,
    category_id INT,
    FOREIGN KEY(user_id_a) REFERENCES s_user(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(category_id) REFERENCES s_category(category_id) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE(user_id_a,category_id)
);

-- 用户上传壁纸表 s_user_upload
CREATE TABLE IF NOT EXISTS s_user_upload(
    user_id INT,
    img_id INT,
    FOREIGN KEY(user_id) REFERENCES s_user(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(user_id) REFERENCES s_user(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);