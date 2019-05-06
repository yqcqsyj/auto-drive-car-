# auto-drive-car

Hardware:Rapberry Pi, Rapberry Pi Camera, 2WD assemble car kit, L298N motor driver, female-female Dupont line, male-female Dupont line

Usage method：

1.Assemble the raspberry cart hardware.

2.Use car.py to control the front and rear movement of the car, and cooperate with collect_data.py to operate manually, so that the car can collect data on its own runway. (the process is carried out in Raspberry Pi)

3.After data acquisition is completed, process_img.py is used to process the collected data, and some data cleaning work is completed before. (computer execution)

4.Using neural network model to train data, train.py, get a trained model. (computer execution)

5.Auto-driving on the original runway can be realized by using zth_drive and trained model in the raspberry dispatch car and loading the model. (raspberry pie execution)

