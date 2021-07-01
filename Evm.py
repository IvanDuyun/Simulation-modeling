
class Evm():
    def __init__(self, model_type, number):
        self.model_type = model_type
        self.name = 'EVM %s' % str(number)
        self.state = 'Free'
        self.task = None
        self.time = 0

    def set_work_state (self, task):
        self.task = task
        self.state = 'Work - %s' % task.name
        self.task.set_proc_state()

    def next_time(self):
        if self.state.split()[0] == 'Work':
            self.time += 1
            if self.name == 'EVM 1':
                self.task.dec_time(1)
            if self.name == 'EVM 2':
                self.task.dec_time(2)
            if self.name == 'EVM 3':
                self.task.dec_time(3)

            if self.task.time_be4_cmplt_evm1 == 0:
                self.state = 'Free'
                self.task.set_cmpl_state()
              #  self.task = None
            if self.task.time_be4_cmplt_evm2 == 0 or self.task.time_be4_cmplt_evm3 == 0:
                self.state = 'Free'
                self.task.set_cmpl_state()
                #  self.task = None