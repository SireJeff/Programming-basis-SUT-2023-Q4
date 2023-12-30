class MrKrabs:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        result = ""

        if self.data.startswith("m"):
            # Process Mr. Krabs data
            result = self.process_mr_krabs_data()
        elif self.data.startswith("sb"):
            # Process SpongeBob data
            result = self.process_spongebob_data()
        elif self.data.startswith("s") and self.data[1] != "b":
            # Process Squidward data
            result = self.process_squidward_data()
        else:
            result = "invalid input"

        return result

    def process_mr_krabs_data(self):
        # Duplicate the first 10 characters at the end
        result = self.data + self.data[:10]
        return result

    def process_spongebob_data(self):
        # Replace 'tt' with 'o' and sort the DNA
        result = self.data.replace("x", "(0_0)")
        return result + "1"

    def process_squidward_data(self):
        # Replace any three consecutive repeated characters with '(0_0)'
        result = ""
        i = 0
        while i < len(self.data):
            count = 1
            while i + count < len(self.data) and self.data[i] == self.data[i + count]:
                count += 1

            if count >= 3:
                result += "(0_0)"
                i += count
            else:
                result += self.data[i]
                i += 1

        return result

# Read input
input_data = input().strip()

# Create Mr. Krabs object
mr_krabs = MrKrabs(input_data)

# Process and print the result
result = mr_krabs.process_data()
print(result)
