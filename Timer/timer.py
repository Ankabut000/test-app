class Time:
    def __init__(self,HH,MM,SS,Addition) -> None:
        self.hour = HH
        self.minute = MM
        self.second = SS
        self.addition = Addition

    def add(self,to_hour = 0,to_minute = 0,to_second = 0):

        self.second += to_second
        if self.second > 59:
            self.minute += self.second//60
            self.second %= 60

        self.minute += to_minute
        if self.minute > 59:
            self.hour += self.minute//60
            self.minute %= 60
        
        self.hour += to_hour
        if self.minute > 23:
            self.hour %= 24

    def __str__(self) -> str:
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}"
        


class Hour(Time):
    def __init__(self, HH, MM, SS,Addition) -> None:
        super().__init__(HH, MM, SS,Addition)
        self.add(to_hour=Addition)

class Minute(Time):
    def __init__(self, HH, MM, SS,Addition) -> None:
        super().__init__(HH, MM, SS,Addition)
        self.add(to_minute=Addition)

class Second(Time):
    def __init__(self, HH, MM, SS, Addition) -> None:
        super().__init__(HH, MM, SS, Addition)
        self.add(to_second=Addition)


if __name__=="__main__":

    hour,minute,second = map(int,input().split(':'))
    addition = int(input("Qancha qo'shmoqchisiz: "))

    print(Hour(hour,minute,second,addition))
    print(Minute(hour,minute,second,addition))
    print(Second(hour,minute,second,addition))
    