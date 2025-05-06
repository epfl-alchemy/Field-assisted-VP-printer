# ALCHEMY Project

## Getting Started with Raspberry Pi

### Enable I2C Communication
To control the Adafruit DC and stepper motor hat, enable I2C communication:

1. Open the boot configuration file from the terminal:
    ```bash
    sudo nano /boot/firmware/config.txt
    ```
2. Add the following lines to the file, save, and then reboot the Raspberry Pi:
    ```bash
    dtparam=i2c_arm=on
    dtparam=i2c_vc=on
    ```

### Verify the I2C Address
Make sure the motor controller is connected by performing a scan to detect the I2C address:

1. Install I2C tools:
    ```bash
    sudo apt-get install i2c-tools
    ```
2. Run the detection command:
    ```bash
    i2cdetect -y 1
    ```

The address of the first stepper motor is `0x60`. Additional controllers can be added for supplementary motors.

### Check Python Version
Ensure you have the required Python version installed:
```bash
python -version
python3 -version
```

## Create Virtual Environment

### Install venv and Check Version
```bash
sudo apt install -y python3 python3-venv
```

### Create Virtual Environment
Create a virtual environment named `alchemy`:
```bash
python3 -m venv alchemy
```

### Activate Virtual Environment
Activate the virtual environment:
```bash
source /home/alchemy/ALCHEMY/alchemy2/bin/activate
```

### Deactivate Virtual Environment
To deactivate the virtual environment:
```bash
deactivate
```

## Installation

### Clone the Repository
Clone the ALCHEMY repository:
```bash
git clone https://github.com/AViollet74/ALCHEMY
```

### Install Dependencies
Install the required dependencies:
```bash
sudo apt install -r requirements.txt
```

### Test Installation Process
Check the installed packages:
```bash
pip list
```

## Run the `Main_3.py` Script

### Activate Virtual Environment
Activate the virtual environment:
```bash
source /home/alchemy/ALCHEMY/alchemy2/bin/activate
```

### Run the Script
Run the `Main_3.py` script:
```bash
python3 /home/alchemy/ALCHEMY/main_3.py
```

### Follow Terminal Instructions
Provide the following inputs as prompted:

- Enter the name of the folder containing the images and the file with layer state information (both must have the same name and be stored in `/home/ALCHEMY/PRINT` and `/home/ALCHEMY/LAYERS`, respectively).
- Enter layer thickness in mm (default: 0.08 mm).
- Enter the size of the resin container in mm (default: 74 mm).
- Position the magnets by rotating the lead screw manually.
- Enter the GPIO pin number for the UV-light (default: 27).
- Enter the GPIO pin number for the photoelectric sensor (default: 4).
- Enter the number of vibration motors, their associated GPIO pin numbers, and their activation time in seconds.
- If not already set, specify the initial position and orientation of the build table (yes/no).

The print process is then launched, and information about the print will be displayed during the process.

## Workflow Description
The `Main_3.py` script performs the following steps:

1. Specify the part name and layer thickness.
2. Initialize the hardware components (GPIO pin numbers, activation times, etc.).
3. Move the platform downward to the initial position and set the build table.
4. Enter the printing loop:
    - Move the build platform upward and downward to the layer position.
    - Turn the LCD black.
    - Activate the particle control system (vibration motors or magnet sliding).
    - Display the image on the LCD.
    - Turn on the UV light.
    - Turn off the UV light.

---

For more details, refer to the repository documentation or contact [Arnaud Viollet](https://github.com/AViollet74).
