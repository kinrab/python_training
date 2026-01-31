from pytest_bdd import given, when, then, parsers
from MODEL.group import Group

@given('a group list', target_fixture="group_list")
def group_list(db):
    return db.get_group_list()

@given(parsers.parse('a group with {name}, {header} and {footer}'),target_fixture="new_group")
def new_group(name, header, footer):
    return Group(group_name=name, group_header=header, group_footer=footer)

@when('I add a new group')
def add_new_group(app, new_group):
    app.group.Add_New_Group(new_group)

@then ('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_group_list = group_list
    new_group_list = db.get_group_list()
    old_group_list.append(new_group)
    assert sorted(old_group_list, key = Group.id_or_max) == sorted(new_group_list, key = Group.id_or_max)
