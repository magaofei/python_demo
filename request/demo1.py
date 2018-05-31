
import requests

proxies = {
  "http": "http://124.250.24.247",
  "https": "http://124.250.24.247",
}
r = requests.get('http://work.haibian.com/myCourse/getUserByCourseDetails?course_id=14046&user_id=1519207&type=1', proxies=proxies)
print(r.json())