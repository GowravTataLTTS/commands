import subprocess

if __name__ == "__main__":
    subprocess.run('prefect deployment build prefect_scheduler.py:trigger -n prefect_checker -q test interval 60')
    subprocess.run('prefect deployment apply trigger-deployment.yaml')
    subprocess.run('prefect deployment run trigger/prefect_checker')
    subprocess.run('prefect agent start -q test')
