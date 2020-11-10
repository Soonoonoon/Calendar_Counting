import typing
import calendar
import re
mon=['mon','monday']
tue=['tue','tuesday']
wed=['wed','wednesday']
thu=['thu','thursday']
fri=['fri','friday']
sat=['sat','saturday']
sun=['sun','sunday']
dict_week={1:mon,2:tue,3:wed,4:thu,5:fri,6:sat,7:sun}
class Dateday(object):
    ____change_dash=""
    ____splitext=['/','-','~',',','\\','_']
    
    def __init__(self,dateofday):
        self.origindal_day=dateofday
        dateofday=str(dateofday)
        s=self._____get()
 
    def __repr__(self):
        return ( self.____change_dash) 
    def _____get(self):
        global ____change_dash
        for i in self.____splitext:  #yyyy-mm-dd
            
            if i in self.origindal_day:
               self.____change_dash=self.origindal_day.replace(i,'-')
               year,month,day=self.origindal_day.split(i)
               self.year=year
               self.month=month
               self.day=day
               return ( self.____change_dash)
        if len(self.origindal_day)==8 :     #yyyymmdd:
            self.year=self.origindal_day[:4]
            self.month=(self.origindal_day[4:6])
            self.day=(self.origindal_day[6:])
        elif len(self.origindal_day)==6 :   #yyyy m d:
            
            
            self.year=self.origindal_day[:4]
            self.month=(self.origindal_day[4:5])
            self.day=(self.origindal_day[5:])
        self.____change_dash=str(self.year)+'-'+str(self.month)+'-'+str(self.day )
            
        return ( self.____change_dash)
    def get_week_alp2num(daychoose):
    
            for i in dict_week:
                for j in dict_week[i]:
                 
                    if re.findall(j,daychoose,re.IGNORECASE):
                        daychoose=i
                        
                        return daychoose
def get_weektimes(year,month,times,daychoose:typing.Union[int,str]):
        if isinstance(daychoose,str):
            daychoose=get_week_alp2num(daychoose)
       
        arr_week=calendar.monthcalendar(year,month)
        counday=0
        for each in arr_week:
          
            if each[daychoose-1]:
                counday+=1
                
                
                if counday==times:
                    
                    day=Dateday(str(year)+'/'+str(month)+"/"+str(each[daychoose-1]))
                    return day
