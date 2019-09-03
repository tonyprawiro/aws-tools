import subprocess
import sys
import json
from pprint import pprint

# Usage: python aws-cpu-info.py account1,account2,account3 ap-southeast-1
profiles = sys.argv[1].split(",")
region = sys.argv[2]

total_cores = 0
total_vcpus = 0

for profile in profiles:

	print("Profile %s" % profile)
	ret = subprocess.check_output(["aws", "ec2", "describe-instances", "--profile", profile, "--region", region])
	obj = json.loads(ret)

	for reservation in obj["Reservations"]:

		for instance in reservation["Instances"]:

			cpuopt = instance["CpuOptions"]
			cores = cpuopt.get("CoreCount", 1)
			threads = cpuopt.get("ThreadsPerCore", 1)
			total_cores += cores
			total_vcpus += cores * threads
			print("%s,%s,%d,%d" %(instance["InstanceId"], instance["InstanceType"], cores, threads))

print("Total: %d cores, %d vCPUs" % (total_cores, total_vcpus))
