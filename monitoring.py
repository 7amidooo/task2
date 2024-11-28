import threading

class Monitor:
    def __init__(self):
        # Declaring shared variables
        self.shared_variable = 0
        self.condition = threading.Condition()

    def p1(self):
        with self.condition:
            # Procedure p1 implementation
            print("Procedure p1 is executing.")
            # Example of modifying shared variable
            self.shared_variable += 1
            print(f"Shared variable updated to {self.shared_variable}.")
            # Notify other threads waiting on this condition
            self.condition.notify_all()

    def p2(self):
        with self.condition:
            # Procedure p2 implementation
            print("Procedure p2 is executing.")
            # Example of modifying shared variable
            self.shared_variable += 2
            print(f"Shared variable updated to {self.shared_variable}.")
            # Notify other threads waiting on this condition
            self.condition.notify_all()

    def pn(self):
        with self.condition:
            # Procedure pn implementation
            print("Procedure pn is executing.")
            # Example of modifying shared variable
            self.shared_variable += 3
            print(f"Shared variable updated to {self.shared_variable}.")
            # Notify other threads waiting on this condition
            self.condition.notify_all()

    def initialization_code(self):
        # Initialization code
        print("Initialization code executed.")
        self.shared_variable = 0  # Initialize shared variable

# Example usage
if __name__ == "__main__":
    monitor = Monitor()
    monitor.initialization_code()

    # Creating threads that will execute the monitor procedures
    thread1 = threading.Thread(target=monitor.p1)
    thread2 = threading.Thread(target=monitor.p2)
    thread3 = threading.Thread(target=monitor.pn)

    # Starting the threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Joining the threads to wait for their completion
    thread1.join()
    thread2.join()
    thread3.join()

    print("Final value of shared variable:", monitor.shared_variable)