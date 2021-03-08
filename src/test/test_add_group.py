
def test_add_group(app):
    old_groups = app.groups.get_group_list()
    app.groups.add_group("Group Test")
    new_groups = app.groups.get_group_list()
    old_groups.append("Group Test")

    assert sorted(new_groups) == sorted(old_groups)
