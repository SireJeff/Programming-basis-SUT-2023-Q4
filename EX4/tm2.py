class RoseDictionary:
    def __init__(self):
        self.entries = []

    def __getitem__(self, target_key):
        for stored_key, value in self.entries:
            if stored_key == target_key:
                return value
        raise KeyError('Value was not found and no default value/message was specified.')

    def __setitem__(self, new_key, new_value):
        for i, (stored_key, _) in enumerate(self.entries):
            if stored_key == new_key:
                self.entries[i] = (new_key, new_value)
                return
        self.entries.append((new_key, new_value))

    def pop_item(self, raise_error=True, default=None, error_msg='error_msg'):
        if not self.entries:
            if raise_error:
                if error_msg:
                    raise KeyError(error_msg)
                else:
                    raise KeyError('Dictionary was empty and no default value/message was specified.')
            else:
                return default
        else:
            popped_key, popped_value = self.entries.pop()
            return popped_value
            # popped_index = len(self.entries) - 1
            # popped_key, popped_value = self.entries[popped_index]
            # self.entries = self.entries[:popped_index]  # Remove the last item
            # return popped_value


    def get_item(self, target_key, raise_error=True, default=None, error_msg='error_msg'):
        if raise_error:
            return self.__getitem__(target_key)
        elif not self.entries:
            return default
        else:
            for stored_key, value in self.entries:
                if stored_key == target_key:
                    return value
            return default


d = RoseDictionary()
d["mike"] = "report1"
print(d["mike"])

d["john"] = "report2"
print(d.pop_item()) 

print(d.pop_item(raise_error=False, default="Default Value"))  

print(d.get_item("mike",raise_error=False,default="Default Value"))  
print(d.get_item("sam", raise_error=False, default="Not Found"))  