# from flask import  Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase,Mapped, MappedColumn
# from sqlalchemy import Integer, String, Float
#
# from day_63_library_project.main import all_books
#
#
# class Base(DeclarativeBase):
#     pass
#
# db = SQLAlchemy(model_class=Base)
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
# db.init_app(app)
#
# class Books(db.Model):
#     id: Mapped[int] = MappedColumn(primary_key=True)
#     title: Mapped[str] = MappedColumn(unique=True)
#     author: Mapped[str]
#     rating: Mapped[str]
#
#     def __repr__(self):
#         return f'<Book {self.title}>'
#
# # with app.app_context():
# #     new_book = Books(id=1, title="Harry Potter", author="J.K. Rowling", rating="9.3")
# #     db.session.add(new_book)
# #     db.session.commit()
#
# with app.app_context():
#     result = db.session.execute(db.select(Books).order_by(Books.title))
#     all_book = result.scalars()
#     print(all_books)
#
# with app.app_context():
#     book_To_update = db.session.execute(db.select(Books).where(Books.id == 1)).scalar()
#     book_To_update.title = "Harry Potter and the Philosopher's Stone"
#     db.session.commit()
#




class Student():
    student_name = ""
    student_id = ""


    def __init__(self):
        self.student_name = "Adam"
        self.student_id = 12


stud = Student()
#get all attribute name
print({atr: getattr(stud, atr) for atr in stud.__dict__.keys()})
print(getattr(stud, "student_name"))

print(stud.__dict__)