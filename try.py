import random
import time
from datetime import datetime
import tkinter
from tkinter import scrolledtext

class Device:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = 'Off'

    def turn_on(self):
        self.status = 'On'
        self.save_device_status("sensor_data.txt")
        self.update_status_label()

    def turn_off(self):
        self.status = 'Off'
        self.save_device_status("sensor_data.txt")
        self.update_status_label()

    def update_status_label(self):
        pass

    def save_device_status(self, filename): #save the status of device in the file
        with open(filename, 'a') as file:
            current_datetime = datetime.now()  #get the current time
            timestamp_str = current_datetime.strftime('%Y:%m:%d %H:%M:%S')
            file.write(f"Time: {timestamp_str}, Device: {self.device_id}, Status: {self.status}\n")

class SmartLight(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.brightness = 20 #default brightness
        self.min_bright = 0
        self.max_brihgt = 100
    
    def set_brightness_up(self):
        if self.status == 'On':
            if self.min_bright < self.brightness < self.max_brihgt:
                self.brightness = self.brightness + 1
                self.save_SmartLight_data("sensor_data.txt")
                current_brightness_label.config(text=f'Living room Light Brightness: {smartlight.brightness}%')
                root.update()
                print(f"Brightness sets {self.brightness}%")
            else:
                print(f"Plese select the number between {self.min_bright}% and {self.max_brihgt}%")
        else:
            print("The current status is Off")

    def set_brightness_down(self):
        if self.status == 'On':
            if self.min_bright < self.brightness < self.max_brihgt:
                self.brightness = self.brightness - 1
                self.save_SmartLight_data("sensor_data.txt")
                current_brightness_label.config(text=f'Living room Light Brightness: {smartlight.brightness}%')
                root.update()
                print(f"Brightness sets {self.brightness}%")
            else:
                print(f"Plese select the number between {self.min_bright}% and {self.max_brihgt}%")
        else:
            print("The current status is Off")

    def update_status_label(self):
        status_label.config(text=f'Living room Light : {self.status}')
        root.update()  # update the window

    def save_SmartLight_data(self, filename):
        with open(filename, 'a') as file:
            current_datetime = datetime.now()  #get the current time
            timestamp_str = current_datetime.strftime('%Y:%m:%d %H:%M:%S')
            file.write(f"Time: {timestamp_str}, Device: {self.device_id}, Status: {self.status}, Brightness: {self.brightness}%\n")
    

class Thermostat(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.temperature = 20 #default temperautere
        self.min_temp = 15
        self.max_temp = 40

    def set_temperature_up(self):
        if self.status == 'On':
            if self.min_temp < self.temperature < self.max_temp:
                self.temperature = self.temperature + 1
                self.save_Thermostat_data("sensor_data.txt")
                current_temperature_label.config(text=f'Living room Temperature: {thermostat.temperature}')
                root.update()
                print(f"The current temperature is {self.temperature}")
            else:
                print(f"Please select the number between {self.min_temp} and {self.max_temp}")
        else:
           print("The current status is Off")

    def set_temperature_down(self):
        if self.status == 'On':
            if self.min_temp < self.temperature < self.max_temp:
                self.temperature = self.temperature - 1
                self.save_Thermostat_data("sensor_data.txt")
                current_temperature_label.config(text=f'Living room Temperature: {thermostat.temperature}')
                root.update()
                print(f"The current temperature is {self.temperature}")
            else:
                print(f"Please select the number between {self.min_temp} and {self.max_temp}")
        else:
           print("The current status is Off")

    def update_status_label(self):
        current_temperature_status.config(text=f'Living room Thermostat : {self.status}')
        root.update()  # update the window

    def save_Thermostat_data(self, filename):
        with open(filename, 'a') as file:
            current_datetime = datetime.now()  #get the current time
            timestamp_str = current_datetime.strftime('%Y:%m:%d %H:%M:%S')
            file.write(f"Time: {timestamp_str}, Device: {self.device_id}, Status: {self.status}, Temperature: {self.temperature}\n")

class SecurityCamera(Device):
    def __init__(self, device_id):
        super().__init__(device_id)

    def update_status_label(self):
        current_camara_status.config(text=f'Security Camera : {self.status}')
        root.update()  # update the window

class SmartKey(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
    
    def lock_key(self):
        self.turn_on()
        print("The door is locked")
        
    def unlock_key(self):
        self.turn_off()
        print("The door is unlocked")

    def update_status_label(self):
        current_key_status.config(text=f'Smart Key : {self.status}')
        root.update() #update the window


class AutomationSystem:
    def __init__(self):
        self.devices = []
        self.sensor_data = []
        self.motion = 'No'
        self.automation = 'Off'

    def add_discovering_device(self, device):
        if device in self.devices:
            print(f"This device is already registerd")
        else:
            self.devices.append(device)  #add the device to the list

    def excute_task(self):
        self.motion = random.choice(["Yes", "No"])
        motion_detect_label.config(text=f'Motion Detection : {self.motion}')
        root.update()
        if self.motion == 'Yes':
            print("Motion detected")
        else:
            print("Motion is not detected")

        for device in self.devices:
            if isinstance(device, SmartLight) and self.motion == 'Yes': #if motion is detected light will be turn on automatically
                device.turn_on()
                print(f"Motion detected! Turning on {device.device_id}")

            elif isinstance(device, SmartKey) and self.motion == 'Yes': #if motion is detected smartkey will be unlocked
                device.unlock_key()
            elif isinstance(device, SmartKey) and self.motion == 'No': #if motion is detected smartkey will be locked
                device.lock_key()

            elif isinstance(device, SecurityCamera) and self.motion == 'Yes': #if motion is detected security camera will be turned on
                device.turn_on()
                print(f"Motion detected! Turning on {device.device_id}")

    def excute_randomly_andsave(self, filename):
        self.automation = 'On'
        print(f"Automation : {self.automation}")
        random_label.config(text=f'Automation Status : {automationsystem.automation}')
        root.update()  # update the window
        while self.automation != 'Off':
            for device in self.devices:
                with open(filename, 'a') as file:
                    current_datetime = datetime.now()  #get the current time
                    timestamp_str = current_datetime.strftime('%Y:%m:%d %H:%M:%S')
                    if isinstance(device, SmartLight):
                        device.status = random.choice(["On", "Off"])
                        status_label.config(text=f'Living room Light : {smartlight.status}')
                        root.update()  # update the window
                        print(f"{device.device_id} is {device.status}")
                        if device.status == 'On':
                            device.brightness = random.randint(0, 100)
                            current_brightness_label.config(text=f'Living room Light Brightness: {smartlight.brightness}%')
                            root.update()
                            print(f"Brightness is {device.brightness}%")
                        file.write(f"Time: {timestamp_str}, Device: {device.device_id}, Status: {device.status}, Brightness: {device.brightness}%\n")
                    elif isinstance(device, Thermostat):
                        device.status = random.choice(["On", "Off"])
                        current_temperature_status.config(text=f'Living room Thermostat : {thermostat.status}')
                        root.update()  # update the window
                        print(f"{device.device_id} is {device.status}")
                        if device.status == 'On':
                            device.temperature = random.randint(15, 40)
                            current_temperature_label.config(text=f'Living room Temperature: {thermostat.temperature}')
                            root.update()
                            print(f"Temperature is {device.temperature}")
                        file.write(f"Time: {timestamp_str}, Device: {device.device_id}, Status: {device.status}, Temperature: {device.temperature}\n")
                    elif isinstance(device, SecurityCamera):
                        device.status = random.choice(["On", "Off"])
                        current_camara_status.config(text=f'Security Camera : {securitycamera.status}')
                        root.update()  # update the window
                        print(f"{device.device_id} is {device.status}")
                        file.write(f"Time: {timestamp_str}, Device: {device.device_id}, Status: {device.status}\n")
                    elif isinstance(device, SmartKey):
                        device.status = random.choice(["On", "Off"])
                        current_key_status.config(text=f'Smart Key : {smartkey.status}')
                        root.update() #update the window
                        print(f"{device.device_id} is {device.status}")
                        file.write(f"Time: {timestamp_str}, Device: {device.device_id}, Status: {device.status}\n")
            time.sleep(5) #we have 5 second to change the status again

    def automation_turn_off(self):
        self.automation = 'Off'
        random_label.config(text=f'Automation Status : {automationsystem.automation}')
        root.update()  # update the window
        print(f"Automation : {self.automation}")


    def random_excute(self):
        self.excute_randomly_andsave("sensor_data.txt")
        
def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return  str(e)
    
def update_content():
    file_path = "sensor_data.txt" #designate the file name

    new_content = read_file_content(file_path)
    current_content = text.get(1.0, tkinter.END)

    if current_content != new_content:
        text.delete(1.0, tkinter.END)
        text.insert(tkinter.END,new_content)
        text.see(tkinter.END)

    root.after(1000, update_content) #update the content per second




#Code for Gui
root = tkinter.Tk()
root.title('Smart Home IoT Simulator')
root.geometry('600x600')
smartlight = SmartLight(device_id='Smartlight')
thermostat = Thermostat(device_id='Thermostat')
securitycamera = SecurityCamera(device_id='Securitycamera')
smartkey = SmartKey(device_id='Smartkey')
automationsystem = AutomationSystem()
automationsystem.add_discovering_device(smartlight)
automationsystem.add_discovering_device(thermostat)
automationsystem.add_discovering_device(securitycamera)
automationsystem.add_discovering_device(smartkey)

#label of Smartlight
current_brightness_label = tkinter.Label(root, text=f"Living room Light Brightness: {smartlight.brightness}%")
status_label = tkinter.Label(root, text=f"Living room Light : {smartlight.status}")
#label of Thermostat
current_temperature_label = tkinter.Label(root, text =f"Living room Temperature : {thermostat.temperature}")
current_temperature_status = tkinter.Label(root, text =f"Living room Thermostat : {thermostat.status}")
#label of SecurityCamera
current_camara_status = tkinter.Label(root, text = f"Security Camera : {securitycamera.status}")
#label of SmartKey
current_key_status = tkinter.Label(root, text = f"Smart Key : {smartkey.status}")
#label of motion detect
motion_detect_label = tkinter.Label(root, text=f'Motion Detection : {automationsystem.motion}')
motion_rule1 = tkinter.Label(root, text='Motion Detection - Yes : SmartLight - On, Smartkey - Off, SecurityCamera - On')
motion_rule2 = tkinter.Label(root, text = 'Motion Detection - No : Smartkey - On')
#label of randome
random_label = tkinter.Label(root, text=f'Automation Status : {automationsystem.automation}')
#button for SmartLight
brightness_turn_on = tkinter.Button(root, text="On", command=smartlight.turn_on, width=5, bg='gray')
brightness_turn_off = tkinter.Button(root, text="Off", command=smartlight.turn_off, width=5, bg='gray')
brightness_up_button = tkinter.Button(root, text="+", command=smartlight.set_brightness_up, width=5, bg='gray')
brightness_down_button = tkinter.Button(root, text="-", command=smartlight.set_brightness_down, width=5, bg='gray')
#button for Thermostat
thermostat_turn_on = tkinter.Button(root, text="On", command=thermostat.turn_on, width=5, bg='gray')
thermostat_turn_off = tkinter.Button(root, text="Off", command=thermostat.turn_off, width=5, bg='gray')
thermostat_up_button = tkinter.Button(root, text="+", command=thermostat.set_temperature_up, width=5, bg='gray')
thermostat_down_button = tkinter.Button(root, text="-", command=thermostat.set_temperature_down, width=5, bg='gray')
#button for security camera
securitycamera_turn_on = tkinter.Button(root, text = "On", command=securitycamera.turn_on, width=5, bg='gray')
securitycamera_turn_off = tkinter.Button(root, text= "Off", command=securitycamera.turn_off, width=5, bg='gray')
#button for smartkey
smartkey_turn_on = tkinter.Button(root, text = "On", command=smartkey.turn_on, width=5, bg='gray')
smartkey_turn_off = tkinter.Button(root, text = "Off", command=smartkey.turn_off, width=5, bg='gray')
#button for motion detection
motion_button = tkinter.Button(root, text ='Random Detect Motion', command=automationsystem.excute_task, width=25, bg='gray')
#button for random
random_activate_button = tkinter.Button(root, text='On', command=automationsystem.random_excute, width=5, bg='gray')
random_turn_off_button = tkinter.Button(root, text='Off', command=automationsystem.automation_turn_off, width=5,bg='gray')
#file
text = scrolledtext.ScrolledText(root, height= 14)
text.place(x=20,y=400)
update_content()
#smartlight
status_label.place(x=75,y=0)
current_brightness_label.place(x=50, y=60)
brightness_up_button.place(x=80, y=90)
brightness_down_button.place(x=145, y=90)
brightness_turn_on.place(x=80, y=30)
brightness_turn_off.place(x=145, y=30)
#thermostat
current_temperature_status.place(x = 370, y= 0)
thermostat_turn_on.place(x=395, y=30)
thermostat_turn_off.place(x=460, y=30)
current_temperature_label.place(x=370, y=60)
thermostat_up_button.place(x=395,y=90)
thermostat_down_button.place(x=460, y=90)
#securitycamera
current_camara_status.place(x=75,y=140)
securitycamera_turn_on.place(x=80,y=170)
securitycamera_turn_off.place(x=145,y=170)
#smartkey
current_key_status.place(x=410, y=140)
smartkey_turn_on.place(x=395,y=170)
smartkey_turn_off.place(x=460,y=170)
#motion detection
motion_detect_label.place(x=250,y=210)
motion_button.place(x= 220,y=235)
motion_rule1.place(x=120, y=270)
motion_rule2.place(x=120,y=290)
#random
random_label.place(x=250, y=330)
random_activate_button.place(x=260,y=360)
random_turn_off_button.place(x=325,y=360)

root.mainloop()
