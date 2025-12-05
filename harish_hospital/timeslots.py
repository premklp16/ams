from datetime import date, timedelta


def generate_timeslots(doctor, days=30):
    """
    Automatically generates timeslots for a doctor when registered
    """
    from harish_hospital.models import TimeSlot
    if TimeSlot.objects.filter(doctor=doctor).exists():
        return
    
    default_times = ["10:00 AM" ,"11:00 AM", "12:00 PM", "01:00 PM", "02:00 PM"]
    start = date.today()
    
    for day in range(days):
        slot_date = start + timedelta(days=day)

        for t in default_times:
            TimeSlot.objects.get_or_create(
                doctor=doctor,
                date=slot_date,
                time=t
            )
            
