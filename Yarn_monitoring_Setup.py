
# Kerberos Authentication

kinit -kt {PATH OF KEEYTAB} USER@COMPANY.com

#Knowledge using shell
yarn application -list      # This will list all YARN applctions
yarn application -list -appStates ALL   # will list all yarn app


"""
Using Yarn Logs:

In logs you can see tracking URL: http://<nn>:8088/proxy/application_*****/

If you copy and open the link you can see all the logs for the application in Resourcemanager.

2.Using Spark application:

From sparkContext we can get the applicationID.

print(spark.sparkContext.aplicationId)
3. Using yarn application command:

Use yarn application --list command to get all the running yarn applications on the cluster then use

yarn application --help
-appStates <States>             Works with -list to filter applications
                                 based on input comma-separated list of
                                 application states. The valid application
                                 state can be one of the following:
                                 ALL,NEW,NEW_SAVING,SUBMITTED,ACCEPTED,RUN
                                 NING,FINISHED,FAILED,KILLED
 -appTypes <Types>               Works with -list to filter applications
                                 based on input comma-separated list of
                                 application types.
 -help                           Displays help for all commands.
 -kill <Application ID>          Kills the application.
 -list                           List applications. Supports optional use
                                 of -appTypes to filter applications based
                                 on application type, and -appStates to
                                 filter applications based on application
                                 state.
 -movetoqueue <Application ID>   Moves the application to a different
                                 queue.
 -queue <Queue Name>             Works with the movetoqueue command to
                                 specify which queue to move an
                                 application to.
 -status <Application ID>        Prints the status of the application.
List all the finished applications:

yarn application -appStates FINISHED -list
"""

# Is it possible to get yarn application id using application name via yarn cli?
yarn application -list | grep APPNAME | awk '{print $1}'   # This will give appID of given appName

running_app=$( yarn application -list | grep APPNAME | wc -l)  # this wiill gve no of appname yarn running  # each lnee 1 yarn
# if it is 0 that means no yarn app s running for given ap name
if [[ $running_app -eq 0 ]] ; then
#executee spark job -- this will run your kiled spark job automatically 





