def add_time(start, duration, day = None):

    # here I mess with the start time
    # until I got the hours and minutes like ints in a list
    # maybe this can be done in a line or two
    # but that's all I could think of
    if "PM" in start:
        first = (start.replace("PM", "")).rstrip()
        am_pm = "PM"
    else:
        first = (start.replace("AM", "")).rstrip()
        am_pm = "AM"

    first_list = first.split(":")

    if am_pm == "PM":
        first_hours = int(first_list[0]) + 12
    else:
        first_hours = int(first_list[0])

    first_minutes = int(first_list[1])

    # here I'll mess with the given duration
    # hope this works
    given_duration = duration.split(":")
    given_hours = int(given_duration[0])
    given_minutes = int(given_duration[1])

    # here we got the final minutes
    # i tested it. if it's wrong i'll bang my head on the floor
    final_minutes = first_minutes + given_minutes
    if final_minutes > 59:
        final_minutes -= 60
        given_hours += 1
    if final_minutes < 10:
        final_minutes = "0{}".format(final_minutes)
    else:
        final_minutes = str(final_minutes)

    # i'll try the hours
    final_hours = first_hours + given_hours

    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days_passed = 0
    days_text = ""

    while final_hours > 23:
        days_passed += 1
        final_hours -= 24

    if final_hours >= 12:
        final_hours -= 12
        final_am_pm = "PM"
    else:
        final_am_pm = "AM"

    if final_hours == 0:
      final_hours = 12
    
    final_hours = str(final_hours)

    if day == None:
      if days_passed == 0:
          days_text = ""
          new_time = "{}:{} {}".format(final_hours, final_minutes, final_am_pm).rstrip()
      elif days_passed == 1:
          days_text = "(next day)"
          new_time = "{}:{} {} {}".format(final_hours, final_minutes, final_am_pm, days_text).rstrip()
      else:
          days_text = "({} days later)".format(days_passed)
          new_time = "{}:{} {} {}".format(final_hours, final_minutes, final_am_pm, days_text).rstrip()
    else:
      sum_days = 0
      start = 7
      while sum_days < days_passed:
        for i in range(6):
          keep_date = i
          if day == week[i]:
            start = i
          if start == i:
            sum_days += 1
      final_day = week[keep_date - 1]

      if days_passed == 0:
          days_text = ""
          new_time = "{}:{} {}, {}".format(final_hours, final_minutes, final_am_pm, final_day).rstrip()
      elif days_passed == 1:
          days_text = "(next day)"
          new_time = "{}:{} {}, {} {}".format(final_hours, final_minutes, final_am_pm, final_day, days_text).rstrip()
      else:
          days_text = "({} days later)".format(days_passed)
          new_time = "{}:{} {}, {} {}".format(final_hours, final_minutes, final_am_pm, final_day, days_text).rstrip()
  
    return new_time
