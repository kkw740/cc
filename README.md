# cc

2X Assignment 1:Install Google App Engine. Create hello world app and other simple web applications using python/java. 
-> https://www.youtube.com/watch?v=2lhOEO-zmjw

2X Assignment 2:Use GAE launcher to launch the web applications. 
->https://www.youtube.com/watch?v=8re44RiaocY

Assignment 4:Find a procedure to transfer the filesfrom one virtual machine to another virtual machine. 
->https://www.youtube.com/watch?v=0MaS0nZCTZc

Assignment 5:Find a procedure to launch virtual machine using aws
->https://www.youtube.com/watch?v=FLLnxIDPUMQ

Assignment 6:Design and deploy a web application in a PaaS environment. 
->https://www.youtube.com/watch?v=12Thoc5MsF8

Assignment 7:Design and develop custom Application (Mini Project) using Salesforce Cloud. 
->https://youtu.be/n4Nx7YD5_mY?si=nXGIGtSs5jxPoYvN

Assignment 8:Design an Assignment to retrieve, verify, and store user credentials using Firebase Authentication, the Google App Engine standard environment, and Google Cloud Data store. 
->https://www.youtube.com/watch?v=--qUoDXqPos
->https://www.youtube.com/watch?v=2crtIMKf9bs

2nd and 6th:
1.new project
2.billing check
3.app engine create project
4.iam>service accn>manage permission>jason file
5.cmd:
1]ls
2]upload json,folder
3]cd filename
4]gcloud app deploy
5]gcloud app browse
6]rm -r name .....to delete the file or folder\n

commands for 4th/n
**Commands**:

### VM1:
```bash
ifconfig
ping <IP of VM2>
ls
touch file.txt         # Create file
nano file.txt          # Edit file
# (Ctrl + X, then Y, then Enter to save)
cat file.txt           # Display content
scp file.txt vagrant@192.168.56.102:/home/vagrant
###vm2
ifconfig
ping <IP of VM1>
ls
ls / home
ls / home / vagrant
cat file.txt
