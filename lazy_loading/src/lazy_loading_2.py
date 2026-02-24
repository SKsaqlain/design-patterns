from abc import ABC, abstractmethod
from typing import List


# Data class representing a single employee record
class Employee:
    def __init__(self, employee_name: str, employee_salary: float, employee_designation: str):
        self.employee_name = employee_name
        self.employee_salary = employee_salary
        self.employee_designation = employee_designation

    def __str__(self):
        return f'Employee Name: {self.employee_name}, Employee Designation: {self.employee_designation}, Employee Salary: {self.employee_salary}'


# Abstract interface for fetching employee lists
class ContactList(ABC):

    @abstractmethod
    def get_employee_list(self) -> List[Employee]:
        pass


# Real implementation — builds the full employee list immediately
class ContactListImpl(ContactList):
    @staticmethod
    def _get_emp_list():
        emp_list = [  # simulates an expensive data fetch (e.g. DB query)
            Employee('Lokesh', 2565.55, 'SE'),
            Employee('Kushagra', 22574, 'Manager'),
            Employee('Susmit', 3256.77, 'G4'),
            Employee('Vikram', 4875.54, 'SSE'),
            Employee('Achint', 2847.01, 'SE')
        ]
        return emp_list

    def get_employee_list(self):
        return self._get_emp_list()


# Proxy — delays creation of ContactListImpl until first access (lazy loading)
class ContactListProxyImpl(ContactList):
    def __init__(self):
        self.contact_list = None  # real implementation not yet created

    def get_employee_list(self) -> List[Employee]:
        if self.contact_list is None:  # load only on first call
            print("Fetching list of employees")
            self.contact_list = ContactListImpl()  # create real impl lazily
        return self.contact_list.get_employee_list()


# Client — holds company info and a contact list reference (possibly a proxy)
class Company:
    def __init__(self, company_name, company_address, company_contact_no, contact_list: ContactList):
        self.company_name = company_name
        self.company_address = company_address
        self.company_contact_no = company_contact_no
        self.contact_list = contact_list  # injected as proxy, loaded lazily

    def get_company_name(self):
        return self.company_name

    def get_company_address(self):
        return self.company_address

    def get_company_contact_no(self):
        return self.company_contact_no

    def get_contact_list(self):
        return self.contact_list


def main():
    contact_list = ContactListProxyImpl()  # proxy — no employees loaded yet
    company = Company('Company_name', 'company_location', 'xxx-xxx-xxxx', contact_list)
    print(f'Company Name: {company.get_company_name()}')
    print(f'Company Address: {company.get_company_address()}')
    print(f'Company Contact No: {company.get_company_contact_no()}')
    print("Requesting for contact list")

    contact_list = company.get_contact_list()
    emp_list = contact_list.get_employee_list()  # triggers lazy load on first call
    for emp in emp_list:
        print(emp)


if __name__ == '__main__':
    main()
