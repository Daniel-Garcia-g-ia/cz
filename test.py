import os
from dotenv import load_dotenv
from scripts.file import *
from scripts.get_date import *
from scripts.create_dir import *

load_dotenv()

URL_REPORT = os.getenv('URL_REPORT')
URL_SUMMARY_DIRECTORY = os.getenv('URL_SUMMARY_DIRECTORY')
NAME_FILE_REPORT = os.getenv('NAME_FILE_REPORT')



data=[["24/9/2013 05:42",1,2,1,1,12,1,18,12,50,140,33,0,0,0,0,0],
      ['24/9/2013 05:42',1,2,1,1,12,1,18,12,50,140,33,0,0,0,0,0],
      ['24/9/2013 05:42',1,2,2,2,12,1,18,12,50,160,33,0,0,0,0,0],
      ['24/9/2013 05:42',1,2,3,3,11,1,18,11,50,140,37,0,0,0,0,0],
      ['24/9/2013 05:43',1,2,4,4,13,1,18,13,50,160,76,0,0,0,0,0],
      ['24/9/2013 05:43',1,2,5,5,14,1,18,14,50,50,35,0,0,0,0,0],
      ['24/9/2013 05:43',1,2,6,6,12,1,18,11,50,100,29,0,0,0,0,0],
      ['24/9/2013 05:44',1,2,7,7,11,1,18,11,50,80,47,0,0,0,0,0],
      ['24/9/2013 05:45',1,2,8,8,12,1,18,12,50,90,34,0,0,0,0,0],
      ['24/9/2013 05:46',1,2,9,1,12,1,18,12,50,140,34,0,0,0,0,0],
      ['24/9/2013 05:46',1,2,10,2,10,1,18,9,50,140,36,0,0,0,0,0],
      ['24/9/2013 05:47',1,2,11,3,13,1,18,12,50,40,38,0,0,0,0,0],
      ['24/9/2013 05:47',1,2,12,4,14,1,18,14,50,60,77,0,0,0,0,0],
      ['24/9/2013 05:47',1,2,14,6,10,1,18,10,50,60,29,0,0,0,6,0],
      ['24/9/2013 05:47',1,2,13,5,12,1,18,12,50,50,35,0,0,0,0,0],
      ['24/9/2013 05:48',1,2,15,7,10,1,18,10,50,80,48,0,0,0,0,0],
      ['24/9/2013 05:48',1,2,16,8,10,1,18,10,50,40,34,0,0,0,0,0],
      ['24/9/2013 05:49',1,2,17,1,10,1,18,10,50,80,35,0,0,0,0,0]
      ]


#summary yesteday

""" 
path_summary_day_report, path_summary_report, day, month_text, path_created, file_exists = create_dir_yesterday(URL_SUMMARY_DIRECTORY,NAME_FILE_REPORT)


try:
      if file_exists:
            name_file= f'{NAME_FILE_REPORT}_{month_text}.xlsx'
            path_update_file= f'{path_summary_report}/{name_file}'            
            file_day_summary(path_update_file, path_summary_report, data, day, month_text)
            print('update file succefull')
      else:
            file_day_summary(URL_REPORT, path_summary_report, data, day, month_text)
            print('created file succefull')
            
except NameError:
      print('created does not existed') """


# summary turn

""" start_time, end_time, turn = get_current_turno_prev()

path_turn_report_day, day, created = create_dir_day(URL_SUMMARY_DIRECTORY, turn)

file_turn_report_excel(URL_REPORT,path_turn_report_day, turn, day, data) """



# summary day now
""" path_summary_day_report, path_summary_report, day, month_text, path_created, file_exists = create_dir_day_now(URL_SUMMARY_DIRECTORY,NAME_FILE_REPORT)


try:
      if file_exists:
            name_file= f'{NAME_FILE_REPORT}_{month_text}.xlsx'
            path_update_file= f'{path_summary_report}/{name_file}'            
            file_day_summary(path_update_file, path_summary_report, data, day, month_text)
            print('update file succefull')
      else:
            file_day_summary(URL_REPORT, path_summary_report, data, day, month_text)
            print('created file succefull')
            
except NameError:
      print('created does not existed') """












