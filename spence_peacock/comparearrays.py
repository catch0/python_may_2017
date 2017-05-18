class call(object):
    def __init__(self, unique_id, caller_name, caller_num, call_time, call_reason):
        self.unique_id=unique_id
        self.caller_name=caller_name
        self.caller_num=caller_num
        self.call_time=call_time
        self.call_reason=call_reason
    def display(self):
            print "%s %s %s %s %s" % (self.unique_id, self.caller_name, self.caller_num,self.call_time,self.call_reason)
call1 = call(123,'joe rogan','213-213-2131','90 seconds','pissed off about bill')
class callCenter(object):
    def __init__(self, calls)
        self.