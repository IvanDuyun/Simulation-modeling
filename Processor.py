import random_values

class Processor():
    def __init__(self, num, proc_life_tm, proc_reboot_tm, model_type, m_1, sigma_1, m_2, sigma_2):
        self.name = 'Processor %s' % str(num)
        self.model_type = model_type
        self.proc_life_tm = proc_life_tm
        self.proc_reboot_tm = proc_reboot_tm
        self.state = 'Free'
        self.task = None
        self.time = 0
        if model_type == 'imit':
            self.m_1 = m_1
            self.sigma_1 = sigma_1
            self.m_1 = m_2
            self.sigma_1 = sigma_2
            N = 10080
            self.cnt_rnd = 0
            x1 = random_values.random_cong(N)
            x2 = random_values.random_irrat_num(N)
            self.list_of_proc_life_tm, self.list_of_proc_reboot_tm = [], []
            for i in range(N):
                self.list_of_proc_life_tm.append(int(abs(random_values.normal_distribution(x1[i], x2[i], m_1, sigma_1))))
                self.list_of_proc_reboot_tm.append(int(abs(random_values.normal_distribution(x1[i], x2[i], m_2, sigma_2))))
            self.proc_life_tm = self.list_of_proc_life_tm[self.cnt_rnd]
            self.proc_reboot_tm = self.list_of_proc_reboot_tm[self.cnt_rnd]

    def set_work_state(self, task):
        self.task = task
        self.state = 'Work - %s' % task.name
        self.task.set_proc_state()

    def next_time(self):
        if self.state.split()[0] == 'Work':
            self.time += 1
            self.task.dec_time()
            if self.task.time_be4_cmplt == 0:
                self.state = 'Free'
                self.task.set_cmpl_state()
                self.task = None
            if self.time >= self.proc_life_tm:
                self.state = 'Crash'
                if self.model_type == 'imit':
                    self.cnt_rnd += 1
                    self.proc_life_tm = self.list_of_proc_life_tm[self.cnt_rnd]
                if self.task != None and self.task.state != 'Complete':
                    self.task.set_wait_state()
                self.time = 0

        elif self.state.split()[0] == 'Crash':
            self.time += 1
            if self.time > self.proc_reboot_tm:
                self.time = 0
                if self.model_type == 'imit':
                    self.proc_reboot_tm = self.list_of_proc_reboot_tm[self.cnt_rnd]
                self.state = 'Free'
