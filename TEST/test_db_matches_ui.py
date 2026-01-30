
from MODEL.group import Group
from timeit import timeit

def test_group_list(app,db):

    # Замер времени
    # time_ui = timeit(lambda: app.group.get_group_list(), number=1)
    # print("\n Время вызова UI app.group.get_group_list()"+str(time_ui)+ "\n")  # Время вызова UI app.group.get_group_list()0.7770849000080489 sec
    # Замер времени
    #time_db = timeit(lambda: map(clean, db.get_group_list()), number=1 )
    #print("\n Время вызова DB db.get_group_list()" + str(time_db) + "\n") # Время вызова DB db.get_group_list()0.0024258000194095075 sec

    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(group_id=group.group_id, group_name=group.group_name.strip())

    db_list = map(clean, db.get_group_list())

    # Замер времени
    #time_db = timeit(lambda: map(clean, db.get_group_list()), number=1 )
    #print("\n Время вызова DB db.get_group_list()" + str(time_db) + "\n") # Время вызова DB db.get_group_list()0.0024258000194095075 sec

    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

# Функция map() в Python применяет заданную функцию к каждому элементу
# одного или нескольких итерируемых объектов(списков, кортежей и. т.д.)
# и возвращает итератор с результатами этих преобразований, что позволяет обрабатывать
# коллекции без явных циклов for , экономя память и делая код более лаконичным.
# Это функция высшего порядка, которая "отображает" функцию на коллекцию элементов,
# преобразуя их в новую последовательность.

