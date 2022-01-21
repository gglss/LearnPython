
def login_verify(fn):
    def inner(*args, **kwargs):
        ret = fn(*args, **kwargs)
        return ret
    return inner


@login_verify
def add():
    print("添加员工信息")

@login_verify
def delete():
    print("删除员工信息")

@login_verify
def upd():
    print("修改员工信息")

@login_verify
def search():
    print("查询员工信息")


add()
delete()