import optparse
import calendar
import time

from main import Request

parser = optparse.OptionParser()

parser.add_option('-f', '--from',
                  action="store", dest="fromoption",
                  help="query string", default="0 months 0 day 0 hour")

parser.add_option('-t', '--to',
                  action="store", dest="tooption",
                  help="query string", default="0 months 0 day 0 hour")

options, args = parser.parse_args()

fromopt = options.fromoption.split()
toopt = options.tooption.split()

frommonths, fromdays, fromhours, tomonths, todays, tohours = 0, 0, 0, 0, 0, 0

if 'months' in fromopt:
    frommonths = int(fromopt[fromopt.index('months') - 1])

if 'day' in fromopt:
    fromdays = int(fromopt[fromopt.index('day') - 1])

if 'hour' in fromopt:
    fromhours = int(fromopt[fromopt.index('hour') - 1])

if 'months' in toopt:
    tomonths = int(toopt[toopt.index('months') - 1])

if 'day' in toopt:
    todays = int(toopt[toopt.index('day') - 1])

if 'hour' in toopt:
    tohours = int(toopt[toopt.index('hour') - 1])

result = calendar.timegm(time.gmtime())
fromtime = result - frommonths * 2592000 - fromdays * 86400 - fromhours * 3600
totime = result - tomonths * 2592000 - todays * 86400 - tohours * 3600


def check(fromtime, totime):

    print(Request.tagTimeContent(Request, 'timeStamp', fromtime))
    print(Request.tagTimeContent(Request, 'timeStamp', totime))

    pass

check(fromtime, totime)


class WrongOptionsException(Exception):
    """ exception that is raised upon fails """



