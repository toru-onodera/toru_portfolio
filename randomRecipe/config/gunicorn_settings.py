import os

bind = '54.249.197.75:' + str(os.getenv('PORT', 80))
proc_name = 'Infrastructure-Practice-Flask'
workers = 1