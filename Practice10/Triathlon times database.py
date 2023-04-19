class triathlon():
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = swim_time + cycle_time + run_time

    def print_details(self):
        print(f"{self.first_name} {self.last_name} competed in a triathlon at {self.location}.",end = ' ')
        print(f"Swim time: {self.swim_time}",end = ' ')
        print(f"Cycle time: {self.cycle_time}",end = ' ')
        print(f"Run time: {self.run_time}",end = ' ')
        print(f"Total time: {self.total_time}",end = ' ')
        
# Example usage:
triathlete = triathlon("Harry", "Paul", "Haining", 10.5, 20.2, 30.1)
triathlete.print_details()
