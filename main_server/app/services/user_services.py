from app.models.auth_models import Account, Picker, Customer
from abc import ABC, abstractmethod
import SQLAlchemy

db = SQLAlchemy()

class AccountServices(ABC):
    def get_user_by_email(self, email):
        return Account.query.filter_by(email=email).first()
    

class PickerServices(AccountServices):
    def get_picker_by_account_id(self, account_id):
        return Picker.query.filter_by(account_id=account_id).first()
    
    def get_picker_by_email(self, email):
        account = self.get_user_by_email(email)
        return self.get_picker_by_account_id(account.id)
    
    def create_picker(self, name, phone_number, account_id):
        picker = Picker(name=name, phone_number=phone_number, account_id=account_id)
        db.session.add(picker)
        db.session.commit()
        return picker
    
    def update_picker(self, picker_id, name, phone_number):
        picker = Picker.query.get(picker_id)
        picker.name = name
        picker.phone_number = phone_number
        db.session.commit()
        return picker
    
    def delete_picker(self, picker_id):
        picker = Picker.query.get(picker_id)
        db.session.delete(picker)
        db.session.commit()
        return picker
    
class CustomerServices(AccountServices):
    def get_customer_by_account_id(self, account_id):
        return Customer.query.filter_by(account_id=account_id).first()
    
    def get_customer_by_email(self, email):
        account = self.get_user_by_email(email)
        return self.get_customer_by_account_id(account.id)
    
    def create_customer(self, name, phone_number, account_id):
        customer = Customer(name=name, phone_number=phone_number, account_id=account_id)
        db.session.add(customer)
        db.session.commit()
        return customer
    
    def update_customer(self, customer_id, name, phone_number):
        customer = Customer.query.get(customer_id)
        customer.name = name
        customer.phone_number = phone_number
        db.session.commit()
        return customer
    
    def delete_customer(self, customer_id):
        customer = Customer.query.get(customer_id)
        db.session.delete(customer)
        db.session.commit()
        return customer