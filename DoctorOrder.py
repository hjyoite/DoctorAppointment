#!/usr/bin/env python
#coding: utf-8

from Config import *
import json
import urllib
import urllib2

from mail_api import send_mail

doctor_schedule_url = 'http://www.hk515.com/DoctorIndex/GetSchedulings'
doctor_profile_url = 'http://www.hk515.com/Doctor/'

def check_doctor_available(doctor_id):
	data = {
		'doctorId':doctor_id,
		'ticketPoolName': 'ningyuan',
	}
	post_data = urllib.urlencode(data)
	req = urllib2.Request(url=doctor_schedule_url, data=post_data)
	resp = urllib2.urlopen(req)
	resp_data = resp.read()
	# print resp_data
	json_data = json.loads(resp_data)
	available_slots = []
	for item in json_data['Schedulings']:
		schedule_date, count = item['SchedulingDate'], item['AvailableCount']
		# print schedule_date, count
		available_slots.append((schedule_date, count))
	return available_slots

def main():
        docotr_list = Follow_List
        contents = []
        is_available = False
        for doctor_id in docotr_list:
		result = check_doctor_available(doctor_id)
		for item in result:
			if item[1] > 0:
				print doctor_id, item[0], item[1]
				is_available = True
                                contents.append('<li><span style="margin:10px"><a href="{url}{doctor_id}">{doctor_id}</a></span><span style="margin:10px">{date}</span><span style="margin:10px">{count}</span></li>'.format(url=doctor_profile_url, doctor_id=doctor_id, date=item[0], count=item[1]))
	if is_available:
        	send_mail(To_Address_List, '医生预约', '<br>'.join(contents))

if __name__ == '__main__':
	main()
