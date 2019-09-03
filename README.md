# aws-tools

Collection of small scripts to make work easier and more exciting

License: no license, use it as whenever you see fit. No mention of origin necessssary

No support, no warranty, everything provided as-is

## aws-cpu-info.py

Collect info about CPU (core count, threads/core, and vCPUs) across multiple accounts using CLI profiles

```
$ python aws-cpu-info.py account1,account2,account3 ap-southeast-1
Profile account1
i-0a27db6d111111111,m4.large,1,2
i-08f7268f111111111,t2.small,1,1
i-05a7a48a111111111,t2.micro,1,1
i-00dd13af111111111,m4.large,1,2
i-046d3d23111111111,g2.2xlarge,4,2
Profile account2
Profile account3
Total: 8 cores, 8 threads, 14 vCPUs
```