def input_user_details():
        errors = []
        re_enter = ['name', 'age', 'email', 'phone', 'address','gender','password']
        while True:
            errors.clear()

            if 'name' in re_enter:
                name = input('Enter name: ')
                if len(name) == 0:
                    errors.append('[Error] Name cannot be empty')
                    # re_enter.append('name')
                else:
                    if 'name' in re_enter:
                        re_enter.remove('name')

            if 'age' in re_enter:
                age = int(input('Enter age: '))
                if age < 15:
                    errors.append('[Error] Age is not valid')
                    # re_enter.append('age')
                else:
                    if 'age' in re_enter:
                        re_enter.remove('age')
            
            if 'email' in re_enter:
                email = input('Enter email: ')
                if len(email) == 0:
                    errors.append('[Error] email cannot be empty')
                    # re_enter.append('email')
                elif '@' not in email or '.' not in email:
                    errors.append('[Error] email is not valid')
                    # re_enter.append('email')
                else:
                    if 'email' in re_enter:
                        re_enter.remove('email')

            
            if 'phone' in re_enter:
                phone = input('Enter phone: ')
                if len(phone) == 0:
                    errors.append('[Error] phone no must be 10 digits')
                    # re_enter.append('phone')
                else:
                    if 'phone' in re_enter:
                        re_enter.remove('phone')

            if 'address' in re_enter:
                address = input('Enter address: ')
                if len(address) == 0:
                    errors.append('[Error] address cannot be empty')
                    # re_enter.append('address')
                else:
                    if 'address' in re_enter:
                        re_enter.remove('address')


            if 'gender' in re_enter:
                gender = input('Enter gender: ')
                if len(gender) == 0:
                    errors.append('[Error] gender cannot be empty')
                    # re_enter.append('gender')
                else:
                    if 'gender' in re_enter:
                        re_enter.remove('gender')

            if 'password' in re_enter:
                self.password = input('Enter password: ').encode('utf-8')
                self.password = hashlib.sha256(self.password).hexdigest()
                
                if len(self.password) < 6:
                    errors.append('[Error] password must be minimam 6 characters long')
                else:
                    if 'password' in re_enter:
                        re_enter.remove('password')


            if len(errors) != 0:
                print('Errors found:')
                for error in errors:
                    print(error)
                print('Please re-enter the details')
            else:
                break


input_user_details()