#!/usr/bin/python

# Example using a character LCD connected to a Raspberry Pi
import time
import random
import Adafruit_CharLCD as LCD


# Raspberry Pi pin configuration:
lcd_rs        = 25
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 21
lcd_d7        = 22

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# decalare the variable lists 

firstnamelist = [
			'Audience Recognition',
		    'Big Data',
			'Bitcoin',
			'Brand Experience',
			'Brand Score',
			'Brand Story',
			'Brogramming',
		    'Chief Uber',
			'Cloud',
			'Contextual Computing',
			'Culture',
			'Click-Through',
			'Collaboration',
			'Connection',
			'Content',
			'Convergence',
			'Conversation',
			'Crowdfunding',
			'Cryptocurrency',
			'Data',
			'Decentralized Information Asset',
			'DevOps',
			'Digital',
			'Digital Media',
			'Engagement',
			'Emoji',
			'Facebook',
			'Functionality',
			'Human Experience',
			'Idea',
			'In-House Social Media',
			'Information',
			'Innovation',
			'Intelligence',
			'Kickstarter',
			'Longform Engagement',
			'Mobile Intimacy',
			'Mobile Platform',
			'Naked',
			'Online Space',
		    'Pinterest',
		    'Platform',
		    'Principal Digital Imaging',
		    'Quantification',
		    'Reddit',
		    'Scalability',
		    'Self-Quantification',
		    'Senior Information',
		    'Shareability',
			'Social Media',
			'Software',
			'Startup',
			'Strategic Partnership',
			'Tablet',
			'Technology',
			'Thought',
			'Tinder',
			'Trend',
			'Tumblr',
			'Twitter',
			'User Experience',
			'Unique Experience',
			'Video Experience',
			'Wearables',
			'Webinar']
			
lastnamelist = [
			 'Advocate',
			 'Amplifier',
			 'Architect',
			 'Agitator',
			 'Baron',
			 'Commander',
			 'Conductor',
			 'Connector',
			 'Consultant',
			 'Curator',
			 'Custodian',
			 'Directress',
		     'Disruptor', 
			 'Disruptionist',
	         'Disruptor',  
	         'Evangelist',
			 'Fellow',
			 'Futurist',
			 'Hacker',
             'Hacktivist',
			 'Gatekeeper',
			 'General',
			 'Guardian',
			 'Guru',
			 'Instigator',
			 'Lord',
			 'Maestro',
			 'Mastermind',
			 'Maven',
			 'Mentor',
			 'Messiah',
			 'Minister',
			 'Mystic',
			 'Nerd',
			 'Ninja',
			 'Officer',
			 'Overlord',
			 'Philosopher',
			 'Prophet',
			 'Pioneer',
			 'Proctor',
			 'Resident',
			 'Revisionist',
			 'Sage',
             'Savant',
			 'Seer',
			 'Sentry',
			 'Shaman',
			 'Shepherd',
			 'Sherpa',
			 'Steward',
			 'Strategist',
			 'Sultan',
			 'Superintendent',
			 'Svengali',
			 'Tinkerer',
			 'Translator',
			 'Tsar',
			 'Visionary',
			 'Warden',
			 'Warlock',
			 'Watchman',
			 'Wizard']
            
fullnamelist = [
			 'Conductor of Datafication',   
			 'Crowd-Funder-in-Residence',
			 'Quantified-Self-in-Residence',
			 'Creator of Things',
			 'Curator of Datafication',
			 'Curator of Brand Stories',
			 'Custodian of Datafication',
			 'Custodian of the Quantified Self',
			 'Custodian of the Twitterverse',
			 'Custodian of the Reddit-sphere',
			 'Brogrammer-in-Residence',
			 'Data-Miner-in-Residence',
			 'Digitizer-in-Residence',
	         'Disruptor-in-Residence',
	         'Early-Adopter-in-Residence',
			 'Explainer-in-Residence',
			 'Game-Changer-in-Residence',
			 'Gamifyer-in-Residence',
			 'Geek-in-Residence',
			 'Genius-in-Residence',
			 'Grand Poobah of Bitcoin',
			 'Grand Poobah of Brand Utilization',
			 'Grand Poobah of Cryptocurrencies',
			 'Grand Poobah of Big Data',
			 'Grand Poobah of Digital Media',
			 'Grand Poobah of Digital Innovation',
			 'Grand Poobah of Disruptive Innovation',
			 'Grand Poobah of Functionality',
			 'Grand Poobah of Scalability',
			 'Grand Poobah of the Online Space',
			 'Grand Poobah of Wearables',
			 'Grand Poobah of Video Experience',
			 'Hacker-in-Chief',
			 'High Priest of Bitcoins',
			 'High Priest of Cryptocurrencies',
			 'High Priest of Brand Utilization',
			 'High Priestess of Data',
			 'High Priest of Datafication',
			 'High Priestess of Digital Media Solutions',
			 'High Priest of Digital Innovation',
			 'High Priestess of Disruptive Innovation',
			 'High Priest of Functionality',
			 'High Priestess of the Quantified Self',
			 'High Priest of Scalability',
			 'High Priest of the Online Space',
			 'High Priest of Wearables',
			 'High Preist of Video Experience',
			 'In-House Cryptocurrency Wizard',
			 'In-House Data Miner',
			 'In-House Disruptor',
			 'In-House Explainer',
			 'In-House Game Changer',
			 'In-House Gamifyer',
			 'In-House Genius',
			 'In-House Evangelist',
			 'In-House Pioneer',
			 'In-House Tech Evangelist',
			 'In-House Tech Mastermind',
			 'In-House Tech Maven',
			 'In-House Tech Mentor',
			 'In-House Tech Mystic',
			 'In-House Tech Pioneer',
			 'In-House Tech Primo',
			 'In-House Tech Sage',
			 'In-House Tech Shaman',
			 'In-House Tech Sherpa',
			 'In-House Tech Sultan',
			 'In-House Tech Superintendent',
			 'In-House Tech Svengali',
			 'In-House Tech Wizard',
			 'Influencer-in-Residence',
			 'Harbinger of Digital Media',
			 'Harbinger of Disruptive Innovation',
			 'Instagrammer-in-Chief',
			 'Instagrammer-in-Residence',
			 'Maker of Things',
			 'Mastermind-in-Residence',
			 'Maven-in-Residence',
			 'Mentor-in-Residence',
			 'Nerd-in-Residence',
			 'Resident Agitator',
			 'Resident Brogrammer',
			 'Resident Digitizer',
			 'Resident Disruptionist',
			 'Resident Evangelist',
			 'Resident Future-Maker',
			 'Resident Gamifyer',
			 'Resident Influencer',
			 'Resident Mastermind',
			 'Resident Nerd',
			 'Resident Tech Maven',
			 'Resident Tech Mentor',
			 'Resident Tech Mystic',
			 'Resident Tech Pioneer',
			 'Resident Tech Primo',
			 'Resident Tech Sage',
			 'Resident Tech Shaman',
			 'Resident Tech Sherpa',
			 'Resident Tech Sultan',
			 'Resident Tech Svengali',
			 'Resident Tech Wizard',			 
			 'Resident Thought Leader',
			 'Pioneer-in-Residence',
			 'Snapchatter-in-Residence',
			 'Tech-Shaman-in-Residence',
			 'Tech-Sherpa-in-Residence',
			 'Tech-Sultan-in-Residence',
			 'Tech-Svengali-in-Residence',
			 'Tech-Wizard-in-Residence',			 
			 'Thought-Leader-in-Residence']		



def getNewJob():
    x = random.randint(1,3)
    if x == 1:
        return random.choice(fullnamelist)
    else:
        return random.choice(firstnamelist)+' '+random.choice(lastnamelist)

# Print a two line message
message = 'Edward Pryor:  \n'
message2 = getNewJob()
#message2 = random.choice(fullnamelist)
#lcd.message(message+message2)
i = 0
oldtime = time.time()
deleteflag = False
while True:
    time.sleep(0.5)
    if len(message2) <= 16:
        message2 = message2.ljust(16)
        lcd.message(message+message2)
        if time.time() - oldtime >=60:
            oldtime=time.time()
            #message2 = random.choice(fullnamelist)
            message2 = getNewJob()
    else:
        if not deleteflag:
            m = message2+'   '+message2
        else:
            m = message2+'                  '
        disp = m[i:16+i]
        lcd.message(message+disp)
        i = i+1
        if i >= len(message2)+3:
            i = 0
            if deleteflag:
                # message2 = random.choice(fullnamelist)
                message2 = getNewJob()
                deleteflag = False
        if time.time() - oldtime >=60 and i < 16:
            deleteflag = True
            oldtime=time.time()

