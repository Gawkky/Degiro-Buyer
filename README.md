# Degiro-Buyer

This is an automated stock buyer for Degiro.
As more and more brokers are adding the possibility to put in recurring orders this is still a feature which is missing in Degiro.

This is the reason I've build a script for automatic putting order in your own orderbook.
By setting up a recurring payment from your bank to your cashposition in Degiro you can run an automated script on your PC or server.

## Getting Started

### Installing

Clone this repo by using

```
git clone https://github.com/Gawkky/Degiro-Buyer.git
```

or by downloading the latest release with

```
curl https://github.com/Gawkky/Degiro-Buyer/archive/refs/tags/Stable-V1.0.1.zip
```

### Dependacies

```
pip install degiroapi os python-dotenv
```

### Automated running script

Running the script automated is the whole purpose of this script. 

#### Linux

If running it on a Linux machine you can make use of a cron-job.

```
crontab -e
0 10 */100,1-7 * 1 'PATH_TO_PYTHON_EXECUTABLE' 'PATH_TO_SCRIPT'
crontab -l
```

'0 0 */100,1-7' --> “At 10:00 on every 100th day-of-month and every day-of-month from 1 through 7 if it's on Monday.”

create your own cron-schedule via: https://crontab.guru/

#### Windows

Create this via Task-scheduler. I'm not going to explain the workflow as it is self-explanatory.