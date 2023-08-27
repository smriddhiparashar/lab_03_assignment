

class Flight:
    def __init__(self, P_ID, Process, Start_Time, Priority):
        self.P_ID = P_ID
        self.Process = Process
        self.Start_Time = Start_Time
        self.Priority = Priority

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def sort_by_P_ID(self):
        self.flights.sort(key=lambda flight: flight.P_ID)

    def sort_by_Start_Time(self):
        self.flights.sort(key=lambda flight: flight.Start_Time)

    def sort_by_Priority(self):
        priority_order = {'High': 1, 'MID': 2, 'Low': 3}
        self.flights.sort(key=lambda flight: priority_order[flight.Priority])

    def display_table(self):
        for flight in self.flights:
            print(f"P_ID: {flight.P_ID}, Process: {flight.Process}, Start Time: {flight.Start_Time}, Priority: {flight.Priority}")



print("Name: Smriddhi Parashar\nEnroll: E22CSEU1524\nBatch: 28\n\n")
flight_table = FlightTable()

flight_table.add_flight(Flight("P1", "VSCode", 100, "MID"))
flight_table.add_flight(Flight("P23", "Eclipse", 234, "MID"))
flight_table.add_flight(Flight("P93", "Chrome", 189, "High"))
flight_table.add_flight(Flight("P42", "JDK", 9, "High"))
flight_table.add_flight(Flight("P9", "CMD", 7, "High"))
flight_table.add_flight(Flight("P87", "NotePad", 23, "Low"))

print("Choose sorting parameter:")
print("1. Sort by P_ID")
print("2. Sort by Start Time")
choice = int(input("Enter your choice: "))

if choice == 1:
    flight_table.sort_by_P_ID()
elif choice == 2:
    flight_table.sort_by_Start_Time()
elif choice == 3:
    flight_table.sort_by_Priority()
else:
    print("Invalid choice")

print("\nSorted Flight Table:")
flight_table.display_table()

