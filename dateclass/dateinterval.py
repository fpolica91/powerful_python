'''
>>> di_21st = DateInterval(datetime.date(2000, 1, 1), datetime.date(2099, 12, 31))

>>> datetime.date.today() in di_21st
True

>>> datetime.date(2010, 6, 15) in di_21st
True
'''

import datetime

class DateInterval:
  BEGINNING_OF_TIME = datetime.date(1,1,1)
  END_OF_TIME = datetime.date(9999,12,31)

  def __init__(self, start, end):
    if start is None:
      start = self.BEGINNING_OF_TIME
    if end is None:
      end = self.END_OF_TIME
    assert start <= end, (start, end)
    self.start = start
    self.end = end
  
  def __iter__(self):
    when = self.start
    while when <= self.end:
      yield when
      when = when + datetime.timedelta(days=1)

  @classmethod
  def all(cls):
    return cls(cls.BEGINNING_OF_TIME, cls.END_OF_TIME)
  
  @classmethod
  def from_args(cls, args):
    return cls(args.start, args.end)

  def __contains__(self, date):
    return self.start<= date <= self.end



