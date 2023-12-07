class RoseDictionary:
    def __init__(self):
        self.dictionary = {}

    def __getitem__(self, key):
        if key in self.dictionary:
            return self.dictionary[key]
        else:
            raise KeyError('Value was not found and no default value/message was specified.')

    def __setitem__(self, key, value):
        self.dictionary[key] = value

    def pop_item(self, raise_error=True, default=None, error_msg='error_msg'):
        if not self.dictionary:
            if raise_error:
                if error_msg:
                    raise KeyError(error_msg)
                else:
                    raise KeyError('Dictionary was empty and no default value/message was specified.')
            else:
                return default
        else:
            key = list(self.dictionary.keys())[-1]
            value = self.dictionary.pop(key)
            return value

    def get_item(self, key, raise_error=True, default=None, error_msg='error_msg'):
        if raise_error:
            return self.__getitem__(key)
        elif not self.dictionary:
            return default
        else:
            return self.dictionary.get(key, default)


d = RoseDictionary()
d["mike"] = "report1"
print(d["mike"])

d["john"] = "report2"
print(d.pop_item()) 

print(d.pop_item(raise_error=False, default="Default Value"))  

print(d.get_item("mike",raise_error=False,default="Default Value"))  
print(d.get_item("sam", raise_error=False, default="Not Found"))  