
from abc import ABC

class Person(abc):
    def __init__(self,id_,name,e_tamas):
        self.id_=id_
        self.name=name
        self.e_tamas=e_tamas


    def update_contact_detail(self.n_e_tamas=None):
        self.e_tamas=n_e_tamas or e_tamas


    


    def __str__(self):







#..............................




class Admin(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.staff_members = []

    def create_staff_account(self, staff_details):
    pass
    def remove_staff_member(self, staff_id):
    pass

    def update_staff_role(self, staff_id, new_role=None):
       pass
    def approve_maintenance_request(self, room_id, maintenance_type):
    pass
    def generate_payroll_report(self):
        pass


     def __str__(self):
           return f""
    
#...................................


class Staff(Person):
    def __init__(self, staff_id, name, contact_info, role):
        super().__init__(unique_id=staff_id, name=name, contact_info=contact_info)
        self.role = role

    def _read_file(self, filename):
       pass

    def _write_file(self, filename, data):
   pass
    def book_guest(self, guest_id, room_id):
       pass
    def check_out_guest(self, guest_id):
      pass
      
    def mark_room_cleaned(self, room_id):
        pass
       

    def request_cleaning_supplies(self):
         pass
    def report_repair_done(self, room_id):
     
    def order_repair_materials(self, 

     def __str__(self):
           return f""
    
#.................................



    class Rooms:
    def __init__(self):
        self.rooms_data = []

    def set_room_status(self, room_id, new_status):
        for room in self.rooms_data:
            if room['room_id'] == room_id:
                room['status'] = new_status
                return f"Room {room_id} status changed to {new_status}."
     

    def schedule_room_maintenance(self, room_id, maintenance_type):
        for room in self.rooms_data:
            if room['room_id'] == room_id:
                room['maintenance_type'] = maintenance_type
                return f"Maintenance scheduled for Room {room_id}. Type: {maintenance_type}."
       

    def __str__(self):
        return f""
    

#....................

    class Hotel:
    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.rooms = Rooms()
        self.guests = []
    
    
    def __str__(self):
        return f""
    