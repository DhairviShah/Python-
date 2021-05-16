import time
from plyer import notification

def drink_notify():
    notification.notify(
 			title = "Please Drink Water Now!!",
 			message ="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
 			app_icon = "C://Users//mis//Desktop//python//Drink water notify//water.ico" ,
            timeout = 6
            )


if __name__ == '__main__':
 	while True:
 		drink_notify()
 		#	time.sleep(6)
 		time.sleep(60*60)