# WorkSampleSimulation
User Manual: Running "WorkSampleSimulation.py"

Python: Ensure that Python is installed on your system. You can download the latest version from the official Python website (https://www.python.org) and follow the installation instructions specific to your operating system.



Download the "WorkSampleSimulation.py" script and save it to a folder of your choice.
Place the "ssh_logs_sample" file in the same folder as the script. Ensure that the input file has the exact name "ssh_logs_sample" without any additional extensions in case that user want to use a diferent log file , delete the default "ssh_logs_sample" and add the new log with that exact name

Running the Script

Windows:
Follow these steps to run the script on a Windows system:

Open the Command Prompt:
Press Win + R to open the Run dialog.
Type cmd and press Enter.
Navigate to the folder where you saved the script and input file using the cd command. For example, if the script is located in the "C:\Scripts" folder, run the following command:
bash
Copy code
cd C:\Scripts
Execute the script by running the following command:
Copy code
python WorkSampleSimulation.py
Enter the IP address when prompted by the script.
The script will process the data and display the number of login attempts from the specified IP address.
Linux:
Follow these steps to run the script on a Linux system:

Open a terminal by searching for "Terminal" in the applications menu or using the keyboard shortcut Ctrl + Alt + T.
Navigate to the folder where you saved the script and input file using the cd command. For example, if the script is located in the "/home/user/scripts" folder, run the following command:
bash
Copy code
cd /home/user/scripts
Execute the script by running the following command:
Copy code
python3 WorkSampleSimulation.py
Enter the IP address when prompted by the script.
The script will process the data and display the number of login attempts from the specified IP address.
macOS:
Follow these steps to run the script on a macOS system:

Launch the Terminal application. You can find it in the "Applications/Utilities" folder or use the Spotlight search (press Cmd + Space and type "Terminal").
Navigate to the folder where you saved the script and input file using the cd command. For example, if the script is located in the "/Users/username/scripts" folder, run the following command:
bash
Copy code
cd /Users/username/scripts
Execute the script by running the following command:
Copy code
python3 WorkSampleSimulation.py
Enter the IP address when prompted by the script.
The script will process the data and display the number of login attempts from the specified IP address.