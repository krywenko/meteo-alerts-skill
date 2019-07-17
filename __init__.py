from mycroft import MycroftSkill, intent_file_handler
import subprocess
import os.path
#import os


class MeteoAlerts(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)


    def initialize(self):
        self._setup()
        self.settings.set_changed_callback(self.on_websettings_changed)

    def on_websettings_changed(self):
        # Only attempt to load if the host is set
        self.log.debug("websettings changed")
        self._setup()

    def _setup(self):
        self.web_id = self.settings.get('web_id','')
        self.title_id = self.settings.get('title_id','')
        self.cap_id = self.settings.get('cap_id','')
        self.lang_id = self.settings.get('lang_id','')
        
        
        SETTINGS = self.web_id + " \'" + self.title_id + "\' " + self.cap_id + " " + self.lang_id
        print(self.web_id + " \'" + self.title_id + "\' " + self.cap_id + " " + self.lang_id)
        RUN = os.popen("skills/meteo-alerts-skill/./ALERT " + self.web_id + " \'" + self.title_id + "\' " + self.cap_id + " " + self.lang_id + " >/tmp/metro 2>&1 | echo started") 

    @intent_file_handler('alerts.meteo.intent')
    def handle_alerts_meteo(self, message):
        self.log.debug("handle_alerts for web_id {}".format(self.web_id))
        if not self.web_id:
            self.speak_dialog('error')
            return
        ##alerts = os.popen("ls").read()
        alerts = os.popen("skills/meteo-alerts-skill/./alert.sh " + self.web_id + " \'" + self.title_id + "\' " + self.cap_id + " " + self.lang_id).read()
        mesg = os.popen("skills/meteo-alerts-skill/./mesg.sh "+ self.web_id + " \'" + self.title_id + "\' " + self.cap_id + " " + self.lang_id).read()
        print(alerts)
        print(self.web_id + " \'" + self.title_id + " \' " + self.cap_id + " " + self.lang_id)
        self.speak(alerts)  
        #self.speak(' Currently ')
        self.speak(mesg)

def create_skill():
    return MeteoAlerts()

