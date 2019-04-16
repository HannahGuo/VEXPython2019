# VEX EDR Python-Project
import sys
import vex

#region config
left          = vex.Motor(1)
flywheelLeft  = vex.Motor(2)
rampIntake    = vex.Motor(3)
flyWheelRight = vex.Motor(4)
intakeWheels  = vex.Motor(6)
right         = vex.Motor(10)
joystick      = vex.Joystick()
timer = 0

enableHighFlywheelTimer = False
highFlywheelBuildUpTimer = 0

enableLowFlywheelTimer = False
lowFlywheelBuildUpTimer = 0
#endregion config

while True:
    timer += 0.0022
    straight = joystick.axis3() 
    steering = joystick.axis1()
    
    left.run(-straight + steering)
    right.run(straight + steering)
    # print(timer)
    
    if(joystick.b6up()): # high speed flywheel
        if(not enableHighFlywheelTimer):
            enableHighFlywheelTimer = True
            highFlywheelBuildUpTimer = timer
            
        flywheelLeft.run(-100) 
        flyWheelRight.run(100)
        
        if(timer - highFlywheelBuildUpTimer > 2.8):
            rampIntake.run(-100)
        
    elif(joystick.b6down()): # low speed flywheel
        if(not enableLowFlywheelTimer):
            enableLowFlywheelTimer = True
            lowFlywheelBuildUpTimer = timer
                
        flywheelLeft.run(-70) 
        flyWheelRight.run(70)
        
        if(timer - lowFlywheelBuildUpTimer > 2.8):
            rampIntake.run(-100)
    elif(joystick.b8down()):
        rampIntake.run(-80)
        intakeWheels.run(-50)
    else:
        rampIntake.run(0)
        intakeWheels.run(0)
        flywheelLeft.run(0)
        flyWheelRight.run(0)
        enableHighFlywheelTimer = False
        enableLowFlywheelTimer = False
