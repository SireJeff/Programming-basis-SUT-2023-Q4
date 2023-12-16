class DoctorOffice:
    def __init__(self):
        self.patients = {}
        self.visits = {}

    def add_patient(self, id, name, family_name, age, height, weight):
        if id in self.patients:
            return "error: this ID already exists"
        if age < 0:
            return "error: invalid age"
        if height < 0:
            return "error: invalid height"
        if weight < 0:
            return "error: invalid weight"

        self.patients[id] = {
            'name': name,
            'family_name': family_name,
            'age': age,
            'height': height,
            'weight': weight
        }
        return "patient added successfully"

    def display_patient(self, id):
        if id not in self.patients:
            return "error: invalid ID"
        patient_info = self.patients[id]
        return f"patient name: {patient_info['name']}\npatient family name: {patient_info['family_name']}\npatient age: {patient_info['age']}\npatient height: {patient_info['height']}\npatient weight: {patient_info['weight']}"

    def add_visit(self, id, beginning_time):
        if id not in self.patients:
            return "error: invalid id"
        if not (9 <= beginning_time <= 18):
            return "error: invalid time"
        if beginning_time in self.visits.values():
            return "error: busy time"

        self.visits[id] = beginning_time
        return "visit added successfully!"

    def delete_patient(self, id):
        if id not in self.patients:
            return "error: invalid id"

        del self.patients[id]
        # Remove patient's visits as well
        self.visits = {k: v for k, v in self.visits.items() if k != id}
        return "patient deleted successfully!"

    def display_visit_list(self):
        schedule = sorted(self.visits.items(), key=lambda x: x[1])
        result = "SCHEDULE:\n"
        for id, time in schedule:
            result += f"{time:02d}:00 ({self.patients[id]['name']}) ({self.patients[id]['family_name']})\n"
        return result.strip()


def main():
    office = DoctorOffice()
    while True:
        command = input().split()
        if command[0] == "add":
            if command[1] == "patient":
                print(office.add_patient(int(command[2]), command[3], command[4], int(command[5]), int(command[6]), int(command[7])))
            elif command[1] == "visit":
                print(office.add_visit(int(command[2]), int(command[3])))
        elif command[0] == "display":
            if command[1] == "patient":
                print(office.display_patient(int(command[2])))
            elif command[1] == "visit" and command[2] == "list":
                print(office.display_visit_list())
        elif command[0] == "delete":
            if command[1] == "patient":
                print(office.delete_patient(int(command[2])))
        elif command[0] == "exit":
            break
        else:
            print("invalid command")


if __name__ == "__main__":
    main()
