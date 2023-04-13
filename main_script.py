import subprocess


def something():
	status = "BACKUP"
	process = subprocess.Popen(["./keepalived_status_checker.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	result = process.communicate()
	for i in result:
		if 'master' in i.lower():		
			status="MASTER"
	return status


print(something())
