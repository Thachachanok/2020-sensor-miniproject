## EC463 Hardware Mini Project Report

Brandon Miller, Thachachanok (Pan) Menasuta

Since this assignment mostly involves data analysis, we decided to work separately in our own repository and cross-check the results. Both repositories are submitted.

### Task 0
The greeting message is “ECE Senior Capstone IoT simulator”

### Task 1
See attached code in the repositories.

### Task 2

 Both of us separately collected and analyzed the data.
	
    Brandon’s Data: 
    Class 1 Temperature (Degrees Celsius) Median: 26.99, Variance: 24.47
    Lab 1 Temperature (Degrees Celsius) Median: 20.99, Variance: 22.99
    Office Temperature (Degrees Celsius) Median: 23.02 Variance: 3.68
    Class 1 Occupancy Median: 19 Variance: 19.35
    Lab 1 Occupancy Median: 5 Variance: 5.07
    Office Occupancy Median: 2 Variance: 2.11
    Run the analyze file to see the PDF of each sensor type
    Time Interval (seconds): Mean: 0.62 Variance: 1.19
    The time interval PDF (see analyze.py) mimics a Gaussian distribution
    
. 

    Thachachanok’s Data obtained from dataAnalyze.py
    All Room Temperature Data: Median: 23.00 Celsius, Variance: 36.64 Celcius
    All Room Occupancy Data: Median: 5.0, Variance: 64.40 
    I chose the room ‘Class1’: Please see the distribution in the files Figure1-4.jpg
    Time Interval: Median = 0.64 second, Variance = 0.96 second
    
The time interval distribution mimics a Gaussian distribution.

### Task 3
* We defined the anomaly data points to be the ones that are three times the standard deviations away from the mean value. We separately find these anomalies.
Thachachanok’s ‘dataAnalyze.py’ code lists out the anomalies as a text file named ‘anamoly.txt’. The file 'analyze.py' was not used.
Brandon’s design.py code finds the amount of anomalies for the temperature sensors in each room, and prints them out in the terminal window. 
Anomalies:

    Class 1: 14

    Lab 1: 14

    Office: 20

* Persistent changes in temperature does not always indicate a failed sensor. The data from a failed sensor would not form a bell-shaped or distribution.

* We defined the bounds of the temperature to be three standard deviations away from the mean values. These bounds are (in degrees Celsius):

    Class1: Upper: 41.9 Lower:12.24

    Lab1: Upper: 35.27 Lower:6.51

    Office: Upper: 28.84 Lower:17.34

### Task 4
* In the real world the activities happening in the room will contribute to the randomness of the data and will be the reason that the data distribution resembles a normal distribution.
* The simulation fails to account for typical human cycles. The data readings during the middle of the day were the same as the data readings during the middle of the night. In most typical building environments there would be a noticeable difference in the data readings between night and day. Additionally there doesn’t seem to be enough correlation between the CO2 and the occupancy data which contradicts the fact that humans produce CO2.
 
* We were glad to use the Python websockets instead of the C++ websockets, because of their built-in modules that were easier to work with in our opinion.
 
* We believe that it is better to have the server continuously poll the sensors as it is a good method of affirming that the sensors are working. A possible drawback is the energy consumption which can easily be solved by using energy-efficient sensors and mode of communication.
