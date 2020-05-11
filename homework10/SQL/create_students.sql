create table if not exists students
(
	id int unsigned auto_increment
		primary key,
	name varchar(20) default '' null,
	age tinyint unsigned default 0 null,
	height decimal(5,2) null,
	gender enum('男', '女', '中性', '保密') default '保密' null,
	cls_id int unsigned default 0 null,
	is_delete bit default b'0' null
);

