import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--num_y", help="number of years", type=int)
parser.add_argument("--num_d", help="number of days", type=int)
args = parser.parse_args()
import datetime
now = datetime.datetime.now()
from dateutil.relativedelta import relativedelta
print ("current date:" , now)
print ("given years:", args.num_y)
print ("given days:", args.num_d)
print ("Final date:", now + relativedelta(years= args.num_y)+ (datetime.timedelta(days=args.num_d)) )