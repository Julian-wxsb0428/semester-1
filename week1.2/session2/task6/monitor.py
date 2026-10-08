# Week 1.2, Session 2: Task 6
temperature=int(input("Please enter the the machine's temperature in degrees Celsius "))
pressure=int(input("Please enter the machine's pressure in PSI"))
optional_status=int(input("Please enter the achine's operational status (1 for operating, 0 for stopped)"))
if temperature>80:
    print("The temperature is too high, please shutting down the merchine")
elif 50<=temperature<=80:
    print("The temperature is within safe limits")
else:
    print("The temperature is low and no action is needed")
if pressure>100:
    print("High pressure is detected and recommend maintenance.")
elif 70<=pressure<=100:
    print("Pressure is stable.")
else:
    print("The pressure is low and the system is operating normally.")
if optional_status == 0:
    print("The machine is stopped.")
elif temperature>80 or pressure>100:
    print("the machine is running in unsafe conditions and recommend shutting it down.")
else:
    print("The machine is running normally.")