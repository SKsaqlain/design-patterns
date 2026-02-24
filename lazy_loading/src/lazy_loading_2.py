from abc import ABC, abstractmethod
from typing import List


class Employee:
    def __init__(self, employee_name: str, employee_salary: float, employee_designation: str):
        self.employee_name=employee_name
        self.employee_salary=employee_salary
        self.employee_designation=employee_designation

    
    def __str__(self):
        return f'Employee Name: {self.employee_name}, Employee Designation: {self.employee_designation}, Employee Salary: {self.employee_salary}'
    


class ContactList(ABC):
    
    @abstractmethod
    def get_employee_list(self)-> List[Employee]:
        pass

class ContactListImpl(ContactList):
    @staticmethod
    def _get_emp_list():
        emp_list = [
            Employee('Lokesh', 2565.55, 'SE'),
            Employee('Kushagra', 22574, 'Manager'),
            Employee('Susmit', 3256.77, 'G4'),
            Employee('Vikram', 4875.54, 'SSE'),
            Employee('Achint', 2847.01, 'SE')
        ]
        return emp_list

    def get_employee_list(self):
        return self._get_emp_list()
    

class ContactListProxyImpl(ContactList):
    def __init__(self):
        self.contact_list=None
    
    def get_employee_list(self)-> List[Employee]:
        if self.contact_list is None:
            print("Fetching list of employees")
            self.contact_list=ContactListImpl()
        return self.contact_list.get_employee_list()
    
class Company:
    def __init__(self,company_name, company_address, company_contact_no, contact_list: ContactList):
        self.company_name=company_name
        self.company_address=company_address
        self.company_contact_no=company_contact_no
        self.contact_list=contact_list
    
    def get_company_name(self):
        return self.company_name
    
    def get_company_address(self):
        return self.company_address
    
    def get_company_contact_no(self):
        return self.company_contact_no
    
    def get_contact_list(self):
        return self.contact_list
    

def main():
    contact_list=ContactListProxyImpl()
    company=Company('Company_name','company_location','xxx-xxx-xxxx',contact_list)
    print(f'Company Name: {company.get_company_name()}')
    print(f'Company Address: {company.get_company_address()}')
    print(f'Company Contact No: {company.get_company_contact_no()}')
    print("Requesting for contact list")

    contact_list=company.get_contact_list()
    emp_list=contact_list.get_employee_list()
    for emp in emp_list:
        print(emp)
    
if __name__=='__main__':
    main()