import calendar


class Calendar(calendar.Calendar):
    def __init__(self, year, month):

        super().__init__(firstweekday=6)
        self.year = year
        self.month = month
        self.day_names = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
        self.months = (
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        )

    def get_days(self):

        weeks = self.monthdays2calendar(self.year, self.month)
        days = []
        for week in weeks:
            for day, _ in week:  # unpacking => tuple일 때 가능 / _ : 다른 하나가 필요 없을 때 사용 가능
                days.append(day)
        return days

    def get_month(self):

        return self.months[self.month - 1]
