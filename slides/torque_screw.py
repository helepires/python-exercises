applied_torque = float(input("Enter the applied torque (in Nm): "))
recommending_tightening_torque = float(input("Enter the recommended tightening torque (in Nm): "))

if 0.90 * recommending_tightening_torque < applied_torque < 1.1 * recommending_tightening_torque:
    print("The screw is tightened properly.")
else:
    print("The screw is not tightened properly.")