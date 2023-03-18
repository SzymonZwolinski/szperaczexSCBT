import board
import adafruit_mpu6050

def ReadAccelerometr():
    i2c = board.I2C()
    mpu = adafruit_mpu6050.MPU6050(i2c)
    # TODO: move registry to main and send reference

    outFile = open("AccelerometrDate.txt", "w") #TODO: change saving file.
    readings = "x:" +\
               mpu.acceleration[0] +\
               " Y: " +\
               mpu.acceleration[1] +\
               " Z: " +\
               mpu.acceleration[2] +\
               "\n"
    outFile.write(readings)
    outFile.close()
