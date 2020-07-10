# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime
import plotly.graph_objects as go
import plotly.express as px
import chart_studio
import chart_studio.plotly as py
import plotly.io as pio
import pandas as pd
from statistics import mean
import os
import shutil
import random

date = "2020-04-01"
username = 'spaz_277'
api_key = 'tlLUmEVdfFpr9IFr7qfk'
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
leakages = {"Pump3Vindhya" : 0 , "Pump3GuestHouse" : 0, "PumpP5Vindhya" : 0, "PumpP5Bakul" : 0, "PumpP9NBHParijat" : 0, "PumpP9GuestHouse" : 0 ,"PumpP8OBH": 0, "PumpP10Himalaya" : 0,"PumpP1FacultyQuarters" : 0,"ManjeeraVindhya" : 0, "ManjeeraNBHParijat" : 0, "ManjeeraFacultyQuarters" : 0}
class Final(models.Model):
    id = models.SmallIntegerField(db_column='Sno', primary_key=True)  # Field name made lowercase.
    recdate = models.DateField(db_column='RecDate', blank=True, null=True)  # Field name made lowercase.
    old_qtr = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ananda_nivas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    budha_nivas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    palash = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    kadamb = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    parijaat = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bakul = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sahana_aithi_house = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nilgiri = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    vindhya = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    admin_block = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    krb = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bodh = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total_in_kl = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    type_of_reading = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'final'

    def get_by_date(self, date):
        x = []
        for e in self.objects.all():
            if e.recdate == date:
                x.append(e.total_in_kl)
        fin = round(sum(x), 2)
        avg = self.get_avg_by_season(self)
        if fin < 2*avg[0]:
            return fin
        else:
            return "Anomaly Detected!"

    def get_avg_by_block(self):
        old_qtr = []
        ananda_nivas = []
        budha_nivas = []
        palash = []
        kadamb = []
        parijaat = []
        bakul = []
        sahana_aithi_house = []
        nilgiri = []
        vindhya = []
        admin_block = []
        krb = []
        bodh = []
        count = 0
        for e in self.objects.all():
            old_qtr.append(e.old_qtr)
            ananda_nivas.append(e.ananda_nivas)
            budha_nivas.append(e.budha_nivas)
            palash.append(e.palash)
            kadamb.append(e.kadamb)
            parijaat.append(e.parijaat)
            bakul.append(e.bakul)
            sahana_aithi_house.append(e.sahana_aithi_house)
            nilgiri.append(e.nilgiri)
            vindhya.append(e.vindhya)
            admin_block.append(e.admin_block)
            krb.append(e.krb)
            bodh.append(e.bodh)
            if e.type_of_reading == "Manjeera Water":
                count = count + 1
        avg = []
        avg.append(round(sum(old_qtr)/count,2))
        avg.append(round(sum(ananda_nivas)/count, 2))
        avg.append(round(sum(budha_nivas)/count, 2))
        avg.append(round(sum(palash)/count, 2))
        avg.append(round(sum(kadamb)/count, 2))
        avg.append(round(sum(parijaat)/count, 2))
        avg.append(round(sum(bakul)/count, 2))
        avg.append(round(sum(sahana_aithi_house)/count, 2))
        avg.append(round(sum(nilgiri)/count, 2))
        avg.append(round(sum(vindhya)/count, 2))
        avg.append(round(sum(admin_block)/count, 2))
        avg.append(round(sum(krb)/count, 2))
        avg.append(round(sum(bodh)/count, 2))

        per = []
        for block in avg:
            per.append(block/sum(avg)*100)
        blks = ['Old Quarter','Ananda Nivas', 'Budha Nivas', 'Palash Nivas', 'Kadamba', 'Parijaat', 'Bakul Nivas', 'Sahana Aithi House', 'Nilgiri', 'Vindhya', 'Admin Block', 'KCIS', 'Himalya Bodh']
        avgpp = {}
        pop = [100,100,300,1200,300,500,600,100,400,800,100,200,300]
        for i in range(13):
            d = {blks[i]:round(avg[i]/pop[i], 2)}
            avgpp.update(d)
        avgpp = {k: v for k, v in sorted(avgpp.items(), key=lambda item: item[1])}
        return avg, per, avgpp

    def get_avg_by_season(self):
        winter = []
        spring = []
        summer = []
        monsoon = []

        win = ['Nov', 'Dec', 'Jan']
        spr = ['Feb', 'Mar']
        summ = ['Apr', 'May', 'Jun', 'Jul']
        mon = ['Aug', 'Sep', 'Oct']

        for e in self.objects.all():
            if e.recdate.strftime('%b') in win:
                winter.append(e.total_in_kl)
            if e.recdate.strftime('%b') in spr:
                spring.append(e.total_in_kl)
            if e.recdate.strftime('%b') in summ:
                summer.append(e.total_in_kl)
            if e.recdate.strftime('%b') in mon:
                monsoon.append(e.total_in_kl)
        avg = []
        avg.append(2*sum(winter)/len(winter))
        avg.append(2*sum(spring)/len(spring))
        avg.append(2*sum(summer)/len(summer))
        avg.append(2*sum(monsoon)/len(monsoon))

        return avg

    def get_avg_by_weekday(self):
        mon = []
        tue = []
        wed = []
        thur = []
        fri = []
        sat = []
        sun = []

        for e in self.objects.all():
            if e.recdate.strftime('%a') == "Mon":
                mon.append(e.total_in_kl)
            if e.recdate.strftime('%a') == "Tue":
                tue.append(e.total_in_kl)
            if e.recdate.strftime('%a') == "Wed":
                wed.append(e.total_in_kl)
            if e.recdate.strftime('%a') == "Thu":
                thur.append(e.total_in_kl)
            if e.recdate.strftime('%a') == "Fri":
                fri.append(e.total_in_kl)
            if e.recdate.strftime('%a') == "Sat":
                sat.append(e.total_in_kl)
            if e.recdate.strftime('%a') == "Sun":
                sun.append(e.total_in_kl)

        avg = []
        avg.append(2*sum(mon)/len(mon))
        avg.append(2*sum(tue)/len(tue))
        avg.append(2*sum(wed)/len(wed))
        avg.append(2*sum(thur)/len(thur))
        avg.append(2*sum(fri)/len(fri))
        avg.append(2*sum(sat)/len(sat))
        avg.append(2*sum(sun)/len(sun))

        return avg

    def curr_week(self):
        curr = datetime.date.today()
        curr_yr = curr.year - 1
        curr = curr.replace(year = curr_yr)
        week = []
        for i in range(7):
            ans = self.get_by_date(self, curr)
            week.append(ans)
            curr = curr - datetime.timedelta(days = 1)
        week = list(reversed(week))
        return week

    def val_by_month(self):
        jan = []
        feb = []
        mar = []
        apr = []
        may = []
        jun = []
        jul = []
        aug = []
        sep = []
        octo = []
        nov = []
        dec = []

        for e in self.objects.all():
            if e.recdate.strftime('%b') == "Jan":
                jan.append(e.total_in_kl)
            if e.recdate.strftime('%b') == "Feb":
                feb.append(e.total_in_kl)
            if e.recdate.strftime('%b') == "Mar":
                mar.append(e.total_in_kl)
            if e.recdate.strftime('%b') == "Apr":
                apr.append(e.total_in_kl)
            if e.recdate.strftime('%b') == "Jun":
                jun.append(e.total_in_kl)
            if e.recdate.strftime('%b') == "Jul":
                jul.append(e.total_in_kl)
            if e.recdate.strftime('%b') == "Aug":
                aug.append(e.total_in_kl)
            if e.recdate.strftime('%b') == "Oct":
                octo.append(e.total_in_kl)
            if e.recdate.strftime('%b') == "Nov":
                nov.append(e.total_in_kl)
            if e.recdate.strftime('%b') == "Sep":
                sep.append(e.total_in_kl)
            if e.recdate.strftime('%b') == "Dec":
                dec.append(e.total_in_kl)
            if e.recdate.strftime('%b') == "May":
                may.append(e.total_in_kl)


        month = []
        month.append(sum(jan))
        month.append(sum(feb))
        month.append(sum(mar))
        month.append(sum(apr))
        month.append(sum(may))
        month.append(sum(jun))
        month.append(sum(jul))
        month.append(sum(aug))
        month.append(sum(sep))
        month.append(sum(octo))
        month.append(sum(nov))
        month.append(sum(dec))
        # print(month)

        return month


    def getgraph_avgblock_pie(self):
        x = ['Old Quarter','Ananda Nivas', 'Budha Nivas', 'Palash Nivas', 'Kadamba', 'Parijaat', 'Bakul Nivas', 'Sahana Aithi House', 'Nilgiri', 'Vindhya', 'Admin Block', 'KCIS', 'Himalya Bodh']
        y, z, x = self.get_avg_by_block(self)
        y =[ '%.3f' % elem for elem in y ]
        # Use textposition='auto' for direct text
        fig = go.Figure(data=[go.Pie(labels=('Old Quarter','Ananda Nivas', 'Budha Nivas', 'Palash Nivas', 'Kadamba', 'Parijaat', 'Bakul Nivas', 'Sahana Aithi House', 'Nilgiri', 'Vindhya', 'Admin Block', 'KCIS', 'Himalya Bodh'), values=y)])
        # fig = go.Figure(data=[go.Bar(
        #             x=x, y=y,
        #             text=y,
        #             # textposition='auto',
        #         )])

        #fig.show()
        # fig.update_layout(title_text='Yearly Consumption per lock')
        #pio.write_html(fig, file='avg_consumption_1.html', auto_open=False)

    def getgraph_season_bar(self):
        colors = ['darkblue','royalblue','cyan','green']
        fig = go.Figure(data=[go.Bar(
            x=['Winter','Spring','Summer','Monsoon'],
            y=self.get_avg_by_season(self),
            marker_color=colors # marker color can be a single color value or an iterable
        )])
        fig.update_layout(title_text='Consumption Distribution by Season')
        #fig.show()
        pio.write_html(fig, file='season_consumption.html', auto_open=False)

    def getgraph_dayofweek_bar(self):
        colors = ['lightslategray', 'tan', 'aqua', 'aquamarine', 'azure','powderblue', 'khaki']
        fig = go.Figure(data=[go.Bar(
            x=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
            y=self.get_avg_by_weekday(self),
            marker_color=colors # marker color can be a single color value or an iterable

        )])
        fig.update_layout(title_text='Consumption Distribution by Weekday')
        #fig.show()
        pio.write_html(fig, file='weekday_consumption.html', auto_open=False)

    def getgraph_currweek_line(self):
        d1 = datetime.date.today()
        x = [d1 - datetime.timedelta(days=6), d1 - datetime.timedelta(days=5), d1 - datetime.timedelta(days=4), d1 - datetime.timedelta(days=3), d1 - datetime.timedelta(days=2), d1 - datetime.timedelta(days=1), d1]
        y = self.curr_week(self)
        fig = go.Figure(data=go.Scatter(x=x, y=y))
        #fig.show()
        pio.write_html(fig, file='curr_week_consumption.html', auto_open=False)
        f1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'curr_week_consumption.html')
        f2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates/curr_week_consumption.html')
        shutil.move(f1,f2)


    def getgraph_season_sunburst(self):
        sectors = ["Jan", "Feb", "March", "Apr", "May",
           "June", "July", "Aug", "Sep", "Oct","Nov","Dec"]
        regions = ["Winter","Spring","Spring","Summer","Summer"
        ,"Summer","Summer","Monsoon","Monsoon","Monsoon","Winter","Winter"]
        use = self.val_by_month(self)
        df = pd.DataFrame(
            dict(sectors=sectors, regions=regions, use=use)
        )
        print(df)
        fig = px.sunburst(df, path=['regions', 'sectors'], values='use')
        #fig.update_traces(textposition='inside', textinfo='percent')
        #fig.show()
        # pio.write_html(fig, file='season_consumption_sunburst.html', auto_open=False)

    def getgraph_month_bar(self):
        colors = ['lightslategray', 'tan','green', 'aqua','powderblue', 'aquamarine', 'azure','cyan', 'khaki','darkblue','royalblue']
        fig = go.Figure(data=[go.Bar(
            x=['January','February','March','April','May','June','July','August','September','October','November','December'],
            y=self.val_by_month(self),
            marker_color=colors # marker color can be a single color value or an iterable
        )])
        fig.update_layout(title_text='Consumption Distribution per Month')
        py.plot(fig, filename = 'cons_distri_per_month', auto_open=True)
        #fig.show()
        # pio.write_html(fig, file='month_consumption.html', auto_open=False)

    def get_leakages(self):
        # blocks = ['Old Quarter','Ananda Nivas', 'Budha Nivas', 'Palash Nivas', 'Kadamba', 'Parijaat', 'Bakul Nivas', 'Sahana Aithi House', 'Nilgiri', 'Vindhya', 'Admin Block', 'KCIS', 'Himalya Bodh']
        ## pipes names
        global leakages
        global date
        pipes = ["Pump3Vindhya", "Pump3GuestHouse", "PumpP5Vindhya", "PumpP5Bakul", "PumpP9NBHParijat", "PumpP9GuestHouse","PumpP8OBH", "PumpP10Himalaya","PumpP1FacultyQuarters","ManjeeraVindhya", "ManjeeraNBHParijat", "ManjeeraFacultyQuarters"]
        print(leakages)
        print("************************")
        print(date)
        print("###############")
        today_date = datetime.date.today()
        print("***********************today's date is ****************************")
        print(today_date)
        if date == today_date:
            return leakages
        else:
            leakages = {"Pump3Vindhya" : 0 , "Pump3GuestHouse" : 0, "PumpP5Vindhya" : 0, "PumpP5Bakul" : 0, "PumpP9NBHParijat" : 0, "PumpP9GuestHouse" : 0 ,"PumpP8OBH": 0, "PumpP10Himalaya" : 0,"PumpP1FacultyQuarters" : 0,"ManjeeraVindhya" : 0, "ManjeeraNBHParijat" : 0, "ManjeeraFacultyQuarters" : 0}
            n = random.randint(1, 5)  ## number of pipes which are leaking
            for i in range(n):
                m = random.randint(0, 11)
                pipe = pipes[m]
                # leakages[pipe] = random.randint(0, 300)
                leakages[pipe] = round(random.random(), 2)
                
            date = today_date
            return leakages

    # def send_email(self, block)
