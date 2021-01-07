#encoding=utf-8
class ControlPanel:
    menubar = '编号\t\t学号\t\t\t姓名\t\t\t年级\t\t\t成绩'
    def __init__(self):
        self.dm = DataManager()

    def show(self):
        students = self.dm.showStudents()
        if 0 == len(students):
            print('暂无学生信息')
        else:
            print(self.menubar)
            for student in students:
                print(student)

    def listById(self):
        try:
            choice = int(input('请输入编号(-1退出)：'))
            if choice == -1:
                return
            student = self.dm.selectById(choice)
            if student is None:
                print('查无此人')
            else:
                print(self.menubar)
                print(student)
        except ValueError:
            print('输入错误，请重新输入')
            self.listById()

    def listByStuId(self):
        try:
            choice = int(input('请输入学号(-1退出)：'))
            if choice == -1:
                return
            student = self.dm.selectByStuId(choice)
            if student is None:
                print('查无此人')
            else:
                print(self.menubar)
                print(student)
        except ValueError:
            print('输入错误，请重新输入')
            self.listByStuId()

    def add(self):
        try:
            stu_id = int(input('请输入学号(-1退出)：'))
            if stu_id == -1:
                return
            name = input('请输入姓名：')
            grade = input('请输入年级：')
            score = int(input('请输入成绩：'))
            stu = Student(-1, stu_id, name, grade, score)
            if self.dm.addStudent(stu):
                print('添加成功')
            else:
                print('当前学号已存在，添加失败')
                while True:
                    choice = input('是否继续添加？(y/n)')
                    if choice == 'y' or choice == 'Y':
                        self.add()
                        break
                    elif choice == 'n' or choice == 'N':
                        break
                    else:
                        print('输入有错，请重新输入！')
        except ValueError:
            print('输入错误，请重新输入')
            self.add()

    def delete(self):
        try:
            sid = int(input('请输入编号：(-1退出)'))
            if sid == -1:
                return
            if self.dm.deleteStudent(sid):
                print('删除成功')
            else:
                print('编号不存在，没有查询到当前学生，删除失败')
                while True:
                    choice = input('是否继续删除？(y/n)')
                    if choice == 'y' or choice == 'Y':
                        self.delete()
                        break
                    elif choice == 'n' or choice == 'N':
                        break
                    else:
                        print('输入有错，请重新输入！')
        except ValueError:
            print('输入错误，请重新输入')
            self.delete()

    def update(self):
        try:
            sid = int(input('请输入编号：(-1退出)'))
            if sid == -1:
                return
            student = self.dm.selectById(sid)
            if student is None:
                print('查无此人')
            else:
                new_name = input('请输入修改后的学生姓名({})：'.format(student.name))
                new_grade = input('请输入修改后的学生班级({})：'.format(student.grade))
                new_score = int(input('请输入修改后的学生成绩({})：'.format(student.score)))
                if self.dm.updateStudent(sid, new_name, new_grade, new_score):
                    print('修改成功')
                else:
                    print('编号不存在，没有查询到当前学生，修改失败')
                    while True:
                        choice = input('是否继续修改？(y/n)')
                        if choice == 'y' or choice == 'Y':
                            self.update()
                            break
                        elif choice == 'n' or choice == 'N':
                            break
                        else:
                            print('输入有错，请重新输入！')
        except ValueError:
            print('输入错误，请重新输入')
            self.update()

    def loop(self):
        flag = True
        while flag:
            print('学生信息管理系统'.center(50, '*'))
            print('\t1.查询展示所有学生信息')
            print('\t2.根据编号查询学生信息')
            print('\t3.根据学号查询学生信息')
            print('\t4.新增学生')
            print('\t5.删除学生')
            print('\t6.修改学生')
            print('\t0.退出')
            print(''.center(50, '*'))
            try:
                choice = int(input('请选择：'))
            except ValueError:
                print('输入错误，请重新输入')
            else:
                if choice in range(7):
                    if choice == 1:
                        self.show()
                    elif choice == 2:
                        self.listById()
                    elif choice == 3:
                        self.listByStuId()
                    elif choice == 4:
                        self.add()
                    elif choice == 5:
                        self.delete()
                    elif choice == 6:
                        self.update()
                    else:
                        while True:
                            choice = input('确定要退出吗？(y/n)')
                            if choice == 'y' or choice == 'Y':
                                flag = False
                                print('感谢您的使用!')
                                break
                            elif choice == 'n' or choice == 'N':
                                break
                            else:
                                print('输入有错，请重新输入！')
                else:
                    print('输入错误，请重新输入')


class DataManager:
    def __init__(self):
        # self.students = []
        self.students = [Student(1, 200, '张三', '软工1班', 100), Student(2, 201, '李四', '工管1班', 80),
                         Student(3, 202, '王五', '通信1班', 90),
                         Student(4, 203, '陈二小', '计科1班', 60)]

    def showStudents(self):
        return self.students

    def selectById(self, sid=-1):
        for student in self.students:
            if student.sid == sid:
                return student
        return None

    def selectByStuId(self, stu_id=-1):
        for student in self.students:
            if student.stu_id == stu_id:
                return student
        return None

    def addStudent(self, new_stu):
        if new_stu.stu_id not in list(stu.stu_id for stu in self.students):
            new_stu.sid = self.students[len(self.students)-1].sid+1
            self.students.append(new_stu)
            return True
        return False

    def deleteStudent(self, sid):
        for stu in self.students:
            if sid == stu.sid:
                del self.students[sid - 1]
                return True
        return False

    def updateStudent(self, sid, name, grade, score):
        for stu in self.students:
            if stu.sid == sid:
                stu.name = name
                stu.grade = grade
                stu.score = score
                return True
        return False


class Student:
    def __init__(self, sid, stu_id, name, grade, score=0):
        self.sid = sid
        self.stu_id = stu_id
        self.name = name
        self.grade = grade
        self.score = score

    def __str__(self):
        return '{0}\t\t{1}\t\t\t{2}\t\t\t{3}\t\t\t{4}'.format(self.sid, self.stu_id, self.name, self.grade, self.score)


def main():
    cp = ControlPanel()
    cp.loop()


if __name__ == '__main__':
    main()
