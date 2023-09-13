import sqlite3 as s
c=s.connect("school.db")
print("ok")

#table creation 

c.execute(''' 
CREATE TABLE STUDENT (id INT NOT NULL,
          name varchar(20),
          age int not null,
          PRIMARY KEY (id)
          )
''')
c.commit()
print("created")

c.execute("insert into student values(1,'ashish',21)")
c.execute("insert into student values(2,'ash',22)")
c.execute("insert into student values(3,'manu',25)")
c.commit()
print("ready")


c.execute(''' 
update STUDENT set name="avishna" where id=2
''')
c.commit()
print("updated")

c.execute(''' 
update student set name="abc" where id=3
''')
c.commit()
print("updated !!!!")

c.execute(''' 
alter table student add column place varchar(10)
''')
print("hai")

c.execute(''' 
update student set place="palakkad" where id=3
''')
c.commit()
print("updated !!!!")

c.execute(''' 
alter table student rename to stud
''')
c.commit()
print("changed")


c.execute(""" 
alter table stud rename column place to address
""")
c.commit()
print("changed")

c.execute('''
alter table stud drop column address
''')
c.commit()
print("changed")

c.execute('''
delete from stud where id=2
''')
c.commit()
print("changed")

c.execute('''
drop table stud
''')
c.commit()
print("changed")
c.close()