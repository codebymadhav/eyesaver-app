from plyer import notification
import time
import random

strings = ["Remember to take a 5-minute break every hour to rest your eyes and stretch your legs",
           "A quick walk or stretch can boost your productivity and reduce eye strain.",
           "Taking regular breaks can help prevent burnout and keep you energized throughout the day",
           "Step away from your screen and refresh your mind for better focus",
           "Give your eyes a break: Look away from your screen and focus on a distant object for a few minutes",
           "Move around! A few minutes of physical activity can do wonders for your concentration.",
           "Short breaks improve mental clarity and creativity. Step away from your computer for a bit!",
           "It's time for a break! Stand up, stretch, and take a deep breath.",
           "Break time! Step away from your computer and recharge with a brief pause."]

if __name__=='__main__':
    while True:
        random_string = random.choice(strings)
        notification.notify(
        title='Take rest',
        message=random_string,
        app_icon='yoga.ico',
        timeout=5)
        
        time.sleep(1200)#20 minutes break