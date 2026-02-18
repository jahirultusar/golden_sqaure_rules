
class ToDo:
    # initialises the class
        # - no argument
    def __init__(self):
        self.todo_list = []
        self.marked_done =[]
    # add method
        # - one argument
    def add(self, task):
        if not isinstance(task, str):
            raise TypeError("Entry should be string only")
        self.todo_list.append(task)
    # complete method
        # - one argument
    def complete(self, done):
        if done in self.todo_list:
            self.marked_done.append(done)
            self.todo_list.remove(done)
        else:
            raise ValueError("No task found!")
            
