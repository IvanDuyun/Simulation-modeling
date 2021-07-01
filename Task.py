class Task():
    def __init__(self, name, time_be4_cmplt_evm1, time_be4_cmplt_evm2, time_be4_cmplt_evm3):
        self.name = name
        self.time_be4_cmplt_evm1 = time_be4_cmplt_evm1
        self.time_be4_cmplt_evm2 = time_be4_cmplt_evm2
        self.time_be4_cmplt_evm3 = time_be4_cmplt_evm3
        self.state = 'Wait'
        self.name_evm = 0

    def set_proc_state(self):
        self.state = 'Proc'

    def set_wait_state(self):
        self.state = 'Wait'

    def set_cmpl_state(self):
        self.state = 'Complete'

    def set_del_state(self):
        self.state = 'Deleted'

    def dec_time(self, name_evm):
        self.name_evm = name_evm
        if self.name_evm == 1:
            self.time_be4_cmplt_evm1 -= 1
        if self.name_evm == 2:
            self.time_be4_cmplt_evm2 -= 1
        if self.name_evm == 3:
            self.time_be4_cmplt_evm3 -= 1
